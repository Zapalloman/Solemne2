#creado por Javier Farías
#no me hago responsable de la distribucion de este codigo

from os import system
system("cls")
import pandas as pd
import matplotlib.pyplot as plt



class AnalizadorDatos:
    def __init__(self):
        system("cls")
        self.matriz_datos = []

    def menu_principal(self) -> None:
        print("1. Análisis del Archivo de Datos (1_EmpresasInversiones-One.csv)")
        print("2. Analítica de Datos 1")
        print("3. Analítica de datos 2")
        print("4. Salir")
        print("")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            #elegir la opcion 1
            self.analisis_archivo()
        elif opcion == "2":
            #elegir la opcion 2
            self.analitica_1()
        elif opcion == "3":
            #elegir la opcion 3
            self.analitica_2()
        elif opcion == "4":
            #salir del programa
            exit()
        else:
            #en caso de que no se elija una opcion valida
            print("Opción inválida")
            #se vuelve a llamar a la funcion
            self.menu_principal()


    #leer archivo
    def analisis_archivo(self) -> None:
        datos = pd.read_csv('1_EmpresasInversiones_One.csv')
    
        #se rellenan los valores sin datos con el "fillna", poniendo "SIN DATOS"
        datos["Pais"].fillna("SIN DATOS", inplace = True)  
        
        #borra las filas sin datos.
        datos.dropna(inplace = True)

        #Con la funcion replace, se remplaza el simbolo "$" con un valor vacio, para quitarlo.
        datos["Ingresos Anuales(USD MM)"] = datos["Ingresos Anuales(USD MM)"].str.replace("$", "")
        datos["Gastos Anuales(USD MM)"] = datos["Gastos Anuales(USD MM)"].str.replace("$", "")

        datos.to_csv('datos_modificados.csv', index=False)
        #se imprimen los datos modificado
        print(datos.to_string())

        #se usa la funcion describe para describir los datos del csv.
        print(datos.describe())
        input("[>] Presione enter para continuar...")
        self.menu_principal()

    

    #funcion para la razon de ingresos/gastos
    def razon_ingresos_gastos(self,df) -> None:
        df['Razon'] = df['Ingresos Anuales(USD MM)'] / df['Gastos Anuales(USD MM)']
        print(df['Razon'])
        return df['Razon']


    def analitica_1(self) -> None:
        #utilizar el archivo modificado para realizar el dataframe y el grafico
            datos = pd.read_csv('1_EmpresasInversiones_One.csv')
        
            #se rellenan los valores sin datos con el "fillna", poniendo "SIN DATOS"
            datos["Pais"].fillna("SIN DATOS", inplace = True)  
            
            #borra las filas sin datos.
            datos.dropna(inplace = True)

            #Con la funcion replace, se remplaza el simbolo "$" con un valor vacio, para quitarlo.
            datos["Ingresos Anuales(USD MM)"] = datos["Ingresos Anuales(USD MM)"].str.replace("$", "").astype(float)
            datos["Gastos Anuales(USD MM)"] = datos["Gastos Anuales(USD MM)"].str.replace("$", "").astype(float)

            datos.to_csv('datos_modificados.csv', index=False)

        #crear dataframe
            df = pd.DataFrame(datos)
            
            print(df)
            
        #razon ingresos/datos
            self.razon_ingresos_gastos(df)
            df = pd.DataFrame(df)
        
        #grafico
            plt.figure(figsize=(10, 10))
            plt.bar(df['Fundacion'], df['Razon'], color='blue')
            plt.title('Razon de Ingresos/Gastos por Año de Fundación')
            plt.xlabel('Año de Fundación')
            plt.ylabel('Razon de Ingresos/Gastos')
            #imprimir conclusion
            print("Se puede concluir que la razon de ingresos/gastos es mayor en los años 2008 y 2011, y menor en los años 2009 y 2012")
            print("")
            plt.show()
            input("[>] Presione enter para continuar...")  
            self.menu_principal()



    def analitica_2(self) -> None:
            #utilizar el archivo modificado para realizar el grafico
            
            datos = pd.read_csv('1_EmpresasInversiones_One.csv')
            #se rellenan los valores sin datos con el "fillna", poniendo "SIN DATOS"
            datos["Pais"].fillna("SIN DATOS", inplace = False)  
            #borra las filas sin datos
            datos.dropna(inplace = True)
            #Con la funcion replace, se remplaza el simbolo "$" con un valor vacio, para quitarlo.
            datos["Ingresos Anuales(USD MM)"] = datos["Ingresos Anuales(USD MM)"].str.replace("$", "").astype(float)
            datos["Gastos Anuales(USD MM)"] = datos["Gastos Anuales(USD MM)"].str.replace("$", "").astype(float)
            datos.to_csv('datos_modificados.csv', index=False)
            print(datos)
        #crear dataframe
            df = pd.DataFrame(datos)
            #seleccionar los datos de las industrias de energia y transporte
            df = df.loc[(df['Industria'] == 'Energía') | (df['Industria'] == 'Transporte')]
            print(df)       
            #seleccionar los datos de los años 2002 al 2009
            df = df.loc[(df['Fundacion'] >= 2002) & (df['Fundacion'] <= 2009)]
            print(df)
            #seleccionar los datos de los paises
            df = df.groupby(['Pais']).sum()
            #seleccionar los datos de los gastos anuales
            df = df['Gastos Anuales(USD MM)']
            #seleccionar los datos de los gastos anuales acumulados
            df = df.cumsum()
            #seleccionar los datos del porcentaje de gastos anuales acumulados
            df = df / df.max() * 100       
            print(df)
            #guardar el dataframe en un archivo txt
            df.to_csv('DF_P3.txt', index=False)
            #grafico
            plt.figure(figsize=(10, 10))
            plt.pie(df, labels=df.index, autopct='%1.1f%%', shadow=True, startangle=90)
            plt.title('Porcentaje de Gastos Anuales Acumulados por País')
            plt.show()
            #imprimir conclusion
            print("Se puede concluir que el porcentaje de gastos anuales acumulados por país de empresas fundadas entre los años 2002 al 2009 de las industrias de Energía y Transporte, es mayor en Uruguay, y menor en Argentina")
            input("[>] Presione enter para continuar...")  
            self.menu_principal()

    #ejecucion del programa
    def main(self):
        self.menu_principal()

analizador = AnalizadorDatos()
analizador.main()
