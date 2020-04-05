from django.db import models


class Confirmed(models.Model):
    id = models.IntegerField(primary_key=True)
    categories = models.CharField(db_column='Categories', max_length=13, blank=True,
                                  null=True)  # Field name made lowercase.
    values = models.CharField(db_column='Values', max_length=3, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.categories

    class Meta:
        unique_together = ("categories", "values")
        managed = False
        db_table = 'confirmed'
