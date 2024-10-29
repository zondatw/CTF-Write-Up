from z3 import BitVec, Solver, And, Or, If, sat, Int


# op1 = BitVec("op1", 32)
# op2 = BitVec("op2", 32)
# op3 = BitVec("op3", 32)
# op4 = BitVec("op4", 32)
# op5 = BitVec("op5", 32)
# op6 = BitVec("op6", 32)
# op7 = BitVec("op7", 32)
op1 = Int("op1")
op2 = Int("op2")
op3 = Int("op3")
op4 = Int("op4")
op5 = Int("op5")
op6 = Int("op6")
op7 = Int("op7")

# Create a solver instance
solver = Solver()

a = 100 - 3 * op1 + 3 * op2 + 5 * op4 - 4 * op5 - 1 * op7
b = 100 - 2 * op3 + 6 * op6
c = 100 + 1 * op2 - 1 * op4 + 2 * op5
d = 100 + 4 * op1 + 3 * op3 + 4 * op4 - 5 * op5 - 2 * op6 + 1 * op7
e = 100 + 4 * op6 - 5 * op7
f = 100 - 3 * op1 + 1 * op4 + 3 * op5 + 2 * op7

solver.add((a + b + c + d + e + f) == 638)
solver.add((op1 + op2 + op3 + op5 + op6) <= 13)
solver.add(op1 >= 0)
solver.add(op2 >= 0)
solver.add(op3 >= 0)
solver.add(op4 >= 0)
solver.add(op5 >= 0)
solver.add(op6 >= 0)
solver.add(op7 >= 0)


# Check if the constraints are satisfiable
if solver.check() == sat:
    model = solver.model()
    print(f"Solution found: {model}")
else:
    print("No solution found.")
