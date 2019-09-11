from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('folder/', include('folder.urls')),
    path('user/', include('user.urls')),
]
