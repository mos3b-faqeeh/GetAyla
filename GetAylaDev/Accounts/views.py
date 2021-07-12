from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, HttpResponse

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

from .tokens import account_activation_token


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return JsonResponse({'err_code': '2'})
                # return redirect('/mydash')
            else:
                return JsonResponse({'err_code': '1', 'description': '''<div class="alert alert-warning alert-dismissible fade show" role="alert" style="background-image: none">
                    <strong>Oops!!! </strong><br>Your Email is not verified. Please verify your email first!! In order to access your account.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>'''})
        else:
            return JsonResponse({'err_code': '1', 'description': '''<div class="alert alert-warning alert-dismissible fade show" role="alert" style="background-image: none">
                    <strong>Oops!!! </strong><br> This User Credential Is Not Valid! Please Try with another one!.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>'''})

    else:
        return render(request, 'login.html', {})


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        # User.objects.all().delete()
        if User.objects.filter(email=email).exists():
            return JsonResponse({'err_code': '1', 'description': 'Email is exist, please use another email'})
        else:
            user = User.objects.create_user(username=email, first_name=first_name, email=email, password=pwd)
            user.save();
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            emailMsg = EmailMessage(
                mail_subject, message, to=[email]
            )
            emailMsg.content_subtype = "html"
            emailMsg.send()
            return JsonResponse({'err_code': '2',
                                 'description': 'Thank you for registering. You will receive an activation email shortly.'})
    else:
        return render(request, 'register.html', {})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('/mydash')
    else:
        return HttpResponse('Activation link is invalid!')


def myprofile(request):
    return render(request, 'myprofile.html', {})


def updatePass(request):
    return render(request, 'updatePass.html', {})


def updatePayment(request):
    return render(request, 'updatePayment.html', {})


def updateNum(request):
    return render(request, 'updateNum.html', {})


def updateEmail(request):
    return render(request, 'updateEmail.html', {})


