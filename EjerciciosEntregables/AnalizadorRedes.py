amigos = eval(input("Digite la cantidad de amugos que tiene en la red social: "))
publicaciones = eval(input("Digite la cantidad de publicaciones"))

if amigos >= 1 and amigos <= 50 and publicaciones < 20:
    categoria = "Bajo"
elif amigos > 50 and amigos <= 200 and publicaciones >= 20 and publicaciones < 90:
    categoria = "Bajo - medio"
elif amigos > 200 and amigos <= 600 and publicaciones >= 90 and publicaciones < 300:
    categoria = "medio"
elif amigos > 600 and amigos <= 1200 and publicaciones >= 300 and publicaciones < 1200:
    categoria = "medio - alto"
elif amigos > 1200 and publicaciones < 20 and publicaciones >= 1200:
    categoria = "alto"
else:
    print("Cantida de amigos o publicaciones no valido")