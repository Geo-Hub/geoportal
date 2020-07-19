from django.core.mail import EmailMessage
from django.shortcuts import render
from .models import *
from .forms import LandRegistrationForm
from django.http import HttpResponseRedirect
from django.core.serializers import serialize
from chartit import DataPool, Chart


# Create your views here.
def home(request):
    title = 'Home'
    template = 'home.html'
    context = {'title': title}
    return render(request, template, context)


def about(request):
    title = 'About'
    template = 'about.html'
    context = {'title': title}
    return render(request, template, context)


def contact(request):
    title = 'Contact'
    helpmessage = None
    if request.method == 'POST':
        intention = request.POST.get("intention")
        if intention == "submit_form":
            showform = False
            name = request.POST.get("name_of_sender")
            email_address = request.POST.get("email_address")
            message = request.POST.get("message")
            if name and message and email_address:
                message = "Hey good people,\nThis is a message from the contact form at" \
                    "geohub-geoportal.herokuapp.com, beware and don't click any links in the" \
                    "message or be cautious.\n-----------------------------\n" \
                    "contact email address: {}\n\n{}".format(email_address, message)
                email_message = EmailMessage(
                    subject="Feedback on Geohub Geoportal by " + name,
                    body=message,
                    to=["ngenovictor321@gmail.com", "jimmywainaina@gmail.com", "thomas.muteti@gmail.com",
                        "njerimurage92@gmail.com", "nombumurage@gmail.com"],
                )
                email_message.send()

                helpmessage = 'Thank you for your feedback.'
                context = {
                    'title': title,
                    'helpmessage': helpmessage,
                    'showform': showform
                }
                return render(request, 'contact.html', context)
        else:
            helpmessage = 'Fill the form below'
            showform = True
            context = {
                'title': title,
                'helpmessage': helpmessage,
                'showform': showform
            }

            return render(request, 'contact.html', context)

    return render(request, 'contact.html', {})


def data(request):
    template = 'lookupdata.html'
    title = 'Shamba'
    shambas = serialize('geojson', Shamba.objects.all())
    counties = serialize('geojson', KiambuCounty.objects.all())
    constituencies = serialize('geojson', KiambuConstituencies.objects.all())

    context = {
        'title': title,
        'shambas': shambas,
        'counties': counties,
        'constituencies': constituencies
    }
    return render(request, template, context)


def registershamba(request):
    template = 'registershamba.html'
    title = 'Register'
    reg_form = LandRegistrationForm()
    context = {
        'title':title,
        'reg_form': reg_form
    }
    if request.method == 'POST':
        pass
    else:
        return render(request, template, context)

def update_payment(request):
    template = 'update-payment.html'
    shambas = Shamba.objects.all().order_by('-parcel_no')[:20]
    message = None
    if request.method == "POST":
        post_type = request.POST.get('post-type')
        if post_type == "yearly-update":
            if request.user.is_staff:
                for shamba in Shamba.objects.all():
                    try:
                        value = int(shamba.balance)
                        new_bal = value+100
                        shamba.balance = new_bal
                        shamba.save()
                    except Exception:
                        shamba.balance = 100
                        shamba.save()
                message = "All records have been updated with n yearly fee of KSH.{}".format(100)
            else:
                message = "You need to be staff to take that action"
        elif post_type == "payment-update":
            if request.user.is_staff:
                arrears = request.POST.get('arrears-update')
                payment = request.POST.get('payment-update')
                shamba_id = request.POST.get('shamba-id')
                shamba_obj = Shamba.objects.get(id=int(shamba_id))
                try:
                    new_bal = int(shamba_obj.balance) # db has saved int value
                except Exception: # db has maybe none in db
                    new_bal = 0
                if payment:
                    new_bal -= int(payment)
                if arrears:
                    new_bal += int(arrears)
                shamba_obj.balance = new_bal
                shamba_obj.save()
                message = "Details for user {} has been updated.".format(shamba_obj.shamba_owner)
            else:
                message = "You need to be staff to take that action"
    context = {
        'shambas':shambas,
        'message':message
    }
    return render(request, template, context)

def discardshamba(request):
    template = 'discardshamba.html'
    title = 'Discard'
    # shambas = OwnershipInfo.objects.all()
    context = {
        'title': title,
        # 'shambas':shambas,
    }
    return render(request, template, context)


def changeowner(request):
    template = 'changeowner.html'
    title = 'Change'
    context = {
        'title': title,
    }
    return render(request, template, context)


def statistics(request):
    template = 'statistics.html'
    title = 'Statistics'
    # Step 1: Create a DataPool with the data we want to retrieve.
    order_by = request.GET.get('order_by', 'id')
    data = Shamba.objects.all().order_by('id')
    context = {
        'title': title,
        'data': data
    }
    return render(request, template, context)
