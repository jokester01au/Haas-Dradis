from django.conf.urls import url

from authentication.views import login_view
from authentication.views import logout_view

urlpatterns = [
    url(r'^login', login_view, name="login_view"),
    url(r'^logout', logout_view, name="logout_view")
]
