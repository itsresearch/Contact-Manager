from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.contact_list, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("delete/<int:id>/",views.contact_delete, name="delete-contact"),
    path("update/<int:id>/",views.contact_update, name="update-contact"),
    path("create/",views.contact_create,name="create-contact"),
    ]