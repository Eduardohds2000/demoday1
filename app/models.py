from django.db import models

# Create your models here.

class login(models.Model):

	#nome = models.CharField(max_length=20, null=False)
	email = models.EmailField(null=False)
	senha = models.CharField(max_length=2, null=False)
	#validarSenha = models.CharField(max_length=2, null=False)

