from django.urls import path


from . import views
from rest_framework import routers
from .views import AdminObjectViewset

router = routers.SimpleRouter()
router.register('adminView',AdminObjectViewset,basename="adminView")
from django.conf.urls import include, url


urlpatterns = [
    url(r'^',include(router.urls))
]