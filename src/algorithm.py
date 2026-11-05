import random
from contextlib import redirect_stdout

def days_selection() -> dict[str, list[str]]:
    """Selecciona el número de días en los que se repartiran las recetas"""

    print("\nSelecciona en cuantos días quieres repartir las recetas")
    
    print("1. De lunes a viernes.")
    print("2. De lunes a domingo.")

    try:
        while True:
            opcion = input("\nOpción: ")

            if opcion == "1":
                estructura = {"Lunes":[], "Martes":[], "Miércoles":[], "Jueves":[], "Viernes":[]}
                return estructura

            elif opcion == "2":
                estructura = {"Lunes":[], "Martes":[], "Miércoles":[], "Jueves":[], "Viernes":[], "Sábado":[], "Domingo":[]}
                return estructura
            
            else:
                print("Opción Inválida.")

    except KeyboardInterrupt:
        print("Cerrando programa...")

def recipes_input() -> list[str]:
    """Abre el archivo de texto que contiene las recetas y las guarda
    en una lista de strings."""

    recetas = []

    try:
        with open("recetas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                #print(linea.strip())   
                recetas.append(linea.strip())
    except FileNotFoundError:
        print("El archivo no existe.")

    #print(f"\n{recetas}")
    return recetas

def menu_generator(lista_recetas, menu):
    """Función que genera el menú."""

    recetas = lista_recetas.copy()

    for dia in menu.keys():
        for i in range(2):
    
            if not recetas:
                return menu
    
            tamaño_lista = len(recetas)
            indice = random.randint(0, tamaño_lista-1)

            receta = recetas[indice]
            menu[dia].append(receta)
            recetas.remove(receta)

    return menu

def menu_output(menu) -> None:
    """Muestra el menú semanal en formato de tabla."""

    ancho_minimo = 20
    separacion = 2

    # Calcular el ancho de cada columna según el día y sus recetas
    anchos = {}

    for dia, recetas in menu.items():
        longitud_maxima = max(
            [len(dia)] + [len(receta) for receta in recetas]
        )

        anchos[dia] = max(ancho_minimo, longitud_maxima + separacion)

    # Crear separador horizontal
    separador = "+" + "+".join(
        "-" * anchos[dia] for dia in menu
    ) + "+"

    ancho_total = len(separador)

    print("\n" + "=" * ancho_total)
    print("MENÚ SEMANAL".center(ancho_total))
    print("=" * ancho_total)

    print(separador)

    # Mostrar los días
    print("|", end="")

    for dia in menu:
        print(f"{dia.upper():^{anchos[dia]}}|", end="")

    print()
    print(separador)

    # Mostrar las recetas
    max_recetas = max(
        (len(recetas) for recetas in menu.values()),
        default=0
    )

    for i in range(max_recetas):
        print("|", end="")

        for dia, recetas in menu.items():
            receta = recetas[i] if i < len(recetas) else ""

            print(f"{receta:<{anchos[dia]}}|", end="")

        print()

    print(separador)

def main():
    """MAIN"""
    print("\nGENERADOR DE MENÚS AUTOMÁTICO\n")

    recetas = recipes_input()
    menu_vacio = days_selection()

    menu = menu_generator(recetas, menu_vacio)

    menu_output(menu)
    with open("menu_semanal.txt", "w", encoding="utf-8") as archivo:
        with redirect_stdout(archivo):
            menu_output(menu)

if __name__ == "__main__":
    main()