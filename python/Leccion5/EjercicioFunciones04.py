#Ej 4: Calculadora de Impuestos
# Crear una funcion para calcular el total de un pago incluyendo
# un impuesto aplicado (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_son_impuesto * (impuesto/100)
# Proporciones el pago sin impuesto: 1000
#Proporciones el monto del impuesto: 21%
# Pago con impuesto: xxxxx

#Creamos la funcion q calcula el total del pago incluyendo el impuwsto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos la función
pago_sin_impuesto = float(input('Digite el pago sin impuesto: '))
impuesto = float(input('Digite el monto del impuesto a aplicar: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')