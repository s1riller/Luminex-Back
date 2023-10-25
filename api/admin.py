# abstract_user/users/admin.py
from django.contrib import admin

from .models import User, Imperfection, SkinType

admin.site.register(User)
admin.site.register(Imperfection)
admin.site.register(SkinType)
