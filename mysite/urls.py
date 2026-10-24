from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import home, haqqimda, elan_detay, secilmisler_goster, favori_toggle, yeni_elan

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("haqqimda/", haqqimda, name="haqqimda"),
    path("secilmisler/", secilmisler_goster, name="secilmisler"),
    path("favori-toggle/<int:id>/", favori_toggle, name="favori_toggle"),
    path("elan/<int:id>/", elan_detay, name="elan_detay"),
    path("elan-yerlesdir/", yeni_elan, name="yeni_elan"),  # Bu sətir əlavə olundu
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)