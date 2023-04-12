nombre=input("Cómo te llamas: ")
ventas=float(input("Cuanto fue el monto en soles de las ventas de este mes: "))
comision=round(ventas*13/100,2)
print(f"Usted señor {nombre} recibira una comisión de {comision} nuevos soles.Felicitaciones!!")