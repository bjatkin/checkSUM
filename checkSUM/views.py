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

def request_login(request):
    body_data = json.loads(request.body)
    email = body_data["email"]
    password = body_data["password"]
    try:
        u = User.objects.get(user_email=email)
        if (u.password == password):
            return HttpResponse("{\"success\": true}")
        else:
            return HttpResponse("{\"success\": false}")
    except:
        return HttpResponse("{\"success\": false}")

def create_account(request):
    body_data = json.loads(request.body)
    email = body_data["email"]

    try:
        u = User.objects.get(user_email=email)
        return HttpResponse("{\"success\": false}")
    except:
        password = body_data['password']
        fname = body_data['fname']
        lname = body_data['lname']
        bday = body_data['bdate']
        bcity = body_data['bcity']
        bstate = body_data['bstate']
        s = User(user_email=email, password=password, first_name=fname, last_name=lname, birthday=bday, birth_city=bcity, birth_state=bstate)
        s.save()
        return HttpResponse("{\"success\": true}")

def get_account_info(request):
    body_data = json.loads(request.body)
    email = body_data["email"]

    try:
        u = User.objects.get(user_email=email)
        return HttpResponse("{\"success\": true, \"first_name\":\""+u.first_name+"\", \"last_name\":\""+u.last_name+"\", \"birth_date\":\""+u.birthday+"\"}")
    except:
        return HttpResponse("{\"success\": false}")