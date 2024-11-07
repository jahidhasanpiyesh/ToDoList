from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class add_post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank =True)
    title = models.CharField(max_length=200)
    desh = models.TextField()
    complete = models.BooleanField(default=False)