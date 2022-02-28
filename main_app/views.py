from django.shortcuts import render, redirect
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import View, Star
from .forms import EventForm


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ViewListView(LoginRequiredMixin, ListView):
    model = View
    template_name = 'views/index.html'
    # context_object_name = 'view_list'
    # queryset = View.objects.filter(user=request.user)
    
    # def get_queryset(self):
    #     queryset = super(r, self).get_queryset()
    #     return queryset.filter(user=request.user)

class ViewCreate(LoginRequiredMixin, CreateView):
    model = View
    fields = '__all__'
    # method to call when a valid model form is submitted
    def form_valid(self, form):
      # assigning new main model instance to logged_in user
      form.instance.user = self.request.user 
      return super().form_valid(form)

class ViewUpdate(LoginRequiredMixin, UpdateView):
    model = View
    fields = ['location', 'occassion', 'credit']

class ViewDelete(LoginRequiredMixin, DeleteView):
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
class StarList(LoginRequiredMixin, ListView):
  model = Star

class StarDetail(LoginRequiredMixin, DetailView):
  model = Star

class StarCreate(LoginRequiredMixin, CreateView):
  model = Star
  fields = '__all__'

class StarUpdate(LoginRequiredMixin, UpdateView):
  model = Star
  fields = ['name', 'color']

class StarDelete(LoginRequiredMixin, DeleteView):
  model = Star
  success_url = '/stars/'

