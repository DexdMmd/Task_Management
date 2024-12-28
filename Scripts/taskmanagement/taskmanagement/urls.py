from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from task_management_app.views import TaskView

router = routers.DefaultRouter()
router.register(r'tasks', TaskView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
