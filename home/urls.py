from django.urls import path

from . import views
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/',views.EquipmentDetailView.as_view()),
    url(r'^(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

]