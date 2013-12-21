degrees = int(raw_input ("How much Fahrenheit degrees do you want to convert? "))

def to_celsius(degrees):
  return (degrees - 32) / 1.8
  

cel = to_celsius(degrees)
print "This will be",cel,"Celsius degrees"
