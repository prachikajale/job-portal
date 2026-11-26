from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('home/', include('placement_portal.urls')),
    path('', include('placement_portal.urls')),
    path('accounts/', include('accounts.urls')),
]
