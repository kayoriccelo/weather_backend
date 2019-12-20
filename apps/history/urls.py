from rest_framework.routers import DefaultRouter

from .viewsets import HistoryViewSet


router = DefaultRouter()
router.register(r'history', HistoryViewSet)
