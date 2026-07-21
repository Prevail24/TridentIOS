from core.planner.rules.redirect_vhost_rule import RedirectVhostRule


class FakeMissionContext:
    def __init__(self, surfaces=None, vhosts=None):
        self._surfaces = surfaces or []
        self._vhosts = vhosts or []

    def web_surfaces(self):
        return self._surfaces

    def web_vhosts(self):
        return self._vhosts


def test_recommends_vhost_discovery_for_redirect():
    context = FakeMissionContext(
        surfaces=[
            {
                "url": "http://10.10.11.10",
                "redirect_location": "http://paper.htb/",
            }
        ]
    )

    recommendation = RedirectVhostRule().evaluate(context)

    assert recommendation is not None
    assert recommendation.capability == "Virtual Host Discovery"
    assert recommendation.confidence == "High"
    assert recommendation.rule == "Redirect Virtual Host Rule"


def test_returns_none_without_redirect():
    context = FakeMissionContext(
        surfaces=[
            {
                "url": "http://10.10.11.10",
                "redirect_location": None,
            }
        ]
    )

    recommendation = RedirectVhostRule().evaluate(context)

    assert recommendation is None


def test_returns_none_when_vhosts_already_exist():
    context = FakeMissionContext(
        surfaces=[
            {
                "url": "http://10.10.11.10",
                "redirect_location": "http://paper.htb/",
            }
        ],
        vhosts=[
            {
                "hostname": "paper.htb",
                "url": "http://paper.htb/",
            }
        ],
    )

    recommendation = RedirectVhostRule().evaluate(context)

    assert recommendation is None