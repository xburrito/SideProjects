#Albert Chang
#CSC 11300 - 2N Programming Language

import math

print("Part A:");
a = 42 * 60
print("42 minutes and 42 seconds contains ",end="");
print(a + 42,end=" ")
print("seconds.")
print("")

print("Part B:")

r = 4
print("The volume of a sphere with a radius of 4 is: ",end="")
print((4/3)*math.pi*r**3)

r2 = 6
print("The volume of a sphere with a radius of 6 is: ",end="")
print((4/3)*math.pi*r2**3)
print("")

print("Part C:")
# °F = (°C × 9/5) + 32
# °C = (°F − 32) x 5/9

farenheit = ((-40 * (9/5))+32)
celcius = (((-40-32)*5)/9)
print("-40° in farenheit is ", end="");
print(farenheit, "°")
print("-40° in celcius is also ", end="");
print(celcius, "°")
print("")

print("Part D:")
prismR = 1*2*3
cubeC = 1
fit = prismR/cubeC
print("The volume of of the prism is", prismR, "a units^3")
print("The volume of each cube is", cubeC, "a units^3")
print("Because of this",fit, "cubes can fit into each prism.")
