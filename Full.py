import R
import C
import L
import EDS

class Full():

    def serialize(elem, step):

        if elem['type'] == 'R':
            return Full.R(elem, step)

        if elem['type'] == 'E':
            return Full.EDS(elem, step)

        if elem['type'] == 'C':
            return Full.C(elem, step)

        if elem['type'] == 'L':
            return Full.L(elem, step)
        (elem, step)

    def R(elem, step):
        return R.R(elem, step)

    def EDS(elem, step):
        return EDS.EDS(elem, step)

    def C(elem, step):
        return C.C(elem, step)

    def L(elem, step):
        return L.L(elem, step)