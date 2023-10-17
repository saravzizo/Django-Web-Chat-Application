from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path


from django.urls import re_path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from Chat.consumers import ChatConsumer


# application = ProtocolTypeRouter({
#     "websocket": URLRouter([
#         path("ws/chat/<str:username>/", consumers.ChatConsumer.as_asgi()),
#     ]),
# })


websocket_urlpatterns = [
    
    path("ws/<str:username>/", ChatConsumer.as_asgi()),
]