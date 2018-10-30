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

    def getMaterialType(self):
        import globals
        return globals.MATERIAL_NONE

    def toString(self):
        import globals
        return self.getName() + " - L: " + str(self.getLength()) + ", W: " + str(self.getWidth()) + ", MAT: " + globals.MATERIAL_NAME[self.getMaterialType()];

class ElementLaminatedBoard(Form):
    def getMaterialType(self):
        import globals
        return globals.MATERIAL_PLATE

class ElementMetal(Form):
    def getMaterialType(self):
        import globals
        return globals.MATERIAL_METAL

class ElementMDF19(Form):
    def getMaterialType(self):
        import globals
        return globals.MATERIAL_MDF19

#this class is responsible for the group of Form() to change their parameters in the same way
class FormsGroup():
    forms = []
    def __init__(self, forms):
        self.forms = forms

    def toString(self):
        group = "";
        for form in self.forms:
            group = group + form.toString() + "\n"
        return group

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
    extraElements = []
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
                ruleResult = self.checkRules(globals.RULE_EXACT_HEIGTH, newHeigth)
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
            if rule.isCorrectRule(ruleType) == True:
                ruleResult = rule.execRule(value)
                if(ruleResult != True):
                    break
            #ruleResult = rule.execIfCorrectRule(ruleType, value)
            #if(ruleResult != True):
                #break
        return ruleResult
    def toString(self):
        import globals
        output = (self.getName() + " - " + str(self.getColor()) + "\n")
        for form in self.allForms.forms:
            output = output + form.toString() + "\n"
        return output
    def destroy(self):
        self.rules.clear()
        self.mods.clear()
        self.allForms.forms.clear()
        self.extraElements.clear()
        self.groups.clear()
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
                            self.__exactValues__, #exactHeigth [6]
                            ]

    def isCorrectRule(self, ruleType):
        if (self.type == ruleType):
            return True
        return False

    def execRule(self, value):
        return self.execution[self.type](value)

    #TO REMOVE; holding in case of unexpected errors after refactoring
    #def execIfCorrectRule(self, ruleType, value):
        #if self.isCorrectRule(ruleType) == True:
            #return self.execRule(value)
        #return True

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

    def __exactValues__(self, newValue):
        for value in self.value:
            if(value == newValue):
                return True
        import globals
        return globals.ERROR_RULE[self.type] + ": " + str(self.value) + " [mm]"

class ExtraElements():
    def __setForms__(self, group):
        self.allForms = group

class Drawer(ExtraElements):
    __length__ = 0
    __width__ = 0
    __heigth__ = 0
    def setLength(self, length):
        self.__length__ = length

    def setWidth(self, width):
        self.__width__ = width

    def setHeigth(self, heigth):
        self.__heigth__ = heigth

    def setSlide(self, slideType, length):
        self.slide = slideType
        import globals
        correctValue = False
        self.acceptAbleSlideValues = []
        if slideType == globals.SLIDE_PK44:
            self.acceptAbleSlideValues = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
        elif slideType == globals.SLIDE_PK05:
            self.acceptAbleSlideValues = [250, 300, 350, 400, 450, 500, 550, 600]
        elif slideType == globals.SLIDE_PK06:
            self.acceptAbleSlideValues = [300, 350, 400, 450, 500, 550]
        for value in self.acceptAbleSlideValues:
            if(value == length):
                correctValue = True
        if(correctValue == False):
            return correctValue
        self.slideLength = length
        return True

    def changeSlideLength(self, newLength):
        if (self.setSlide(self.slide, newLength) == False):
            print("Błędna długość prowadnicy, akceptowalne wartosci: ", self.acceptAbleSlideValues)

"""
TODO:
    ADD SPECIFIC CLASS FOR FURNITURE THAT HAVE SPECIAL STUFF (EXAMPLE: DRAWER)
"""
