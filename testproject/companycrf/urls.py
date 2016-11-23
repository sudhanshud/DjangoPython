from django.conf.urls import *

urlpatterns = patterns('companycrf.views',
(r'^$', 'home'),
(r'^crating/', 'companyrating'),
(r'^crs/', 'companycrs'),
(r'^crsgraph/', 'companycrsgraph'),
)