import random
import time
from datetime import datetime

try:
    import obd
except ImportError:
    obd = None


class SimulationDataSource:
    def get_data(self):
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "rpm": random.randint(700, 3500),
            "speed": random.randint(0, 120),
            "coolant_temp": random.randint(70, 100)
        }


class RealOBDDataSource:
    def __init__(self, port):
        if obd is None:
            raise Exception("OBD library not installed")
        self.connection = obd.OBD(port, fast=False)

        if not self.connection.is_connected():
            raise Exception("Failed to connect to OBD device")

    def get_data(self):
        rpm = self.connection.query(obd.commands.RPM).value
        speed = self.connection.query(obd.commands.SPEED).value
        coolant = self.connection.query(obd.commands.COOLANT_TEMP).value

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "rpm": str(rpm),
            "speed": str(speed),
            "coolant_temp": str(coolant)
        }