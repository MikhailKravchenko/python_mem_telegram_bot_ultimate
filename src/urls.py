from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from src.settings import MEDIA_ROOT, MEDIA_URL, config

schema_view = get_schema_view(
    openapi.Info(
        title=config.SWAGGER_TITLE,
        default_version="v1",
        description=config.SWAGGER_DESCRIPTION,
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path(
        "api/v1/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
