from django.shortcuts import render, redirect
from .models import Home, Service, Recruit, Contact
from .forms import RecruitForm, ContactForm
from django.core.mail import EmailMessage

# -----------------------Home-----------------------


def home(request, id):
    data = Home.objects.get(pk=id)
    return render(request, 'index.html', {'data': data})


# -----------------------Service-----------------------


def service(request):
    data = Service.objects.all()
    return render(request, 'service.html', {'data': data})


def to_airklass(request):
    return redirect("http://airklass.com")


def to_login(request):
    return redirect("http://airklass.com/master")

# -----------------------Recruit-----------------------


def recruit(request):
    data = Recruit.objects.all()
    return render(request, 'recruit.html', {'data': data})


def apply_recruit(request):
    if request.method == 'POST':
        form = RecruitForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            email = EmailMessage('Apply For Job', name+email+phone, to=['es.halvers@gmail.com'])
            email.send()
            form.save()
        return redirect('/home/recruit')
    else:
        form = RecruitForm()
    return render(request, 'apply_recruit.html', {'form': form})

# -----------------------Contact-----------------------


def contact(request):
    data = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            email = EmailMessage('Sending Message', name + email + phone + message, to=['es.halvers@gmail.com'])
            email.send()
            form.save()
        return redirect('/index/contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'data': data})