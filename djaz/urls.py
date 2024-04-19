from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('to-do', views.TodoViewSet, 'to-do')

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('api/', include(router.urls))
]
