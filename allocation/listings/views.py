from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from listings.form import AllocationForm

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

def allocationlist(request):
    allocations = Allocation.objects.all()
    return render(request, 'listings/allocation.html', {'allocations': allocations})

def create_allocation(request):
    if request.method == 'POST':
        form = AllocationForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            allocation_data = form.cleaned_data
            # Create Allocation object from form data
            allocation_obj = Allocation(
                allocation_date=allocation_data['allocation_date'],
                allocation_price=allocation_data['allocation_price'],
                allocation_nbr_days=allocation_data['allocation_nbr_days'],
                client_id=allocation_data['client_id'],
                car_id=allocation_data['car_id']
            )
            # Save the object to the database
            allocation_obj.save()
            return redirect('views.allocation')  # Redirect to allocation list page after creation
    else:
        form = AllocationForm()
    return render(request, 'listings/create_allocation.html', {'form': form})

def update_allocation(request, pk):
    allocation = get_object_or_404(Allocation, pk=pk)
    if request.method == 'POST':
        form = AllocationForm(request.POST, instance=allocation)
        if form.is_valid():
            form.save()
            return redirect('views.allocation')  # Redirect to allocation list page after update
    else:
        form = AllocationForm(instance=allocation)
    return render(request, 'listings/update_allocation.html', {'form': form})

def delete_allocation(request, pk):
    allocation = get_object_or_404(Allocation, pk=pk)
    if request.method == 'POST':
        allocation.delete()
        return redirect('views.allocation')  # Redirect to allocation list page after delete
    return render(request, 'listings/delete_allocation.html', {'allocation': allocation})

