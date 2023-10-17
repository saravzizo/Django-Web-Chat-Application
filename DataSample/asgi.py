
import os
import django

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path

from Chat import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataSample.settings')
django.setup()

import django
django.setup()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack
    (
        URLRouter(
           routing.websocket_urlpatterns
        )

    )
})