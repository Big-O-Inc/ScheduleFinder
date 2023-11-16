from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from users.models import User
from django import forms

class UsersChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class UsersAdmin(UserAdmin):
    form = UsersChangeForm

# Register your models here.
admin.site.register(User)