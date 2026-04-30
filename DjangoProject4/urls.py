from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.views import register_template_viwe, login_template_viwe, logout_view, online_shop_viwe, add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', online_shop_viwe, name='online_shop'),
    path('register' , register_template_viwe , name='register'),
    path('login' , login_template_viwe , name='login'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('logout', logout_view , name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
