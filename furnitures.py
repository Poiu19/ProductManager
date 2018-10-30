from manager import *
from apicontroler import ApiControler
#container for Furniture, it loads parametrs from Db
class ProductDetails():
    productId = None
    forceLoad = False
    def setId(self, id):
        self.productId = id

    def loadProduct(self):
        api = ApiControler({'getData': "productEditDetails", 'productId': str(self.productId)})
        for product in api.getResponse():
            if(product['code'] == "KAW01"):
                self.product = KAW01(int(product['color']))
                self.forceLoad = True
            if(product['code'] == "STBR01"):
                self.product = STBR01(int(product['color']))
                self.forceLoad = True

class DrawerPK44(Drawer):
    def __init__(self, group, defaultDimensions, slideLength):
        import globals
        self.__setForms__(group)
        self.setLength(defaultDimensions[0])
        self.setWidth(defaultDimensions[1])
        self.setHeigth(defaultDimensions[2])
        self.setSlide(globals.SLIDE_PK44, slideLength)
        print(group.toString())

#the class of a particular model of furniture, has the task to create
#a particular piece of furniture which will then be modified
#methods of this class should not be invoked from outside
class KAW01(Furniture):
    def __init__(self, color):
        self.__setName__("Stolik kawowy KAW01")
        self.__setDefaultDim__(900, 600, 550)
        self.__setColor__(color)
        self.__addForms__([ ElementLaminatedBoard(900, 600, 18, "Blat górny"), ElementLaminatedBoard(764, 464, 18, "Blat środkowy"),
                            ElementLaminatedBoard(764, 60, 18, "Listwy wzmacniające cz. A"), ElementLaminatedBoard(764, 60, 18, "Listwy wzmacniające cz. A"),
                            ElementLaminatedBoard(428, 60, 18, "Listwy wzmacniające cz. B"), ElementLaminatedBoard(428, 60, 18, "Listwy wzmacniające cz. B"),
                            ElementLaminatedBoard(532, 120, 18, "Nogi cz. A"), ElementLaminatedBoard(532, 120, 18, "Nogi cz. A"), ElementLaminatedBoard(532, 120, 18, "Nogi cz. A"),
                            ElementLaminatedBoard(532, 120, 18, "Nogi cz. A"), ElementLaminatedBoard(532, 102, 18, "Nogi cz. B"), ElementLaminatedBoard(532, 102, 18, "Nogi cz. B"),
                            ElementLaminatedBoard(532, 102, 18, "Nogi cz. B"), ElementLaminatedBoard(532, 102, 18, "Nogi cz. B")])
        self.__groupForms__()
        self.__addMods__()
        self.__addRules__()

    def __groupForms__(self):
        self.groups.append(FormsGroup(self.allForms.forms[0:4])) #dlugosc = dlugosc
        self.groups.append(FormsGroup(self.allForms.forms[0:2])) #szerokosc = szerokosc
        self.groups.append(FormsGroup(self.allForms.forms[4:6])) #szerokosc = dlugosc
        self.groups.append(FormsGroup(self.allForms.forms[6:14])) #wysokosc = dlugosc

    def __addMods__(self):
        self.addMod(self.groups[0], "ltl", 1)
        self.addMod(self.groups[1], "wtw", 1)
        self.addMod(self.groups[2], "wtl", 1)
        self.addMod(self.groups[3], "htl", 1)

    def __addRules__(self):
        import globals
        self.rules.append(Rule(globals.RULE_MIN_LENGTH, 800))
        self.rules.append(Rule(globals.RULE_MAX_LENGTH, 1200))
        self.rules.append(Rule(globals.RULE_MIN_WIDTH, 600))
        self.rules.append(Rule(globals.RULE_MAX_WIDTH, 800))
        self.rules.append(Rule(globals.RULE_MIN_HEIGTH, 450))
        self.rules.append(Rule(globals.RULE_MAX_HEIGTH, 600))

class STBR01(Furniture):
    def __init__(self, color):
        self.__setName__("Stolik - Biurko robocze - STBR01")
        self.__setDefaultDim__(1200, 600, 728)
        self.__setColor__(color)
        self.__addForms__([ ElementLaminatedBoard(1200, 600, 18, "Blat"), ElementMetal(710, 60, 0, "Noga FI-60"), ElementMetal(710, 60, 0, "Noga FI-60"),
                            ElementMetal(710, 60, 0, "Noga FI-60"), ElementMetal(710, 60, 0, "Noga FI-60")])
        self.__groupForms__()
        self.__addMods__()
        self.__addRules__()

    def __groupForms__(self):
        self.groups.append(FormsGroup(self.allForms.forms[0:1])) #dlugosc = dlugosc
        self.groups.append(FormsGroup(self.allForms.forms[0:1])) #szerokosc = szerokosc
        self.groups.append(FormsGroup(self.allForms.forms[1:5])) #wysokosc = dlugosc

    def __addMods__(self):
        self.addMod(self.groups[0], "ltl", 1)
        self.addMod(self.groups[1], "wtw", 1)
        self.addMod(self.groups[2], "htl", 1)

    def __addRules__(self):
        import globals
        self.rules.append(Rule(globals.RULE_MIN_LENGTH, 800))
        self.rules.append(Rule(globals.RULE_MAX_LENGTH, 1350))
        self.rules.append(Rule(globals.RULE_MIN_WIDTH, 600))
        self.rules.append(Rule(globals.RULE_MAX_WIDTH, 1000))
        self.rules.append(Rule(globals.RULE_EXACT_HEIGTH, [728, 838, 1118]))

class STBR02(Furniture):
    def __init__(self, color):
        self.__setName__("Stolik - Biurko robocze - STBR02")
        self.__setDefaultDim__(1200, 600, 838)
        self.__setColor__(color)
        self.__addForms__([ ElementLaminatedBoard(1200, 600, 18, "Blat"), ElementMetal(820, 60, 0, "Noga FI-60"), ElementMetal(820, 60, 0, "Noga FI-60"),
                            ElementMetal(820, 60, 0, "Noga FI-60"), ElementMetal(820, 60, 0, "Noga FI-60"),
                            ElementLaminatedBoard(400, 350, 18, "Bok GŁ. KORP. SZUF"), ElementLaminatedBoard(400, 350, 18, "Bok GŁ. KORP. SZUF"),
                            ElementLaminatedBoard(364, 350, 18, "Tył GŁ. KORP. SZUF"), ElementLaminatedBoard(382, 364, 18, "Spód GŁ. KORP. SZUF"),
                            ElementMDF19(400, 347, 19, "Front"), ElementLaminatedBoard(350, 220, 18, "Bok szuflady"), ElementLaminatedBoard(350, 220, 18, "Bok szuflady"),
                            ElementLaminatedBoard(301, 220, 18, "Przód/tył szuflady"), ElementLaminatedBoard(301, 220, 18, "Przód/tył szuflady"),
                            ElementLaminatedBoard(314, 301, 18, "Spód szuflady")])
        self.__groupForms__()
        self.__addMods__()
        self.__addRules__()
        self.__addExtraElements__()

    def __groupForms__(self):
        self.groups.append(FormsGroup(self.allForms.forms[0:1])) #dlugosc = dlugosc
        self.groups.append(FormsGroup(self.allForms.forms[0:1])) #szerokosc = szerokosc
        self.groups.append(FormsGroup(self.allForms.forms[1:5])) #wysokosc = dlugosc
        self.groups.append(FormsGroup(self.allForms.forms[5:15])) #drawer

    def __addMods__(self):
        self.addMod(self.groups[0], "ltl", 1)
        self.addMod(self.groups[1], "wtw", 1)
        self.addMod(self.groups[2], "htl", 1)

    def __addRules__(self):
        import globals
        self.rules.append(Rule(globals.RULE_MIN_LENGTH, 800))
        self.rules.append(Rule(globals.RULE_MAX_LENGTH, 1350))
        self.rules.append(Rule(globals.RULE_MIN_WIDTH, 600))
        self.rules.append(Rule(globals.RULE_MAX_WIDTH, 1000))
        self.rules.append(Rule(globals.RULE_EXACT_HEIGTH, [838, 1118]))

    def __addExtraElements__(self):
        self.extraElements.append(DrawerPK44(self.groups[3], [350, 400, 400], 500))
        self.extraElements[-1].changeSlideLength(340)