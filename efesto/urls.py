from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='lang')),
    path('gallery/', include('gallery.urls', namespace='lang')),
    path('project/<int:id>', include('project.urls', namespace='lang')),
    path('team/', include('team.urls', namespace='lang')),
    path('team/<int:id>', include('team.urls', namespace='lang')),
   # path('services/', views.services),
   # path('contact-us/', views.contact_us),
   # path('news/', views.news),
]

urlpatterns += i18n_patterns (
    path('', include('home.urls', namespace='lang')),
    path('gallery/', include('gallery.urls', namespace='lang')),
    path('project/', include('project.urls', namespace='lang')),
    path('team/', include('team.urls', namespace='lang')),
)