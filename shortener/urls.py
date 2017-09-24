from django.conf.urls import url

from .views import (
    HomeView,
    MyBitlyRedirectView,
)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<shortcode>[\w-]+)$', MyBitlyRedirectView.as_view(), name='short'),
]
