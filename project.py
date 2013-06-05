import foundingpoint
import interpolation
import sys
try:
	infilename = sys.argv[1]
except:
    print( " Usage :",sys.argv[0], " infile outfile ")
    sys.exit(1)
ifile = open(infilename, 'r')
price=[]
demand=[]
supply=[]
for line in ifile:
    row = line.split(',')
    price.append(float(row[0]))
    demand.append(float(row[1]))
    supply.append(float(row[2]))
ifile.close()
k1 = interpolation.parabolinter(price,demand) 
k2 = interpolation.parabolinter(price,supply) 
x = foundingpoint.balanceFinder(k1,k2)
y = [0,0]
y[0] = k1[0]*x[0]*x[0] + k1[1]*x[0] + k1[2]
y[1] = k1[0]*x[1]*x[1] + k1[1]*x[1] + k1[2]
print('A = ('+(str(x[0]))+';'+(str(y[0]))+')\n B = ('+(str(x[1]))+';'+(str(y[1]))+')')



