lista = [2,3,6,8,0,1,4,6,3,4,78,2]

def sumar_lista(lista) : 
    sumatotal = 0 
    for numero in lista : 
        sumatotal += numero 
    return sumatotal 

resultado = sumar_lista(lista) 
print(f"el resultado es: {resultado}")
        
