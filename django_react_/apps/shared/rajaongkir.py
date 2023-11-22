import os
import http.client


class RajaOngkirAPI:
    base_url = "api.rajaongkir.com"
    api_key = os.environ.get("RAJAONGKIR_API")

    @staticmethod
    def get_instance():
        connection = http.client.HTTPSConnection(RajaOngkirAPI.base_url)
        headers = {
            "key": RajaOngkirAPI.api_key,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        return connection, headers
