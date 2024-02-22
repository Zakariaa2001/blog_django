from django.db import models

# Create your models here.

class CategoryCourse(models.Model):
    name = models.CharField(max_length=50)
class Courses(models.Model) :
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category_course = models.ForeignKey(CategoryCourse,on_delete=models.CASCADE)