from django.urls import path,include
from .views import index,project,project_click
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name="home"),
    path('project/',project,name="project"),
    path('project/<int:project_id>/click/', project_click, name='project_click'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)