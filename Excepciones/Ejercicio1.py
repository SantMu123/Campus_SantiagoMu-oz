try:
    num = print(7/0)
except ZeroDivisionError:
    print("Division por cero")
finally:
    print("Continua el codigo")

