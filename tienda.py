# Creamos una lista vacía para almacenar las ventas diarias
ventas_diarias = []

# Solicitamos al usuario ingresar las ventas de cada día
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

for dia in range(1, 8):  # 7 días en la semana
    venta_dia = float(input(f"Ingrese las ventas del {dias_semana[dia-1]} en dólares: "))
    ventas_diarias.append(venta_dia)

# Calculamos el total de ventas en la semana
total_semanal = sum(ventas_diarias)

# Imprimimos el balance semanal
print(f"Balance semanal de ventas:")
for dia, venta_dia in enumerate(ventas_diarias, start=1):
    print(f"{dias_semana[dia-1].capitalize()}: ${venta_dia:.2f}")

print(f"Total semanal: ${total_semanal:.2f}")
