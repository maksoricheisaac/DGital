from django.contrib import admin
from .models import Contact, Newsletter

# Register your models here.
@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sendedAt')
    
@admin.register(Newsletter)
class AdminNewsletter(admin.ModelAdmin):
    list_display = ('email', 'addedAt')

