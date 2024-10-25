from django.db import models

# Create your models here.
class menu(models.Model):
    itemName = models.CharField(max_length=30)
    price = models.IntegerField()

    def _str_(self):
        return self.itemName