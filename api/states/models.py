# from django.db import models
#
#
# # from django.db import models
# # from django.contrib.auth.models import User
# #
# #
# # class State(models.Model):
# #     name = models.CharField(max_length=100)
# #
# #     def __str__(self):
# #         return self.name
# #
# #
# # class Cases(models.Model):
# #     states = models.ForeignKey(State, related_name='numbers', on_delete=models.CASCADE)
# #     cases = models.CharField(max_length=100)
# #
# #     def __str__(self):
# #         return self.cases
# #
#
# class StatesCases(models.Model):
#     id = models.IntegerField(primary_key=True)
#     cases = models.CharField(max_length=100)
#     states_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'states_cases'
#
#
# class StatesState(models.Model):
#     name = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'states_state'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    states = models.CharField(db_column='States', max_length=13, blank=True, null=True)  # Field name made lowercase.
    cases = models.CharField(db_column='Cases', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data'
