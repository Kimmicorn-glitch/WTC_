def main():
    while True:     
        try: 
            fraction = input("Fraction: ").strip()
            percent= convert(fraction)
            print(gauge(percent))
            
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    try:   
        x , y = fraction.split("/")
        x = int(x)
        y = int(y)
    
    
        if y == 0 or x < 0 or y < 0 or x > y:
            raise ValueError
        return round((x/y)*100)
    except (ValueError, ZeroDivisionError):
        raise ValueError
    

            
def gauge(percentage):           
    if percentage <= 1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return(f"{percentage}%")
      
if __name__=="__main__":
    main()
