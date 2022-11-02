from django.contrib.auth.urls import urlpatterns
from django.urls import path

from . import views
urlpatterns = [
    path('',views.task,name='task'),
    path('result',views.task_view,name='task_view')

]