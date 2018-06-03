from math import fabs


class MetodoDeNewton(object):
    def __init__(self, f, f_derivada, x0, precisao=0.001, max_interacoes=15):
        self.__X = [x0]
        self.__interacoes = 0
        
        while(self.interacoes < max_interacoes):        
            self.__X.append(self.X[-1] - f(self.X[-1]) / f_derivada(self.X[-1]))
            
            self.__interacoes += 1
            
            if fabs(self.X[-2] - self.X[-1]) <= precisao:
                break
    
    @property
    def X(self):
        return self.__X
    
    @property
    def x(self):
        return self.__X[-1]
    
    @property
    def interacoes(self):
        return self.__interacoes
