from django.contrib import admin
from django.urls import path, include
from core.views import home_view

urlpatterns = [
    path('', home_view, name='home'),  # ✅ now / will work
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),  
]
