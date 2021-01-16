from django.db import models

class Positions(models.Model):
	parent = models.CharField(max_length=30)
	name = models.CharField(max_length=120)
	price = models.CharField(max_length=10)
	image = models.ImageField(blank=True, upload_to='homepage/static/homepage/positions/', help_text='150x150px', verbose_name='Ссылка картинки')
	def __str__(self):
		return self.name