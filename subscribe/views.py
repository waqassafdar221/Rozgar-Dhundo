from django.shortcuts import redirect, render
from django.urls import reverse

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    email_empty_error =""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
        #     print("Valid FOrm")
        #     first_name = subscribe_form.cleaned_data['first_name']
        #     last_name = subscribe_form.cleaned_data['last_name']
        #     email = subscribe_form.cleaned_data['email']
        # # print(email)
        # # if email=="":
        # #     email_empty_error ="Please Enter Email"
        #     subscribe = Subscribe(first_name=first_name,last_name=last_name,email=email)
        #     subscribe.save()
            return redirect(reverse('thank_you'))
            
    context ={"form": subscribe_form,"email_empty_error":email_empty_error}
    return render(request,'subscribe/subscribe.html', context)

def thank_you(request):
    context={}
    return render(request,'subscribe/thank_you.html',context)