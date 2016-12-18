
from serializers import BucketlistSerializer, BucketlistItemSerializer, UserSerializer
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from models import Bucketlist, BucketlistItem
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly


class BaseMixin(object):
    """
    The class contained shared resources amongst viewsets
    i.e. : permissions, filtering and authentication
    """
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)


class UserViewSet(viewsets.ModelViewSet):
    """
    The class contained creates users via requests
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BucketlistView(BaseMixin, generics.ListCreateAPIView):
    """
    The class creates and retrieves Bucketlists
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def get_queryset(self):
        """ Method to return bucketlists by user """
        return Bucketlist.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        """ Method to save bucketlists by user """
        user = self.request.user
        serializer.save(created_by=self.request.user)


class BucketlistDetail(BaseMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    The class retrieves, updates and destroys bucketlists
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class BucketlisItemView(BaseMixin, generics.CreateAPIView):
    """
    The class creates bucketlist items
    """
    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer

    def get_queryset(self):
        """ Method to return bucketlist items by bucketlists """
        buck_id = self.kwargs['pk']
        return BucketlistItem.objects.filter(bucketlist=buck_id)

    def perform_create(self, serializer):
        """ Method to save bucketlist items by bucketlist """
        buck_id = Bucketlist.objects.filter(id=int(self.kwargs['pk'])).first()
        serializer.save(bucketlist=buck_id)



class BucketlistitemDetail(BaseMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    The class retrieves, updates and destroys bucketlist items
    """
    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer

    def get_queryset(self):
        """ Method to get bucketlist item by id """
        buck_id = self.kwargs['id']
        item_id = self.kwargs['pk']
        bucketlistitem = BucketlistItem.objects.filter(id=item_id, bucketlist=buck_id)
        return bucketlistitem
