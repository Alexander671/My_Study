from django.urls import path
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularSwaggerView,
                                   SpectacularRedocView)


urlpatterns = [
    # Swagger
    path('swagger_yml/', SpectacularAPIView.as_view(), name='schema'),

    # Optional UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
