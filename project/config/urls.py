from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   re_path(r'^simpleapp/', include('simpleapp.urls')),
   re_path(r'^news/', include('news.urls')),
]