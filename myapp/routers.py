from rest_framework.routers import DefaultRouter
from .viewsets import TodoViewSets
# from .urls import urlpatterns

router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSets,  basename= 'viewset-todo')

# urlpatterns+=router.urls