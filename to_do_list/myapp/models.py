from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),        
        ('completed', 'Completed'),
        ('failed', 'Failed')           
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  
    ends_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.ends_at and self.ends_at < datetime.now():
            self.status = 'failed'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
