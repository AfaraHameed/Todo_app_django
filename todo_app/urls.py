from django.contrib.auth.urls import urlpatterns
from django.urls import path

from . import views
urlpatterns = [
    path('',views.task_view,name='task_view'),
    path('delete/<int:task_id>',views.delete,name='delete'),
    path('update/<int:task_id>',views.update,name='update'),
    path('cbvtask/',views.TaskListView.as_view(),name='cbvtask'),
    path('cbvdetail/<int:pk>',views.TaskDetailView.as_view(),name='cbvdetail')

]