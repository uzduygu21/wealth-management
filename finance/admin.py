from django.contrib import admin

from .models import User, Contact, Account, Quiz

# Register your models here.

admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Account)
admin.site.register(Quiz)



