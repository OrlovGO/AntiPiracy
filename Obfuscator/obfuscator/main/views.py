from django.shortcuts import render
from .forms import CodeForm
from random import randint

def CreateVarName():
    case = randint(1, 3)
    if (case == 1):
        trick = "user_key" + str(randint(1, 100))
    if (case == 2):
        trick = "valid_key" + str(randint(1, 100))
    if (case == 3):
        trick = "license_key" + str(randint(1, 100))
    return trick

def CreateStr1(var):
    trick = "int " + var + "=" + str(randint(1000, 5000)) + ";"
    return trick

def CreateStr2(var1, var2):
    trick = "if(" + var1 + " == " + var2 + "){bool valid = 1;}"
    return trick

def index(request):
    submitbutton = request.POST.get("submit")

    code_raw = ''
    code = ''
    flag_main = 0

    form = CodeForm(request.POST or None)
    if form.is_valid():
        code_raw = form.data.get("code_field")
        code = code_raw.split("\r\n")
        flag = 0
        i = 0
        while code[i] != "return 0;":
            if code[i] == "int main(){":
                flag_main = 1
            if code[i] == "int main(){" or code[i] == "};":
                flag = 1

            if code[i] == "while" or code[i] == "for" or code[i] == "if" or code[i] == "return 0;":
                flag = 0

            if flag == 1:
                line = CreateVarName()
                line2 = CreateVarName()
                code.insert(i + 1, CreateStr1(line))
                code.insert(i + 2, CreateStr1(line2))
                code.insert(i + 3, CreateStr2(line, line2))
                i += 3
            i += 1

    context = {'form': form, 'code': code, 'submitbutton': submitbutton, 'flag_main': flag_main}

    return render(request, 'test.html', context)

