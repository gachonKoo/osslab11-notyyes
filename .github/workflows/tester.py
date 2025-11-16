import geo.utils as utils

a, b, r = map(int, input().split())

c = utils.pythagoras(a, b)
area = utils.circle(r)

print(c)
print(area)
