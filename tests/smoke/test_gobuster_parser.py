from core.models.web_path_observation import WebPathObservation
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
