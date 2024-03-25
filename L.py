import element_class

class L(element_class.SuperClass):
    def __init__(self, elem, step):
        super().__init__(elem, step)
        self.impedance = 2 * elem['Inductance'] / step
        self.current = elem["Current"]
        self.E = 0


    def set_volt(self):
        self.E = (self.impedance * self.current + self.volt)

    def get_volt(self,t):
        return self.E


    def set_current(self):
        self.current = (self.E - (self.fi_start - self.fi_end)) / self.impedance
        self.volt = (self.current * self.impedance - self.E)

    def get_volt_for_graph(self):
        return self.volt
    
    def get_current_for_graph(self):
        return self.current