from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from apps.shared.rajaongkir import RajaOngkirAPI
import json
import http.client


class GetProvinces(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            connection, headers = RajaOngkirAPI.get_instance()
            endpoint = "/starter/province"
            connection.request("GET", endpoint, headers=headers)
            response = connection.getresponse()

            if response.status == 200:
                data = response.read()
                return Response(
                    json.loads(data.decode("utf-8")), status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "error": f"Failed to fetch province data from RajaOngkir API. Status code: {response.status}"
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except Exception as error:
            return Response(
                {
                    "error": f"Failed to fetch province data from RajaOngkir API: {error}"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class GetShippingCost(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            ongkos_dto = request.data
            connection, headers = RajaOngkirAPI.get_instance()
            endpoint = "/starter/cost"
            payload = {
                "origin": ongkos_dto["asal"],
                "destination": ongkos_dto["tujuan"],
                "weight": ongkos_dto["berat"],
                "courier": ongkos_dto["kurir"],
            }
            payload_str = "&".join([f"{key}={value}" for key, value in payload.items()])
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            connection.request("POST", endpoint, body=payload_str, headers=headers)
            response = connection.getresponse()

            if response.status == 200:
                data = response.read()
                return Response(
                    json.loads(data.decode("utf-8")), status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "error": f"Failed to get shipping cost from RajaOngkir API. Status code: {response.status}"
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except Exception as error:
            return Response(
                {"error": f"Failed to get shipping cost from RajaOngkir API: {error}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class GetCity(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id_prov):
        try:
            connection, headers = RajaOngkirAPI.get_instance()
            endpoint = f"/starter/city?province={id_prov}"
            connection.request("GET", endpoint, headers=headers)
            response = connection.getresponse()

            if response.status == 200:
                data = response.read()
                return Response(
                    json.loads(data.decode("utf-8")), status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "error": f"Failed to fetch city data from RajaOngkir API. Status code: {response.status}"
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except Exception as error:
            return Response(
                {"error": f"Failed to fetch city data from RajaOngkir API: {error}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
