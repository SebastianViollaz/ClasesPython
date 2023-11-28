with open(r"Archivos\Data\archivo.txt","r") as file:
    
    #Devuelvo una lista dodne cada elemento es una linea del archivo
    data = file.readlines()
    
    #Elimina espacios en blanco o saltos de linea de cada linea
    for i in range(len(data)):
        data[i] = data[i].strip()

###Formato de archivo de texto        
INGRESADO = input("Ingrese el DNI del alumno: ")


#Recorre a toda la lista buscando el alumno con el dni ingresado
for linea in data:
    
    #Obtiene una lista con los datos de los alumnoes en el formato:
    #[DNI,Nombre,Apellido,Domicilio]
    info_alumno = linea.split("/")
    
    #Pregunta si el DNI ingresao es el correcto
    if info_alumno[0]  == INGRESADO :
        print(f"DNI = {info_alumno[0]}")
        print(f"Nombre = {info_alumno[1]}")
        print(f"Apellido = {info_alumno[2]}")
        print(f"Direccion = {info_alumno[3]}")
        break   #para dejar de buscar si ya encotre



#####
####De esta forma se reescribe el archivo en caso de que se momdifique
# with open(r"Data\archivo.txt","w") as f:
#     for linea in data:
#         f.write(linea)