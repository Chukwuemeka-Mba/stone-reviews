from django.contrib import admin
from django.urls import path, include
from movies.views import LandingPageView, landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('movies/', include('movies.urls', namespace='movies')),
]
