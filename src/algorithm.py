
def days_selection():
    """Selecciona el número de días en los que se repartiran las recetas"""

    print("\nSelecciona en cuantos días quieres repartir las recetas")
    
    print("\n1. De lunes a viernes.")
    print("\n2. De lunes a domingo.")

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

#def recipes_input():

#def menu_generator():

#def menu_output():

def main():
    """MAIN"""

    menu_vacio = days_selection()

if __name__ == "__main__":
    main()