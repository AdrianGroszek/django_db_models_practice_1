from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class Todo(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='todos')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    due_date = models.DateField(auto_now=False)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(default='', unique=True, db_index=True)

    def get_priority_label(self):
        if self.priority <= 2:
            return "🟢 Niski"
        elif self.priority <= 4:
            return "🟡 Średni"
        else:
            return "🔥 Wysoki"

    def get_priority_class(self):
        if self.priority <= 2:
            return "low"
        elif self.priority <= 4:
            return "medium"
        else:
            return "high"

    def __str__(self):
        return f'{self.title} [{self.priority}]'
