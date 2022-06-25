#Portfolio Optimization problem

import pandas as pd

# Reading excel sheets and turn into lists

stock_info_info = pd.read_excel('NLP_dataset.xlsx','Stock information')
Stocks = range(len(stock_info['Stock']))
prices = range(len(sotck_info['Price']))
exp_prices = sotck_info['Expected Price']
variances = stock_info['Vairnace of the price']

other_info = pd.read_excel('NLP_dataset.xlsx','Budget and min_exp_profit')
budgets = other_info['Budget']
min_exp_rev = other_info['Minimum Expected profit']

#################
# building a model

Portfolio_optimization = Model('Portfolio_optimization')

# adding a lists as variables
x=[]
for i in markets:
    x.append(Portfolio_optimization.addVar(1b = 0, vtype = GRB.CONTINUOUS, name = 'x' + str(i+1))

# defining the objective function
Portfolio_optimization.setObjective(
    quicksum(variances[i] * x[i] * x[i] for i in stocks) , GRB.MINIMIZE)

# Constraints definition
Portfolio_optimization.addConstrs((quicksum(prices[i] * x[i] for i in stocks) <= budget, 'Budget Limit')

Portfolio_optimization.addConstrs((quicksum(exp_prices[i] for i in stocks) >= min_exp_rev, 'min expected revenue') 

Portfolio_optimization.optimize()

########################
# print the result

for i in stocks:
    print(x[i].varName, '=', x[i].x)

print('z* = Portfolio_optimization.objVal')

print('Expected profit =', sum(exp_prices[i] * x[i].x for i in stocks))
print('Total spending =', sum(exp_prices[i] * x[i].x for i in stocks))
    

