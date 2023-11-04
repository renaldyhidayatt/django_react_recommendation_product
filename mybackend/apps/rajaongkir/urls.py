from django.urls import path
from .views import GetProvinces, GetShippingCost, GetCity

urlpatterns = [
    path("get-provinces/", GetProvinces.as_view(), name="get-provinces"),
    path("get-shipping-cost", GetShippingCost.as_view(), name="get-shipping-cost"),
    path("get-city/<int:id_prov>/", GetCity.as_view(), name="get-city"),
]
