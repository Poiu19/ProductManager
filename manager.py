#Structure responsible for the physical element of the furniture, 1 specific dimension, form
class Form():
    def __init__(self, length, width, thick, name=None):
        self.setLength(length)
        self.setWidth(width)
        self.setThick(thick)
        self.setName(name)

    def setName(self, name):
        self.__name__ = name

    def setLength(self, length):
        self.__length__ = length

    def setWidth(self, width):
        self.__width__ = width

    def setThick(self, thick):
        self.__thick__ = thick

    def addLength(self, delta):
        self.setLength(self.getLength() + delta)

    def addWidth(self, delta):
        self.setWidth(self.getWidth() + delta)

    def addThick(self, delta):
        self.setThick(self.getThick() + delta)

    def getName(self):
        return self.__name__

    def getLength(self):
        return self.__length__

    def getWidth(self):
        return self.__width__

    def getThick(self):
        return self.__thick__

#this class is responsible for the group of Form() to change their parameters in the same way
class FormsGroup():
    forms = []
    def __init__(self, forms):
        self.forms = forms

#this class is responsible for modyfing forms placed in groups by chosen modification (mod)
class GroupModificator():
    def __init__(self, group, mod, scale):
        self.group = group
        self.setScale(scale)
        self.setMod(mod)
        #########################################################################################
        # ltw = length to width - changing length affects width of form on the selected scale   #
        # ltl = length to length - changing length affects length of form on the selected scale #
        # wtl = width to length - changing width affects length of form on the selected scale   #
        # wtw = width to width - changing width affects width of form on the selected scale     #
        # htl = heigth to length - changing heigth affects length of form on the selected scale #
        # htw = heigth to width - changing heigth affects width of form on the selected scale   #
        #########################################################################################
        if(mod == "ltl" or mod == "wtl" or mod == "htl"):
            self.modExec = self.lengthMod
        elif(mod == "ltw" or mod == "wtw" or mod == "htw"):
            self.modExec = self.widthMod
    def setMod(self, mod):
        self.__mod__ = mod

    def getMod(self):
        return self.__mod__

    def setScale(self, scale):
        self.__scale__ = scale

    def getScale(self):
        return self.__scale__

    def lengthMod(self, delta):
        for form in self.group.forms:
            form.addLength(delta*self.getScale())

    def widthMod(self, delta):
        for form in self.group.forms:
            form.addWidth(delta*self.getScale())

#class that supports modifications of the furniture, contains the entire "logic"
class Furniture():
    mods = []
    groups = []
    rules = []
    allForms = None
    __color__ = None
    __name__ = None
    def addMod(self, group, mod, scale):
        self.mods.append(GroupModificator(group, mod, scale))

    def __setDefaultDim__(self, l, w, h):
        self.__setLength__(l)
        self.__setWidth__(w)
        self.__setHeigth__(h)

    def __setHeigth__(self, h):
        self.__heigth__ = h

    def __setWidth__(self, w):
        self.__width__ = w

    def __setLength__(self, l):
        self.__length__ = l

    def __setName__(self, name):
        self.__name__ = name

    def getHeigth(self):
        return self.__heigth__

    def getWidth(self):
        return self.__width__

    def getLength(self):
        return self.__length__

    def getName(self):
        return self.__name__

    def __addForms__(self, formList):
        self.allForms = FormsGroup(formList)

    def changeLength(self, newLength):
        for mod in self.mods:
            if(mod.getMod() == "ltw" or mod.getMod() == "ltl"):
                import globals
                ruleResult = self.checkRules(globals.RULE_MIN_LENGTH, newLength)
                if(ruleResult != True):
                    return ruleResult
                ruleResult = self.checkRules(globals.RULE_MAX_LENGTH, newLength)
                if(ruleResult != True):
                    return ruleResult
                mod.modExec(newLength - self.getLength())
        self.__setLength__(newLength)
        return True

    def changeWidth(self, newWidth):
        for mod in self.mods:
            if(mod.getMod() == "wtl" or mod.getMod() == "wtw"):
                import globals
                ruleResult = self.checkRules(globals.RULE_MIN_WIDTH, newWidth)
                if(ruleResult != True):
                    return ruleResult
                ruleResult = self.checkRules(globals.RULE_MAX_WIDTH, newWidth)
                if(ruleResult != True):
                    return ruleResult
                mod.modExec(newWidth - self.getWidth())
        self.__setWidth__(newWidth)
        return True

    def changeHeigth(self, newHeigth):
        for mod in self.mods:
            if(mod.getMod() == "htl" or mod.getMod() == "htw"):
                import globals
                ruleResult = self.checkRules(globals.RULE_MIN_HEIGTH, newHeigth)
                if(ruleResult != True):
                    return ruleResult
                ruleResult = self.checkRules(globals.RULE_MAX_HEIGTH, newHeigth)
                if(ruleResult != True):
                    return ruleResult
                mod.modExec(newHeigth - self.getHeigth())
        self.__setHeigth__(newHeigth)
        return True

    def __setColor__(self, color):
        self.__color__ = color

    def getColor(self):
        return self.__color__

    def checkRules(self, ruleType, value):
        ruleResult = True
        for rule in self.rules:
            ruleResult = rule.execIfCorrectRule(ruleType, value)
            if(ruleResult != True):
                break
        return ruleResult
    def printFormsDimensions(self):
        print(self.getName() + " - " + str(self.getColor()))
        for form in self.allForms.forms:
            print(form.getName() + " - L: "+ str(form.getLength()) +", W: "+ str(form.getWidth()))

#the class of a particular model of furniture, has the task to create
#a particular piece of furniture which will then be modified
#methods of this class should not be invoked from outside
class KAW01(Furniture):
    def __init__(self, color):
        self.__setName__("Stolik kawowy KAW01")
        self.__setDefaultDim__(900, 600, 550)
        self.__setColor__(color)
        self.__addForms__([ Form(900, 600, 18, "Blat górny"), Form(764, 464, 18, "Blat środkowy"),
                            Form(764, 60, 18, "Listwy wzmacniające cz. A"), Form(764, 60, 18, "Listwy wzmacniające cz. A"),
                            Form(428, 60, 18, "Listwy wzmacniające cz. B"), Form(428, 60, 18, "Listwy wzmacniające cz. B"),
                            Form(532, 120, 18, "Nogi cz. A"), Form(532, 120, 18, "Nogi cz. A"), Form(532, 120, 18, "Nogi cz. A"),
                            Form(532, 120, 18, "Nogi cz. A"), Form(532, 102, 18, "Nogi cz. B"), Form(532, 102, 18, "Nogi cz. B"),
                            Form(532, 102, 18, "Nogi cz. B"), Form(532, 102, 18, "Nogi cz. B")])
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

class Rule():
    execution = []
    #ruleType should be int, in fact it's index of table
    def __init__(self, ruleType, value):
        self.__createExecutionTable__()
        self.type = ruleType
        self.value = value

    def __createExecutionTable__(self):
        self.execution = [  self.__minValue__, #minLength [0]
                            self.__maxValue__, #maxLength [1]
                            self.__minValue__, #minWidth [2]
                            self.__maxValue__, #maxWidth [3]
                            self.__minValue__, #minHeigth [4]
                            self.__maxValue__, #maxHeigth [5]
                            ]

    def execIfCorrectRule(self, ruleType, value):
        if self.type == ruleType:
            return self.execution[self.type](value)
        return True

    def __minValue__(self, newValue):
        if(newValue < self.value):
            import globals
            return globals.ERROR_RULE[self.type] + ": " + str(self.value) + " [mm]"
        return True

    def __maxValue__(self, newValue):
        if(newValue > self.value):
            import globals
            return globals.ERROR_RULE[self.type] + ": " + str(self.value) + " [mm]"
        return True
