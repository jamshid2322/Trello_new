from rest_framework import serializers

class CustomAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
    def to_representation(self, instance):
        res =  super().to_representation(instance)
        res['created_at'] = instance.created_at.strftime("%b %d, %Y")
        res['update_at'] = instance.update_at.strftime("%b %d, %Y")
        return res