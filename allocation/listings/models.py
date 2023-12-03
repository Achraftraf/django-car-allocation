from django.db import models

class Allocation(models.Model):
    allocation_id = models.AutoField(primary_key=True)
    allocation_date = models.DateField()
    allocation_price = models.DecimalField(max_digits=10, decimal_places=2)
    allocation_nbr_days = models.IntegerField()
    client_id = models.IntegerField()
    car_id = models.IntegerField()

    class Meta:
        db_table = 'allocation'
