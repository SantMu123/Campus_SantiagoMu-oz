def menuRegistro():
    try:
        comando = input("""
          Selecciona según tu necesidad:
        A: Registrar nuevo usuario
        B: Seleccionar Carrera
        C: Ver Ranking
        D: Ver usuarios
        """
    )
        return comando
    except Exception:
        print("Comando incorrecto")
    

def menuCarrera():
    try:
        carrera = int(input("""
            Selecciona según tu necesidad:
            1: Atletismo
            2: Ciclismo
            3: Patinaje
            """
    ))
        return carrera
    except Exception:
        print("Comando incorrecto")

    