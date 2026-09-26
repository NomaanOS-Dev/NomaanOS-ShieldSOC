import os
import glob
import platform
import socket

def read_thermal_sensor():
    """Linux thermal zone check for genuine SoC temperature."""
    thermal_paths = glob.glob("/sys/class/thermal/thermal_zone*/temp")
    if not thermal_paths:
        return None
    try:
        with open(thermal_paths[0], "r") as f:
            raw_temp = f.read().strip()
            return round(float(raw_temp) / 1000.0, 2)
    except Exception:
        return None

def get_genuine_telemetry():
    """Collects actual host metrics without simulation mocks."""
    temp = read_thermal_sensor()
    try:
        load_avg = os.getloadavg()
    except AttributeError:
        load_avg = (None, None, None)

    return {
        "host": socket.gethostname(),
        "arch": platform.machine(),
        "os": platform.system(),
        "temperature_celsius": temp,
        "load_1m": load_avg[0],
        "sensor_source": "sysfs" if temp is not None else "unsupported_hardware"
    }

if __name__ == "__main__":
    import json
    data = get_genuine_telemetry()
    print("=" * 50)
    print("      REAL HOST TELEMETRY PROBE")
    print("=" * 50)
    print(json.dumps(data, indent=2))
    print(f"\n[+] Hardware Interface: {'ACTIVE ✅' if data['temperature_celsius'] else 'FAIL-SAFE (Safe None) ✅'}")
