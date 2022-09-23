from django.db import models
from django.conf import settings

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=256)
	isbn = models.IntegerField()
	author = models.CharField(max_length=256)
	year = models.IntegerField()
	rate = models.FloatField()
	image = models.URLField(max_length=512)
	
	def __str__(self):
		return f"{ self.title } ({ self.year }) - { self.author }"

class borrow(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "customer" )
	book = models.ManyToManyField("Book", blank=False,related_name="books")
	date = models.DateField()
	expDate = models.DateField()
	
	def __str__(self):
		return f"/{self.expDate}/"
	