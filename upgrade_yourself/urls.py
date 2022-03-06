from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from account.urls import router as account_router
from scheduler.urls import router as scheduler_router
from symptom.urls import router as symptom_router

router = routers.DefaultRouter()
router.registry.extend(account_router.registry)
router.registry.extend(scheduler_router.registry)
router.registry.extend(symptom_router.registry)


urlpatterns = [
    path("", include(router.urls)),
    path("", include("my_auth.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
