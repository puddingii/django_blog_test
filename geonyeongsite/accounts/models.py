from django.db import models

# Create your models here.
class Account(models.Model):
    acc_id = models.CharField(max_length = 20)
    acc_password = models.CharField(max_length = 20)
    password_chk = models.CharField(max_length = 20)

    #print title
    def __str__(self):
        return self.acc_id