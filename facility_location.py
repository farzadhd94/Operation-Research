#Facility Location problem

import pandas as pd

# Reading excel sheets and turn into lists

basic_info = pd.read_excel('IP_dataset.xlsx','Basic information')
Cities = range(len(basic_info['city']))
Markets = range(len(basic_info['market']))

city_info = pd.read_excel('IP_dataset.xlsx','City\'s information')
operating_costs = city_info['Operating cost']
Capacities = city_info['Capacity']

market_info = pd.read_excel('IP_dataset.xlsx','Market\'s information')
demands = market_info['Demand']

shipping_info = pd.read_excel('IP_dataset.xlsx','Shipping cost', index_col=0)
shipping_costs = []

for i in shipping_info.index:
    shipping_costs.append(list(shipping_info.loc[i]))

#################
# building a model

facility_location = Model('facility_location')

# adding a list as variables
x=[]
for j in cities:
    x.append(facility_location.addVar(1b = 0, vtype = GRB.BINARY, name = 'x' + str(j+1)))
y=[]
for i in markets:
    y.append(facility_location.addVar(1b = 0, vtype = GRB.CONTINUOUS, name = 'y' + str(i+1) + str(j+1)))

# defining the objective function
facility_location.setObjective(
    quicksum(operating_costs[j]*x[j] for j in cities) + quicksum(quicksum(shipping_costs[i][j] * y[i][j] for j in cities) for i in markets), GRB.MINIMIZE)

# Constraints definition
facility_location.addConstrs((quicksum(y[i][j] for i in markets) <= capacities[j] * x[j] for j in cities), 'Product Capacity')

facility_location.addConstrs((quicksum(y[i][j] for j in cities) >= demands[i] for i in markets), 'demand_fulfillment') 

facility_location.optimize()

########################
# print the result

print('result:')

for j in cities:
    print(x[j].varName, '=', x[j].x)

# Head of the result table
print ('\tMarket1\tMarket2\tMarket3\tMarket4\tMarket5')

for j in cities:
    print('CIty' + str(j+1), '\t', end='')
    for i in markets:
        if len(str(y(i)(j).x)) < 7:
            print(y[i][j].x,'\t', end='')
        else:
            print(y[i][j].x, '', end='')
    print('')

print('z* = facility_location.objVal')

    

