from django.db import models

# Create your models here.
class memberdetails(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=20)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'memberdetails'
        verbose_name_plural = 'memberdetails'


def __str__(self):
    return self.firstname
