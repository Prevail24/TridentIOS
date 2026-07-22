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
    assert (
        recommendation.capability_id
        == "web.recon.virtual-host-discovery"
    )
    assert recommendation.confidence == "High"
    assert recommendation.rule == "RedirectVhostRule"
    assert recommendation.inputs == (
        ("target", "http://10.10.11.10"),
        ("domain", "paper.htb"),
    )
    assert recommendation.scope == "paper.htb"
    assert recommendation.required_inputs == (
        "wordlist",
    )
    assert recommendation.executable is False


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
        vhosts=["office.paper.htb"],
    )

    recommendation = RedirectVhostRule().evaluate(context)

    assert recommendation is None

def test_keeps_unknown_vhost_inputs_required():
    context = FakeMissionContext(
        surfaces=[
            {
                "url": None,
                "redirect_location": "/login",
            }
        ]
    )

    recommendation = RedirectVhostRule().evaluate(context)

    assert recommendation is not None
    assert recommendation.inputs == ()
    assert recommendation.scope is None
    assert recommendation.required_inputs == (
        "target",
        "domain",
        "wordlist",
    )
    assert recommendation.executable is False

def test_uses_http_target_as_scope_for_relative_redirect():
    context = FakeMissionContext(
        surfaces=[
            {
                "url": "http://10.10.11.10",
                "redirect_location": "/login",
            }
        ]
    )

    recommendation = RedirectVhostRule().evaluate(context)

    assert recommendation is not None
    assert recommendation.scope == "http://10.10.11.10"
    assert recommendation.inputs == (
        ("target", "http://10.10.11.10"),
    )
    assert recommendation.required_inputs == (
        "domain",
        "wordlist",
    )