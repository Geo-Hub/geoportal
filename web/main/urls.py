from django.urls import include, path
from . import views
from django_registration.backends.activation import urls as registration_urls

urlpatterns = [
    path('', views.home,name='home'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('data/',views.data, name='data'),
    path('shamba/register/',views.registershamba, name='registershamba'),
    path('shamba/update-payment/',views.update_payment, name='payment'),
    path('shamba/discard/',views.discardshamba,name='discardshamba'),
    path('shamba/changeowner/',views.changeowner,name='changeowner'),
    path('statistics/',views.statistics,name='statistics'),
]
