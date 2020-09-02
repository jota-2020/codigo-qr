import qrcode
from PIL import Image
print("---------------------------------------------------")
print("Bienvenido a plataforma de ingreso Pasajeros TurBus")
print("---------------------------------------------------")
nombre_pasajero=input("Nombre Pasajero: ")
numero_boleto=input("Numero de Boleto: ")
asiento_numero=input("Numero de asiento: ")
lugar_destino=input("Lugar de Destino: ")
imagen=qrcode.make(("Nombre: ")+nombre_pasajero+(" Numero de boleto: ")+numero_boleto+(" Numero de asiento: ")+asiento_numero+(" Lugar de destino: ")+lugar_destino)

nombre_imagen=input("Ingrese Rut pasajero sin puntos ni guion: ")+'.png'
archivo_imagen=open(nombre_imagen,'wb')
imagen.save(archivo_imagen)
archivo_imagen.close

ruta_imagen='./'+nombre_imagen
Image.open(ruta_imagen).show()
