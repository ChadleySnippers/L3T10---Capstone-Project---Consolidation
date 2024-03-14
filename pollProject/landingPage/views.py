from django.shortcuts import render

# View function for rendering the 'index.html' template
def index(request):
    return render(request, 'pages/index.html')
