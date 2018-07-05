from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/role/post/all', views.insert),
    path('api/v1/role/delete/id', views.delete_by_id),
    path('api/v1/role/get/all', views.select_all),
    path('api/v1/role/get/id', views.select_by_id),
    path('api/v1/role/patch/all', views.update_by_id),
]
