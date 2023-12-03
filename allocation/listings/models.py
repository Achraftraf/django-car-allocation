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
        
        
        
        # add an object 
        
        
#         from listings.models import Allocation  

# # Create an Allocation object
# allocation_obj = Allocation(
#     allocation_date='2023-12-03',
#     allocation_price=150.00,
#     allocation_nbr_days=5,
#     client_id=1,
#     car_id=4
# )

# # Save the object to the database
# allocation_obj.save()
