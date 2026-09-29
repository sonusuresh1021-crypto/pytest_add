
def simple_interest(principal, rate, time):
      return (p * r * t) / 100

if __name__ =="__main__":     

  p = float(input("Enter principal amount: "))
  r = float(input("Enter rate of interest: "))
  t = int(input("Enter time in years: "))


print("Simple Interest =", simple_interest(p, r, t))