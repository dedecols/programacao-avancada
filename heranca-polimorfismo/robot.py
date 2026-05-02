# Classe pai ou superclasse: Robot (robot.py)
# Classe filho ou subclasse: NurseRobot (nurse_robot.py)

class Robot:

    def __init__(self, nome, ano_fabr):
        self._nome = nome
        self._ano_fabricacao = ano_fabr
    
    def falar_oi(self):
        print("Oi, sou {} de {}".format(self._nome, self._ano_fabricacao))
