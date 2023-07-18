from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name='home'),
    path('events/', include('events.urls')),
    path('search_weather', main.views.search_weather, name='search-weather')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

