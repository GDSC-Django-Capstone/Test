from django.db import models
from django.conf import settings
from users.models import CustomUser

# Create your models here.
class Book(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	pcs_left = models.CharField(max_length=50)
	genre =  models.CharField(max_length=150)
	cover_image = models.ImageField(upload_to='Book-Covers/', default='defaults/no-cover.jpeg')
	rating = models.IntegerField(default=0)
	description = models.TextField(default='No description available.')	
	borrowers = models.ManyToManyField(CustomUser)
	# comments =  book.comment_set.all()	
		# borrowers
	# books = CustomUser.book_set.all()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["title"]

class Comment(models.Model):
	id = models.IntegerField(primary_key=True)
	content = models.TextField()		
	time_posted = models.TimeField(auto_now_add=True)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)

	# poster --> relation with user

	class Meta:
		ordering = ["time_posted"]

	