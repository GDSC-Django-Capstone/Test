from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookApp.models import Comment, Book
from django.conf import settings
from bookApp.forms import CommentForm, SearchForm, BookUploadForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
	books = Book.objects.all()

	if request.method == "POST":
		form = BookUploadForm(request.POST)
		if form.is_valid():
			# prompt = form.cleaned_data["prompt"]
			# books = help_search(prompt)
			form.save()
			
	else:
		form = CommentForm()

	return render(request, 'bookApp/home.html', {'books':books, 'search_form':SearchForm()})

@login_required
def book_upload(request):
	if request.method == "POST":
		form = BookUploadForm(request.POST, request.FILES)
		if form.is_valid():
			print(request.FILES)
			form.save()
			return redirect("/")
			
	else:
		form = BookUploadForm()
	return render(request, 'bookApp/book_upload.html', {'form':form})


def book_detail(request, book_id):
	book = Book.objects.filter(id=book_id)
	comments = book.first().comment_set.all()

	
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			cont = form.cleaned_data["content"]
			_comment = Comment()
			_comment.content = form.cleaned_data["content"]
			_comment.book = book.first()
			_comment.save()

	else:
		form = CommentForm()

	return render(request, 'bookApp/book_detail.html', {'book':book, 'form':form, 'comments':comments, 'search_form':SearchForm()})	# book_id = request.GET.get('book_id')
	

def search_books(request, book_id=None):
	# form = SearchForm()
	books = []
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			prompt = form.cleaned_data["prompt"]
			books = help_search(prompt)
			
	else:
		form = CommentForm()
	return render(request, 'bookApp/search.html', {'search_form':form, 'book':books})

def help_search(prompt):
	by_title = Book.objects.filter(title=prompt)
	by_author = Book.objects.filter(author=prompt)
	return by_title + by_author