
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

def menu_generator(lista_recetas, menu_vacio):
    """Función que genera el menú."""
    menu = menu_vacio
    contador = 0

    for dia in menu.keys():
        for i in range(2):
            if not lista_recetas:
                print(menu)
                return menu
            receta = lista_recetas[0]
            menu[dia].append(receta)
            lista_recetas.remove(receta)

#def menu_output():

def main():
    """MAIN"""
    print("\nGENERADOR DE MENÚS AUTOMÁTICO\n")

    recetas = recipes_input()
    menu_vacio = days_selection()

    menu = menu_generator(recetas, menu_vacio)

if __name__ == "__main__":
    main()