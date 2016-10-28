from django.contrib import admin
from bank.models import Transaction, Profile
# Register your models here.

admin.site.register([Transaction, Profile])
