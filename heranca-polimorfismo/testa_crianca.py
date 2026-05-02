# Executar no terminal: python testa_crianca.py
# Verificar diretório com comando pwd
# Mudar para o diretório certo: cd heranca-polimorfismo
# Executar no terminal: python testa_crianca.py

from robot import Robot
from nurse_robot import NurseRobot
from crianca import Crianca

z = Robot("Torg", 2008)
enf = NurseRobot("Florence", 2019)
c = Crianca("Joãozinho")

c.brincar(z)
c.brincar(enf)
