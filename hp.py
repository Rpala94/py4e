hrs = input("Enter Hours:")
rate = input("Enter hourly rate:")
h = float(hrs)
r = float(rate)
if h <= 40:
    print(h*r)
else:
    print((h-40)*(1.5*r) + (40*r));