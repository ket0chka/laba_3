import element_class

class EDS (element_class.SuperClass):
    def __init__(self, elem, step):
        super().__init__(elem, step)
        self.impedance = elem['Impedance']
        self.volt = elem['Volt']

    def set_current(self):
        self.current = (self.volt - (self.fi_start - self.fi_end)) / self.impedance