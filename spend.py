import datetime
import os
class MoneyManager:
    def __init__(self):
        self.spends=[]
    # listemiz oluşturuyoruz fiyat, kategori , tarih olacak sekilde
    #We create our list as price, category, date
    def add_spends(self,amount,category):
        spend_info=f"Amount: {amount} Category: {category}, Date:{datetime.datetime.now().strftime('%Y-%m-%d')}\n"
        self.spends.append(spend_info)
        with open("spends.txt","a+") as file:
            file.write(spend_info)

    def see_daily_spends(self):
        self._see_period_spends("daily")
    def see_weekly_spends(self):
        self._see_period_spends("weekly")
    def see_monthly_spends(self):
        self._see_period_spends("monthly")

    def _see_period_spends(self,period):
        try:
            total_amount=0
            today=datetime.datetime.now()
            with open("spends.txt","r") as file:
                # satır satır ayırıp satır içinde "," den sonra strip ile küme olacak sekilde ayırıyoruz
                #We separate line by line and separate them in a cluster with a strip after "," in the line
                lines=file.readlines()
                for line in lines:
                    parts=line.strip(",")
                    date=datetime.datetime.strptime(parts[2].split(":")[1].strip(),"%Y-%m-%d")
                    if period=="daily" and date.date()==today.date():
                        amount=float(parts[0].split(":")[1].strip())
                        total_amount+=amount
                        print(line.strip())
                    elif period=="weekly" and today - datetime.timedelta(days=7)<=date<=today:
                        amount=float(parts[0].split(":")[1].strip())
                        total_amount+=amount
                        print(line.strip())
                    elif period=="monthly" and date.month==today.month and date.year==today.year:
                        amount=float(parts[0].split(":")[1].strip())
                        total_amount+=amount
                        print(line.strip())
            print(f"Total amount for{period.capitalize()} Period: {total_amount}")
        except FileNotFoundError:
            print("No spendig yet.")

    #kategori türüne göre tüm zamanların harcaması
    #all-time spending by category type
    def see_category_spends(self,category):
        try:
            total_amount=0
            with open("spends.txt","r") as file:
                lines=file.readlines()
                for line in lines:
                    parts=line.split(",")
                    spend_category=parts[1].split(":")[1].strip()
                    if spend_category.lower()==category.lower():
                        amount=float(parts[0].split(":")[1].strip())
                        total_amount+=amount
                        print(line.strip())
            print(f"Total Amount for Category '{category.capitalize()}': {total_amount}")
        except FileNotFoundError:
            print("No spending yet.")
    #tüm harcamalar toplamı
    #all spending sum
    def see_all_spend(self):
        try:
            total_amount=0
            with open("spends.txt","r") as file:
                lines=file.readlines()
                for line in lines:
                    parts=line.split(",")
                    amount=float(parts[0].split(":")[1].strip())
                    total_amount+=amount
                    print(line.strip())
            print(f"The all time spend is {total_amount}")
        except FileNotFoundError:
            print("Not spending yet.")




                    


def main():

    moneymanager=MoneyManager()
    while True:
        print("Hello to Money Managment\n ")
        print("What wiil you do?\n")
        print("1-Add spend\n")
        print("2-See daily spend\n")
        print("3-See wekly spend\n")
        print("4-See monthly spend\n")
        print("5-See all time spend\n")
        print("6-See all time spend by kategory\n")
        print("7-Exit\n")
        choice=input("Your choice : ")

        if choice=="1":
            amount=float(input("How much do you spend?"))
            category=input("Which category: market/fun/cloth/food/travel/transport/other")
            moneymanager.add_spends(amount, category)
            print("Spend added")
        elif choice=="2":
            moneymanager.see_daily_spends()
        elif choice=="3":
            moneymanager.see_weekly_spends()
        elif choice=="4":
            moneymanager.see_monthly_spends()
        elif choice=="5":
            moneymanager.see_all_spend()
        elif choice=="6":
            moneymanager.see_category_spends()
        elif choice=="7":
            print("Bye Bye...")
            break
        else:
            print("Wrong input")

if __name__=="__main__":
    main()
        
