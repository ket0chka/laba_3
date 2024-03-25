import element_class

class C(element_class.SuperClass):
    def __init__(self, elem, step):
        super().__init__(elem, step)
        self.impedance = (step / ( elem['Capacity'])) 
        self.volt = elem['Volt']

    def set_volt(self):
        self.volt = self.current * self.impedance + self.volt

    def get_volt(self,t):
        return self.volt

    def set_current(self):
        self.current = (-self.volt + (self.fi_start - self.fi_end)) / self.impedance

    def get_volt_for_graph(self):
        return self.volt

    def get_current_for_graph(self):
        return self.current