from django.shortcuts import render
from .models import View
# class View:
#     def __init__(self, name, location, occassion, credit):
#         self.name = name
#         self.location = location
#         self.occassion = occassion
#         self.credit = credit

# views = [
#     View('salt sunset', 'mamaia', 'a calm walk by the beach', 'Foresight'),
#     View('Lolo', 'tabby', 'foul little demon', 'Me'),
#     View('Sachi', 'tortoise shell', 'diluted tortoise shell', 'Me'),
#     View('Raven', 'black tripod', '3 legged cat', 'Bella')
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def views_index(request):
    views = View.objects.all()
    return render(request, 'views/index.html', {'views': views })

def views_detail(request, view_id):
    view = View.objects.get(id=view_id)
    return render(request, 'views/detail.html', {'view': view })

# Create your views here.
