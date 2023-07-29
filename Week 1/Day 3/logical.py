"""logical operators
AND 
condition 1     condition 2     result
   F               F              F
   T               F              F
   F               T              F
   T               T              T

   OR
   condition 1   condition 2    result
   F               F              F
   T               F              T
   F               T              T
   T               T              T
   T               T              T


   not 
   reverse of the result
"""

physics = 45
chemistry = 19

print(physics > 33 and chemistry > 33)
print(physics > 33 or chemistry > 33)
print(not physics > 22)
