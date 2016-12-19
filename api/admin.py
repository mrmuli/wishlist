from django.contrib import admin
from models import Bucketlist, BucketlistItem

class BucketlistAdmin(admin.ModelAdmin):
    """ Bucketlist model admin display """
    model = Bucketlist
    list_display = ('name', 'date_created', 'date_modified')
    list_filter = ['name']
    search_fields = ['name', 'created_by']


class BucketlistItemAdmin(admin.ModelAdmin):
    """ Bucketlist item model admin display """
    model = BucketlistItem
    list_display = ('item_name', 'bucketlist', 'is_done')


admin.site.register(Bucketlist, BucketlistAdmin)
admin.site.register(BucketlistItem, BucketlistItemAdmin)
