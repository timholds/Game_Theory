

class GameScript():
    def __init__(self):
        self.retail_price = None
        self.wholesale_price = None
        self.quantity_demanded = None
        self.quantity_produced = None
        self.cost_of_effort = None

        self.retail_price_org_FT = None
        self.retail_price_org_conv = None
        self.retail_price_reg_FT = None
        self.retail_price_reg_conv = None

        self.wholesale_price_FT = None
        self.wholesale_price_org_conv = None
        self.wholesale_price_reg_conv = None

        self.quantity_produced_org = None
        self.quantity_produced_reg_FT = None
        self.quantity_produced_reg_conv = None

        self.quantity_demanded_org_FT = None
        self.quantity_demanded_org_conv = None
        self.quantity_demanded_reg_FT = None
        self.quantity_demanded_reg_conv = None

        self.cost_of_effort_org = None
        self.cost_of_effort_reg = None

    def input_cases(self, trade="Conv", material="Reg"):
        if (trade == "FT"):
            self.wholesale_price = self.wholesale_price_FT
            if (material == "Org"):
                self.retail_price = self.retail_price_org_FT
                self.quantity_produced = self.quantity_produced_org
                self.quantity_demanded = self.quantity_demanded_org_FT
                self.cost_of_effort = self.cost_of_effort_org
            else if (material == "Reg"):
                self.retail_price = self.retail_price_reg_FT
                self.quantity_produced = self.quantity_produced_reg_FT
                self.quantity_demanded = self.quantity_demanded_reg_FT
                self.cost_of_effort = self.cost_of_effort_reg

        else if (trade == "Conv"):
            if (material == "Org"):
                self.retail_price = self.retail_price_org_conv
                self.wholesale_price = self.wholesale_price_org_conv
                self.quantity_produced = self.quantity_produced_org
                self.quantity_demanded = self.quantity_demanded_org_conv
                self.cost_of_effort = self.cost_of_effort_org
            else if (material == "Reg"):
                self.retail_price = self.retail_price_reg_conv
                self.wholesale_price = self.wholesale_price_reg_conv
                self.quantity_produced = self.quantity_produced_reg_conv
                self.quantity_demanded = self.quantity_demanded_reg_conv
                self.cost_of_effort = self.cost_of_effort_reg

        farmer_profit = (self.wholesale_price * self.quantity_produced) - self.cost_of_effort
        retailer_profit = (self.retail_price * min(self.quantity_produced, self.quantity_demanded)) - (self.wholesale_price * self.quantity_produced)



class Transaction():
    def __init__(self, price = None):
        selling_price_org_ft = price
        selling_price_org_conv = price
        selling_price_reg_ft = price
        selling_price_reg_conv = price
        # Wholesale_org_ft === wholesale_reg_ft
        wholesale_org_ft = price
        wholesale_org_conv = price
        wholesale_reg_conv = price

    @property
    def selling_price_org_ft(self):
        return self.selling_price_org_ft

    @selling_price_org_ft.setter
    def selling_price_org_ft(self, price)
        self.selling_price_org_ft = price
    @property
    def selling_price_org_conv(self):
        return self.selling_price_org_conv

    @selling_price.setter
    def selling_price_org_conv(self, price)
        self.selling_price_org_conv = price

    @property
    def selling_price_reg_ft(self):
        return self.selling_price_reg_ft

    @selling_price_reg_ft.setter
    def selling_price_reg_ft(self, price)
        self.selling_price_reg_ft = price

    @property
    def selling_price_reg_conv(self):
        return self.selling_price_reg_conv

    @selling_price_reg_conv.setter
    def selling_price_reg_conv(self, price)
        self.selling_price_reg_conv = price

    @property
    def wholesale_org_ft(self):
        return self.wholesale_org_ft

    @wholesale_org_ft.setter
    def wholesale_org_ft(self, price)
        self.wholesale_org_ft = price

    @property
    def wholesale_org_conv(self):
        return self.wholesale_org_conv

    @wholesale_org_conv.setter
    def wholesale_org_conv(self, price)
        self.wholesale_org_conv = price

    @property
    def wholesale_reg_conv(self):
        return self.wholesale_reg_conv

    @wholesale_reg_conv.setter
    def wholesale_reg_conv(self, price)
        self.wholesale_reg_conv = price

    cost_of_effort = Farmer.costEffort(Org)


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

    def profit(self, type):
        if type == OrgFT
        else if type == OrgConv
        else if type == RegFT
        else if type == RegConv

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

If you the retailer choose FT, let farmer choose wholeSale price
If you choose Conv, the market chooses wholeSale price (set the market with a slider to see what happens as market changes)
Visualize with a graph of how profit changes as the wholesale price changes

Farmer chooses cost of effort