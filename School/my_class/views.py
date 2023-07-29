from django.shortcuts import render, redirect
from .models import Students_here,Department

# Create your views here.
def index(request):
    return render(request,'index.html')


def all_std(request):
    stds = Students_here.objects.all()
    context = {
        'stds' : stds
    }
    return render(request,'all_std.html',context)


def add_std(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        roll = request.POST.get('roll')
        department_id = request.POST.get('dept')

        # Check if all required fields are filled
        if first_name and last_name and roll and department_id:
            # Get the department object based on the selected ID
            department = Department.objects.get(pk=department_id)

            # Save the student to the database
            student = Students_here(first_name=first_name, last_name=last_name, roll=roll, dept=department)
            student.save()

            # Redirect to the success page or any other page you wish
            return redirect('success_page')
        else:
            # Handle the case where required fields are not filled
            error_message = "Please fill in all required fields."
            context = {
                'departments': Department.objects.all(),
                'error_message': error_message,
            }
            return render(request, 'add_std.html', context)
    else:
        # Render the form for GET requests
        context = {
            'departments': Department.objects.all(),
        }
        return render(request, 'add_std.html', context)


def remove_std(request):
    return render(request,'remove_std.html')


def filter_std(request):
    return render(request,'filter_std.html')




def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})


