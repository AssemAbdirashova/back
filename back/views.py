
from django.shortcuts import render
from django.contrib import auth
import pyrebase

config = {

    'apiKey': "AIzaSyDsfNki_M-ktvaNXyvOWv5VSf-oGLJFAsE",
    'authDomain': "project-33c22.firebaseapp.com",
    'databaseURL': "https://project-33c22.firebaseio.com",
    'projectId': "project-33c22",
    'storageBucket': "project-33c22.appspot.com",
    'messagingSenderId': "425224201703",
    'appId': "1:425224201703:web:70e19a09efa4b2803dc942",
    'measurementId': "G-DH0YKRR8LW"
  }

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()
def singIn(request):

    return render(request, "signIn.html")

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid crediantials"
        return render(request,"signIn.html",{"msg":message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "welcome.html",{"e":email})
def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')


def signUp(request):
    return render(request, "signup.html")


def postsignup(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        data= {"name":name,"status":"1"}
        database.child("users").child(uid).child("details").set(data)
    except:
        message="Unable to create account try again"
        return render(request,"signup.html",{"messg":message})



    return render(request,"signIn.html")