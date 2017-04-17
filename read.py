import csv
import os
from shutil import copyfile

path = '/home/user/Downloads/nexar_traffic_light_train/'
def Copy_TO(directory, src, name):
	if not os.path.exists(directory):
		os.makedirs(directory)
	try:
                copyfile(src, directory+'/'+name)
        except:
                return
	print  'Copied > '+ directory + '/' + name

f=open('/home/user/Downloads/nexar_traffic_light_train/labels.csv')
csv_f=csv.reader(f)
#red_signal=[]
for row in csv_f:
	#print row[0],
	name=row[0]
	row[0]= path+row[0]
	if row[1]=='2':
		Copy_TO('GREEN', row[0], name)
	elif row[1]=='1':
		Copy_TO('RED', row[0], name)
	else:
		Copy_TO('NO', row[0], name)

