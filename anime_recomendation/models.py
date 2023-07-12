from django.db import models

class ani_model(models.Model):
    name = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 200)
    rating = models.IntegerField(blank=True, null=True)

    # def __str__(self):
    #     return self.name + ' ' + self.description