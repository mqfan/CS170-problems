from pulp import * 

prob1 = LpProblem("constraint1", LpMaximize)

# Variables 
x1 = LpVariable("x1", 0, 1) 
x2 = LpVariable("x2", 0, 1) 
x3 = LpVariable("x3", 0, 1) 
z = LpVariable("z") 

# Objective 
prob1 += z
prob1 += x1+x2+x3 == 1
prob1 += 10*x1 - 4*x2 - 6*x3 + z <= 0
prob1 += -3*x1 + x2 + 9*x3 + z <= 0
prob1 += -3*x1 + 3*x2 - 2*x3 + z <= 0

GLPK().solve(prob1) 

# Solution 
for v in prob1.variables(): 
	print v.name, "=", v.varValue

print "objective=", value(prob1.objective)
s1 = value(prob1.objective)


# prob2 = LpProblem("constraint1", LpMinimize)

# # Variables 
# y1 = LpVariable("y1", 0, 1) 
# y2 = LpVariable("y2", 0, 1) 
# y3 = LpVariable("y3", 0, 1) 
# w = LpVariable("w") 

# # Objective 
# prob2 += w
# prob2 += y1+y2+y3 == 1
# prob2 += 10*y1 - 3*y2 - 3*y3 - w <= 0
# prob2 += -4*y1 + y2 + 3*y3 - w <= 0
# prob2 += -6*y1 + 9*y2 - 2*y3 - w <= 0

# GLPK().solve(prob2) 

# # Solution 
# for v in prob2.variables(): 
# 	print v.name, "=", v.varValue

# print "objective=", value(prob2.objective)