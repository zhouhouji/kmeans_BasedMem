
import memristorCell as mc
import const

const.INITIAL = 0    ##initial state
const.READ  = 1      ##read state
const.WRITE = 2      ##write state



if __name__ == '__main__':
    popt = mc.funcConducdence()
    conductenceList = []
    Conductance, pulse_after = mc.memristorCell(const.WRITE,0,1,0.5,popt)
    print(Conductance)
    pass