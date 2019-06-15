from django.db import models

class Client(models.Model):
    cl_id = models.IntegerField(blank=True, null=True)
    cl_name = models.CharField(max_length=255, blank=True, null=True)
    cl_surname = models.CharField(max_length=255, blank=True, null=True)
    cl_pwd = models.IntegerField(blank=True, null=True)
    cl_id = models.IntegerField(blank=True, null=True)

class Account(models.Model):
    acc_client = models.ForeignKey(Client, related_name="cl_accounts", on_delete=models.SET_NULL, null=True, blank=True)
    acc_id = models.IntegerField(blank=True, null=True)
    acc_number = models.IntegerField(blank=True, null=True)
    acc_type = models.CharField(max_length=255, blank=True, null=True)
    acc_opened = models.DateField(blank=True, null=True)

class Transaction(models.Model):
    tr_account = models.ForeignKey(Account, related_name="acc_transactions", on_delete=models.SET_NULL, null=True, blank=True)
    tr_id = models.IntegerField(blank=True, null=True)
    tr_amount = models.FloatField(blank=True, null=True)
    tr_date = models.DateField(blank=True, null=True)


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
