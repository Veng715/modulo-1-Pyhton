carrito = {}

def menu():
    print("Este es su carrito de compras\n")
    print("1. Añadir")
    print("2. Ver")
    print("3. Remover")
    print("4. Suma total")
    print("5. Salir")

articulos = [("Manzanas", 2), ("Pan", 3), ("Leche", 5), ("Huevos", 5), ("Arroz", 3), ("Queso", 6)]

def main():
    while True:
        menu()
        option = input("¿Qué elección deseas elegir?: ")
        if option == "1":
            añadir()
        elif option == "2":
            ver()
        elif option == "3":
            remover()
        elif option == "4":
            suma_total()
        elif option == "5":
            print("Gracias por usar el carrito de compras")
            break
        else:
            print("Opcion no válida, intenta de nuevo.")

def añadir():
    print("\nArtículos disponibles:")
    for i, (nombre, precio) in enumerate(articulos, 1):
        print(f"{i}. {nombre} - ${precio}")
    try:
        eleccion = int(input("¿Qué artículo desea añadir? (número): "))
        if 1 <= eleccion <= len(articulos):
            nombre, _ = articulos[eleccion - 1]
            cantidad = int(input(f"¿Cuánto {nombre} desea añadir?: "))
            if cantidad > 0:
                carrito[nombre] = carrito.get(nombre, 0) + cantidad
                print(f"Se han añadido {cantidad} {nombre} al carrito.")
            else:
                print("Cantidad no válida.")
        else:
            print("Artículo no válido.")
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número.")

def ver():
    if not carrito:
        print("\nEl carrito está vacío.")
    else:
        print("\nContenido del carrito:")
        for nombre, cantidad in carrito.items():
            precio = next(pre for art, pre in articulos if art == nombre)
            print(f"{nombre} - Cantidad: {cantidad} - Precio unitario: ${precio}")

def remover():
    if not carrito:
        print("\nEl carrito está vacío. No hay nada que remover.")
        return
    print("\nArtículos en el carrito:")
    for i, nombre in enumerate(carrito.keys(), 1):
        print(f"{i}. {nombre} (Cantidad: {carrito[nombre]})")
    try:
        eleccion = int(input("¿Qué artículo desea remover? (número): "))
        if 1 <= eleccion <= len(carrito):
            nombre = list(carrito.keys())[eleccion - 1]
            cantidad = int(input(f"¿Cuántos {nombre} desea remover?: "))
            if 0 < cantidad < carrito[nombre]:
                carrito[nombre] -= cantidad
                print(f"Se han removido {cantidad} {nombre} del carrito.")
            elif cantidad >= carrito[nombre]:
                carrito.pop(nombre)
                print(f"Se han removido todos los {nombre} del carrito.")
            else:
                print("Cantidad no válida.")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número.")

def suma_total():
    total = 0
    for nombre, cantidad in carrito.items():
        precio = next(pre for art, pre in articulos if art == nombre)
        total += precio * cantidad
    print(f"\nEl total a pagar es: ${total}")

if __name__ == "__main__":
    main()