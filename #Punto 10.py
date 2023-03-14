print("inresa una distancia en METROS")
Dist=float(input())
VL= 299792458
VS=343
VC=341.106944
VB=12.42
Velocidad_luz = Dist/VL
Velocidad_sonido= Dist/VS
Velocidad_comercial= Dist/VC
Velocidad_bolt= Dist/VB

print("Velocidad de la luz:", Velocidad_luz, "segundos")
print("Velocidad del sonido", Velocidad_sonido,"segundos")
print("Velocidad del vehiculo mas rapido", Velocidad_comercial,"segundos")
print("Velocidad de Usain Bolt", Velocidad_bolt, "segundos")
