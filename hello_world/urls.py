from django.contrib import admin
from django.urls import path, include
from .views import chat_view, index  # make sure to import index
from hello_world.core.views import sessions_view

# urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls')),
    path('chat/', chat_view, name='chat_view'),
    path("sessions/", sessions_view, name='sessions_view'),
    path("", index, name='index_view'),  
]

