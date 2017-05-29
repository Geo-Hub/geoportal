from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.core.serializers import serialize
from chartit import DataPool, Chart

# Create your views here.
def home(request):
	title = 'Home'
	template = 'home.html'
	context = {'title':title}
	return render(request, template, context)
def about(request):
	title = 'About'
	template = 'about.html'
	context = {'title':title}
	return render(request, template, context)
def contact(request):
	title = 'Contact'
	form = ContactMessageForm()
	buttonmessage = "Submit"
        helpmessage = None
        newurl = None
	if request.method == 'POST':
		form = ContactMessageForm(request.POST)
                if form.is_valid():
                	instance = form.save(commit=False)
                	instance.save()
                	helpmessage = 'Successful'
                	buttonmessage = 'Create New'
                	newurl = '{% url "contact" %}'
        	context = {
        	'title':title,
        	'helpmessage':helpmessage,
        	'newurl':newurl,
        	'buttonmessage':buttonmessage,
        	}
        	return render(request,'contact.html', context)

	else:
		helpmessage = 'Fill the form below'
                context = {
                'title':title,
                'form': form,
                'helpmessage':helpmessage,
                'buttonmessage':buttonmessage,
                }

        	return render(request, 'contact.html', context)

def data(request):
        template = 'lookupdata.html'
        title = 'Shamba'
        shambas = serialize('geojson', Shamba.objects.all())
        counties = serialize('geojson',KiambuCounty.objects.all())
        constituencies = serialize('geojson',KiambuConstituencies.objects.all())

        context = {
        'title':title,
        'shambas':shambas,
        'counties':counties,
        'constituencies':constituencies
        }
        return render (request, template, context)

def registershamba(request):
        template = 'registershamba.html'
        title = 'Register'
        message = None
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        instance = form.save(commit=False)
                        instance.save()
                message = 'Sent'
                context = {
                'form':form,
                'message':message,
                'title':title,
                }
                return render(request, template, context)
        else:
                message = 'Fill below'
                form = RegistrationForm
                context = {
                'title':title,
                'message':message,
                'form':form,
                }
                return render(request,template,context)

def discardshamba(request):
        template = 'discardshamba.html'
        title = 'Discard'
        # shambas = OwnershipInfo.objects.all()
        context = {
        'title':title,
        # 'shambas':shambas,
        }
        return render(request, template, context)
def changeowner(request):
        template = 'changeowner.html'
        title = 'Change'
        context = {
        'title':title,
        }
        return render(request, template, context)

def statistics(request):
        template = 'statistics.html'
        title = 'Statistics'
        #Step 1: Create a DataPool with the data we want to retrieve.
        order_by = request.GET.get('order_by', 'id')
        data = Shamba.objects.all().order_by('id')
        context = {
        'title':title,
        'data':data
        }
        return render(request, template, context)