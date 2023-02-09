from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee


def getOrNone(request, name):
    try:
        return request.GET[name]
    except:
        return None


# Create your views here.


def create(request):
    eid = 0
    ename = 0
    eemail = 0
    econtact = 0

    submit = 0
    if request.GET:
        eid = request.GET["eid"]
        ename = request.GET["ename"]
        eemail = request.GET["eemail"]
        econtact = request.GET["econtact"]

        opt = request.GET["option"]
        ms = Employee()
        ms.eid = eid
        ms.ename = ename
        ms.eemail = eemail
        ms.econtact = econtact

        ms.save()
        print("saved")

        if opt == "submit":
            submit = eid

    return render(request, "create.html",
                  {"eid": eid, "ename": ename, "eemail": eemail, "econtact": econtact, "submit": submit})


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/deleted")
