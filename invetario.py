# 1. Estructura de inventario UNIFORME y con "cantidad"
inventario = [
    {"nombre": "Kyawthuita", "descripcion": "Mineral raro", "precio": 0.0, "cantidad": 1, "activo": False},
    {"nombre": "Manzana", "descripcion": "Fruta roja y deliciosa", "precio": 0.50, "cantidad": 200, "activo": True}, 
    {"nombre": "Pan", "descripcion": "Alimento basico", "precio": 1.00, "cantidad": 50, "activo": True},
    {"nombre": "Agua", "descripcion": "Esencial para la vida", "precio": 0.75, "cantidad": 150, "activo": True},
    {"nombre": "Libro", "descripcion": "Contiene informacion valiosa", "precio": 15.00, "cantidad": 25, "activo": True},
    {"nombre": "Lapiz", "descripcion": "Herramienta de escritura", "precio": 0.25, "cantidad": 500, "activo": True},
    {"nombre": "Camisa", "descripcion": "Prenda de vestir", "precio": 10.00, "cantidad": 80, "activo": True},
    {"nombre": "Zapatos", "descripcion": "Protege y conforta los pies", "precio": 20.00, "cantidad": 40, "activo": True},
    {"nombre": "Reloj", "descripcion": "Mide y muestra el tiempo", "precio": 50.00, "cantidad": 15, "activo": True},
    {"nombre": "Mochila", "descripcion": "Bolsa de transporte", "precio": 30.00, "cantidad": 30, "activo": True}, 
] 

# 2. Función mejorada con filtro "activo" y cálculo (precio * cantidad)
def calcular_valor_total(inventario):
    """Calcula el valor total del inventario solo para productos 'activos'."""
    total = 0.0
    for item in inventario:
        # A. Verificar si el producto está ACTIVO
        if item.get("activo") is True:
            # B. Obtener precio y cantidad de forma segura (con valor predeterminado)
            precio = item.get("precio", 0.0)
            cantidad = item.get("cantidad", 0)
            
            # C. Acumular el valor subtotal (Precio * Cantidad)
            total += precio * cantidad
            
    # D. Corregido: sintaxis simple de return
    return total

# Ejecución para probar el resultado
valor_total = calcular_valor_total(inventario)
print(f"El valor total del inventario ACTIVO es: ${valor_total:,.2f}")