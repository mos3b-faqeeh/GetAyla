from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register (request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=email).exists():
                messages.info(request,'user Taken')
                return redirect('register')



            elif User.objects.filter(email=email).exists():
                messages.info(request,'email Taken')
                return redirect('register')


            else:
             user = User.objects.create_user(username=email, first_name=first_name, email=email, password=password1)
             user.save();
             messages.info(request, 'User Created')
             return redirect('register')




        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')

        return redirect('/')





    else:
        return render(request, 'register.html', {})




