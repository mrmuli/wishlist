from rest_framework import serializers
from models import Bucketlist, BucketlistItem
from django.contrib.auth.models import User


class BucketlistItemSerializer(serializers.ModelSerializer):
    """
    Serialier class for a bucketlist item
    """
    def validate_name(self, data):
        if data['name'] == " ":
            raise serializers.ValidationError('Name cannot be empty!')
        return data

    def validate_bucketlists(self, name):

        view = self.context['view']
        bucket_id = view.kwargs['id']
        if self.context['request'].method == 'POST':
            item = BucketlistItem.object.filter(item_name__iexact=item_name)
        elif self.context['request'].method == 'PUT':
            item_id = vire.kwargs['pk']
            item = BucketlistItem.object.filter(item_name__iexact=item_name, bucketlist=bucket_id).exclude(id=item_id)
        if item:
            raise serializers.ValidationError('You already have that item!')
            return name

    class Meta:
        model = BucketlistItem
        fields = ('id', 'item_name', 'date_created', 'date_modified', 'is_done')
        read_only_fields = ('id', 'date_created', 'date_modified')


class BucketlistSerializer(serializers.ModelSerializer):
    """
    serializer class for bucketlists
    """
    bucketlist_items = BucketlistItemSerializer(many=True, read_only=True)

    def validate_bucketlists(self, name):
        user = self.context['request'].user
        view = self.context['view']
        bucket_id = view.kwargs['id']
        if self.context['request'].method == 'POST':
            buck = Bucketlist.object.filter(name__iexact=name, created_by=user)
        elif self.context['request'].method == 'PUT':
            buck = Bucketlist.object.filter(name__iexact=name, created_by=user).exclude(id=bucket_id)
        if buck:
            raise serializers.ValidationError('You already have that bucketlist!')
            return name

    def validate_name(self, data):
        if data['name'] == " ":
            raise serializers.ValidationError('Name cannot be empty!')
        return data

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
