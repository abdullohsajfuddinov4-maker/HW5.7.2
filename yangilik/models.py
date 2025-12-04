from django.db import models

# Create your models here.
class Categoriy(models.Model):
    name = models.CharField(max_length=100)
    where = models.DateField()

    def __str__(self):
        return self.name

class Yangilik(models.Model):
    name = models.CharField(max_length=100)
    qachon = models.DateField(auto_now_add=True)
    categoy = models.ForeignKey(Categoriy,on_delete=models.CASCADE)
    desc = models.TextField()

    def __str__(self):
        return self.name
    