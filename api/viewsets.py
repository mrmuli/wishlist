
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
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BucketlistView(BaseMixin, generics.ListCreateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def get_queryset(self):
        """
        This view returns a list of all the bucketlists
        for the currently authenticated user.
        """
        return Bucketlist.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=self.request.user)


class BucketlistDetail(BaseMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class BucketlisItemView(BaseMixin, generics.CreateAPIView):
    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer

    def get_queryset(self):
        buck_id = self.kwargs['pk']
        return BucketlistItem.objects.filter(bucketlist=buck_id)

    def perform_create(self, serializer):
        buck_id = Bucketlist.objects.filter(id=int(self.kwargs['pk'])).first()
        serializer.save(bucketlist=buck_id)



class BucketlistitemDetail(BaseMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer

    def get_queryset(self):
        buck_id = self.kwargs['id']
        item_id = self.kwargs['pk']
        bucketlistitem = BucketlistItem.objects.filter(id=item_id, bucketlist=buck_id)
        return bucketlistitem


# class BucketlistItemUpdate(BaseMixin, generics.UpdateAPIView):
#     queryset = BucketlistItem.objects.all()
#     serializer_class = BucketlistItemSerializer
#
#     def get_queryset(self):
#         buck_id = self.kwargs['id']
#         item_id = self.kwargs['pk']
#         bucketlistitem = BucketlistItem.objects.filter(id=item_id, bucketlist=buck_id)
#         return bucketlistitem
#
#
# class BucketlistItemDestroy(BaseMixin, generics.DestroyAPIView):
#     queryset = BucketlistItem.objects.all()
#     serializer_class = BucketlistItemSerializer
#
#     def get_queryset(self):
#         buck_id = self.kwargs['id']
#         item_id = self.kwargs['pk']
#         bucketlistitem = BucketlistItem.objects.filter(id=item_id, bucketlist=buck_id)
#         return bucketlistitem
