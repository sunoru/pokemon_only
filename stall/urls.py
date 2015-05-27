from django.conf.urls import include, url
from stall.views import SignupView, ValidateView, LoginView


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^validate/(?P<validate_code>.+)/$', ValidateView.as_view(), name='validate'),
]
