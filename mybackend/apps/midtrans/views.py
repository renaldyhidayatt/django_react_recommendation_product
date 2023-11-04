from apps.shared.midtrans import snap
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import uuid4


class CreateTransaction(APIView):
    def post(self, request):
        try:
            order_id = "order-csb-" + str(uuid4())
            gross_amount = request.data.get("gross_amount")
            firstname = request.data.get("firstname")
            lastname = request.data.get("lastname")
            email = request.data.get("email")
            phone = request.data.get("phone")

            parameter = {
                "transaction_details": {
                    "order_id": order_id,
                    "gross_amount": gross_amount,
                },
                "credit_card": {
                    "secure": False,
                },
                "customer_details": {
                    "first_name": firstname,
                    "last_name": lastname,
                    "email": email,
                    "phone": phone,
                },
                "callbacks": {
                    "finish": "http://localhost:3000/orders",
                },
            }

            response = snap.create_transaction(parameters=parameter)

            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"error": f"Failed to create transaction: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
