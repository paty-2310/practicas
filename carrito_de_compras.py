carrito = [
    {"pruducto": "nevera", "categoria": "electrodomestico", "precio": 1200, "cantidad": 1}, 
    {"pruducto": "televisor", "categoria": "electrodomestico", "precio": 800, "cantidad": 2}, 
    {"pruducto": "laptop", "categoria": "electronica", "precio": 1500, "cantidad": 1}, # 15% Desc.
    {"pruducto": "camisa", "categoria": "ropa", "precio": 60, "cantidad": 8},        # 10% Desc.
] 

def aplicar_descuento(carrito): 
    subtotal_total = 0.0 
    monto_final = 0.0 
    
    # BUCLE FOR: PROCESA CADA ARTÍCULO INDIVIDUALMENTE
    for producto in carrito: 
        subtotal_producto = producto['precio'] * producto['cantidad'] 
        descuento_producto = 0.0 

        # 1. Regla: Categoría 'electronica' (15%)
        if producto['categoria'] == 'electronica': 
            descuento_producto += 0.15 
            
        # 2. Regla: Compra Mayorista (10% si cantidad >= 5). Es un 'if' separado, no un 'elif'.
        if producto['cantidad'] >= 5: 
            descuento_producto += 0.10 
            
        # Calcular el precio final del artículo
        precio_con_desc = subtotal_producto * (1 - descuento_producto) 
        
        # Acumular los totales
        subtotal_total += subtotal_producto  # Costo original acumulado
        monto_final += precio_con_desc       # Costo con descuentos individuales acumulado
        
        # 🛑 NOTA: El 'return' NO va aquí. Debe ir fuera del bucle.

    # --- REGLA DE DESCUENTO GLOBAL (FIDELIDAD) ---
    # 3. Regla: Aplicar el 5% de descuento global (Solo si el subtotal es mayor a $200)
    if subtotal_total > 200: 
        monto_final *= 0.95 # Aplica el 5% al monto final.
        
    # 1. SOLUCIÓN: El 'return' va aquí, al final de la función.
    return subtotal_total, monto_final

# Ejecución y Resultados
subtotal_original, precio_final = aplicar_descuento(carrito)

print(f"💰 Precio Original (Subtotal): ${subtotal_original:,.2f}")
print(f"💳 Precio Final con Descuentos: ${precio_final:,.2f}")