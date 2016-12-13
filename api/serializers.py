from rest_framework import serializers
from models import Bucketlist, BucketlistItem
from django.contrib.auth.models import User


class BucketlistItemSerializer(serializers.ModelSerializer):
    """
    Serialier class for a bucketlist item
    """

    class Meta:
        model = BucketlistItem
        fields = ('id', 'item_name', 'date_created', 'date_modified', 'is_done')
        read_only_fields = ('id', 'date_created', 'date_modified')


class BucketlistSerializer(serializers.ModelSerializer):
    """
    serializer class for bucketlists
    """
    bucketlist_items = BucketlistItemSerializer(many=True, read_only=True)

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'description', 'date_created', 'date_modified', 'bucketlist_items')
        read_only_fields = ('id', 'date_created', 'date_modified','created_by', 'bucketlist_items')


class UserSerializer(serializers.ModelSerializer):
    """
    serializer class for Users
    """
    bucketlists = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'bucketlists')

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
