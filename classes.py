class innerGasPipeline:
    """docstring for innerGasPipeline"""
    def __init__(self, diameter=None, lenght=None):
        self.diameter = diameter
        self.lenght = lenght

class outerGasPipeline:
    """docstring for outerGasPipeline"""
    def __init__(self, polyDiameter=None, steelDiameter=None, lenght=None):
        self.polyDiameter = polyDiameter
        self.steelDiameter = steelDiameter 
        self.lenght = lenght
                        
class middlePressurePipeline:
    """docstring for middlePressurePipeline"""
    def __init__(self):
       self.distributivePipeline = outerGasPipeline()
       self.entryPipeline = outerGasPipeline()

class lowPressurePipeline(middlePressurePipeline):
    """docstring for lowPressurePipeline"""
    def __init__(self):
        super().__init__()
        self.buildingPipeline = innerGasPipeline()
        
class GasPipeline:
    """docstring for GasPipeline"""
    def __init__(self):
        self.highMiddlePressure = middlePressurePipeline()
        self.lowPressure = lowPressurePipeline()
        
class MagicFeature:
    """Универсальный класс, на основе которого буду
    создавать объекты с 2-мя атрибутами"""
    def __init__(self, mF1=None, mF2=None):
        self.mF1 = mF1
        self.mF2 = mF2
        
class GasReducer:
    """docstring for GasReducer"""
    def __init__(self):
        #mF1-name, mF2-amount
        self.gasControlPoint = MagicFeature()
        #mF1-name, mF2-amount
        self.pressureRegulator = MagicFeature()
        
class GasCorrector(MagicFeature):
    """docstring for GasCorrector"""
    #mF1-name, mF2-amount
    def __init__(self, mF1, mF2):
        super().__init__(mF1, mF2)
        
class GasCounter(MagicFeature):
    """docstring for GasCounter"""
    #model-model of gas counter, mF1-name, mF2-amount
    def __init__(self, model=None, mF1, mF2):
        super().__init__(mF1, mF2)
        self.model = model
        
class GasEquipment(MagicFeature):
    """docstring for GasEquipment"""
    #info-name&amount, mF1-power, mF2-gas consumption
    def __init__(self, info=None, mF1, mF2):
        super().__init__(mF1, mF2)
        self.info = info

class ContractDate(MagicFeature):
    """docstring for ContractDate"""
    #mF1-name of contract, mF2-date of action
    def __init__(self, mF1, mF2):
        super().__init__(mF1, mF2)
       
class PayDate(MagicFeature):
    """docstring for PayDate"""
    #mF1-bill for pay, mF2-date of action
    def __init__(self, mF1, mF2):
        super().__init__(mF1, mF2)

class Zayavka:
    """docstring for Zayavka"""
    def __init__(self):
        self.date = None                    #
        self.address = None                 #
        self.region = None                  #
        self.client = None                  #
        self.buildOrganization = None       #
        self.techCondition = None           #
        self.projectDate = None             #
        self.projectOrganization = None     #
        self.aim = None                     #
        self.pipeline = GasPipeline()       #
        self.reducer = GasReducer()         #
        self.equipment = GasEquipment()     #
        self.counter = GasCounter()         #
        self.corrector = GasCorrector()     #

class ItemFromMagazin(Zayavka):
    """docstring for ItemFromMagazin"""
    def __init__(self):
        super().__init__()
        self.number = None
        self.city = None
        self.street = None
        self.build = None
        self.flat = None
        self.contract = ContractDate() 
        self.pay = PayDate() 
        self.acceptDate = None 
        self.transferDate = None 
        self.engineer = None
        