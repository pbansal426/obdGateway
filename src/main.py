import time
from config_loader import load_config
from data_source import SimulationDataSource, RealOBDDataSource
from uploader import Uploader


def main():
    config = load_config()

    mode = config["mode"]
    interval = config["upload_interval_seconds"]

    if mode == "SIMULATION":
        print("Running in SIMULATION mode")
        data_source = SimulationDataSource()

    elif mode == "REAL":
        print("Running in REAL OBD mode")
        data_source = RealOBDDataSource(config["obd_port"])

    else:
        raise Exception("Invalid mode in settings.json")

    uploader = Uploader(
        config["server_url"],
        config["vehicle_id"]
    )

    while True:
        data = data_source.get_data()
        uploader.send(data)
        time.sleep(interval)


if __name__ == "__main__":
    main()