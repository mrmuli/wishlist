from django.contrib.auth.models import User
from api.models import Bucketlist, BucketlistItem
import factory


class BucketlistFactory(factory.django.DjangoModelFactory):
    """ Bucketlist Factory Class """
    class Meta:
        model = Bucketlist


class BucketlistItemFactory(factory.django.DjangoModelFactory):
    """ Bucketlist item Factory Class """
    class Meta:
        model = BucketlistItem


class UserFactory(factory.django.DjangoModelFactory):
    """ User Factory Class """
    class Meta:
        model = User
