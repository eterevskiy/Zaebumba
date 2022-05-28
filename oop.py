# Реалізувати клас Герой що має мати наступні атрибути: ім‘я, здоров‘я, ранг, сила і метод вдарити.
#  Метод вдарити повинен наносити шкоду противнику в розмірі сили героя. 
#  Герой має мати наступні обмеження: здоров‘я від 0 до 100, ранг 1,2,3. Сила не більше 10% теперішнього здоров‘я героя. 
#  Не можна бити героїв здоров‘я яких менше 5.


# Реалізувати клас маг, який може відновлювати здоров'я інших героїв, також він має ранг як герой і може наносити удари.
#  За відновлення здоров'я він бере гроші. ( Вам потрібно реалізувати цей функціонал ). Герой заробляє гроші за перемогу у 
#  бою з іншим героєм, також при перемозі він забирає всі гроші суперника. Скільки герой отримує грошей за перемогу і 
#  скільки коштує відновити здоров'я, на ваш розсуд)

from unicodedata import name


class Hero :
    def __init__(self,name) :
        self.name=name
        self.__health=100
        self.__rang=1
        self.__strong=self.__health/100 *10
        self.__money=100

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self,value):
        self.__health=value
        self.__strong=self.__health/100 *10


    def hit(self,player):
        if player.health < 5 :
            print(f'{self.name},ne ne idi nahui')
        player.health+=-self.__strong

    def info(self):
        print(f'{self.name}  {self.__health} {self.__strong}')


p1=Hero("Nazarenko")
p2=Hero('Strela')

p1.hit(p2)
p1.info()
p2.info()
