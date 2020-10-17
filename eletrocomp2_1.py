import math
import matplotlib.pyplot as plot
import numpy

mi_0 = 4*math.pi*pow(10,-7)

dataH = []
dataB = []
x_range = []
# aux = 0

def calK (i,r):
  return -i/(2*math.pi*r)

def calJ (i,r1):
  return i/(math.pi*pow(r1,2))

def inductionCable(i,r1,r2,r3):
  answer = ((mi_0*i)/((2*math.pi)/i))*(math.log(r2/r1) + 3*math.log(r3,r2) + 1/4*math.pi)
  return answer

def magnetField (r,I):
  if r < 0.015:
    answer = (I*r)/(math.pi*2.0*pow(0.015,2))
  elif r < 0.03:
    answer = I/(2.0*math.pi*r)
  else:
    answer = 0
  return answer

def magnetInduction (r,I):
  if r < 0.015:
    answer = mi_0*magnetField(r,I)
  elif r < 0.02:
    answer = mi_0*magnetField(r,I)
  elif r < 0.03:
    answer = 3*mi_0*magnetField(r,I)
  else:
    answer = 0
  return answer

for i in numpy.arange(0,0.03,0.0001):
  dataH.append(magnetField(i,1.0))
  dataB.append(magnetInduction(i,1.0))
  x_range.append(i)

print("J=%.7f \t\tK=%.7f \nB_r2-=%.7f \t\tB_r2+=%.7f \nH_r2-=%.7f \t\tH_r2+=%.7f \nL=%.10f"%
  (calJ(1,0.015),calK(1,0.03),magnetInduction(0.019999,1),magnetInduction(0.020001,1),magnetField(0.019999,1),magnetField(0.020001,1),inductionCable(1.0,0.015,0.02,0.03)))

#############################
plot.figure(1)
plot.plot(x_range,dataH)
plot.xlabel('r(m)')
plot.ylabel('H,A/m')
plot.title('H X r')
#############################
plot.figure(2)
plot.plot(x_range,dataB)
plot.ylabel('B,(T)')
plot.xlabel('r(m)')
plot.title('B(T) X r')
plot.show()