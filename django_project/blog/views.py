from django.shortcuts import render

# Create your views here.
posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 27, 2018",
    },
]


def home(request):
    context = {
        "posts": posts,
        "title": "Home",
    }
    return render(request, "blog/home.html", context)


def about(request):
    context = {
        "title": "About",
    }
    return render(request, "blog/about.html", context)
