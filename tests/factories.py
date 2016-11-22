from django.contrib.auth.models import User
from api.models import Bucketlist, BucketlistItem
import factory


class BucketlistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bucketlist


class BucketlistItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BucketlistItem


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
