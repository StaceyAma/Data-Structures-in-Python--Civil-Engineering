
L = 12 #length(span) of beam [meters]
w = 10 #intensity[kN/m]

#import packages
import sympy as sp
#symbolic variables
x = sp.symbols('x')

#formula for Bending moment M
M = w*(-6*x**2 + 6*L**x - L**2)/12
#formula for shear force V of the beam
V = w*(L/2 - x)/2

######### QUESTION A ########

#at x = 0 and x = L
#bending moment at x = 0
bendingMomentAt0 = M.subs(x,0)
#shear force at x = L
shearForceAt0 = V.subs(x,0)
#bending moment at x = L
bendingMomentAtL = M.subs(x,L)
#Shear force at x = L
shearForceAtL = M.subs(x,L)

#Display the BM and SF at x = 0
print(f"At x = 0: Bending Moment = {bendingMomentAt0}, Shear Force = {shearForceAt0}")
#Display the BM and SF at x = L
print(f"At X = L: Bending Moment = {bendingMomentAtL}, Shear force = {shearForceAtL}")


######### QUESTION B #########
# Complete the square and solve for the roots
distance_M_0_roots = sp.solve(sp.simplify(M), x)
print(f"Points of contra-flexure (M = 0): {distance_M_0_roots}")


######### QUESTION C ########

# Complete the square and solve for the roots
distance_V_0_roots = sp.solve(sp.simplify(V), x)
print(f"Point where shear force is zero (V = 0): {distance_V_0_roots}")

####### QUESTION D ########
import numpy as np

# creating an array span of L=12m and discretizing it
span = np.arange(0, L+0.01, 0.01)

# Evaluate bending moment at each step
bending_moments = [M.subs(x, step_point) for step_point in span]
print("Bending Moments along the span:", bending_moments)


######## QUESTION E ########

#Evaluating shear forces at each step
shear_forces = [V.subs(x, step_point)  for step_point in span]
print("Shear forces along the span:", shear_forces)


####### QUESTION F ##########

# points alond L with minimum bending moments values
min_moment_points = [span[i] for i in range(len(bending_moments)) if abs(bending_moments[i]) == min(map(abs, bending_moments))]
print("Points where absolute bending moment is minimum:", min_moment_points)


####### QUESTION G ##########

# Extract numerical values from symbolic expressions
zero_moment_points_numeric = [sp.N(point) for point in zero_moment_points]

# Calculate relative errors
relative_errors = [abs((numeric - estimated) / numeric) * 100 for numeric, estimated in zip(zero_moment_points_numeric, min_moment_points)]
print("Relative errors:", relative_errors)


###### QUESTION H ##########

max_moment_point = span[np.argmax(bending_moments)]
min_moment_point = span[np.argmin(bending_moments)]

print(f"Point of maximum bending moment: {max_moment_point}")
print(f"Point of minimum bending moment: {min_moment_point}")
