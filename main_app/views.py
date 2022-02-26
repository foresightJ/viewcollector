from django.shortcuts import render
from django.views.generic import ListView
from .models import View

class ViewListView(ListView):
    model = View
    template_name = 'views/index.html'
    

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def views_index(request):
#     views = View.objects.all()
#     return render(request, 'views/index.html', {'views': views })

def views_detail(request, view_id):
    view = View.objects.get(id=view_id)
    return render(request, 'views/detail.html', {'view': view })

# Create your views here.
