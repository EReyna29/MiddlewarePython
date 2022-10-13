import threading,time,serial

def escribirtxt (cadena):
    try:
        file = open('prueba.txt','w')
        file.write(cadena)
        file.close()
    except:
        print("Exception occurred while you are trying to open file, something wrong...")

def leertxt ():
    while True:
        file = open('prueba.txt','r')
        mensaje= file.read()
        print(mensaje)
        palabras=mensaje.split("|")
        print(palabras)
        file.close()
        time.sleep(1)

def leerPuerto():
    puertoPIC=serial.Serial('COM3',9600)
    puertoPIC.write('getValue'.encode('utf-8')) ## Puede ser ascii, utf-8
    time.sleep(1)
    
    while True:
        try:
            cadenaRecibida = puertoPIC.readline().decode('ascii')
            escribirtxt(cadenaRecibida)
        except:
            print("Exception occurred, somthing wrong...")
    
    ##puertoPIC.close()
        



##hilo1 = threading.Thread(name='escribir',target=escribirtxt)
##hilo2 = threading.Thread(name='leer',target=leertxt)
##hilo1.start()
##hilo2.start()