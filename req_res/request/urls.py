from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('request/', views.req, name="request"),
    path('request/app-attributes/', views.app_attributes, name="app-attributes"),
    path('request/middleware/', views.middleware, name="middleware"),
    path('request/querydict/', views.querydict, name="querydict"),
    path('request/is-secure/', views.is_secure, name="is-secure"),
    path('response/', views.res, name="response"),
    path('response/subclasses/', views.subclasses, name="subclasses"),
    path('response/json/', views.json, name="json"),
    path('response/streaming/', views.streaming, name="straming"),
    path('response/file/', views.file, name="file"),
    path('response/base/', views.base, name="base"),
]