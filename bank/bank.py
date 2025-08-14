def main():
    bank_teller = input("Greet Customer:").strip().lower()
    if bank_teller.startswith("hello"):
        print("$0")
    elif bank_teller.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
