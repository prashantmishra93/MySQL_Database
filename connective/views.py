from django.shortcuts import render
from .forms import FormAddContactForm
from .models import ContactForm
from django.contrib import messages

# Create your views here.

def Contactform(request):
    if request.method == 'POST':
        form = FormAddContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            password = request.POST['password']
            re_password = request.POST['re_password']

            if ContactForm.objects.filter(name=name).exists():
                ctx = {'error':'name must be different'}
                return render(request, 'contact.html', ctx)

            elif ContactForm.objects.filter(email=email).exists():
                ctx1 = {'error1':'email must be different'}
                return render(request, 'contact.html', ctx1)

            elif ContactForm.objects.filter(contact=contact).exists():
                ctx2 = {'error2':'contact must be different'}
                return render(request, 'contact.html', ctx2)

            elif password != re_password:
                ctx2 = {'form': form, 'error3': ' both password must be same '}
                return render(request, 'contact.html', ctx2)

            else:
                form.save()
                return render(request, 'success.html')

    return render(request, 'contact.html')

def success(request):
    employees = ContactForm.objects.all()
    return render(request, 'success.html', {'employees':employees})

def logindata(request):
    if request.method == 'POST':
        try:
            userdetail = ContactForm.objects.get(email = request.POST['email'], password = request.POST['password'])
            request.session['email']=userdetail.email
            return render(request, 'success.html')
        except ContactForm.DoesNotExist as e:
            messages.success(request, 'Email / Password is Invalid..!')
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['email']
    except:
        return render(request, 'success.html')
    return render(request, 'success.html')

def show(request):
    employees = ContactForm.objects.all()
    return render(request, 'show.html', {'employees':employees})