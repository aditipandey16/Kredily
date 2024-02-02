# BasicHRMS/urls.py
from django.urls import path
from .views import home, add_employee, get_all_employees, employee_details, mark_attendance, get_attendance_details, employee_count

urlpatterns = [
    path('', home, name='home'),
    path('add_employee/', add_employee, name='add_employee'),
    path('get_all_employees/', get_all_employees, name='get_all_employees'),
    path('employee_details/<int:employee_id>/', employee_details, name='employee_details'),
    path('mark_attendance/<int:employee_id>/', mark_attendance, name='mark_attendance'),  # New endpoint
    path('get_attendance_details/<int:employee_id>/', get_attendance_details, name='get_attendance_details'),  # New endpoint
    path('employee_count/', employee_count, name='employee_count'),
]
