from src.constants import propselector
from functions.velocity import changeVelocity, setZero
from functions.thrust import changeThrust
from src.constants import *
from functions.readImg import readImg
from functions.writeData import writeData

propselector.activate()

setZero()
changeVelocity()
changeThrust()

result = readImg()
filename = 'data.txt'

try:
    file = open(f'./{filename}', 'a+')
except:
    raise FileNotFoundError

file.write('# Air Speed [m/s]         RPM      Thrust [N]      Power Output [W]    Power Absorbed [W]      Efficiency [%]      Prop Thrust Coeff   A/C Thrust Coeff    Tip Mach Number     075R Pitch Angle [deg]\n')
file.close()

# TODO: change air speed value and get data again 30 times.
for i in range(30):
    writeData(result, filename)


# propselector.close()