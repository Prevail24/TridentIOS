from core.models.web_path_observation import WebPathObservation
from core.models.web_vhost_observation import WebVhostObservation
from core.parsers.gobuster.parser import GobusterParser


def test_gobuster_parser_returns_web_path_observations():
    raw_output = """
assets      (Status: 301) [Size: 178] [--> http://orion.htb/assets/]
index.php   (Status: 200) [Size: 12272]
.git        (Status: 403) [Size: 162]
""".strip()

    observations = GobusterParser().parse(
        raw_output,
        base_url="http://orion.htb",
    )

    assert len(observations) == 3
    assert all(
        isinstance(observation, WebPathObservation)
        for observation in observations
    )
    assert observations[0].path == "assets"
    assert observations[0].status_code == 301
    assert observations[0].content_length == 178
    assert observations[0].redirect_location == (
        "http://orion.htb/assets/"
    )
    assert observations[1].url == "http://orion.htb/index.php"
    assert observations[1].status_code == 200
    assert observations[2].path == ".git"
    assert observations[2].status_code == 403


def test_gobuster_parser_returns_vhost_observations():
    raw_output = """
research.bedside.htb Status: 200 [Size: 3152]
mail.bedside.htb Status: 301 [Size: 349] [--> http://bedside.htb/]
""".strip()

    observations = GobusterParser().parse_vhosts(
        raw_output,
        base_url="http://10.129.36.93",
    )

    assert len(observations) == 2
    assert all(
        isinstance(observation, WebVhostObservation)
        for observation in observations
    )
    assert observations[0].hostname == "research.bedside.htb"
    assert observations[0].url == "http://research.bedside.htb"
    assert observations[0].status_code == 200
    assert observations[0].content_length == 3152
    assert observations[1].redirect_location == "http://bedside.htb/"
