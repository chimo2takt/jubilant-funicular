from data import Customer
from data import Account
from data import Bank

bank = Bank()

while True:
    print('--------------------------------------------')
    print('Välj ett av följande alternativ:')
    print(' 1. Skapa en ny kund')
    print(' 2. Skapa ett nytt konto')
    print(' 3. Ta bort konto')
    print(' 4. Sätta in pengar')
    print(' 5. Ta ut pengar')
    print(' 6. Överför pengar')
    print(' 7. Skriv ut alla konton')
    print(' 8. Sök på kund på del av namn')
    print(' 9. Skriv ut samtliga kunder (bokstavsordning) och dess konton')
    print(' 10. Avsluta programmet')
    choice = int(input())
    if choice == 1:
        print('Du har valt att skapa en ny kund.')
        print('Skriv in kundens namn:', end=' ')
        namn = str(input())
        print('Skriv in kundens personnummer, på formen ÅÅÅÅMMDD:', end=' ')
        personnr = int(input())
        print(f"Kunden tillagd med kundnummer {bank.add_customer(name=namn, personal_nbr=personnr)}.")
    elif choice == 2:
        print('Du har valt att skapa ett nytt konto.')
        print('Ange kundnummer för kunden som ska ha kontot', end=' ')
        kundnr = str(input())
        if bank.get_customer(kundnr):
            print(f"Kontot skapades med kontonummer {bank.create_account(kundnr)}.")
        else:
            print('Det finns ingen kund med det kundnumret.')
    elif choice == 3:
        print('Du har valt att ta bort ett konto.')
        print('Ange kontonummer för kontot som ska tas bort', end=' ')
        kontonr = int(input())
        if bank.remove_account(kontonr):
            print('Kontot togs bort.')
        else:
            print('Kontot kunde inte tas bort.')
    elif choice == 4:
        print('Du har valt att sätta in pengar.')
        print('Ange kontonummer', end=' ')
        kontonr = int(input())
        print('Ange belopp', end=' ')
        belopp = int(input())
        if bank.get_account(kontonr):
            account = bank.get_account(kontonr)
        if account.deposit(belopp):
            print(f"Insättning lyckades, saldot på kontot är nu {account.get_balance()}.")
        else:
            print('Kontot hittades inte.')
    elif choice == 5:
        print('Du har valt att ta ut pengar.')
        print('Ange kontonummer', end=' ')
        kontonr = int(input())
        print('Ange belopp', end=' ')
        belopp = int(input())
        if bank.get_account(kontonr):
            account = bank.get_account(kontonr)
        if account.withdraw(belopp):
            print(f"Uttag lyckades, saldot på kontot är nu {account.get_balance()}.")
        else: 
            print(f"Uttag misslyckades, saldot på kontot är {account.get_balance()}.")
    elif choice == 6:
        print('Du har valt att överföra pengar.')
        print('Ange kontonummer att överföra från', end=' ')
        fran = int(input())
        print('Ange kontonummer att överföra till', end=' ')
        till = int(input())
        print('Ange belopp', end=' ')
        belopp = int(input())
        if bank.transfer(fran, till, belopp):
            print('Överföring lyckades.')
        else:
            print('Överföring misslyckades.')
    elif choice == 7:
        print('Du har valt att skriva ut alla konton.')
        for account in bank.all_accounts():
            print(str(account))
    elif choice == 8:
        print('Du har valt att söka på (del av) kundnamn.')
        print('Skriv in (del av) namn att söka på:', end=' ')
        namn = str(input())
        print('Följande kunder hittades:')
        for customer in bank.find_customer_by_part_of_name(namn):
            print(str(customer))
    elif choice == 9:
        pass
    elif choice == 10:
        pass
    else: 
        pass