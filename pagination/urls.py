

from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from .paginator import CustomPaginator


# app_name = 'pagination'

urlpatterns = [
    path("", views.index, name="index"),
    path('create_image/', views.create_image, name='create_image'),
    path('image_list/', views.image_list, name='image_list'),
    path("paginated_image_list/",CustomPaginator.as_view() , name="paginated_image_list"),
    path("create_name/",views.create_name, name="create_name"),
    path("name_list/",views.name_list, name="name_list"),
    path("show_names",views.show_names, name="show_names"),
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)