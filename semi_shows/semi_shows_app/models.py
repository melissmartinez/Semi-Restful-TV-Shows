from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['title'])<2:
            errors['title'] = "error, input must be 2 characters long and more."
        if len(data['network'])<3:
            errors['network']= "error, network must be 3 characters or more."
        if len(data['description'])>0 and len(data['description'])<10:
            errors['description'] = "error, description needs 10 characters and more."
        if data['release_date']=="":
            errors['release_date'] = "Date cannot be empty"
        else:
            if datetime.today()<datetime.strptime(data['release_date'], '%Y-%M-%d'):
                errors['release_date']="No dates in the future"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=150)
    network = models.CharField(max_length=150)
    release_date = models.DateField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()