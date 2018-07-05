from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/user/post/all', views.insert),
    path('api/v1/user/delete/id', views.delete_by_id),
    path('api/v1/user/get/all', views.select_all),
    path('api/v1/user/get/id', views.select_by_id),
    path('api/v1/user/patch/all', views.update_by_id),
]
