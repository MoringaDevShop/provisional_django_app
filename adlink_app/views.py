from django.shortcuts import render, render_to_response
from adlink_app.forms import authentication, additionalforms
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from uni_form.helper import FormHelper
from crispy_forms.helper import FormHelper


# Create your views here.

# def home(request):

# 	return render_to_response('home.html',{

# 		})
def register_customer(request):
	context = RequestContext(request)
	registered = False

	if request.method =='POST':
		user_form = authentication(data=request.POST)
		profile_form = additionalforms(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=True)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()

			registered=True
			return HttpResponseRedirect('/home/')
		else:
			print (user_form.errors, profile_form.errors)
	else:
		user_form = authentication()
		profile_form = additionalforms()

		return render(request,
			'register.html',
			{'user_form':user_form, 'profile_form':profile_form, 'registered': registered},
			context_instance=RequestContext(request))

def clerk_login(request):
	context = RequestContext(request)

	if request.method== 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/login/')
			else:
				return HttpResponse('.') 

		else:
			print("invalid login details: {0}, {1}".format(username, password)) 
			return HttpResponse("Invalid login details supplied")
	else:
		return render(request, 'login.html', 
				{},  context_instance=RequestContext(request))


@login_required
def clerk_logout(request):
	logout(request)

	return HttpResponseRedirect('/login/')
