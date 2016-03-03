from tastypie.resources import ModelResource
from .models import Directory

class DirectoryResource(ModelResource):
    class Meta:
        queryset = Directory.objects.all()
        resource_name = 'directory'