from django.db import models

# Create your models here.

class Employers(models.Model):
    employerno = models.AutoField(db_column='EmployerNo', primary_key=True)  # Field name made lowercase.
    work_employer = models.CharField(db_column='Work_Employer', max_length=100)  # Field name made lowercase.
    workaddress = models.CharField(db_column='WorkAddress', max_length=400)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employers'
        
class Customer(models.Model):
    customerno = models.AutoField(db_column='CustomerNo', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=200)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    homeaddress = models.CharField(db_column='HomeAddress', max_length=400)  # Field name made lowercase.
    employerno = models.ForeignKey('Employers', models.DO_NOTHING, db_column='EmployerNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'



class Loans(models.Model):
    loanno = models.AutoField(primary_key=True)
    customerno = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerNo')  # Field name made lowercase.
    interest = models.DecimalField(db_column='Interest', max_digits=10, decimal_places=0)  # Field name made lowercase.
    term = models.IntegerField(db_column='Term')  # Field name made lowercase.
    paydate = models.DateField(db_column='Paydate')  # Field name made lowercase.
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loans'



