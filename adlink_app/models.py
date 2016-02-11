from django.db import models

# Create your models here.

class customer (models.Model):
	
	firstname = models.CharField(max_length=100, unique=False)
	lastname = models.CharField(max_length=100, unique=False)
	email = models.EmailField(max_length=100, unique=True)
	phone = models.CharField(max_length=100, unique=False)
	company = models.CharField(max_length=100, unique=False)
	profile_pic=models.FileField(upload_to='uploads/')
	created_at =models.DateField(auto_now=True, auto_now_add=True)
	updated_at = models.DateField(auto_now=True, auto_now_add=True)
	def __unicode__(self):
		return '%s'  %self.firstname 
]