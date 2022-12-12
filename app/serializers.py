from rest_framework.serializers import ModelSerializer, IntegerField, SerializerMethodField, CharField
from django.contrib.auth.models import User

from .models import Entity, Property

class UserSerializer(ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class PropertySerializer(ModelSerializer):

    class Meta:
        model = Property
        fields = ("key", "value")

    def to_representation(self, instance):
        return instance.key, instance.value


class EntityPostSerializer(ModelSerializer):

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        try:
            self.initial_data = {
                'value': data['data[value]']
            }
        except Exception:
            print('Некорректные данные ')


    class Meta:
        model = Entity
        fields = ('value', )


class EntitySerializer(ModelSerializer):
    properties = PropertySerializer(many=True)
    value = IntegerField()

    class Meta:
        model = Entity
        fields = ("value", "properties")

    def to_representation(self, instance):
        data = {}
        for i in instance.properties.all():
            data[i.key]=i.value
        return {
            "value": instance.value,
            "properties": data
        }