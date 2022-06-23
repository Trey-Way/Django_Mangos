from django.urls import path
from .views.mango import MangosView, MangoView
from .views.mango_shop import Mango_ShopsView, Mango_ShopView

urlpatterns = [
    path('mango/', MangosView.as_view(), name='index'),
    path('mango/<int:pk>', MangoView.as_view(), name="mango"),
    path('mango_shop/', Mango_ShopsView.as_view(), name='index'),
    path('mango_shop/<int:pk>', Mango_ShopView.as_view(), name="mango_shop")
]