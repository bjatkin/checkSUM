from django.shortcuts import render
from django.http import HttpResponse
from checkSUM.models import User
import json

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

def database(request):
    body_data = json.loads(request.body)
    dataType = body_data['type']
    print("DATA TYPE :", dataType)
    print('\n\n\n\n\n\n')
    print("request ", body_data)

    if (dataType == 'dataGet'):
        email = body_data["email"]
        password = body_data["password"]
        u = User.objects.get(user_email=email) #Not really an error. Is created once it is running
        print("User pass: ", u.password)

    if (dataType == 'dataPost'):
        email = body_data['email']
        password = body_data['password']
        fname = body_data['fname']
        lname = body_data['lname']
        bday = body_data['bday']
        bcity = body_data['bcity']
        bstate = body_data['bstate']
        s = User(user_email=email, password=password, first_name=fname, last_name=lname, birthday=bday, birth_city=bcity, birth_state=bstate)
        s.save() #Saves into the database need to figure out how to get

    return HttpResponse("success")