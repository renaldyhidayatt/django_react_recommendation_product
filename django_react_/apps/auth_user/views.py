from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterationSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["email"] = user.email
        token["name"] = user.name

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.
class RegisterView(APIView):
    permission_classes = (AllowAny,)
    serializers_class = RegisterationSerializer

    def post(self, request):
        context = {"request": request}
        serialized = self.serializers_class(data=request.data, context=context)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        data = {"success": True}
        data.update(serialized.data)

        return Response(data=data, status=status.HTTP_201_CREATED)
