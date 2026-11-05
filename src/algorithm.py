import random

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

    try:
        with open("recetas.txt", "r", encoding="utf-8") as archivo:
            recetas = []
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
                print(menu)
                return menu
    
            tamaño_lista = len(recetas)
            indice = random.randint(0, tamaño_lista-1)

            receta = recetas[indice]
            menu[dia].append(receta)
            recetas.remove(receta)

    return menu

#def menu_output(menu):

def main():
    """MAIN"""
    print("\nGENERADOR DE MENÚS AUTOMÁTICO\n")

    recetas = recipes_input()
    menu_vacio = days_selection()

    menu = menu_generator(recetas, menu_vacio)



if __name__ == "__main__":
    main()