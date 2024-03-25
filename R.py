import element_class

class R (element_class.SuperClass):
    def __init__(self, elem, step):
        super().__init__(elem, step)
        self.impedance = elem['Impedance']