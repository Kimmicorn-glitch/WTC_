def main():
    bank_teller = input("Greet Customer:").strip().lower()
    
    
    if bank_teller.startswith("hello"):
        return 0
    elif bank_teller.startswith("h"):
        return 20
    else:
        return 100

print(main())
