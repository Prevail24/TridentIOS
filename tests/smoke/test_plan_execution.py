import pytest

from cli.observer_shell import ObserverShell
from core.planner.recommendation import Recommendation


def install_fake_planner(monkeypatch, recommendations):
    class FakePlanner:
        def plan(self, context):
            return recommendations

    monkeypatch.setattr(
        "cli.observer_shell.Planner",
        FakePlanner,
    )


def test_plan_execute_rejects_invalid_selection(
    monkeypatch,
    capsys,
):
    recommendation = Recommendation(
        capability_id="web.recon.technology-discovery",
        reason="HTTP reconnaissance is required.",
    )
    install_fake_planner(monkeypatch, [recommendation])

    shell = ObserverShell({})
    shell.execute_plan_recommendation("plan execute 2")

    output = capsys.readouterr().out

    assert "Recommendation 2 does not exist" in output


def test_plan_execute_blocks_missing_inputs(
    monkeypatch,
    capsys,
):
    recommendation = Recommendation(
        capability_id="web.recon.virtual-host-discovery",
        reason="A redirect hostname was discovered.",
        inputs=(
            ("target", "http://10.10.11.10"),
            ("domain", "paper.htb"),
        ),
        required_inputs=(
            "wordlist",
        ),
    )
    install_fake_planner(monkeypatch, [recommendation])

    def fail_if_prompted(prompt):
        pytest.fail("Blocked recommendation requested confirmation.")

    monkeypatch.setattr("builtins.input", fail_if_prompted)

    shell = ObserverShell({})
    shell.execute_plan_recommendation("plan execute 1")

    output = capsys.readouterr().out

    assert "not ready to execute" in output
    assert "Missing input: wordlist" in output

    def test_plan_execute_configures_vhost_from_resolved_inputs(
        monkeypatch,
        capsys,
    ):
        recommendation = Recommendation(
            capability_id="web.recon.virtual-host-discovery",
            reason="A redirect hostname was discovered.",
            inputs=(
                ("target", "http://10.10.11.10"),
                ("domain", "paper.htb"),
            ),
            required_inputs=(
                "wordlist",
            ),
        )
        install_fake_planner(monkeypatch, [recommendation])

        calls = []

        class FakeReconSerpent:
            def __init__(
                self,
                *,
                vhost_target=None,
                vhost_domain=None,
                vhost_wordlist=None,
            ):
                calls.append(
                    (
                        "serpent",
                        vhost_target,
                        vhost_domain,
                        vhost_wordlist,
                    )
                )

        class FakeCapabilityRouter:
            def __init__(self, serpents):
                calls.append(("router", serpents))

            def execute_recommendation(
                self,
                selected_recommendation,
                context,
            ):
                calls.append(
                    (
                        "execute",
                        selected_recommendation,
                        context,
                    )
                )
                return [{"executed": True}]

        monkeypatch.setattr(
            "cli.observer_shell.ReconSerpent",
            FakeReconSerpent,
        )
        monkeypatch.setattr(
            "cli.observer_shell.CapabilityRouter",
            FakeCapabilityRouter,
        )
        monkeypatch.setattr(
            "builtins.input",
            lambda prompt: "y",
        )

        shell = ObserverShell({})

        monkeypatch.setattr(
            shell,
            "show_plan",
            lambda: calls.append(("replan",)),
        )

        shell.execute_plan_recommendation(
            "plan execute 1 "
            "--wordlist '/tmp/subdomain words.txt'"
        )

        output = capsys.readouterr().out

        assert calls[0] == (
            "serpent",
            "http://10.10.11.10",
            "paper.htb",
            "/tmp/subdomain words.txt",
        )

        assert calls[1][0] == "router"
        assert len(calls[1][1]) == 1

        executed_recommendation = calls[2][1]

        assert executed_recommendation.required_inputs == ()
        assert executed_recommendation.inputs == (
            ("target", "http://10.10.11.10"),
            ("domain", "paper.htb"),
            ("wordlist", "/tmp/subdomain words.txt"),
        )
        assert executed_recommendation.executable is True
        assert calls[2][2] is shell.mission_context
        assert calls[3] == ("replan",)

        assert "Capability execution completed" in output

def test_plan_execute_can_be_cancelled(
    monkeypatch,
    capsys,
):
    recommendation = Recommendation(
        capability_id="web.recon.technology-discovery",
        reason="HTTP reconnaissance is required.",
    )
    install_fake_planner(monkeypatch, [recommendation])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: "n",
    )

    def fail_if_router_created(serpents):
        pytest.fail("Router was created after cancellation.")

    monkeypatch.setattr(
        "cli.observer_shell.CapabilityRouter",
        fail_if_router_created,
    )

    shell = ObserverShell({})
    shell.execute_plan_recommendation("plan execute 1")

    output = capsys.readouterr().out

    assert "Execution cancelled" in output


def test_plan_execute_dispatches_confirmed_recommendation(
    monkeypatch,
    capsys,
):
    recommendation = Recommendation(
        capability_id="web.recon.technology-discovery",
        reason="HTTP reconnaissance is required.",
    )
    install_fake_planner(monkeypatch, [recommendation])

    calls = []

    class FakeWebSpecies:
        def serpents(self):
            return ["recon-serpent"]

    class FakeCapabilityRouter:
        def __init__(self, serpents):
            calls.append(("router", serpents))

        def execute_recommendation(
            self,
            selected_recommendation,
            context,
        ):
            calls.append(
                (
                    "execute",
                    selected_recommendation,
                    context,
                )
            )
            return [{"executed": True}]

    monkeypatch.setattr(
        "cli.observer_shell.WebSpecies",
        FakeWebSpecies,
    )
    monkeypatch.setattr(
        "cli.observer_shell.CapabilityRouter",
        FakeCapabilityRouter,
    )
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: "y",
    )

    shell = ObserverShell({})
    monkeypatch.setattr(
        shell,
        "show_plan",
        lambda: calls.append(("replan",)),
    )

    shell.execute_plan_recommendation("plan execute 1")

    output = capsys.readouterr().out

    assert calls[0] == (
        "router",
        ["recon-serpent"],
    )
    assert calls[1][0] == "execute"
    assert calls[1][1] == recommendation
    assert calls[1][2] is shell.mission_context
    assert calls[2] == ("replan",)

    assert "Dispatching" in output
    assert "Capability execution completed" in output

def test_plan_execute_rejects_unknown_option(
        monkeypatch,
        capsys,
    ):
        recommendation = Recommendation(
            capability_id="web.recon.technology-discovery",
            reason="HTTP reconnaissance is required.",
        )
        install_fake_planner(monkeypatch, [recommendation])

        shell = ObserverShell({})
        shell.execute_plan_recommendation(
            "plan execute 1 --threads 50"
        )

        output = capsys.readouterr().out

        assert "Unknown option: --threads" in output    

def test_plan_execute_configures_vhost_from_resolved_inputs(
    monkeypatch,
    capsys,
):
    recommendation = Recommendation(
        capability_id="web.recon.virtual-host-discovery",
        reason="A redirect hostname was discovered.",
        inputs=(
            ("target", "http://10.10.11.10"),
            ("domain", "paper.htb"),
        ),
        required_inputs=("wordlist",),
    )
    install_fake_planner(monkeypatch, [recommendation])

    calls = []

    class FakeReconSerpent:
        def __init__(
            self,
            *,
            vhost_target=None,
            vhost_domain=None,
            vhost_wordlist=None,
        ):
            calls.append(
                (
                    "serpent",
                    vhost_target,
                    vhost_domain,
                    vhost_wordlist,
                )
            )

    class FakeCapabilityRouter:
        def __init__(self, serpents):
            calls.append(("router", serpents))

        def execute_recommendation(
            self,
            selected_recommendation,
            context,
        ):
            calls.append(
                (
                    "execute",
                    selected_recommendation,
                    context,
                )
            )
            return [{"executed": True}]

    monkeypatch.setattr(
        "cli.observer_shell.ReconSerpent",
        FakeReconSerpent,
    )
    monkeypatch.setattr(
        "cli.observer_shell.CapabilityRouter",
        FakeCapabilityRouter,
    )
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: "y",
    )

    shell = ObserverShell({})

    monkeypatch.setattr(
        shell,
        "show_plan",
        lambda: calls.append(("replan",)),
    )

    shell.execute_plan_recommendation(
        "plan execute 1 "
        "--wordlist '/tmp/subdomain words.txt'"
    )

    output = capsys.readouterr().out

    assert calls[0] == (
        "serpent",
        "http://10.10.11.10",
        "paper.htb",
        "/tmp/subdomain words.txt",
    )

    assert calls[1][0] == "router"
    assert len(calls[1][1]) == 1

    executed_recommendation = calls[2][1]

    assert executed_recommendation.required_inputs == ()
    assert executed_recommendation.inputs == (
        ("target", "http://10.10.11.10"),
        ("domain", "paper.htb"),
        ("wordlist", "/tmp/subdomain words.txt"),
    )
    assert executed_recommendation.executable is True
    assert calls[2][2] is shell.mission_context
    assert calls[3] == ("replan",)

    assert "Capability execution completed" in output


