from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def sessions_view(request):
    context = {
        "title": "Sessions view",
    }
    # replace 'sessions.html' with your actual template for sessions view
    return render(request, "sessions.html", context)
