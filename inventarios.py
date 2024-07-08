import os

def mostrar_menu():
    menu = "\n--- Menú del Sistema de Inventarios ---\n"
    menu += "1. Listar productos\n"
    menu += "2. Ingresar producto\n"
    menu += "3. Editar producto\n"
    menu += "4. Eliminar producto\n"
    menu += "5. Salir\n"
    
    # Imprimir menú en consola
    print(menu)
    
    # Guardar menú en archivo de texto
    with open('menu.txt', 'w') as file:
        file.write(menu)
    print("Menú guardado en 'menu.txt'.")

def listar_productos(productos):
    if not productos:
        print("No hay productos en el inventario.")
    else:
        print("\n--- Listado de Productos ---")
        print(f"{'ID':<5}{'Nombre':<20}{'Cantidad':<10}{'Precio':<10}")
        for i, producto in enumerate(productos, start=1):
            print(f"{i:<5}{producto[0]:<20}{producto[1]:<10}{producto[2]:<10}")

def ingresar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    precio = input("Ingrese el precio del producto: ")
    productos.append((nombre, cantidad, precio))
    print(f"Producto '{nombre}' ingresado con éxito.")

def editar_producto(productos):
    listar_productos(productos)
    id_producto = int(input("Ingrese el ID del producto a editar: "))
    if 1 <= id_producto <= len(productos):
        print("¿Qué desea editar?")
        print("1. Nombre")
        print("2. Cantidad")
        print("3. Precio")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nuevo nombre del producto: ")
            productos[id_producto - 1] = (nombre, productos[id_producto - 1][1], productos[id_producto - 1][2])
            print(f"Nombre del producto ID {id_producto} editado con éxito.")
        elif opcion == '2':
            cantidad = input("Ingrese la nueva cantidad del producto: ")
            productos[id_producto - 1] = (productos[id_producto - 1][0], cantidad, productos[id_producto - 1][2])
            print(f"Cantidad del producto ID {id_producto} editada con éxito.")
        elif opcion == '3':
            precio = input("Ingrese el nuevo precio del producto: ")
            productos[id_producto - 1] = (productos[id_producto - 1][0], productos[id_producto - 1][1], precio)
            print(f"Precio del producto ID {id_producto} editado con éxito.")
        else:
            print("Opción no válida.")
    else:
        print("ID de producto no válido.")

def eliminar_producto(productos):
    listar_productos(productos)
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    if 1 <= id_producto <= len(productos):
        productos.pop(id_producto - 1)
        print(f"Producto ID {id_producto} eliminado con éxito.")
    else:
        print("ID de producto no válido.")

def cargar_productos(filename):
    productos = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                nombre, cantidad, precio = line.strip().split(',')
                productos.append((nombre, cantidad, precio))
    else:
        productos = [
            ('Arroz', '100', '1.20'),
            ('Frijoles', '50', '0.80'),
            ('Aceite', '30', '2.50'),
            ('Azúcar', '75', '1.00'),
            ('Sal', '90', '0.50')
        ]
    return productos

def guardar_productos(filename, productos):
    with open(filename, 'w') as file:
        for producto in productos:
            file.write(','.join(producto) + '\n')
    print("Inventario guardado con éxito.")

def main():
    filename = 'inventario.txt'
    productos = cargar_productos(filename)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            listar_productos(productos)
        elif opcion == '2':
            ingresar_producto(productos)
            guardar_productos(filename, productos)
        elif opcion == '3':
            editar_producto(productos)
            guardar_productos(filename, productos)
        elif opcion == '4':
            eliminar_producto(productos)
            guardar_productos(filename, productos)
        elif opcion == '5':
            guardar_productos(filename, productos)
            print("Saliendo del sistema de inventarios...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()

