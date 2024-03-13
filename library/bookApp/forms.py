from django import forms
from .models import Book

class CommentForm(forms.Form):
    content = forms.CharField(label="Comment content", max_length=500)

class SearchForm(forms.Form):
    prompt = forms.CharField(label="Search books", max_length=30)

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['title', 'author', 'pcs_left', 'genre', 'cover_image', 'description']
   