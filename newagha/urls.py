from django.contrib import admin
from django.conf import settings # new
from django.conf.urls.static import static # new
from django.urls import path, include
from ajb.views import home
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='master_homepage' ),
    # path('blog', allpst , name='alblogs' ),

    path('schemes/', include('ajbs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)