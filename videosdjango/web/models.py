from django.db import models

# Create your models here.
class video(models.Model):
	recurso = models.FileField()

	def __str__(self):
		return str(self.recurso)