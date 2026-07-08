from pathlib import Path
import subprocess

from core.adapters.base import ToolAdapter
from core.config import Config
from core.engine import TridentEngine
from core.parsers.nmap.xml_parser import NmapXMLParser
from core.services.observation_emitter import ObservationEmitter
from core.services.observation_engine import ObservationEngine

class NmapAdapter(ToolAdapter):
    """
    Executes Nmap and records the run as Trident intelligence input.
    """

    def __init__(self, target: str):
        self.target = target
        self.engine = TridentEngine()

    def execute(self):
        mission_id = self.engine.state.get_active_mission()

        run = self.engine.tool_runs.create(
            tool="nmap",
            target=self.target,
            mission_id=mission_id,
        )

        evidence_root = Config.KNOWLEDGE_DIR / "evidence" / "nmap"
        evidence_root.mkdir(parents=True, exist_ok=True)

        xml_path = evidence_root / f"{run.id}.xml"

        command = [
            "nmap",
            "-sV",
            "-oX",
            str(xml_path),
            self.target,
        ]

        subprocess.run(command, check=True)

        run.evidence.append(str(xml_path))

        # Parse Nmap XML into native observations
        parser = NmapXMLParser()
        observations = parser.parse(xml_path)

        # Emit canonical observations
        emitter = ObservationEmitter()
        engine = ObservationEngine()

        for obs in observations:
            emitted = emitter.emit(
                mission_id=mission_id,
                tool_run_id=run.id,
                evidence_id=str(xml_path),
                category="port",
                data={
                    "host": obs.host,
                    "port": obs.port,
                    "protocol": obs.protocol,
                    "state": obs.state,
                    "service": obs.service,
                    "product": obs.product,
                    "version": obs.version,
                    "extrainfo": obs.extrainfo,
                },
            )

            run.observations.append(emitted.id)
            engine.process(emitted)

        # Save the updated ToolRun
        self.engine.tool_runs.repository.save(run)

        return run