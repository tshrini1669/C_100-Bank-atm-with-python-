class Atm():
    def __init__(self,name,cardnumber,pinnumber,voterid,bank):
        self.name = name
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
        self.voterid = voterid
        self.bank = bank
    def cashwithdrawl(self):
        print("You Have with drawed 5,00,000")
    def be(self):
        print("Your bank balance is " + self.bank + "!")
    def cashwithdrawl(self):
        print("You Withdrawed 150000 INR")
TSR = Atm("Shrini","84481848485","5959989","656498498","4875348653")
TSR.cashwithdrawl()
Shrini = Atm("Turpu Shriniketan Rao","00087111234","04027936147","9160933399","15000")
Shrini.be()


   


