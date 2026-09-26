import platform
import time
from typing import Any, Callable, Dict, Optional


class ShieldSOCMonitor:
    """Minimal telemetry adapter with explicit unverified integrity state.

    This module intentionally does not fabricate sensor values or claim integrity
    verification. Production deployments should inject real readers and a real
    integrity verifier.
    """

    def __init__(
        self,
        cpu_temperature_reader: Optional[Callable[[], Optional[float]]] = None,
        integrity_verifier: Optional[Callable[[], bool]] = None,
    ) -> None:
        self.status = "MONITORING_ACTIVE"
        self._cpu_temperature_reader = cpu_temperature_reader
        self._integrity_verifier = integrity_verifier

    def fetch_telemetry(self) -> Dict[str, Any]:
        cpu_temp = (
            self._cpu_temperature_reader()
            if self._cpu_temperature_reader is not None
            else None
        )
        integrity_verified = (
            bool(self._integrity_verifier())
            if self._integrity_verifier is not None
            else False
        )
        return {
            "schema_version": 1,
            "status": self.status,
            "host": platform.node(),
            "cpu_temp_c": cpu_temp,
            "integrity_check": {
                "verified": integrity_verified,
                "status": "VERIFIED" if integrity_verified else "UNVERIFIED",
            },
            "timestamp": time.time(),
        }


if __name__ == "__main__":
    print("ShieldSOC Telemetry Feed:", ShieldSOCMonitor().fetch_telemetry())
