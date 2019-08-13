from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path 
from django.conf.urls import url
from blog.resources import PostResource, UserResource
from tastypie.api import Api

v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(PostResource())

post_resource = PostResource()

urlpatterns = [
	path('admin/', admin.site.urls),
	path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('', include('blog.urls')),

    url(r'^api/', include(v1_api.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
