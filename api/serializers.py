from rest_framework import serializers
from models import Bucketlist, BucketlistItem
from django.contrib.auth.models import User
from django.db import IntegrityError

class BucketlistItemSerializer(serializers.ModelSerializer):
    """
    Serialier class for a bucketlist item
    """

    def create(self, validated_data):
        try:
            if not validated_data.get('item_name'):
                raise serializers.ValidationError('The name cannot be empty')
            return super(BucketlistItemSerializer, self).create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError('That name already exists')

    def update(self, instance, validated_data):
        try:
            return super(BucketlistItemSerializer, self).update(instance, validated_data)
        except IntegrityError:
            raise serializers.ValidationError('That name already exists')

    class Meta:
        model = BucketlistItem
        fields = ('id', 'item_name', 'date_created', 'date_modified', 'is_done')
        read_only_fields = ('id', 'date_created', 'date_modified')


class BucketlistSerializer(serializers.ModelSerializer):
    """
    serializer class for bucketlists
    """
    bucketlist_items = BucketlistItemSerializer(many=True, read_only=True)

    def create(self, validated_data):
        try:
            if not validated_data.get('name'):
                raise serializers.ValidationError('The name cannot be empty')
            return super(BucketlistSerializer, self).create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError('That name already exists')

    def update(self, instance, validated_data):
        try:
            return super(BucketlistSerializer, self).update(instance, validated_data)
        except IntegrityError:
            raise serializers.ValidationError('That name already exists')

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
        """
        Method call on User Object creation prompt
        """
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
