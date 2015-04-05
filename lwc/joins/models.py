"""
Collection of Models to create db tables for this app
"""
from django.db import models

# Create your models here.
class Join(models.Model):
    """
    Model to save all the emails for people joining the web page
    """
    email = models.EmailField()
    ip_address = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email
