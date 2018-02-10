from django import forms


class SearchForm(forms.Form):
	search_field = forms.CharField()

	title = 'title'
	author = 'author'
	category = 'category'
	
	options = (
		(title, 'title'), 
		(author, 'author'), 
		(category, 'category'),
		)

	search_by = forms.ChoiceField(choices=options)
