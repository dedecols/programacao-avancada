# Classe pai ou superclasse: Robot (robot.py)
# Classe filho ou subclasse: NurseRobot (nurse_robot.py)
from robot import Robot
import time

class NurseRobot(Robot):

    def __init__(self, nome, ano_fabr, num_cre = 123456):
        super().__init__(nome, ano_fabr)
        self._num_cre = num_cre

    def falar_oi(self):
        super().falar_oi()
        print("Sou especialista em Enfermagem!")
        print("Meu CRE é: ", self._num_cre)

    def recarregar(self, outro_robo):
        print(self._nome, "recarregando ", outro_robo._nome)
        for x in range(5):
            print(".", end = " ")
            time.sleep(1)
        print("CARGA COMPLETA!")






# # Classe filha sem sobrescrita ou extensão 
# class NurseRobot(Robot):
#     pass

# # As instâncias da classe filha herdam os atributos e métodos da classe pai
# enf = NurseRobot("Florence", 2019)
# enf.falar_oi()

# # # Herdam até mesmo atributos protegidos
# # enf._nome
# # enf._ano_fabricacao

# # # Método informa os atributos de instância no formato de dicionário
# # enf.__dict__


# #### SOBRESCRITA ####
# class NurseRobot(Robot):

#     # Sobrescrita
#     def falar_oi(self):
#         super().falar_oi() 
#         # Robot.falar_oi(self)
#         print("Sou especialista em Enfermagem!")

# enf = NurseRobot("Florence", 2019)
# enf.falar_oi()


# #### ESTENDER - Exemplo 1 ####
# class NurseRobot(Robot):

#     # Sobrescrita
#     def falar_oi(self):
#         super().falar_oi() 
#         # Robot.falar_oi(self)
#         print("Sou especialista em Enfermagem!")

#     # Estender 
#     def recarregar(self, outro_robo):
#         print(self._nome, "recarregando ", outro_robo._nome)
#         for x in range(5):
#             print(".", end = " ")
#             time.sleep(1)
#         print("CARGA COMPLETA!")

# z = Robot("Torg", 2008)
# enf = NurseRobot("Florence", 2019)

# enf.recarregar(outro_robo=z)


# #### ESTENDER - Exemplo 2 ####
# class NurseRobot(Robot):

#     def __init__(self, nome, ano_fabr, num_cre = 123456):
#         super().__init__(nome, ano_fabr)
#         self._num_cre = num_cre

#     def falar_oi(self):
#         super().falar_oi()
#         print("Sou especialista em Enfermagem!")
#         print("Meu CRE é: ", self._num_cre)

#     def recarregar(self, outro_robo):
#         print(self._nome, "recarregando ", outro_robo._nome)
#         for x in range(5):
#             print(".", end = " ")
#             time.sleep(1)
#         print("CARGA COMPLETA!")

# # enf = NurseRobot("Florence", 2019, 123456)
# enf = NurseRobot("Florence", 2019)
# enf.falar_oi()

# # enf.__dict__


