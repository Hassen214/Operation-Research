import gurobipy as grb

try:
    # Create a simple model
    model = grb.Model("test_model")
    
    # Add variables
    x = model.addVar(vtype=grb.GRB.BINARY, name="x")
    y = model.addVar(vtype=grb.GRB.BINARY, name="y")
    
    # Set objective
    model.setObjective(x + y, grb.GRB.MAXIMIZE)
    
    # Add constraint
    model.addConstr(x + y <= 1, "c0")
    
    # Optimize the model
    model.optimize()
    
    # Print the results
    if model.status == grb.GRB.OPTIMAL:
        print(f"Optimal solution: x = {x.x}, y = {y.x}")
    else:
        print("No optimal solution found.")
except grb.GurobiError as e:
    print(f"Gurobi Error: {e}")
