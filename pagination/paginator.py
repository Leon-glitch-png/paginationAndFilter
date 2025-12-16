from django.views.generic import ListView
from .models import Image


class CustomPaginator(ListView):
    model = Image
    paginate_by = 12;
    page_kwarg = 'page'
    template_name = 'paginated_image_list.html'
    context_object_name = 'images'
    
    

