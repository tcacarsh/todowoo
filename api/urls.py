from django.urls import path
from . import views

urlpatterns = [
    # ToDos
    path('todos', views.ToDoListCreate.as_view()),
    path('todos/<int:pk>', views.ToDoRetrieveDestroy.as_view()),
    path('todos/completed', views.ToDoCompletedList.as_view()),
    path('todos/<int:pk>/complete', views.ToDoComplete.as_view()),

    # API
    path('signup', views.signup),
    path('login', views.login),
]