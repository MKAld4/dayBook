from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from events.views import EventsView

# Url for serialized model
router = SimpleRouter()
router.register('api/event', EventsView)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('search_weather/', include('main.urls')),
                  # Url for view.set
                  path('api/event', EventsView.as_view),
                  path('', include(router.urls)),

                  path('events/', include('events.urls'))

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += router.urls
