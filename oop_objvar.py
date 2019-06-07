class Robot:
    """表示一个带有名字地机器人"""
    population = 0
    def __init__(self,name):
        self.__name = name
        Robot.population+=1
        print('(Initializing {})'.format(self.__name))

    def die(self):
        """我挂了。"""

        print('{} is being destroied!'.format(self.__name))
        Robot.population-=1
        if Robot.population == 0:
            print('{} is the last one'.format(self.__name))
        else:
            print('There are still {} Robots!'.format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候
        没问题，你做得到。"""
        print('Greetings, my masters call me {}.'.format(self.__name))

    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print('We have {} robots!'.format(cls.population))


droid1=Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2=Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

droid1.die()
droid2.die()

Robot.how_many()
print(Robot.__doc__,Robot.say_hi.__doc__)


