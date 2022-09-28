from datetime import datetime
import email
from django.db import models
import os
import datetime

# Create your models here.
def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/',filename)

class item(models.Model):
    name = models.TextField(max_length=200)
    image = models.ImageField(upload_to=filepath,blank=True)

class feedback(models.Model):
    name = models.TextField(max_length=200)
    email = models.TextField(max_length=200, null=True)
    message = models.TextField(max_length=200)