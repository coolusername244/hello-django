from django.db import models

# Create your models here.
# Making a class/model is like making a new spreadsheet on excel


class Item(models.Model):
    # Django will automatically add an ID field
    # Charfield = Characters or text only
    name = models.CharField(max_length=50, null=False, blank=False)
    # True or False only
    done = models.BooleanField(null=False, blank=False, default=False)

    '''In the database, this function below will return the name as what
        we call the task instead of 'Item Object (1)', 'Item Object (2)' '''
    def __str__(self):
        return self.name
