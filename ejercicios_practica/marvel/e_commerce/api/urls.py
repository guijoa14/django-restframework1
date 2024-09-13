from django.urls import path
from e_commerce.api.views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comic-list/', comic_list_api_view, name="comic_list_api_view"),
    path('comic-retrieve/', comic_retrieve_api_view, name="comic_retrieve_api_view"),
    path('comic-create/', comic_create_api_view, name="comic_create_api_view"),
    path('comic-list-filtered-price/', comic_list_filtered_api_view, name="comic_list_filtered_api_view"),
    path('comic-list-filtered-stock/', comic_list_filtered_stock_api_view, name="comic_list_filtered_stock_api_view")
]
