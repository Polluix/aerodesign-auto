from src.constants import propselector
from src.functions.velocity import changeVelocity, setZero, addOne
from src.functions.thrust import changeThrust
from src.constants import *
from src.functions.readImg import readImg
from src.functions.writeData import writeData

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

file.write('# Air Speed [m/s]         RPM      Thrust [N]      Power Output [W]    Power Absorbed [W]      Efficiency [%]\n')
file.close()

for i in range(20):
    if i!=1 and i!=3:
        writeData(result, filename)
        addOne()
        result = readImg()
    else:
        addOne()
        
propselector.close()