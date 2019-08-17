from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as user_views
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from . import apis

router = DefaultRouter()
router.register('profile', user_views.UserProfileViewSet)

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('home', user_views.home, name='home'),
    path('register', user_views.register, name='register'),
    path('create', user_views.ListCreateConsumer.as_view(), name='create'),
    path('create/consumer', user_views.CreateConsumer.as_view(), name='create_consumer'),
    path('api/login', csrf_exempt(user_views.UserLoginApiView.as_view()), name='api+login'),
    path('driver/orders/ready', apis.GetOrdersListApiView.as_view()),

    path('', include(router.urls)),

]
