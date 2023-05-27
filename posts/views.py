from django.views.generic import ListView
from .models import Posts
# Create your views here.
class Alimardon(ListView):
    model = Posts
    template_name = 'home.html'
    context_object_name='Barcha_postlar'
class Fayozbek(ListView):
    model = Posts
    template_name = 'home2.html'
    context_object_name='Barcha_postlar'