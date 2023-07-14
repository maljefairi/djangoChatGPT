# hello_world/admin.py

from django.contrib import admin
from .models import ChatSession, ChatMessage, DefaultChatSettings

class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 1

@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    inlines = [ChatMessageInline]
    list_display = ('id', 'started_at')  # Assuming that you've 'started_at' field in your ChatSession model
    search_fields = ['id']

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('session', 'role', 'content', 'created_at')
    search_fields = ['content', 'role']

@admin.register(DefaultChatSettings)
class DefaultChatSettingsAdmin(admin.ModelAdmin):
    list_display = ('role', 'description')
    search_fields = ['role', 'description']
