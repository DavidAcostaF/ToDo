from django.urls import path
from apps.todo import views
urlpatterns = [
    path('finish_todo/<int:pk>',views.DeleteTodo.as_view(),name='delete_todo')
]