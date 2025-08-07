from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from .supabase_client import supabase

def home(request):
    return render(request, 'core/home.html')
def design(request):
    return render(request, 'core/design.html')



def contact_view(request):
    sent = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                f"Message from {cd['name']} <{cd['email']}>:\n\n{cd['message']}",
                cd['email'],
                ['pefahomes@gmail.com'], 
            )
            sent = True
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form, 'sent': sent})