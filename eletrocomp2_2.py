import math
import matplotlib.pyplot as plot
import numpy

mi_0 = 4*math.pi*pow(10,-7)

b_res = []

x_dim = [
  0.008,
  0.002,
  0.004,
  0.002,
  0.009,
  0.005,
  0.003,
  0.002,
  0.001,
  0.002,
  0.003,
  0.002,
  0.001,
  0.006,
  0.003,
  0.003
]

b_magnet = [
  0.000000,
  0.112250,
  0.119417,
  0.151970,
  0.177037,
  0.237350,
  0.259793,
  0.312057,
  0.332577,
  0.354493,
  0.391510
]

h_magnet = [
  0.000000,
  9979.612441,
  10822.945775,
  21699.612441,
  36726.279108,
  78449.612441,
  94301.612441,
  131847.945775,
  146865.612441,
  162718.279108,
  191082.325775
]

h_magnet_m = [
  -0.000000,
  -9979.612441,
  -10822.945775,
  -21699.612441,
  -36726.279108,
  -78449.612441,
  -94301.612441,
  -131847.945775,
  -146865.612441,
  -162718.279108,
  -191082.325775
]

def areaSe(dimension):
  answer = math.pi*2*(dimension[0]+dimension[11]+dimension[7]+dimension[8])*(dimension[5]*dimension[10])
  # print(answer)
  return answer

def areaSi(dimension):
  answer = math.pi*dimension[13]**2
  # print(answer)
  return answer

def ratio(dimension):
  answer = -mi_0*(areaSe(dimension)/areaSi(dimension))*(dimension[14]/dimension[8])
  print(answer)
  return answer

def bMagnetResponse(h,dimension):
  b = -math.pi*ratio(dimension)*h
  return b

# for i in h_magnet:
#   b_res.append(bMagnetResponse(i,x_dim))

# print(b_res)
# areaSe(x_dim)
# areaSi(x_dim)
# ratio(x_dim)

# print(b_magnet)
# print(b_res)
# plot.figure(1)
# plot.plot(h_magnet,b_res,'-',h_magnet,b_magnet,'--')
# plot.xlabel('H,A/m')
# plot.ylabel('B,T')
# # plot.title('H X r')
# b_magnet.reverse()
# plot.figure(2)
# plot.plot(h_magnet_m,b_res,'-',h_magnet_m,b_magnet,'--')
# plot.xlabel('H,A/m')
# plot.ylabel('B,T')
# # plot.title('H X r')
# plot.show()

# print(185081*mi_0)
print(185081*x_dim[14]/x_dim[8])
print(555243*mi_0)