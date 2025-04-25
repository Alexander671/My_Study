from typing import Dict, Any

from django.urls import path
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES

urlpatterns = [
    # Swagger
    path('swagger_yml/', SpectacularAPIView.as_view(), name='schema'),

    # Optional UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


class CustomAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = 'user.authentication.CustomAuthentication'
    name = 'JWT authentication'

    def get_security_definition(self, auto_schema: AutoSchema) -> Dict[str, Any]:
        return build_bearer_security_scheme_object(
            header_name='Authorization',
            token_prefix=AUTH_HEADER_TYPES
        )
