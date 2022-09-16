from django.urls import path


from . import views
from .views import bookViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register('bookView',bookViewset,basename="bookView")
from django.conf.urls import include, url
from django.urls import include, path


urlpatterns = [
    url(r'^',include(router.urls)),
    # path('', views.index, name='index')
]