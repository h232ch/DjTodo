from django.contrib import admin

# Register your models here.
from todo.models import Todo


@admin.register(Todo) # admin register
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'todo')