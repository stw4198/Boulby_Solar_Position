import matplotlib.pyplot as plt
import numpy as np
import os
import pdb
from matplotlib.ticker import FormatStrFormatter

dirname = os.path.dirname(os.path.realpath(__file__))

# read data for solar angle calculated from keisan.casio.com

def loadSolarPosition(num_hours=24):

	"""
	Load in data for the elevation and azimuthal position of the Sun in 2020 from keisan.casio.com
	"""
	dirname = os.path.dirname(os.path.realpath(__file__))

	times = np.arange(0,num_hours+1) # 0 - 24 h

	Date=[]
	Ele=[]
	Azi=[]

	for i in times:
		date = np.loadtxt(dirname + "/../Data/" + str(i) + "h.txt", delimiter='\t',dtype=np.str,usecols=[0])
		x = np.loadtxt(dirname + "/../Data/" + str(i) + "h.txt", delimiter='\t',usecols=[1,2])
		ele,azi = x[:,0], x[:,1]
		Date.append(date)
		Ele.append(ele)
		Azi.append(azi)

	return Date,Ele,Azi,times

Date,Ele,Azi,times=loadSolarPosition()

def SolarPositionBoulbyPlot(Date,Ele,Azi,times):

	"""
	Plot the elevation of the Sun through the day. Compare days through the year.
	"""

	plt.figure(figsize=(20,20))
	for i in times:
		plt.plot(Date[i],Ele[i],label=i)
		plt.xticks(Date[i],rotation='vertical')
		plt.xlabel('Date')
		plt.ylabel('Elevation Above Horizon')
		plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d$^o$'))
		plt.legend()
	plt.savefig(dirname + "/../Plots/SolarElevationbyDayBoulby.pdf")
	plt.show()
	return


SolarPositionBoulbyPlot(Date,Ele,Azi,times)

print('Mean Solar elevation angle at Boulby = %.4f' % np.mean(Ele),u"\N{DEGREE SIGN}")

def SolarPositionYearBoulbyPlot(Date,Ele,Azi,times):

	"""
	Plot the elevation of the Sun over 1 year (2020)
	"""

	Ele_day = []

	Ele=np.array(Ele)

	days=np.arange(0,74)

	for h in days:
		for j in times:
			ele_day = Ele[j,h]
			Ele_day.append(ele_day)

	Ele_day_length=np.arange(0,len(Ele_day))

	custom_x_ticks = []

	Date=np.array(Date)

	for p in range(0,74):
		custom_ticks = Date[0,p]	
		custom_x_ticks.append(custom_ticks)

	label_pos_x = np.arange(0,len(Ele_day_length),25)

	plt.figure(figsize=(100,100))
	plt.plot(Ele_day_length,Ele_day)
	plt.ylabel('Elevation Above Horizon',fontsize=15)
	plt.xlabel('Date',fontsize=15)
	plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d$^o$'))
	plt.xticks(label_pos_x,custom_x_ticks,rotation=90)
	plt.title('Solar Elevation in 2020 at Boulby',fontsize=20)
	plt.savefig(dirname + "/../Plots/SolarElevation2020Boulby.pdf")
	plt.show()
	
	return

SolarPositionYearBoulbyPlot(Date,Ele,Azi,times)
