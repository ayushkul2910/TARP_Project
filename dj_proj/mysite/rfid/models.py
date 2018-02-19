from django.db import models

# Create your models here.

class Cost(models.Model):
    ID=models.IntegerField(primary_key=True)
    From_city=models.CharField(max_length=250)
    To_city=models.CharField(max_length=250)
    Price=models.CharField(max_length=6)

    def __str__(self):
        return str(self.From_city)+' '+str(self.To_city)+' '+str(self.Price)
