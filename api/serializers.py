from rest_framework import serializers
from models import Bucketlist, BucketlistItem
from django.contrib.auth.models import User


class BucketlistSerializer(serializers.ModelSerializer):
    items = BucketlistitemSerializer(many=True, read_only=True)

    class Meta:
        model = Bucketlist
        fields = ('name', 'description', 'date_created', 'date_modified', 'created_by', 'items')
        read_only_fields = ('id', 'date_created', 'date_modified', 'items')


class BucketlistItemSerializer(serializers.ModelSerializer):
    bucketlist = serializers.StringRelatedField(many=True)

    class Meta:
        model = BucketlistItem
        fields = ('item_name', 'date_created', 'date_modified', 'bucketlist', 'is_done', 'bucketlist')
        read_only_fields = ('id', 'date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    bucketlists = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'bucketlists')

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
