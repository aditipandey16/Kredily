from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
import sqlite3

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        # Handle the POST request to add an employee
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        date_of_joining = request.POST.get('date_of_joining')

        # Create and save the Employee object
        Employee.objects.create(
            name=name,
            designation=designation,
            department=department,
            date_of_joining=date_of_joining
        )

        return HttpResponse('Employee added successfully')
    else:
        # Handle the GET request to show the form
        return render(request, 'add_employee.html')  # Create a template for the form
    

def get_all_employees(request):
    employees = Employee.objects.all()
    data = [{'name': emp.name, 'designation': emp.designation, 'department': emp.department, 'date_of_joining': emp.date_of_joining} for emp in employees]
    return JsonResponse({'employees': data})

def mark_attendance(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        attendance_date = request.POST.get('attendance_date')  # Update to match your form field name
        is_present = request.POST.get('is_present')  # Update to match your form field name

        # Update existing employee's attendance
        employee.attendance_date = attendance_date
        employee.is_present = is_present
        employee.save()

        return HttpResponse('Attendance marked successfully')
    else:
        return render(request, 'attendance_form.html', {'employee': employee})
        

def get_attendance_details(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        attendance_details = {
            'employee_id': employee.id,
            'name': employee.name,
            'attendance_date': employee.attendance_date,
            'is_present': employee.is_present,
        }
        return JsonResponse({'attendance_details': attendance_details})
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)
    
def employee_details(request, employee_id):
    # Retrieve the employee object or return a 404 response if not found
    employee = get_object_or_404(Employee, pk=employee_id)

    # You can customize the context based on your needs
    context = {
        'employee': employee,
    }

    # Render the employee details template with the provided context
    return render(request, 'employee_details.html', context)

def employee_count(request):
    try:
        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT department, count(id) AS employee_count
                FROM BasicHRMS_employee
                GROUP BY department;
            ''')
            rows = cursor.fetchall()

        context = {'employee_counts': rows}
        return render(request, 'employee_count.html', context)
    
    except Exception as e:
        return HttpResponse(f"Error Occurred: {str(e)}")
    
