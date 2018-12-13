# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math as math

phi = 3.14
x1=(np.random.random())
x2=(np.random.random())
if x1>10:
    x1=10
elif x1<-10:
    x1=-10
if x2>10:
    x2=10
elif x2<-10:
    x2=-10
Fungsi=-(np.absolute(np.sin(x1)*np.cos(x2)*math.exp(np.absolute(1-(np.sqrt((x1**2)+(x2**2)))/phi))))
Current=Fungsi
BestSol=Current
#print(BestSol)
i=1;
print(i,"Nilai Minimum dari ",x1," dan ",x2," = ",BestSol)
Temp= 100;
i=i+1
while i < Temp:
    x1=x1+(np.random.random())
    x2=x2+(np.random.random())
    if x1>10:
        x1=10
    elif x1<-10:
        x1=-10
    if x2>10:
        x2=10
    elif x2<-10:
        x2=-10
    Fungsi=-(np.absolute(np.sin(x1)*np.cos(x2)*math.exp(np.absolute(1-(np.sqrt((x1**2)+(x2**2)))/phi))))
    Next = Fungsi
    DeltaE=Next-Current
    if DeltaE<0:
        Current=Next
        BestSol=Current
    else:
        Cek=math.exp(-DeltaE/Temp)
        Bil=np.random.random()
        if Bil<Cek:
            Current=Next
            BestSol=Current
    print(i,"Nilai Minimum dari ",x1," dan ",x2," = ",BestSol)
    i=i+1
    Temp = Temp-1;
    plt.scatter(x1,BestSol)