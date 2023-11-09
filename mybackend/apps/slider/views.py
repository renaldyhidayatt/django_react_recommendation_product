from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .models import Slider
from .serializers import SliderSerializer


class SliderList(APIView):
    def get(self, request):
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        return Response(serializer.data)


class SliderCreate(APIView):
    def post(self, request):
        serializer = SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SliderDetail(APIView):
    def get_object(self, pk):
        try:
            return Slider.objects.get(pk=pk)
        except Slider.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        slider = self.get_object(pk)
        serializer = SliderSerializer(slider)
        return Response(serializer.data)

    def put(self, request, pk):
        slider = self.get_object(pk)
        serializer = SliderSerializer(slider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        slider = self.get_object(pk)
        slider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
