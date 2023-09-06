from django.contrib import admin
from .models import (
    Board,
    TaskCondition,
    TaskItem,
    BoardMember,
    SubTask
)

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "creator")

@admin.register(TaskCondition)
class TaskConditionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "creator", "board", "created_at")

@admin.register(TaskItem)
class TaskItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "creator", "task_condition", "created_at")

@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "board")

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "task_item")