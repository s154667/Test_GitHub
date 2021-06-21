import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq
from numpy import genfromtxt

FileNameD = 'graphene with single rucl3_sample1_04.CSV'
FileNameD1 = 'graphene with green rucl3_sample2_07.CSV'
FileNameD2 = 'graphene with yellow rucl3_sample2_04.CSV'
FileName = 'graphene without single rucl3_sample2_01.CSV'
my_dataD = genfromtxt(FileNameD,delimiter=',')
my_dataD1 = genfromtxt(FileNameD1,delimiter=',')
my_dataD2 = genfromtxt(FileNameD2,delimiter=',')
my_data = genfromtxt(FileName,delimiter=',')

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(my_dataD[1:400,0],my_dataD[1:400,1],'-b',label = 'Doped')
#plt.plot(my_dataD1[1:400,0],my_dataD1[1:400,1]+70,'-r',label = 'Bilayer')
#plt.plot(my_dataD2[1:400,0],my_dataD2[1:400,1]+140,'-g',label = '> Bilayer')
#plt.yscale('log')
plt.ylabel('Intensity [a.u]')
plt.xlabel('Energy [1/cm]')
plt.legend()

plt.subplot(1,2,2)
plt.plot(my_data[1100:3000,0],my_data[1100:3000,1],'-r',label = 'Undoped')
#ax1.title('Raman for Doped Graphene')
#plt.ylabel('Intensity [a.u]')
plt.xlabel('Energy [1/cm]')
plt.legend()
plt.savefig('Raman_Spectroscopy')


#plt.plot(my_dataD[1:400,0],my_dataD[1:400,1],'-b',label = 'Doped')
#ax2.title('Raman for Undoped Graphene')
#ax2.ylabel('Intensity [a.u]')
#ax2.xlabel('Energy [1/cm]')
#ax2.legend()

