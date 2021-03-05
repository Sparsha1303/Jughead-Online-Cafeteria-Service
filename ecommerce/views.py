from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import ContactForm 


# Create your views here.
def home(request):
    context = {
        "title":"Jughead",
        "content":"Welcome to the Home Page",
    }
    print("Home", request.user.is_authenticated)
    if request.user.is_authenticated:
        context["premium"]="YEAHH"
    return render(request,'home.html',context)

def about(request):
    context = {
        "title":"Hello World",
        "content":"Welcome to the About Page"}
    return render(request,'home.html',context)

def contact(request):

    contact_form = ContactForm(request.POST or None)

    context = {"title":"Contact Page",
    "content":"Welcome to the Contact Page",
    "form" : contact_form}

    print(contact_form.is_valid())
    if contact_form.is_valid():

        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message":"Thank you for your submission."})


    if contact_form.errors:
        errors = contact_form.errors.as_json()
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return HttpResponse(errors,status=400,content_type='application/json')


    
    return render(request,'contact/view.html',context)


# def login_page(request):
    
#     loginform = LoginForm(request.POST or None)
#     context = {"form" : loginform}
    
#     print(request.user.is_authenticated)
#     if loginform.is_valid():

#         print(loginform.cleaned_data)
#         username = loginform.cleaned_data.get("username")
#         password = loginform.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         else:
#             print('Error')
#     return render(request,'auth/login.html',context)

# User = get_user_model()
# def register(request):
#     form = RegisterForm(request.POST or None)
#     context = {"form" : form}
    
#     print(form.is_valid())
#     if form.is_valid():
#         print(form.cleaned_data)
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         email    = form.cleaned_data.get("email")
#         new_user = User.objects.create_user(username, email, password)
#         print(new_user)
#     return render(request, "auth/register.html",context)   

    
   



 