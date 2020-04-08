# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Daily(models.Model):
    id = models.IntegerField(primary_key=True)
    Date = models.CharField(db_column='States', max_length=50, blank=True, null=True)  # Field name made lowercase.
    No_of_cases = models.CharField(db_column='No of cases', max_length=50, blank=True, null=True)  # Field name made
    # lowercase.
    No_of_recovered = models.CharField(db_column='No of recovered', max_length=50, blank=True, null=True)  # Field
    # name made lowercase .
    No_of_deaths = models.CharField(db_column='No of deaths', max_length=50, blank=True, null=True)  # Field name made
    # lowercase.

    def __str__(self):
        return self.Date

    class Meta:
        managed = False
        db_table = 'daily'
