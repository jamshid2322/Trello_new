from django.urls import path
from .views import (
    BoardApi,
    BoardEditApi,
    TaskConditionApi,
    TaskConditionsEdit,
    TaskItemApi,
    TaskItemEdit,
    BoardMemberApi,
    BoardMemberEditApi,
    SubTaskApi,
    SubTaskEditApi,
    BoardGetApi
    

)

urlpatterns = [
    path('board/', BoardApi.as_view()),
    path('board/<int:pk>/', BoardApi.as_view()),
    path('board/all/<int:pk>/',BoardGetApi.as_view()),

    path('task/',TaskConditionApi.as_view()),
    path('task/details/<int:pk>/',TaskConditionsEdit.as_view()),

    path('task_item/',TaskItemApi.as_view()),
    path('task_item/details/<int:pk>/',TaskItemEdit.as_view()),

    path("sub_task/", SubTaskApi.as_view()),
    path("sub_task/details/<int:pk>/", SubTaskEditApi.as_view()),

    path("board_member/", BoardMemberApi.as_view()),
    path("board_member/details/<int:pk>/", BoardMemberEditApi.as_view())
]