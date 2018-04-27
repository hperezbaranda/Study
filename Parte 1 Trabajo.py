import numpy as np
import random
from time import time
import matplotlib.pyplot as plt

#Arreglo ordenado
class FilaPrioridad:
    def __init__(self,MAX):
        self.fila=np.array([None]*MAX)
        self.MAX=MAX
        self.cantidad=0

    def FilaVacia(self):
        if self.cantidad==0:
            return True
        else:
            return False


    def Inserir(self,elem):

        if self.cantidad<self.MAX:
            self.fila[self.cantidad]=elem
            pos=len(self.fila)-1
            while(self.fila[pos]>self.fila[pos-1] and pos!=0):
                aux=self.fila[pos-1]
                self.fila[pos-1]=self.fila[pos]
                self.fila[pos]=aux
                pos=pos-1
            self.cantidad+=1
            return True
        elif self.FilaVacia():
            self.fila[0]=elem
            self.cantidad+=1

        else:
            print('Fila llena')
    def Remover(self):
        if self.FilaVacia():
            print('Fila Vacia')
        else:
            aux=self.fila[0]
            for i in range(len(self.fila)-1):
                self.fila[i]=self.fila[i+1]
            return aux

    def Verificar(self):
        return self.fila[0]

class FilaPrioridadDesordenado:
    def __init__(self, MAX):
        self.fila = np.array([None]*MAX)
        self.MAX = MAX
        self.cantidad = 0

    def FilaVacia(self):
        if self.cantidad == 0:
            return True
        else:
            return False
#Arreglo desordenado
    def InserirD(self, elem):

        if self.cantidad < self.MAX:
            self.fila[self.cantidad] = elem
            self.cantidad+=1

        elif self.FilaVacia():
            self.fila[0] = elem
            self.cantidad+=1

        else:
            print('Fila llena')

    def BuscarElemMayorPrior(self):
        if self.FilaVacia():
            print('Fila Vacia')
        elif len(self.fila)==1:
            return self.fila[0]
        else:
            aux=self.fila[0]
            pos=0
            for i in range(len(self.fila)):
                if aux<self.fila[i]:
                    aux=self.fila[i]
                    pos=i
            return pos

    def RemoverD(self):
        if self.FilaVacia():
            print('Fila Vacia')
        else:
            pos=self.BuscarElemMayorPrior()
            for i in range(pos,len(self.fila)):
                self.fila[i]=self.fila[i+1]
            self.cantidad-=1




    def VerificarD(self):
        pos=self.BuscarElemMayorPrior()
        return self.fila[pos]

class FilaPrioridadH:
    def __init__(self, MAX):
        self.fila = np.array([None]*MAX)
        self.MAX = MAX
        self.cantidad=0

    def FilaVacia(self):
        if self.cantidad == 0:
            return True
        else:
            return False
#Heap
    def InsertarH(self,elem):
        if self.FilaVacia():
            self.fila[0]=elem


        elif self.cantidad==self.MAX:
            print('Fila llena')
        else:
            self.fila[self.cantidad]=elem
            pos=self.cantidad
            j=pos/2
            while(self.fila[pos]>self.fila[j]):
                self.fila[j],self.fila[pos]=self.fila[pos],self.fila[j]

                pos=j
                j=pos/2
        self.cantidad+=1

    def RemoverH(self):
        if self.FilaVacia():
            print('Fila Vacia')
        else:
            x=self.fila[0]
            i=0
            self.fila[0]=self.fila[self.cantidad-1]
            self.fila[self.cantidad-1]=0
            while(i<=(self.cantidad/2)-1):
                if self.fila[2*i+1]>self.fila[2*i+2]:
                    self.fila[i],self.fila[2*i+1]=self.fila[2*i+1],self.fila[i]

                    i=2*i+1
                else:
                    self.fila[i], self.fila[2 * i + 2] = self.fila[2 * i + 2], self.fila[i]

                    i = 2 * i + 2

            return x

    def VerificarH(self):
        return self.fila[0]




if __name__=="__main__":
    tam = 10
    xtam=[]
    dados=[[]]*3
    for i in range(5):
        tam=tam*10
        xtam.append(tam)
        print(tam)

        filaD=FilaPrioridadDesordenado(tam)
        filaOr=FilaPrioridad(tam)
        filaheap=FilaPrioridadH(tam)

        time1=time()
        for i in range(tam):
            filaD.InserirD(random.randint(0,1000))
        print("%.4f" %float(time()-time1))
        #print (filaD.fila)

        time2 = time()
        for i in range(tam):
           filaOr.Inserir(random.randint(0,1000))
        print("%.4f" %float(time() - time2))
       # print(filaOr.fila)

        time3 = time()
        for i in range(tam):
            filaheap.InsertarH(random.randint(0,1000))
        print("%.4f" %float(time() - time3))
        #print(filaheap.fila)
        print("----------")





        








