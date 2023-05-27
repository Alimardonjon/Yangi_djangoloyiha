from django.views.generic import ListView
from .models import Post2
# Create your views here.
class Ali(ListView):
    model = Post2
    template_name = 'home3.html'
    context_object_name='Barcha_postlar'
