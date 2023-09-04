from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from .models import User
from api.home.serializers import BoardCreateSerializer
from api.home.models import Board, BoardMember
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_board(self,user):
        board = Board.objects.select_related('creator',).filter(creator = user)
        board_member = BoardMember.objects.select_related('board', 'member').filter(member = user)
        print(board, board_member, user, "salom")
        context = {"boards": {}, "member_boards": {}}
        for i in board:
            context['boards'].update({
                "board_id": i.id,
                "title": i.title
            })
        for i in board_member:
            context['member_boards'].update({
                "board_id": i.id,
                "title": i.board.title,
                "board_creator":{
                    "first_name": i.board.creator.first_name,
                    "last_name": i.board.creator.last_name,
                    "phone": i.board.creator.phone
                }
            })
        return context

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        board = self.get_board(user)
        data['data'] = {
            'id': user.id,
            "phone": user.phone,
            "item": board
        }
        return data


class UserRegisterSerialzier(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True, required=True)
    password2 = serializers.CharField(max_length=255, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('phone','password1', 'password2')

    def validate(self, attrs):
        data = super().validate(attrs)
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if (not password1 or not password2) or (password1 != password2):
            raise serializers.ValidationError("Paswords not given or not mutch")
        return data

    def create(self, validated_data):
        user = User(
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password1'])
        user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'password', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            validated_data.pop('password')
        for key, value in validated_data.items():
            setattr(instance,key, value)
        instance.save()
        return instance
    