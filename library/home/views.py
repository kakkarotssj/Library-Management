# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from search.models import Student

# Create your views here.


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

			if student_signup['password'] != student_signup['confirm']:
				context['password_error'] = "Passwords didn't match. Try again"
				return render(request, 'home/signup.html', context)
			
			signup_status = register_student(student_signup)
			context['signup_status'] = signup_status

		except UnboundLocalError:
			pass

	return render(request, 'home/signup.html', context)


def register_student(student_signup):
	try:
		new_student = Student(
			first_name = student_signup['first_name'],
			last_name  = student_signup['last_name'],
			user_id    = student_signup['user_id'],
			email_id   = student_signup['email_id'],
			contact_no = student_signup['contact'],
			branch     = student_signup['branch'],
			password   = student_signup['password'],
		)
		new_student.save()
	except:
		return "Registration Failed for some reason. Try again"

	return "Registration done successfully"
