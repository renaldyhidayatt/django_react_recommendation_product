from django.urls import path
from .views import SliderList, SliderDetail

urlpatterns = [
    path("", SliderList.as_view(), name="slider-list"),
    path("<int:pk>", SliderDetail.as_view(), name="slider-detail"),
]
