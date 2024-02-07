Height_Average = 0;
User_Height = 0;
Amount_Of_Persons = 0;

print("A continuación ingresa cuántas medidas vas a ingresar: ");
Amount_Of_Persons = int(input("--> "));

for Index in range (0, Amount_Of_Persons):
    print("Ingresa aquí las medidas de la persona #",(Index+1), ", recuerda ingresar los datos en metros(m): ");
    User_Height = float(input("--> "));
    Height_Average =  Height_Average + User_Height; 

Height_Average = Height_Average/Amount_Of_Persons;
print("La altura promedio del grupo de personas ingresado es de: ", "{0:.3f}".format(Height_Average));
5