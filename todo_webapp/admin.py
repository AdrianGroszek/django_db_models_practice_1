from django.contrib import admin
from .models import Todo, Author, Category

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("created_at", "due_date", "priority")


admin.site.register(Todo, TodoAdmin)
admin.site.register(Author)
admin.site.register(Category)
