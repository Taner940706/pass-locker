from django.contrib.auth import get_user_model
from rest_framework import serializers

from PassLocker.groups.models import GroupModel
from PassLocker.main.models import MainModel


UserModel = get_user_model()


class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'


class LockerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainModel
        fields = '__all__'


class GroupModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'

    def create(self, validated_data):
        return GroupModel.objects.create(**validated_data)


class MainModelCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainModel
        fields = '__all__'

    def create(self, validated_data):
        return MainModel.objects.create(**validated_data)


class GroupModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'


class LockerModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainModel
        fields = '__all__'


class LockerModelDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainModel
        fields = '__all__'


class GroupModelDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'

