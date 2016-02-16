from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer (models.Model):
	
	firstname = models.CharField(max_length=100, unique=False)
	lastname = models.CharField(max_length=100, unique=False)
	email = models.EmailField(max_length=100, unique=True)
	phone = models.CharField(max_length=100, unique=False)
	company = models.CharField(max_length=100, unique=False)
	profile_pic=models.FileField(upload_to='uploads/')
	created_at =models.DateField()
	updated_at = models.DateField()

	def __unicode__(self):
		return '%s'  %self.firstname 

class ads(models.Model):
	title= models.CharField(max_length=100, unique=False)
	description = models.CharField(max_length=100, unique=False)
	category = models.CharField(max_length=100, unique=False)
	image = models.FileField(upload_to='ads/')
	physical_location= models.CharField(max_length=100, unique=False)
	def __unicode__(self):
		return '%s'  %self.title


class payments(models.Model):
	payment_for= models.CharField(max_length=100, unique=False)
	amount = models.CharField(max_length=100, unique=False)
	date = models.DateField()
	status = models.CharField(max_length=100, unique=False)
	payment_type = models.CharField(max_length=100, unique=False)
	def __unicode__(self):
		return '%s' %self.payment_for
	
		
class admin(models.Model):
 	user = models.OneToOneField(User)
 	profile_pic= models.FileField(upload_to='profile_pics', blank=False)
 	firstname = models.CharField(max_length=100, unique=False)
 	lastname = models.CharField(max_length=100, unique=False)
 	company = models.CharField(max_length=100, unique=False)

 	
