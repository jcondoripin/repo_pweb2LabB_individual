from django.db import models

# Relación uno a muchos
class Language(models.Model):
    name = models.CharField(max_length=25)

class Framework(models.Model):
    name = models.CharField(max_length=25)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f"Framework {self.name}"

# Relación muchos a muchos
class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.name

class School(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student)

    def __str__(self) -> str:
        return self.name