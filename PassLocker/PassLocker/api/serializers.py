from django.contrib.auth import get_user_model
from rest_framework import serializers

from PassLocker.groups.models import GroupModel
from PassLocker.main.models import MainModel


UserModel = get_user_model()


class ShortGroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'


class ShortUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'


class GroupModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'

    def create(self, validated_data):
        return GroupModel.objects.create(**validated_data)


class LockerModelSerializer(serializers.ModelSerializer):
    user = ShortUserModelSerializer()
    group = ShortGroupModelSerializer()
    class Meta:
        model = MainModel
        fields = '__all__'


class LockerModelCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainModel
        fields = '__all__'

    def create(self, validated_data):
        return MainModel.objects.create(**validated_data)


class AppUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class AppUserModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)