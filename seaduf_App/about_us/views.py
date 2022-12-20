from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def about_us(request):
    return render(request, 'about_us/about_us.html')

def our_services(request):
    return render(request, 'about_us/our_services.html')

def faq(request):
    return render(request, 'about_us/faq.html')
    
def contact_us(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@seaduffurnitures.com', ['admin@seafurnitures.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home")
      
	form = ContactForm()
	return render(request, "about_us/contact_us.html", {'form':form})

def interior(request):
	return render(request, '404.html')
def showroom(request):
	return render(request, '404.html')
def blog(request):
	return render(request, '404.html')

