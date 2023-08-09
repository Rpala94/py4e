def computepay(h, r):
    if h > 40:
        p = 1.5 * r * (h-40) + (40*r) # if rate is over 40 hrs
    else:
        p = h * r
        
    return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter rate per hours:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)