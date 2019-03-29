from django.shortcuts import render

posts = [
    {
        'author': 'Stalin',
        'title': 'World War 1',
        'content': 'First world war',
        'date_posted': 'March 27, 2019'
    },
    {
        'author': 'Clinton ',
        'title': 'Washington Post 2',
        'content': 'Second post content',
        'date_posted': 'March 28, 2019'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title' : 'About'})
