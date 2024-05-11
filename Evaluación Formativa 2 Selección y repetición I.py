import time

contador_PikachuRoll=0
precio_PikachuRoll=4500
precio_OtakuRoll=5000
contador_OtakuRoll=0
precio_PulpoVenenosoRoll=5200
contador_PulpoVenenosoRoll=0
precio_AnguilaEléctricaRoll=4800
contador_AnguilaEléctricaRoll=0

contador_unidades=0



acumulador_subtotal=0


while True:
    print("\nBienvenido a la tienda de shushi")

    while True:
        print("\nCarta")

        print("1. Pikachu Roll $4.500")
        print("2. Otaku Roll $5.000")
        print("3. Pulpo Venenoso Roll $5.200")
        print("4. Anguila Eléctrica Roll $4800")
        print("5. Finalizar pedido")

        try:
            eleccion_menu=int(input("\nEleccion -> "))
        except ValueError:
            print("Caracter invalido")
        else:
            if eleccion_menu==1:
                contador_PikachuRoll=contador_PikachuRoll+1
                contador_unidades=contador_unidades+1
                acumulador_subtotal=acumulador_subtotal+precio_PikachuRoll
                print(f"Subtotal: ${acumulador_subtotal}")
            elif eleccion_menu==2:
                contador_OtakuRoll=contador_OtakuRoll+1
                contador_unidades=contador_unidades+1
                acumulador_subtotal=acumulador_subtotal+precio_OtakuRoll
                print(f"Subtotal: ${acumulador_subtotal}")
            elif eleccion_menu==3:
                contador_PulpoVenenosoRoll=contador_PulpoVenenosoRoll+1
                contador_unidades=contador_unidades+1
                acumulador_subtotal=acumulador_subtotal+precio_PulpoVenenosoRoll
                print(f"Subtotal: ${acumulador_subtotal}")
            elif eleccion_menu==4:
                contador_AnguilaEléctricaRoll=contador_AnguilaEléctricaRoll+1
                contador_unidades=contador_unidades+1
                acumulador_subtotal=acumulador_subtotal+precio_AnguilaEléctricaRoll
                print(f"Subtotal: ${acumulador_subtotal}")
            elif eleccion_menu==5:
                break
            else:
                print("Caracter invalido")

    print("\n********************************")
    print(f"\nCantidas de unidades: {contador_unidades}")
    print(f"Pikachu Roll  x{contador_PikachuRoll}")
    print(f"Otaku Roll  x{contador_OtakuRoll}")
    print(f"Pulpo Venenoso Roll  x{contador_PulpoVenenosoRoll}")
    print(f"Anguila Eléctrica Roll  x{contador_AnguilaEléctricaRoll}")

    print(f"\nSubtotal ${acumulador_subtotal}")

    print("\n********************************")


    codigo_otaku="soyotaku"
    descuento_codigo=0

    while True:
        try:
            print("\nTiene codigo de descuento?\n1. Si\n2. No. Ir a pagar")

            respuesta1=int(input("Elección -> "))
        except ValueError:
            print("\nCaracter invalido")
        else:
            if respuesta1==1:
                ingresar_codigo_descuento=input("Ingresar codigo de descuento: ")
                if (ingresar_codigo_descuento==codigo_otaku):
                    descuento_codigo=0.1
                    break
                else:
                    print("\nCodigo incorrecto")
            elif respuesta1==2:
                break
            else:
                print("Caracter invalido")

    print("\n********************************")
    print(f"\nSubtotal ${acumulador_subtotal}")
    total_descuentos=int(acumulador_subtotal*descuento_codigo)
    print(f"Total descuentos ${total_descuentos}")
    total_final=acumulador_subtotal-total_descuentos
    print(f"total a pagar ${total_final}")
    print("\n********************************")

    while True:
        try:
            print(f"\n¿Confirmar compra de ${total_final}?\n1. Si\n2. No")
            res_confirmacion_compra=int(input("Elección -> "))
        except ValueError:
            print("Caracter invalido")
        else:
            if (res_confirmacion_compra==1):
                time.sleep(1)
                print("\nProcesando...")
                time.sleep(2)
                print("\nGracias por su compra =)")
                break
            elif (res_confirmacion_compra==2):
                print("\nCompra cancelada")
                break
            else:
                print("Caracter invalido")
            
    while True:
        try:
            print("\n********************************\n\n¿Desea realizar un/otro pedido?\n1. Si\n2. No")

            res_otro_pedido=int(input("Elección -> "))
        except ValueError:
            print("Caracter invalido")
        else:
            if (res_otro_pedido==1):
                time.sleep(1)
                print("\nCargando...")
                time.sleep(2)
                print("\n********************************")
                break
                
            elif (res_otro_pedido==2):
                break
            else:
                print("\nCaracter invalido")
    
    if (res_otro_pedido==2):
        break

print("")