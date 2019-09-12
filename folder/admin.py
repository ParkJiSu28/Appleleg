from django.contrib import admin
from .models import Quiz, Management, Wrongnote


# Register your models here.
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['quiz_id', 'email', 'title', 'text', 'text', 'Management_id']
    search_fields = ['quiz_id', 'email', 'title', 'text', 'text', 'Management_id']


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = ['title', 'email']
    search_fields = ['title', 'email']


@admin.register(Wrongnote)
class WrongnoteAdmin(admin.ModelAdmin):
    list_display = ['wrong_id', 'email', 'image', 'title', 'text', 'Management_id']
    search_fields = ['wrong_id', 'email', 'image', 'title', 'text', 'Management_id']
