from django.shortcuts import render, redirect
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import View, Star
from .forms import EventForm

class ViewListView(ListView):
    model = View
    template_name = 'views/index.html'

class ViewCreate(CreateView):
    model = View
    fields = '__all__'

class ViewUpdate(UpdateView):
    model = View
    fields = ['location', 'occassion', 'credit']

class ViewDelete(DeleteView):
    model = View
    success_url = '/views/'
    

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# replaced view function with Class Based Views on the url patterns

# def views_index(request):
#     views = View.objects.all()
#     return render(request, 'views/index.html', {'views': views })

def views_detail(request, view_id):
    view = View.objects.get(id=view_id)
    stars_view_doesnt_have = Star.objects.exclude(id__in = view.stars.all().values_list('id'))
    event_form = EventForm()
    return render(request, 'views/detail.html', {'view': view, 'event_form': event_form, 'stars': stars_view_doesnt_have})

def add_event(request, view_id):
  # create a ModelForm instance using the data in request.POST
  form = EventForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it has view_id assigned
    new_event = form.save(commit=False)
    new_event.view_id = view_id
    new_event.save()
  return redirect('detail', view_id=view_id)

def assoc_star(request, view_id, star_id):
  View.objects.get(id=view_id).stars.add(star_id)
  return redirect('detail', view_id=view_id)

def unassoc_star(request, view_id, star_id):
  View.objects.get(id=view_id).stars.remove(star_id)
  return redirect('detail', view_id=view_id)

# Create your views here.
class StarList(ListView):
  model = Star

class StarDetail(DetailView):
  model = Star

class StarCreate(CreateView):
  model = Star
  fields = '__all__'

class StarUpdate(UpdateView):
  model = Star
  fields = ['name', 'color']

class StarDelete(DeleteView):
  model = Star
  success_url = '/stars/'
