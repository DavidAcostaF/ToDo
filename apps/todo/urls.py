from django.urls import path
from apps.todo import views
urlpatterns = [
    path('delete_todo/<int:pk>',views.DeleteTodo.as_view(),name='delete_todo'),
    path('end_task/<int:pk>',views.EndTask.as_view(),name = 'end_task'),
    path('finished_task/',views.FinishedTask.as_view(),name= 'finished_task')
]