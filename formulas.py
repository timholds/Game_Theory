farmer_profit = (wholesale_price * quantity_produced) - cost_of_effort
# set cost_of_effort = 0 in non-organic case
# set quantity_produced = quantity_produced_org in organic case

retail_price (4 cases)
wholesale_price (3 cases)
quantity_demanded (4 cases)
quantity_produced (3 cases - organic (based on e farmer chooses), regFT, regConv (based on market?))
cost_of_effort (2 cases org and not)

quantity_produced = None
# In organic case, set quantity_produced = quantity_produced_org
quantity_demanded = None

retailer_profit = (retail_price * min(quantity_produced, quantity_demanded)) - (wholesale_price * quantity_produced)

quantity_produced_org = a - b((1-effort)**2)

cost_of_effort_reg = 0
# Do we need to define an actual value for c?
#c = .5
cost_of_switching_to_org = c * (effort**2)
cost_of_effort_org = cost_of_effort_reg + cost_of_switching_to_org

self.assertTrue(0 <= cost_of_effort <= 1)
self.assertTrue(0 <= consumer_surplus_organic <= 1)
self.assertTrue(1 <= consumer_surplus_organic_FT <= 2)


