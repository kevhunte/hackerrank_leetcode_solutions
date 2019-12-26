from math import atan2, degrees, ceil,floor

#####################
AB = int(input())
BC = int(input())

theta = degrees(atan2(AB,BC))
#print(theta)
if(theta % 1.0 < 0.5):
    theta = floor(theta)
else:
    theta = ceil(theta)

print(str(theta)+'°')
#TOA, opp/adj = tan(theta), theta = arctan(opp/adj) => arctan(AB/BC)
