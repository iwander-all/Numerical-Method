import numpy as np

v = np.zeros(20) 

T1 = 20.
Cv = 0.718
Power = 80. * 35 / 1000
Q = Power * 15 * 60

Vroom = 240.
Vperson = 0.075 * 35
Vair = Vroom - Vperson

Pressure = 101.325
R = 8.314
Mwt = 28.97

T2 = T1 / (1 - R*Q/(Cv*Pressure*Vair*Mwt))
print(T2)


