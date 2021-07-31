from django.shortcuts import render, redirect
from .forms import FormAddContactForm
from .models import ContactForm
from django.contrib import messages

# Create your views here.

def Contactform(request):
    form = FormAddContactForm()
    data = {
        'form': form
    }
    if request.method == 'POST':
        form = FormAddContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            password = request.POST['password']
            re_password = request.POST['re_password']

            if ContactForm.objects.filter(name=name).exists():
                messages.error(request, "Name must be different")

            elif ContactForm.objects.filter(email=email).exists():
                messages.error(request, "Email must be different")

            elif ContactForm.objects.filter(contact=contact).exists():
                messages.error(request, "Contact must be different")

            elif password != re_password:
                messages.error(request, "Password must be same")

            else:
                form.save()
                return render(request, 'success.html')

    return render(request, 'contact.html', {'form':data})

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

def destroy(request, id):
    employee = ContactForm.objects.get(id=id)
    employee.delete()
    return redirect('/show')