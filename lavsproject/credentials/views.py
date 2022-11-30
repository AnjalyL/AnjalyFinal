from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from credentials.forms import PersonCreationForm
from credentials.models import City, Person, Account, District


def home(request):
    obj = District.objects.all()
    # obj1 = Team.objects.all()
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password=password)

        if user is not None:
            form = PersonCreationForm()
            results = Account.objects.all
            auth.login(request,user)
            return render(request, "page.html")

        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")
def newform(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = auth.authenticate(username = username,password=password)
    #
    #     if user is not None:
            form = PersonCreationForm()
            results = Account.objects.all
            # auth.login(request,user)
            return render(request, "home.html",{'form': form , "account":results})
    #     else:
    #         messages.info(request, "invalid credentials")
    #         return redirect('login')
    #
    # return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        secondname = request.POST['secondname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already exists")
                return  redirect ('register')

            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email already exists")
                return  redirect ('register')
            else:
                user = User.objects.create_user(username = username, first_name  =  firstname, last_name  = secondname, email = email, password =password)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "Password not match")
            return redirect('register')
        return redirect('/')


    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):

    return render(request, "final.html")


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})

