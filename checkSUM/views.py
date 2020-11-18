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
    print(request.body)
    print('HELLO\n\n\n\n\n\n')
    body_data = json.loads(request.body)
    dataType = body_data['type']
    print("DATA TYPE :", dataType)
    print('\n\n\n\n\n\n')
    print("request ", body_data)

    if (dataType == 'dataGET'):
        email = body_data["email"]
        password = body_data["password"]
        try:
            u = User.objects.get(user_email=email) #Not really an error. Is created once it is running
            if (u.password == password):
                print("User email: ", u.user_email)
                print("User pass: ", u.password)
                print(u.first_name, u.last_name)
            else:
                print("Wrong password")
        except:
            print('No user')
        

    if (dataType == 'dataPOST'):
        email = body_data['email']

        try:
            u = User.objects.get(user_email=email) #Not really an error. Is created once it is running
            print('User already exists')
            print("Email already registered")
        except:
            password = body_data['password']
            fname = body_data['fname']
            lname = body_data['lname']
            bday = body_data['bday']
            bcity = body_data['bcity']
            bstate = body_data['bstate']
            s = User(user_email=email, password=password, first_name=fname, last_name=lname, birthday=bday, birth_city=bcity, birth_state=bstate)
            s.save()
            print('Registered!')
            u = User.objects.get(user_email=email) #Not really an error. Is created once it is running
            print(u.first_name, u.last_name)