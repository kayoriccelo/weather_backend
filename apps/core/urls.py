from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.history.urls import router as history_routers


router = DefaultRouter()

urlpatterns = (
    router.urls + 
    history_routers.urls
)
