"""
Facturación del Servicio de Agua Potable
    El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa 
    de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
    Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y 
    recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.
A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.
Tarifa base:
    Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
    El costo por metro cúbico (m³) de agua es de $200/m³.

Bonificaciones y Recargos según tipo de cliente:

Cliente Residencial:
    Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
    Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

Cliente Comercial:
    Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
    Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
    Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

Cliente Industrial:
    Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
    consumo.
    Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
    Si el consumo es menor a 200 m³, se aplica un recargo del 10%.


    Casos especiales:
    Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
    En todos los casos, se aplica el IVA del 21% sobre el total.

Requerimientos del programa:

Solicitar al usuario:
Cantidad de metros consumidos
Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.

Calcular:
Subtotal de consumo.
Bonificaciones, si corresponde
Recargos, si corresponde
Subtotal, con recargos y bonificaciones.
IVA aplicado (21%), si corresponde.
Total final a pagar.
Mostrar en pantalla el desglose de los cálculos.
"""

factura = 7000
metro_cubico = 200

tipo_cliente = input("Ingrese su tipo de cliente: [Residencial / Comercial / Industrial]: ")
metros_consumidos = input("Ingrese la cantidad de metros cubicos consumidos: ")
consumos = int(metros_consumidos)
subtotal_consumo = metro_cubico * consumos
bonificacion = 1
recargo = 1
iva = 1.21



match tipo_cliente:
    case "Resdidencial":
        if consumos < 30:
            bonificacion = 0.10
        elif consumos > 80:
            recargo = 1.15
    case "Comercial":
        if consumos > 300:
            bonificacion = 0.12
        elif consumos > 150:
            bonificacion =  0.08
        elif consumos < 50:
            recargo = 1.05
    case "Industrial":
        if consumos > 1000:
            bonificacion = 0.30
        elif consumos > 500:
            bonificacion = 0.20
        elif consumos < 200:
            recargo = 1.10


total = (subtotal_consumo  + factura ) * bonificacion * recargo

if tipo_cliente == "Residencial" and total < 35000:
    descuento = 5
    total = total * (descuento / 100)
    print(f'El tipo de cliente {tipo_cliente} con {metros_consumidos} metros cubicos consumidos de agua debe abonar ${total} con un descuento del {descuento}% ')
else:
    total_con_iva = total * iva
    print(f'El tipo de cliente {tipo_cliente} con {metros_consumidos} metros cubicos consumidos de agua debe abonar ${total_con_iva} ')

