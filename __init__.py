from src.constants import propselector
from functions.velocity import changeVelocity, setZero
from functions.thrust import changeThrust
from src.constants import *
from functions.readImg import readImg

propselector.activate()

setZero()
changeVelocity()
changeThrust()

result = readImg()

n = len(result)
for i in range(n):
    print(result[i][1], i)

# propselector.close()