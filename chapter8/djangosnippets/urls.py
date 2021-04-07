from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from snippets.views import top
from snippets import api_views as snippet_api_views

router = routers.DefaultRouter()
router.register('snippets', snippet_api_views.SnippetViewSet)

urlpatterns = [
    path('', top, name='top'),
    path('snippets/', include('snippets.urls')),
    path("accounts/", include("accounts.urls")),
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]
