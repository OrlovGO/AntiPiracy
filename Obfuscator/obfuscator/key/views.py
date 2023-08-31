from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from .forms import LoginForm
from .forms import KeyForm
import uuid
from .generator import LicenseKey
import hashlib
from .models import Key

def index(request):
    submitbutton = request.POST.get("submit")
    key_incorrect = 1
    key = ''
    activation_code = ''
    sum = ''
    salt = 'O0tCMN32'
    dbKeys = Key.objects.all()

    userid = ''

    form = KeyForm(request.POST or None)
    if form.is_valid():
        key = form.data.get("key_field")
        userid = form.data.get("ID_field")

        sum = key + str(userid) + salt
        hash_sum = hashlib.md5(sum.encode())
        activation_code = hash_sum.hexdigest()

        for el in dbKeys:
            if el.key == key:
                key_incorrect = 0
                el.code = activation_code
                el.uid = userid
                el.save()

    context = {'form': form, 'key': key, 'submitbutton': submitbutton, 'userid': userid,
               'activation_code': activation_code, 'salt': salt, 'sum': sum, 'dbKeys': dbKeys, 'key_incorrect': key_incorrect}

    return render(request, 'verify.html', context)

def generator(request):
    submitbutton = request.POST.get("submit")
    user_key = ''
    dbKeys = Key.objects.all()
    license_key = ''
    login = ''

    form = LoginForm(request.POST or None)
    if form.is_valid():
        login = form.data.get("login_field")
        license_key = LicenseKey(4, 4, '-')
        user_key = license_key.generateKey()
        dbKeyNew = Key.objects.create(login = login ,uid='null', key=user_key, code='null')

    context = {'user_key': user_key, 'dbKeys': dbKeys, 'submitbutton': submitbutton, 'form': form}
    return render(request, 'generator.html', context)

