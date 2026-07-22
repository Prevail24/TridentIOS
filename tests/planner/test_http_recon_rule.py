from core.planner.rules.http_recon_rule import HTTPReconRule


class FakeMissionContext:
    def __init__(
        self,
        *,
        has_http=True,
        has_surface=False,
        target="10.10.11.10",
    ):
        self._has_http = has_http
        self._has_surface = has_surface
        self._target = target

    def has_service(self, name):
        return (
            self._has_http
            and name.lower() == "http"
        )

    def has_web_surface(self):
        return self._has_surface

    def target(self):
        return self._target


def test_recommends_http_recon_for_mission_target():
    context = FakeMissionContext(
        target="10.10.11.10",
    )

    recommendation = HTTPReconRule().evaluate(context)

    assert recommendation is not None
    assert (
        recommendation.capability_id
        == "web.recon.technology-discovery"
    )
    assert recommendation.scope == "10.10.11.10"
    assert recommendation.confidence == "High"
    assert recommendation.rule == "HTTPReconRule"


def test_returns_none_without_http_service():
    context = FakeMissionContext(
        has_http=False,
    )

    recommendation = HTTPReconRule().evaluate(context)

    assert recommendation is None


def test_returns_none_when_web_surface_exists():
    context = FakeMissionContext(
        has_surface=True,
    )

    recommendation = HTTPReconRule().evaluate(context)

    assert recommendation is None