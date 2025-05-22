from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='index'),
    path("delete/<int:id>/",views.contact_delete, name="delete-contact"),
    path("update/<int:id>/",views.contact_update, name="update-contact"),
    path("create/",views.contact_create,name="create-contact"),
    ]