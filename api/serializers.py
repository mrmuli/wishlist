from rest_framework import serializers
from models import Bucketlist, BucketlistItem

from django.contrib.auth.models import User


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        fields = ('name', 'description', 'date_created', 'date_modified', 'created_by')

    def create(self, validated_data):
        """
        Create and return a new `Bucketlist` instance, given the validated data.
        """
        return Bucketlist.objects.create(**validated_data)


class BucketlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketlistItem
        fields = ('item_name', 'date_created', 'date_modified', 'bucketlist',)
        

    def create(self, validated_data):
        """
        Create and return a new `Bucketlist` instance, given the validated data.
        """
        return BucketlistItem.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(username=validated_data['username'], email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
