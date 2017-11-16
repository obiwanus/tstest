from django.conf.urls import url
from tstest import views as tstest_views


urlpatterns = [

    # Login
    url(r'fibonacci/$', tstest_views.FibonacciView.as_view(), name='api_fibonacci'),

]

