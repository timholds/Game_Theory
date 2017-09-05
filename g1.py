
class ConsumerTransaction():
    def __init__(self, price = None):
        selling_price = price

    @property
    def selling_price(self):
        return self.selling_price

    @selling_price.setter
    def selling_price(self, price)
        self.selling_price

class WholsaleTransaction():
    def __init__(self, price = None):
        wholesale_price = price

    @property
    def wholesale_price(self):
        return self.wholesale_price_price

    @selling_price.setter
    def selling_price(self, price)
        self.wholesale_price



class Retailer():
    def __init__(self, profitOrgFT = None, profitOrgConv = None, profitRegFT = None, profitRegConv = None):
        self.profitOrgFT = self.profitOrgFT
        self.profitOrgConv = profitOrgConv
        self.profitRegFT = profitRegFT
        self.profitRegConv =  profitRegConv

    @property
    def profitOrgFT(self):
        return self._profitOrgFT

    @classmethod
    def compute_profitOrgFT(cls, self, price, unitsConsumersDemand, unitsFarmerProduced, wholesalePrice):
        revenue = price * (min(unitsConsumersDemand, unitsFarmerProduced))
        cost = wholesalePrice * unitsFarmerProduced
        profit = revenue - cost

    @profitOrgFT.setter
    def profitOrgFT(self, value):
        self._profitOrgFT = value


    @property
    def profitOrgConv(self):
        return self._profitOrgConv

    @classmethod
    def compute_profitOrgConv(cls, self, price, unitsConsumersDemand, unitsFarmerProduced, wholesalePrice):
        price = price
        revenue = price * (min(unitsConsumersDemand, unitsFarmerProduced))
        cost = wholesalePrice * unitsFarmerProduced
        profit = revenue - cost

    @profitOrgConv.setter
    def profitOrgConv(self, value):
        self._profitOrgConv = value

    @property
    def profitRegFT(self):
        return self._profitRegFT

    @profitRegFT.setter
    def profitRegFT(self, value):
        self._profitRegFT = value

    @property
    def profitRegConv(self):
        return self._profitRegConv

    @profitRegConv.setter
    def profitOrgConv(self, value = None):
        if value = None
            self._profitRegConv = value
        else self._profitOrgConv


    def profitOrgFT(self):
    def profitOrgConv(self):
    def profitRegFT(self):
    def profitRegConv(self):

class Farmer():
    def __init__(self, profitOrgFT = None, profitOrgConv = None, profitRegFT = None, profitRegConv = None):
        profitOrgFT = profitOrgFT
        profitOrgConv = profitOrgConv
        profitRegFT = profitRegFT
        profitRegConv =  profitRegConv

    @property
    def profitOrgFT(self):
        return self._profitOrgFT

    @profitOrgFT.setter
    def profitOrgFT(self, value):
        self._profitOrgFT = value

    @property
    def profitOrgConv(self):
        return self._profitOrgConv

    @profitOrgConv.setter
    def profitOrgConv(self, value):
        self._profitOrgConv = value

    @property
    def profitRegFT(self):
        return self._profitRegFT

    @profitRegFT.setter
    def profitRegFT(self, value):
        self._profitRegFT = value

    @property
    def profitRegConv(self):
        return self._profitRegConv

    @profitRegConv.setter
    def profitOrgConv(self, value):
        self._profitRegConv = value

    def profitOrgFT(self):
    def profitOrgConv(self):
    def profitRegFT(self):
    def profitRegConv(self):

    def costEffortOrg(self):
    def costEffortReg(self, ):


class Customer():
    def utilityOrgFT(self):
    def utilityOrgConv(self):
    def UtilityRegFT(self):
    def UtilityRegConv(self):


# Variables
QuantityProduced = None
QuantityDemanded = None
ConsumerDemandOrganic = None
ConsumerDemandConventional = None
s = None




class CalculateGame():
    #Retailer chooses first
    if (Retailer.profitOrgFT() > Retailer.profitOrgConv()
        retailer chooses 1
        if (Farmer.profitOrgFT Farmer.> )
    else retailer chooses 2


class GUI()

    #Make a slider for the variable consumer demand for organic cotton (QO)

    #Make a slider for the variable consumer demand for conventional cotton (QC)

    # Function that takes in your move

    # Function to determine what to show for the opponents move

    # Function to print out the opponent's move

    # Function to print out the payoffs

    # Graph of how the value of s affects the profits for the farmer and retailer

    # Graph of how consumer demand ffects

    # Graph how consumers utility changes over different s