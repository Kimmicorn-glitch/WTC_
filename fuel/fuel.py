def main():
     try: 
        fraction = input("Fraction").strip()\
        percentage = convert(fraction)
        print(gauge(percent))
         break
except (ValueError, ZeroDivisionError)
    continue

def convert(fraction):
       
            x , y = fraction.split("/")
            x = int(x)
            y = int(y)
            if y == 0 or x < 0 or y < 0:
                raise ValueError
                
           return round((x/y)*100)

        except (ValueError, ZeroDivisionError):
            raise ValueError
            
def gauge(percentage):           
    if percent <= 1:
        return "E"
     elif percent >=99:
        return "F"
    else:
        return(f"{percent}%")
      
if __name__=="__main__":
    main()
