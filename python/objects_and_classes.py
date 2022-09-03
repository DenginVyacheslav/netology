class Pets:
    name = ''
    species = ''
    weight = 0
    say =''

    def animal_say(self):
        print(self.say)

    def feeding(self, food):
        self.weight += food

class GiveMilk(Pets):
    milk = 0

    def feeding(self, food):
        self.weight += food
        self.milk += food / 7

    def milking_animal(self, milking):
        self.milk -= milking
        self.weight -= milking

class GiveWool(Pets):
    wool = 0

    def feeding(self, food):
        self.weight += food
        self.wool += food / 7

    def haircut_animal(self, haircut):
        self.wool -= haircut
        self.weight -= haircut

class GiveEggs(Pets):
    eggs = 0

    def feeding(self, food):
        self.weight += food
        self.eggs += food / 7

    def collection(self, egg):
        self.eggs -= egg
        self.weight -= egg

seryy = GiveEggs()
seryy.name = 'серый'
seryy.species = 'гусь'
seryy.weight = 7
seryy.say = 'га-га-га'
seryy.eggs = 3

belyy = GiveEggs()
belyy.name = 'белый'
belyy.species = 'гусь'
belyy.weight = 5
belyy.say = 'га-га-га'
belyy.eggs = 2

manka = GiveMilk()
manka.name = 'манька'
manka.species = 'корова'
manka.weight = 700
manka.say = 'му-му'
manka.milk = 20

barashek = GiveWool()
barashek.name = 'барашек'
barashek.species = 'овца'
barashek.weight = 50
barashek.say = 'бе-бе'
barashek.wool = 3

kudryavyy = GiveWool()
kudryavyy.name = 'кудрявый'
kudryavyy.species = 'овца'
kudryavyy.weight = 60
kudryavyy.say = 'бе-бе'
kudryavyy.wool = 5

koko = GiveEggs()
koko.name = 'ко-ко'
koko.species = 'курица'
koko.weight = 3
koko.say = 'ко-ко-ко'
koko.eggs = 4

kukareku = GiveEggs()
kukareku.name = 'кукареку'
kukareku.species = 'курица'
kukareku.weight = 4
kukareku.say = 'ко-ко-ко'
kukareku.eggs = 5

roga = GiveMilk()
roga.name = 'рога'
roga.species = 'коза'
roga.weight = 40
roga.say = 'ме-ме'
roga.milk = 2

kopyta = GiveMilk()
kopyta.name = 'копыта'
kopyta.species = 'коза'
kopyta.weight = 50
kopyta.say = 'ме-ме'
kopyta.milk = 3

kryakva = GiveEggs()
kryakva.name = 'кряква'
kryakva.species = 'утка'
kryakva.weight = 3
kryakva.say = 'кря-кря'
kryakva.eggs = 2

animals =[seryy, belyy, manka, barashek, kudryavyy, koko, kukareku, roga, kopyta, kryakva]

for animal in animals:
    animal.feeding(7)
    print(animal.species + ", кличка - " + animal.name + ", вес - " + str(animal.weight) + "кг")

print('\n===================================\n')

milk = [manka, roga, kopyta]
aggs = [seryy, belyy, koko, kukareku, kryakva]
wool = [barashek, kudryavyy]

for milking in milk:
    milking.milking_animal(2)
    print(milking.species + ", кличка - " + milking.name + ", вес - " + str(milking.weight) + "кг" +
          ", молоко - " + str(int(milking.milk)))

for agg in aggs:
    agg.collection(2)
    print(agg.species + ", кличка - " + agg.name + ", вес - " + str(agg.weight) + "кг" +
          ", яйца - " + str(int(agg.eggs)))

for haircut in wool:
    haircut.haircut_animal(2)
    print(haircut.species + ", кличка - " + haircut.name + ", вес - " + str(haircut.weight) + "кг" +
          ", шерсть - " + str(int(haircut.wool)))

print('\n===================================\n')

animal_weight = {seryy.name:seryy.weight, belyy.name:belyy.weight, manka.name:manka.weight,
                 barashek.name:barashek.weight, kudryavyy.name:kudryavyy.weight,
                 koko.name:koko.weight, kukareku.name:kukareku.weight, roga.name:roga.weight,
                 kopyta.name:kopyta.weight, kryakva.name:kryakva.weight}
total_weight = 0
for key, value in animal_weight.items():
    total_weight += value
    if max(animal_weight.values()) == value:
        print("Имя самого тяжёлого животного - " + key)

print("Общий вес животных - " + str(total_weight) + "кг")