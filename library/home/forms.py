from django import forms
from search.models import Student

class LoginForm(forms.Form):
	user_id = forms.CharField(max_length=10)
	password = forms.CharField(widget=forms.PasswordInput)
	# class Meta:
	# 	model = Student
	# 	fields = ["user_id", "password"]

	# def __init__(self):
	# 	super(LoginForm, self).__init__()
	# 	self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Enter password'})


class SignupForm(forms.Form):
	first_name = forms.CharField(max_length=120)
	last_name = forms.CharField(max_length=120)
	email_id = forms.EmailField()
	contact_no = forms.IntegerField()
	user_id = forms.CharField(max_length=10)

	cse = 'CSE'
	me = 'ME'
	branches = (
		(cse, 'CSE'), 
		(me, 'ME'), 
		)

	branch = forms.ChoiceField(choices=branches)
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)

	# class Meta:
	# 	model = Student
	# 	fields = [
	# 	"first_name", 
	# 	"last_name", 
	# 	"email_id", 
	# 	"contact_no", 
	# 	"user_id", 
	# 	"branch", 
	# 	"password"
	# 	]

	# def __init__(self):
	# 	super(SignupForm, self).__init__()
	# 	self.fields["password"].widget = forms.PasswordInput(attrs={"placeholder": "Enter password"})
