from core.briefings.mission_brief import MissionBrief
from core.council.council_session import CouncilSession


class Reporter:
    """
    Voice of the Council.

    Reporter transforms a completed CouncilSession into a concise
    operational briefing for the Observer.

    Reporter does not investigate, verify, or create evidence.
    """

    name = "Reporter"

    def brief(
        self,
        session: CouncilSession,
    ) -> MissionBrief:
        assessments = session.assessments

        members = [
            assessment.member
            for assessment in assessments
        ]

        findings = self._unique(
            finding
            for assessment in assessments
            for finding in assessment.findings
        )

        recommendations = self._unique(
            recommendation
            for assessment in assessments
            for recommendation in assessment.recommendations
        )

        warnings = self._unique(
            warning
            for assessment in assessments
            for warning in assessment.warnings
        )

        confidence = self._briefing_confidence(
            assessments
        )

        oracle = next(
            (
                assessment
                for assessment in assessments
                if assessment.member.lower() == "oracle"
            ),
            None,
        )

        if oracle is not None:
            executive_summary = oracle.summary
        elif assessments:
            executive_summary = assessments[-1].summary
        else:
            executive_summary = (
                "The Council produced no assessments."
            )

        context = session.context

        return MissionBrief(
            mission_id=context.current_mission_id(),
            target=self._target(context),
            executive_summary=executive_summary,
            confidence=confidence,
            key_findings=findings,
            priority_actions=recommendations,
            warnings=warnings,
            council_members=members,
        )

    def _briefing_confidence(
        self,
        assessments,
    ) -> float:
        if not assessments:
            return 0.0

        skeptic = next(
            (
                assessment
                for assessment in assessments
                if assessment.member.lower() == "skeptic"
            ),
            None,
        )

        if skeptic is not None:
            return skeptic.confidence

        return sum(
            assessment.confidence
            for assessment in assessments
        ) / len(assessments)

    def _target(
        self,
        context,
    ) -> str | None:
        ports = context.open_ports()

        for port in ports:
            host = port.get("host")

            if host:
                return str(host)

        surfaces = context.web_surfaces()

        for surface in surfaces:
            host = (
                surface.get("host_ip")
                or surface.get("host")
            )

            if host:
                return str(host)

        return None

    def _unique(self, values) -> list[str]:
        return list(
            dict.fromkeys(
                value
                for value in values
                if value
            )
        )