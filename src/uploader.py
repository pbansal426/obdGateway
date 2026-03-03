import requests

class Uploader:
    def __init__(self, server_url, vehicle_id):
        self.server_url = server_url
        self.vehicle_id = vehicle_id

    def send(self, data):
        payload = {
            "vehicle_id": self.vehicle_id,
            "data": data
        }

        try:
            # Uncomment when backend is ready
            # response = requests.post(self.server_url, json=payload, timeout=5)
            # print("Sent:", response.status_code)

            print("Sending:", payload)

        except Exception as e:
            print("Upload failed:", e)