from django.urls import path
from .views import SliderList, SliderDetail, SliderCreate

urlpatterns = [
    path("", SliderList.as_view(), name="slider-list"),
    path("create", SliderCreate.as_view(), name="slider-create"),
    path("<int:pk>", SliderDetail.as_view(), name="slider-detail"),
]
