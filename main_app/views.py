from django.shortcuts import render

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
    return render(request, 'views/index.html', {'views': views })

# Create your views here.
