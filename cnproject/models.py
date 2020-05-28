from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

	#relationship
	# does not work :     user = models.OneToOneField(User)
	#attributes
	first_name = models.CharField(max_length=128)
	dob = models.CharField(max_length=20)
	location = models.CharField(max_length=128)
	phone = models.CharField(max_length=10,unique=True)
	secret = models.CharField(max_length=10,default="Yet to Fil")
	mask=models.BooleanField(default=False)
	hand_sanitizer=models.BooleanField(default=False)
	proper_ventilation=models.BooleanField(default=False)
	wheel_chair=models.BooleanField(default=False)
	body_temperature=models.CharField(max_length=10,default="Yet to Fil")
	blood_pressure=models.CharField(max_length=10,default="Yet to Fil")
	pulse=models.CharField(max_length=10,default="Yet to Fil")
	cleaning=models.BooleanField(default=False)
	facilities=models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.phone)

class h2h(models.Model):

	#relationship
	# does not work :     user = models.OneToOneField(User)
	#attributes
	name = models.CharField(max_length=128)
	dob = models.CharField(max_length=20)
	sex = models.CharField(max_length=128)
	country = models.CharField(max_length=128)
	email = models.CharField(max_length=128)
	state = models.CharField(max_length=128)
	phone = models.CharField(max_length=10)
	problem= models.CharField(max_length=5000)

	def __str__(self):
		return str(self.problem)