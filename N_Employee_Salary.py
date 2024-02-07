Amount_Employee_Normal_Salary = 0;
Amount_Employee_More_3_Millon = 0;
Employee_Salary = 0;
Amount_Of_Employee = 0;
Salary_Cost_To_The_Corp = 0;

print("A continuación ingresa la cantidad de empleados que vas a registrar: ");
Amount_Of_Employee = int(input("--> "));

for Index in range (0, Amount_Of_Employee):
    print("Ingresa aquí el salario del empleado #",(Index+1), ", recuerda ingresar los datos en COP($): ");
    Employee_Salary = float(input("--> "));
    
    Salary_Cost_To_The_Corp = Salary_Cost_To_The_Corp + Employee_Salary;

    if Employee_Salary > 3000000:
        Amount_Employee_More_3_Millon = Amount_Employee_More_3_Millon + 1;

    if Employee_Salary >= 300000 and Employee_Salary <= 10000000:      
        Amount_Employee_Normal_Salary = Amount_Employee_Normal_Salary + 1;

    
print("Actualmente en la empresa existen ", Amount_Employee_Normal_Salary, " personas cuyo salario se encuentra entre $10'000.000 y $300.000 COP. ");
print("De los empleados registrados ", Amount_Employee_More_3_Millon, " tienen un salario de 3'000.000 o superior. ")    
print("Y el costo total de importe de la empresa por el pago de los salarios es de: ", Salary_Cost_To_The_Corp);   
    
    
#Height_Average =  Height_Average + User_Height; 

#Height_Average = Height_Average/Amount_Of_Persons;
#print("La altura promedio del grupo de personas ingresado es de: ", "{0:.3f}".format(Height_Average));