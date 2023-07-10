import os
import numpy as np
os.system("CLS")

rut = []
esc = list(range(1,101))

menu="""
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
Digite opcion:
"""
platinum = 0
gold = 0
silver = 0
i = input("ingrese su numbre: ")
l = input("ingrese su apellido: ")
precios = """
1. Platinum $120000
2. Gold     $80000
3. Silver   $50000
"""
while True:
    try:
        opc=int(input(menu))
        if opc == 5:
            input(f"Gracias por su ingeso o compra señor/a {i} {l} emitido el 10/07/2023")
            break
        elif opc == 1:
            while True:
                try:
                    for i in range(101):
                        print(precios)
                        compra = int(input("Numero de asiento a comprar: "))
                        if compra == esc[i]:
                            esc[i] = 'x'
                            if compra >= 0 and compra < 21:
                                platinum += 1
                            elif compra >= 21 and compra < 51:
                                gold += 1
                            
                            elif compra >= 51 and compra < 101:
                                silver += 1
                                
                            elif compra >= 0 and compra < 21 and esc[i]=='x':
                                print("No esta disponible")
                            elif compra >= 21 and compra < 51 and esc[i]=='x':
                                print("No esta disponible")
                            elif compra >= 51 and compra < 101 and esc[i]=='x':
                                print("No esta disponible")
                            else:
                                print("intente nuevamente")
                            
                            irut=int(input("Ingrese su rut: "))
                            if irut >= 10000000 and irut < 100000000:
                                rut.append(irut)
                            break
                    else:
                        print("intente nuevamente")
                    break
                except:
                    print("Error, ocurrio una excepcion")
        elif opc == 2:
                print(esc)
        elif opc == 3:
                rut.sort()
                print(rut)
        elif opc == 4:
            print(f"""
                    | Tipo entrada     | Cantidad             | Total |
                      Platinum $120000   {platinum}                      {platinum*120000}
                      Gold     $80000    {gold}                      {gold*80000}
                      Silver   $50000    {silver}                      {silver*50000}
                    Total                {platinum+gold+silver}                      {platinum*120000+gold*80000+silver*50000}       
            """)
        
    except:
        print("Error, ocurrio una excepcion")