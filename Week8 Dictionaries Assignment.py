# Sample data
employee_numbers = [121, 122, 123]
employee_names = ['Franz', 'Rey', 'Angela']
employee_salaries = [60000, 45000, 4000]
total_hourly_rates = [45.65, 37.50, 06.37]
company_raises = [5.25, 3.50, 0.20]

# The empty list to record the dictionary items as an employee.
employee_database = []

# I use loop to combine the list from the employees data.
for i in range(len(employee_numbers)):
    # I create a dictionary list using the employee.
    employee_record = {
        "Employee Number": employee_numbers[i],
        "Employee Name": employee_names[i],
        "Salary": employee_salaries[i],
        "Hourly Rate": total_hourly_rates[i],
        "Raise %": company_raises[i]

    }
# Add dictionary list from database.
    employee_database.append(employee_record)

#Lastly print the record.
print("Final Employee Database:")
for record in employee_database:
    print(record)    