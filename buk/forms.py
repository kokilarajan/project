from django import forms

from buk.models import Books



class BooksForm(forms.ModelForm):
	class Meta:
		model = Books
		exclude = ('created_date','buk_by',)
