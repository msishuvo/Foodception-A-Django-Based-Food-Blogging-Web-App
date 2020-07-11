from django.shortcuts import render

# Create your views here.

posts = [{'author': 'Shuvo', 'title': 'Post 1', 'content': 'Content 1', 'date_posted': '11th July, 2020'},
         {'author': 'Shuvo', 'title': 'Post 2', 'content': 'Content 2', 'date_posted': '11th July, 2020'}]

def home(request):
    context = {'posts': posts}
    return render(request, 'thoughtsnideas/index.html', context)

def about(request):
    return render(request, 'thoughtsnideas/about.html', {'title': 'About'})


