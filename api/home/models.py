from django.db import models
from api.utilitie.models import CustomAbstractModel
from api.user.models import User

# Create your models here.
class Board(CustomAbstractModel):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title

class TaskCondition(CustomAbstractModel):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="task_conditions")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=13)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
class TaskItem(CustomAbstractModel):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    task_condition = models.ForeignKey(TaskCondition, on_delete=models.CASCADE, related_name='task_item')

    def __str__(self) -> str:
        return self.title
class SubTask(CustomAbstractModel):
    title = models.CharField(max_length=255)
    task_item = models.ForeignKey(TaskItem, on_delete=models.CASCADE, related_name="sub_task")

    def __str__(self) -> str:
        return self.title
class BoardMember(CustomAbstractModel):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.member.first_name
