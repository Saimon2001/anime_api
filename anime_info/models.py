from django.db import models
from utils.models import BaseModel
from anime_recomendation.models import ani_model
# Create your models here.

class biblio(BaseModel):
    anime_id = models.ForeignKey(ani_model, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class info(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=20)
    release_year = models.IntegerField()