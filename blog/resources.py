
from tastypie.resources import ModelResource
from blog.models import Post
from tastypie.authorization import Authorization
from django.contrib.auth.models import User

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        # authorization = Authorization()
        allowed_methods = ['get', 'post']

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ["email", "password", "is_active", "is_staff", "is_superuser", "first_name", "last_name"]
        allowed_methods = ['get']