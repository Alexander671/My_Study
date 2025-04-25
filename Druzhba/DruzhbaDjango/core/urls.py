from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from qr_code.views import serve_qr_code_image

from core.settings import ENV, PROJECT_NAME, STATIC_ROOT, MEDIA_ROOT
from .yasg import urlpatterns as docs

admin.site.site_title = ENV
admin.site.index_title = PROJECT_NAME
admin.site.site_header = f'{PROJECT_NAME} | {ENV}'

urlpatterns = [
    path('admin/', admin.site.urls),

    # static for DEBUG = False
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

    # media url
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # qr code url
    path('qr-code/', serve_qr_code_image, name='qr_code'),

    # Swagger
    *docs
]
