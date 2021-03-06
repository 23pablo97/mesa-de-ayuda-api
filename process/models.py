from django.db import models
from django.contrib.auth.models import User

class Process(models.Model):
  name = models.CharField(max_length=70, blank=False, default='')
  description = models.TextField(blank=False, default='')
  banner_description = models.TextField(blank=False, default='')
  icon = models.TextField(blank=False, default='')
  created_at = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)
  published = models.BooleanField(default=True)
  created_by = models.ForeignKey(User, default=None, blank=True, on_delete=models.DO_NOTHING, related_name='created_by')
  updated_by = models.ForeignKey(User, default=None, blank=True, on_delete=models.DO_NOTHING, related_name='updated_by')