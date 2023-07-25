# If two sides greater than third then a valid triangle

SELECT x,y,z,IF((x+y>z and x+z>y and y+z>x) ,'Yes', 'No') as triangle
FROM Triangle