# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from search.models import Student
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, SignupForm

# Create your views here.

login_status = False


def home(request):
    context = {}

    return render(request, 'home/home.html', context)


def signup(request):
	context = {}

	if request.method == "POST":
		try:
			student_signup = {}
			for field_name, field_value in request.POST.iteritems():
				student_signup[field_name] = field_value

			if student_signup['password'] != student_signup['confirm_password']:
				context['password_error'] = "Passwords didn't match. Try again"
				return render(request, 'home/signup.html', context)
			
			signup_status = register_student(student_signup)
			if signup_status == "Registration Failed for some reason. Try again":
				context['signup_failed'] = signup_status
				return render(request, 'home/signup.html', context)
			else:
				context['signup_success'] = signup_status
				return HttpResponseRedirect('/login')
				
		except UnboundLocalError:
			return render(request, 'home/signup.html', context)

	else:
		singup_form = SignupForm()
		context["singup_form"] = SignupForm
		return render(request, 'home/signup.html', context)


def register_student(student_signup):
	try:
		new_student = Student(
			first_name = student_signup['first_name'],
			last_name  = student_signup['last_name'],
			user_id    = student_signup['user_id'],
			email_id   = student_signup['email_id'],
			contact_no = student_signup['contact_no'],
			branch     = student_signup['branch'],
			password   = student_signup['password'],
		)
		new_student.save()
	except:
		return "Registration Failed for some reason. Try again"

	return "Registration done successfully"


def login(request):
	context = {}

	if request.method == "POST":
		students = Student.objects.all()
		for student in students:
			if student.user_id == request.POST['user_id']:
				if student.password == request.POST['password']:
					global login_status
					login_status = True
					return HttpResponseRedirect('/student_profile')
				else:
					context['error'] = "Incorrect password. Try again."
		context['error'] = "You are not registered yet."
	else:
		login_form = LoginForm()
		context['login_form'] = login_form
		
	return render(request, 'home/login.html', context)


def student_profile(request):
	context = {}

	print login_status
	context['login_status'] = login_status

	return render(request, 'home/student_profile.html', context)


def logout(request):
	context = {}

	global login_status
	login_status = False

	return HttpResponseRedirect('/')
