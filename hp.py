sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float (sh)
fr = float (sr)
# print (fh, fr)
if fh > 40 : 
 reg = fr * fh 
 opt = (fh - 40.0) * (fr * 0.5)
 xp = reg + otp
else:
 xp = fh * fr

print("Pay:",xp)