from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
	url(r'^upld/$', views.upld, name='upld'),
	url(r'^appreals/$', views.appreals, name='appreals'),
	url(r'^electronics/$', views.electronics, name='electronics'),
	url(r'^shoes/$', views.shoes, name='shoes'),
	url(r'^appliance/$', views.appreals, name='appliance'),
	url(r'^furniture/$', views.furniture, name='furniture'),
	url(r'^books/$', views.books, name='books'),
	url(r'^insert/$', views.insert, name='insert'),
	url(r'^sendmail/$', views.sendmail, name='sendmail'),
	url(r'^product_details/$', views.product_details, name='product_details'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^signup/$', views.signup, name='signup'),
] + static(settings.STATIC_URL)