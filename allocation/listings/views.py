from django.shortcuts import render
from django.http import HttpResponse

from .models import Allocation

# A basic view function
def index(request):
    # Some example data
    return HttpResponse('TEST')



def allocation_list(request):
    allocations = Allocation.objects.all()
    
    allocation_list_html = "<h1>Allocation List</h1><ul>"
    for allocation in allocations:
        allocation_list_html += (
            f"<li>ID: {allocation.allocation_id}, "
            f"Date: {allocation.allocation_date}, "
            f"Price: {allocation.allocation_price}, "
            f"Number of Days: {allocation.allocation_nbr_days}, "
            f"Client ID: {allocation.client_id}, "
            f"Car ID: {allocation.car_id}</li>"
        )
    allocation_list_html += "</ul>"
    
    return HttpResponse(allocation_list_html)

