from email import message
from django.shortcuts import render

from .forms import NewslatterUserSingUpForm
from .models import NewslatterUser


def newslatter_signup(request):
    form = NewslatterUserSingUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewslatterUser.objects.filter(email=instance.email).exists():
            message.warning(request, 'Email already exists')

        else:
            instance.save()
            message.success(request, 'Thanks for signing up, check your email')
            # send email                 
            subject = 'Registrado a Newslatter de la Empresa'
            body = 'Gracias por registrarte en Newslatter de la Empresa'
            from_email = instance.email
            to_email = [instance.email]
        
    context = {
        'form': form
    }
    return render(request, 'newslatter/start_here.html', context)
        