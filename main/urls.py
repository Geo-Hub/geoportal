from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    # url(r'^accounts/profile/$', include('main.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/',views.contact, name='contact'),
    url(r'^data/',views.data, name='data'),
    url(r'^shamba/register/',views.registershamba, name='registershamba'),
    url(r'^shamba/update-payment/',views.update_payment, name='payment'),
    url(r'^shamba/discard/',views.discardshamba,name='discardshamba'),
    url(r'^shamba/changeowner/',views.changeowner,name='changeowner'),
    url(r'^statistics/',views.statistics,name='statistics'),
]
