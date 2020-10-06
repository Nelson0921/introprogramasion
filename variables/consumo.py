consumo= int(input("¿cuanto fue su consumo?"))
if consumo<100:
elif 100<=consumo<=499:
    print("su monto a pagar es 1,20bs.")
elif 500<=consumo<=999:
    print("su monto a pagar es 1.50bs.")
else:
    print("su monto a pagar son 2,00bs.")