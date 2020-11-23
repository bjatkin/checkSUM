from django.shortcuts import render
from django.http import HttpResponse
from checkSUM.models import User
from checkSUM.models import Token
from datetime import datetime
import json
import time

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
            return success_response()
        else:
            return fail_response()
    except:
        return fail_response()

def is_email_available(request):
    body_data = json.loads(request.body)
    email = body_data["email"]

    try:
        u = User.objects.get(user_email=email)
        return HttpResponse("{\"available\": false}")
    except:
        return HttpResponse("{\"available\": true}")

def create_account(request):
    body_data = json.loads(request.body)
    email = body_data["email"]

    try:
        u = User.objects.get(user_email=email)
        return fail_response()
    except:
        password = body_data['password']
        fname = body_data['fname']
        lname = body_data['lname']
        bday = body_data['bdate']
        bcity = body_data['bcity']
        bstate = body_data['bstate']
        s = User(user_email=email, password=password, first_name=fname, last_name=lname, birthday=bday, birth_city=bcity, birth_state=bstate)
        s.save()
        return success_response()

def get_account_info(request):
    body_data = json.loads(request.body)
    email = body_data["email"]

    try:
        u = User.objects.get(user_email=email)
        return HttpResponse("{\"success\": true, \"first_name\":\""+u.first_name+"\", \"last_name\":\""+u.last_name+"\", \"birth_date\":\""+u.birthday+"\"}")
    except:
        return fail_response()

def store_secret(request):
    body_data = json.loads(request.body)
    email = body_data["email"]
    secret = body_data["secret"]

    try:
        u = User.objects.get(user_email=email)
        old_tokens = Token.objects.filter(user_id=u, valid=True)
        for token in old_tokens:
            token.valid=False
            token.save()
        t = Token(user_id=u, token=secret)
        t.save()
        return success_response()
    except:
        return fail_response()

def verify_age(request):
    body_data = json.loads(request.body)
    secret = body_data["secret"]

    try:
        t = Token.objects.get(token=secret, valid=True)
        u = User.objects.get(id=t.user_id.id)
        birth = datetime.strptime(u.birthday, "%m/%d/%Y").timestamp()
        age = (time.time() - birth)/60/60/24/365
        if age > 13:
            return HttpResponse("{\"user is 13 or older\": true}")
        return HttpResponse("{\"user is 13 or older\": false}")
    except:
        return HttpResponse("{\"user is 13 or older\": false}")

def success_response():
    return HttpResponse("{\"success\": true}")

def fail_response():
    return HttpResponse("{\"success\": false}")