from rest_framework import serializers

from PassLocker.groups.models import GroupModel


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


class GroupModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'

