import imp
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.i18n import i18n_patterns
#from django.utils.translation import gettext_lazy as _
from efesto.settings import IMAGES_PATH
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Efesto Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='lang')),
    path('gallery/', include('gallery.urls', namespace='lang')),
    path('project/<int:id>', include('project.urls', namespace='lang')),
    path('team/', include('team.urls', namespace='lang')),
    path('team/<int:id>', include('team.urls', namespace='lang')),
    path('services/', include('services.urls', namespace='lang')),
    path('contact_us/', include('contact_us.urls', namespace='lang')),
    path('news/', include('news.urls', namespace='lang')),
    path('news/<int:id>', include('news.urls', namespace='lang')),
]

urlpatterns += i18n_patterns (
    path('', include('home.urls', namespace='lang')),
    path('gallery/', include('gallery.urls', namespace='lang')),
    path('project/', include('project.urls', namespace='lang')),
    path('team/', include('team.urls', namespace='lang')),
    path('team/<int:id>', include('team.urls', namespace='lang')),
    path('services/', include('services.urls', namespace='lang')),
    path('contact_us/', include('contact_us.urls', namespace='lang')),
    path('news/', include('news.urls', namespace='lang')),
    path('news/<int:id>', include('news.urls', namespace='lang')),
) 