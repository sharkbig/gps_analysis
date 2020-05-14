import numpy as np
import glob 
import os
import matplotlib.pyplot as plt

def julianday(yr,month,day):
	if yr%4==0:
		mc=[31,29,31,30,31,30,31,31,30,31,30,31]
	else:
		mc=[31,28,31,30,31,30,31,31,30,31,30,31]
	month=int(month)
	ds=day+np.sum(mc[:month-1])
	return yr+ds/sum(mc)


def relaxation(t,eqt0):
	if eqt0<t[0] and eqt0>t[-1]:
		return None
	else:
		green=np.ones(shape=t.shape)
		green[t<eqt0]=0
		rex=(1-np.exp(-t+eqt0))*green
		return np.vstack((green,rex))

def fitGPS(t,p,eqt=None):
	sinf=np.sin(6.28*t)
	cosf=np.cos(6.28*t)
	poly0=np.ones(shape=t.shape)
	poly1=t
	greenf=np.vstack((poly0, poly1, sinf, cosf))

	if len(eqt)==0:
		pass
	else:
		for es in eqt:
			greenf=np.vstack((greenf,relaxation(t,es)))
	gtg=np.dot(greenf,greenf.transpose())
	sol=np.linalg.lstsq(gtg,np.dot(greenf,p),rcond=-1)[0]

	return sol,greenf



if __name__ == "__main__": 
	files=glob.glob("*COR")
	for fp in files:
		loadin=np.loadtxt(fp,usecols=[0,6])
		solution= fitGPS(loadin[:,0],loadin[:,1],[julianday(2010,3,4),julianday(2016,2,6)])

		plt.plot(loadin[:,0],loadin[:,1],'^',ms=0.5)
		plt.plot(loadin[:,0],np.dot(solution[0],solution[1]))
		plt.savefig(fp+"_fit"+".jpg")
		plt.close()
