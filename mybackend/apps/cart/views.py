from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartSerializer


class CartListByUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        carts = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.data["user"] = request.user.id

        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, cart_id):
        cart = Cart.objects.filter(pk=cart_id).first()
        if cart:
            cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)


class CartDeleteMany(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        cart_ids = request.data.get("cart_ids", [])
        user = request.user
        carts_to_delete = Cart.objects.filter(pk__in=cart_ids, user=user)
        carts_to_delete.delete()

        return Response(
            {"detail": "Carts deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )
