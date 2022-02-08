from django.urls import path
from.import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<taskid>', views.deletetask, name='deletetask'),
    path('edit/<taskid>', views.edittask, name='edittask'),
    path('completed/<taskid>', views.completed, name='completed'),
    path('pending/<taskid>', views.pending, name='pending'),
]
