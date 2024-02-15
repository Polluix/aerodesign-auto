import pygetwindow as gw
from src.constants import propselector, width, height, topleft_x, topleft_y
from functions.velocity import changeVelocity, setZero
from functions.thrust import changeThrust


propselector.activate()

setZero()
changeVelocity()
changeThrust()



# propselector.close()