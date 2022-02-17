from todos.views import TodoAPIView, TodoDetailAPIView
from django.urls import path


urlpatterns = [
    path("", TodoAPIView.as_view(), name="todos"),
    path("<int:id>", TodoDetailAPIView.as_view(), name="todo"),
]