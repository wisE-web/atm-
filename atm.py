class atm:
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def withdrawn(self,cardnumber):
        print("$20 withdrawal")
    def deposit(self,cardnumber):
        print("$5 deposit")
    def balance(self,cardnumber):
        print("$500")
card=atm(10,10)
print(card.withdrawn(10))