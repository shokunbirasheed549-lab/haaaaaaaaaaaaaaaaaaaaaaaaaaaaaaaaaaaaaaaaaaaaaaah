from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def blog(request):
    return render(request, 'blog.html')

def cases(request):
    return render(request, 'cases.html')

def contact(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'main.html')

def services(request):
    return render(request, 'services.html')




