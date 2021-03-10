"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views import static
from django.views.static import serve
from rest_framework import routers

from drf.settings import MEDIA_ROOT
from goods import views
# from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter() # 路由会显示在页面上
# router = routers.SimpleRouter() # 路由不会显示在页面上
router.register(r'categorys',views.CategoryListView,basename='categorys')
router.register(r'goods',views.GoodsListView,basename='goods')
from rest_framework.authtoken import views as views_token
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('goods/', views.GoodsListView.as_view()),
    # path('categorys/', views.CategoryListView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^api-token-auth/', views_token.obtain_auth_token),
    # re_path(r'^jwt-token-auth/', obtain_jwt_token),
]
