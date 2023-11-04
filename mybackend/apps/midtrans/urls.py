from django.urls import path
from . import views

urlpatterns = [
    path(
        "create-transaction",
        views.CreateTransaction.as_view(),
        name="create-transaction",
    ),
]
