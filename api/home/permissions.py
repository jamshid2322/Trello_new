from rest_framework.permissions import BasePermission
from .models import Board

class IsCreator(BasePermission):
    message = "You cannot modify this board's information."

    def has_permission(self, request, view):
        boards = Board.objects.select_related("creator").filter(creator_id = request.user.id)
        board = Board.objects.select_related("creator").filter(id = view.kwargs.get('pk')).first()
        for board_item in boards:
            if board_item == board:
                return True
        return False