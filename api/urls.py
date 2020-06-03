from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from api.views import open, ServiceListAPIView, ServiceDetailAPIView

app_name = 'account'

urlpatterns = [

    path('login/', obtain_jwt_token),  # -> see accounts/api/views.py for response and url info
    path('services/', ServiceListAPIView.as_view()),
    path('stat/', open),
    path('services/<int:service_id>/', ServiceDetailAPIView.as_view()),
]