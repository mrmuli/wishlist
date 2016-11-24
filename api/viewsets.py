
from serializers import BucketlistSerializer, BucketlistItemSerializer, UserSerializer
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from models import Bucketlist, BucketlistItem


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BucketlistView(generics.ListCreateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def get_queryset(self):
        return Bucketlist.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BucketlistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class BucketlisItemView(generics.CreateAPIView):
    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer

    def get_queryset(self):
        buck_id = self.kwargs['pk']
        return BucketlistItem.objects.filter(bucketlist=buck_id)


class BucketlistItemUpdate(generics.UpdateAPIView):
    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer

    def get_queryset(self):
        buck_id = self.kwargs['buck_id']
        item_id = self.kwargs['pk']
        bucketlistitem = BucketlistItem.objects.filter(id=item_id, bucketlist=buck_id)
        return bucketlistitem


class BucketlistItemDestroy(generics.DestroyAPIView):
    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer

    def get_queryset(self):
        buck_id = self.kwargs['buck_id']
        item_id = self.kwargs['pk']
        bucketlistitem = BucketlistItem.objects.filter(id=item_id, bucketlist=buck_id)
        return bucketlistitem
