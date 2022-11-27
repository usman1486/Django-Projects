from django.shortcuts import render, redirect
from .models import Information
# Create your views here.


def show(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        img = request.FILES['profile']
        gender = request.POST.get('gen')
        hobby = request.POST.getlist('abc[]')
        country = request.POST.get('country')
        obj = Information(name=name, email=email, img=img,
                          gender=gender, hobby=hobby, country=country)
        obj.save()
        return redirect('display')
    else:
        return render(request, 'index.html')


def disp(request):
    bscs = Information.objects.all()
    return render(request, 'view.html', {'bscs': bscs})


def delete(request, id):
    bscs = Information.objects.get(id=id)
    bscs.delete()
    return redirect('display')


def edit(request, id):
    xxx = Information.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        img = request.FILES['profile']
        gender = request.POST.get('gen')
        hobby = request.POST.getlist('abc[]')
        country = request.POST.get('country')
        obj = Information(name=name, email=email,
                          img=img,   gender=gender, hobby=hobby, country=country, id=id)
        obj.save()
        return redirect('display')
    else:
        return render(request, 'edit.html', {'xxx': xxx})
