ancho = float(input("ingrese el ancho: ")) 
altura = float(input("ingresew altura: ")) 

def calcular_area_rectangulo(ancho,altura): 
    area = ancho * altura 
    return area 

area = calcular_area_rectangulo(ancho,altura) 

print(f"el area es: {area}")