from django.contrib import admin
from django.urls import path, include
from flutter_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data/', views.get_data),
    path('api/data/post/', views.post_data),
    path('api/raisehand/', views.raise_hand),
    path('api/requestinstitute/', views.request_institute),
    path('api/institutedetails/', views.get_institute_details),
    path('api/institutedetails/post/', views.post_institute_details),
    path('api/profile/', views.get_profile),
    path('api/', include('dj_rest_auth.urls')),  
]
