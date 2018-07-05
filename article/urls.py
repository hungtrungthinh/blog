from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/article/post/all', views.insert),
    path('api/v1/article/delete/id', views.delete_by_id),
    path('api/v1/article/get/all', views.select_all),
    path('api/v1/article/get/id', views.select_by_id),
    path('api/v1/article/patch/all', views.update_by_id),
]
