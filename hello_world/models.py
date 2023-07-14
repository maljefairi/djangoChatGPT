# hello_world/models.py

from django.db import models

class ChatSession(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set the field to now every time the object is saved.

class ChatMessage(models.Model):
    session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

class DefaultChatSettings(models.Model):
    ROLE_CHOICES = [
        ('system', 'System'),
        ('assistant', 'Assistant'),
        ('user', 'User'),
    ]  

    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    description = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"{self.role} ({self.description})"
