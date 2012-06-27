from django.db import models


# Create your models here.

TITLE_CHOICES = (
    ('Comodo', 'Comodo'),
    ('Thwate', 'Thwate'),
)


"""
class Person(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=50, blank=True)
	email = models.EmailField(max_length=100)
	phone = models.IntegerField(max_length=20, blank=True)

	def __unicode__(self):
		return self.name
"""
class SSL(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    domain = models.CharField(max_length=200)
    reg_date = models.DateField(blank=True)
    exp_date = models.DateField()
    notes = models.TextField(blank=True)
    ca_auth = models.CharField(max_length=20, choices=TITLE_CHOICES)
    #persons = models.ForeignKey(Person)

    def __unicode__(self):
		return self.domain + "/" + self.name

   

