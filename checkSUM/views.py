from django.shortcuts import render
from django.http import HttpResponse
from checkSUM.models import User

MIME_TYPE_HTML = "text/html"
MIME_TYPE_CSS = "text/css"
MIME_TYPE_JS = "text/javascript"
MIME_TYPE_PNG = "image/png"

# Create your views here.
def index(request):
    return serve_file('public/index.html', MIME_TYPE_HTML)
    # return HttpResponse("Hello World")

def bundle_css(request):
    return serve_file('public/bundle.css', MIME_TYPE_CSS)

def bundle_js(request):
    return serve_file('public/bundle.js', MIME_TYPE_JS)

def serve_file(file, mime_type):
    page = open(file)
    return HttpResponse(page.read(), content_type=mime_type)

def dataBase(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        password = request.GET.get('password')
        print(email)
        print(password)
        s = User(user_email=email, password=password)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        bday = request.POST.get('bday')
        bcity = request.POST.get('bcity')
        bstate = request.POST.get('bstate')

        s = User(user_email=email, password=password, first_name=fname, last_name=lname, birthday=bday, birth_city=bcity, birth_state=bstate)
        s.save() #Saves into the database need to figure out how to get
    return HttpResponse("hooray") #need to serve_file public index I believe