from django.shortcuts import render
from api.home.models import (
    Board,
    TaskCondition ,
    TaskItem,
    BoardMember,
    SubTask

)

from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from api.home.permissions import IsCreator
from api.home.serializers import (
    BoardCreateSerializer,
    TaskConditionSerializer,
    TaskItemSerializer,
    SubTaskSerializer,
    BoardMemberSerializer
)
from rest_framework.views import APIView

# Create your views here.
class BoardApi(
    ListCreateAPIView):

    permission_classes = (IsAuthenticated, )
    queryset = Board.objects.all().select_related("creator")
    serializer_class = BoardCreateSerializer


    def get_queryset(self):
        user = self.request.user
        queryset = Board.objects.filter(creator=user)
        return queryset

class BoardGetApi(
    RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = BoardCreateSerializer


    def get_queryset(self):
        user = self.request.user
        queryset = Board.objects.filter(creator=user)
        return queryset
    

class BoardMemberApi(ListCreateAPIView):
    permission_classes= (IsAuthenticated, )
    queryset = BoardMember.objects.all().select_related("board", "member")
    serializer_class = BoardMemberSerializer

class BoardMemberEditApi(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = BoardMember.objects.all().select_related("board", "member")
    serializer_class = BoardMemberSerializer

class BoardEditApi(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = (IsAuthenticated, IsCreator )
    queryset = Board.objects.all().select_related("creator")
    serializer_class = BoardCreateSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Board.objects.select_related('creator').filter(creator=user)
        return queryset


class TaskConditionApi(
    ListCreateAPIView
):
    permission_classes = (IsAuthenticated, )
    queryset = TaskCondition.objects.all().select_related("creator", "board")
    serializer_class = TaskConditionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = TaskCondition.objects.filter(creator=user)
        return queryset


class TaskConditionsEdit(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = (IsAuthenticated, )
    queryset = TaskCondition.objects.all().select_related("creator", "board")
    serializer_class = TaskConditionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = TaskCondition.objects.filter(creator=user)
        return queryset




class TaskItemApi(
    ListCreateAPIView
):
    permission_classes = (IsAuthenticated, )
    queryset = TaskItem.objects.all().select_related('creator', "task_condition")
    serializer_class = TaskItemSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = TaskItem.objects.filter(creator=user)
        return queryset




class TaskItemEdit(
    RetrieveUpdateDestroyAPIView
):
    permission_classes = (IsAuthenticated, )
    queryset = TaskItem.objects.all().select_related('creator', 'task_condition')
    serializer_class = TaskItemSerializer


    def get_queryset(self):
        user = self.request.user
        queryset = TaskItem.objects.filter(creator=user)
        return queryset



class SubTaskApi(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = SubTask.objects.all().select_related('task_item')
    serializer_class = SubTaskSerializer

class SubTaskEditApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = SubTask.objects.all().select_related('task_item')
    serializer_class = SubTaskSerializer

