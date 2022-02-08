from multiprocessing import managers
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tasklist(models.Model):
    manage=models.ForeignKey(User, on_delete=models.CASCADE)
    task=models.CharField(max_length=500)
    status=models.BooleanField(default=False)


    def __str__(self):
        return self.task +' - '+ str(self.status)
