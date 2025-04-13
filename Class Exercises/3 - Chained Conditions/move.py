from directions import carro as car
x = input("AWSD ")

while x:
    
    
    if x == "W":
        car.forward()
        
    elif x == "S":
        car.back()
    
    elif x == "A":
        car.left()
    
    elif x == "D":
        car.right()
    
    else:
        car.stop()
        break
    
    x = input("AWSD ")
