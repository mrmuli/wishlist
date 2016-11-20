from django.contrib import admin
from models import Bucketlist, BucketlistItem

class BucketlistAdmin(admin.ModelAdmin):
    model = Bucketlist
    list_display = ('name', 'date_created', 'date_modified')
    list_filter = ['name']
    search_fields = ['name', 'created_by']


class BucketlistItemAdmin(admin.ModelAdmin):
    model = BucketlistItem
    list_display = ('name', 'date_created', 'date_modified')


admin.site.register(Bucketlist, BucketlistAdmin)
admin.site.register(BucketlistItem, BucketlistItemAdmin)
