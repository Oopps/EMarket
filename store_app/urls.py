from django.conf.urls import url
from store_app.views import ProductView

urlpatterns = [
    url(r'product/', ProductView.as_view())
]