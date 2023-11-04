from django.urls import path
from .views import CartListByUser, CartCreate, CartDelete, CartDeleteMany

urlpatterns = [
    path("user", CartListByUser.as_view(), name="cart-list-by-user"),
    path("create", CartCreate.as_view(), name="cart-create"),
    path("delete/<int:cart_id>", CartDelete.as_view(), name="cart-delete"),
    path("delete-many", CartDeleteMany.as_view(), name="cart-delete-many"),
]
