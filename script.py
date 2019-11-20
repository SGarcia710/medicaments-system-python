import pandas as pd
import  platform, subprocess
import csv
from tempfile import NamedTemporaryFile
import shutil

class Programa:
  def __init__(self):
    self.menu()

  def menu(self):
    op = 9
    while op!=0:
      self.limpiarConsola()
      print ("\t\tMENÚ")
      print ("1 - Ver medicamentos")
      print ("2 - Modificar medicamento")
      print ("3 - Verificar existencia")
      print ("0 - Cerrar")
      op = int(input("\t\tDigite una opción => "))
      if(op == 1):
        self.verMedicamentos()
      elif(op == 2):
        self.modificarMedicamento()
      elif(op == 3):
        self.verificarExistencia()

  def verificarExistencia(self):
    self.limpiarConsola()
    print ("\tVERIFICAR EXISTENCIA DE MEDICAMENTO:")
    codigo = input("Digite el código del medicamento => ")
    filename = 'bd.csv'
    fields = ['Cod.', 'Nombre', 'Cantidad']
    bandera = False
    cantidad = 0
    with open(filename, 'r', encoding='ascii') as csvfile:
      reader = csv.DictReader(csvfile, fieldnames=fields)
      for row in reader:
        if row['Cod.'] == str(codigo):
          bandera = True
          cantidad = int(row['Cantidad']) 
          break
    if bandera:
      if cantidad > 0:
        print("Hay ",cantidad, " existencias disponibles.")
      else:
        print("No hay existencia de este medicamento.")
    else:
      print("No existe un medicamento con este código.")
    pause = input("\n\nPresione cualquier tecla para continuar")


  def modificarMedicamento(self):
    self.limpiarConsola()
    print ("\tMODIFICAR MEDICAMENTO:")
    codigo = input("Digite el código del medicamento => ")
    filename = 'bd.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    fields = ['Cod.', 'Nombre', 'Cantidad']
    bandera = False
    with open(filename, 'r', encoding='ascii') as csvfile:
      reader = csv.DictReader(csvfile, fieldnames=fields)
      for row in reader:
        if row['Cod.'] == str(codigo):
          bandera = True
          break
    if bandera:
      with open(filename, 'r', encoding='ascii') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields) 
        nuevoNombre = input("Digite el nuevo nombre del medicamento => ")
        nuevaCantidad = input("Digite la nueva cantidad del medicamento => ")
        for row in reader:
          if row['Cod.'] == str(codigo):
              row['Nombre'], row['Cantidad']= nuevoNombre, nuevaCantidad
          row = {'Cod.': row['Cod.'], 'Nombre': row['Nombre'], 'Cantidad': row['Cantidad']}
          writer.writerow(row)
      shutil.move(tempfile.name, filename)
    else:
      print("No se encontró")
    pause = input("\nPresione cualquier tecla para continuar")
  
  def verMedicamentos(self):
    self.limpiarConsola()
    print ("\tLISTA DE MEDICAMENTOS")
    bd = pd.read_csv('bd.csv', encoding ='latin1')
    print(bd.to_string(index = False))
    pause = input("\nPresione cualquier tecla para continuar")

  def limpiarConsola(self):
    if platform.system()=="Windows":
      subprocess.Popen("cls", shell=True).communicate() 
    else: 
      print("\033c", end="")

#ejecucion del programa
Programa()