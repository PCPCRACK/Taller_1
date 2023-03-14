print("inresa una distancia en METROS") 
Dist=float(input()) #pide una distancia
VL= 299792458 #velocidad de la luz
VS=343 #velocidad del sonido
VC=341.106944 #velocidad del vehiculo comercial mas rapido
VB=12.42 #velocidad de Bolt
Velocidad_luz = Dist/VL #divide el el valor ingresado por cada uno de los valores establecidos
Velocidad_sonido= Dist/VS
Velocidad_comercial= Dist/VC
Velocidad_bolt= Dist/VB

print("Velocidad de la luz:", Velocidad_luz, "segundos")
print("Velocidad del sonido", Velocidad_sonido,"segundos")
print("Velocidad del vehiculo mas rapido", Velocidad_comercial,"segundos")
print("Velocidad de Usain Bolt", Velocidad_bolt, "segundos")
