from django.urls import path,include
from .views import index,project,blogs
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name="home"),
    path('project/',project,name="project"),
    path('blog/',blogs,name="blogs"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)