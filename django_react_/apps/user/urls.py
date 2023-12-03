
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateUser.as_view(), name='create_user'),
    path('', views.GetAllUser.as_view(), name='get_users'),
    path("<int:pk>", views.GetByIdUser.as_view(), name="get_user"),
    path('update/<int:pk>', views.UpdateUser.as_view(), name='update_user'),
    path('delete/<int:pk>', views.DeleteUser.as_view(), name='delete_user'),
]
