
class BikeRental:

    def __init__(self, name, no_of_bikes) -> None:
        self.name = name
        self.no_of_bikes = no_of_bikes
        self.users = {}


    def rent_bike_hourly(self, name:str, bikes:int):
        """
        Видає людині велосипеди щогодини.
        В якості вхідних даних приймає ім’я людини та кількість велосипедів для прокату.
        """
        if bikes > self.no_of_bikes:
            print(f"Дефіцит велосипедів! Ви можете мати макс {self.no_of_bikes} велосипедів.")

        else:
            self.users.update({name:{"hourly":bikes}})
            print("Велосипед успішно орендований!")
            self.no_of_bikes -= bikes

    def rent_bike_daily(self, name:str, bikes:int):
        """
        Щодня дає людині велосипеди.
         В якості вхідних даних приймає ім’я людини та кількість велосипедів, які можна взяти в оренду
        """
        if bikes > self.no_of_bikes:
            print(f"Дефіцит велосипедів! Ви можете мати макс {self.no_of_bikes} велосипедів.")

        else:
            self.users.update({name:{"daily":bikes}})
            print("Велосипед успішно орендований!")
            self.no_of_bikes -= bikes

    def rent_bike_weekly(self, name:str, bikes:int):
        """
        Виділяє людині велосипеди щотижня.
         В якості вхідних даних приймає ім’я людини та кількість велосипедів для прокату.
        """
        if bikes > self.no_of_bikes:
            print(f"Дефіцит велосипедів! Ви можете мати мак {self.no_of_bikes} велосипедів.")

        else:
            self.users.update({name:{"weekly":bikes}})
            print("Велосипед успішно орендований!")
            self.no_of_bikes -= bikes



    def add(self, num:int):
        self.no_of_bikes = self.no_of_bikes + num

    def min(self, num:int):
        if num > self.no_of_bikes:
            print("Error")
        else:
            self.no_of_bikes = self.no_of_bikes - num


    def issue_bill(self, name:str):
        """
        Видає клієнту рахунок на основі імені клієнта
        """
        if name in self.users.keys():

            for i in self.users[name].keys():
                if i == 'hourly':
                    print(f"{name.capitalize()}, ви орендували {self.users.get(name).get('hourly')} велосипеди на погодинній основі.")
                    bill = 50 * self.users[name]['hourly']
                    print(f"Отже, загальна сума до сплати: {bill}грн")
                    self.no_of_bikes += self.users[name]['hourly']
                    check = input("Натисніть Enter для продовження. ")
                    print("Повернення успішне!")
                    self.users.pop(name)
                
                elif i == 'daily':
                    print(f"{name}, ви орендували {self.users.get(name).get('daily')} велосипед на день.")
                    bill = 200 * self.users[name]['daily']
                    print(f"Отже, загальна сума до сплати: {bill}грн")
                    self.no_of_bikes += self.users[name]['daily']
                    check = input("Натисніть Enter для продовження. ")
                    print("Повернення успішне!")
                    self.users.pop(name)
    
                elif i == 'weekly':
                    print(f"{name.capitalize()}, ви орендували {self.users.get(name).get('weekly')} велосипед на тиждень.")
                    bill = 600 * self.users[name]['weekly']
                    print(f"Отже, загальна сума до сплати: {bill}грн")
                    self.no_of_bikes += self.users[name]['weekly']
                    check = input("Натисніть Enter для продовження. ")
                    print("Повернення успішне!")
                    self.users.pop(name)
    
                else:
                    print("ERROR")

        else:
            print("Введіть ваше ім'я!")


if __name__ == "__main__":

    Nagpur_Bikes = BikeRental("Nagpur Bike Rental Service", 20)





    user = int(input("Авторизація: \n 1. Admin \n 2.Користувач\n"))

    if user == 1:

            while 1:
                task = int(input("Що потрібно:\n 1.Переглянути вільні велосипеди\n 2.Орендувати велосипед\n 3.Повернути велосиед\n 4.Додати\n 5.Видалити\n"))

                if task == 1:
                    print(Nagpur_Bikes.no_of_bikes)


                elif task == 2:
                    type = int(input("На скільки ви хочете орендувати велосипед:\n 1. Погодинно - 50грн \n 2. На день - 200грн \n 3. На тиждень - 600грн\n"))

                    name = input("Введіть ваше ім'я: ")
                    if name in Nagpur_Bikes.users.keys():
                        print("Це ім'я недоступне! Спробуйте з невеликою адаптацією.")
                        continue

                    bikes = int(input("Скільки велосипедів ви хочете орендувати? "))


                    if type == 1:
                        Nagpur_Bikes.rent_bike_hourly(name, bikes)

                    elif type == 2:
                        Nagpur_Bikes.rent_bike_daily(name, bikes)

                    elif type == 3:
                        Nagpur_Bikes.rent_bike_weekly(name, bikes)

                    else:
                        print("Invalid input!")


                elif task == 3:
                    if len(Nagpur_Bikes.users) != 0:
                        for i in Nagpur_Bikes.users.keys():
                            print(f"Ім'я користувача: {i}")
                        name = input("Хто ви з списку? ")
                        Nagpur_Bikes.issue_bill(name)
                    else:
                        print("No one has rented a bike yet!")

                elif task == 4:
                    x = int(input("Додати:"))
                    Nagpur_Bikes.add(x)
                    print(Nagpur_Bikes.no_of_bikes)

                elif task == 5:
                    x = int(input("Видалити:"))
                    Nagpur_Bikes.min(x)
                    print(Nagpur_Bikes.no_of_bikes)


                else:
                    print("Invalid input!")
            print("\n----------------------------------------------------\n")
    elif user == 2:
            while 1:
                    task = int(
                        input("Що потрібно:\n 1.Переглянути вільні велосипеди\n 2.Орендувати велосипед\n 3.Повернути велосиед\n "))

                    if task == 1:
                        print(Nagpur_Bikes.no_of_bikes)


                    elif task == 2:
                        type = int(input(
                            "На скільки ви хочете орендувати велосипед:\n 1. Погодинно - 50грн \n 2. На день - 200грн \n 3. На тиждень - 600грн\n"))

                        name = input("Введіть своє ім'я: ")
                        if name in Nagpur_Bikes.users.keys():
                            print("Це ім'я недоступне! Спробуйте з невеликою адаптацією.")
                            continue

                        bikes = int(input("Скільки велосипедів ви хочете орендувти? "))

                        if type == 1:
                            Nagpur_Bikes.rent_bike_hourly(name, bikes)

                        elif type == 2:
                            Nagpur_Bikes.rent_bike_daily(name, bikes)

                        elif type == 3:
                            Nagpur_Bikes.rent_bike_weekly(name, bikes)

                        else:
                            print("Invalid input!")


                    elif task == 3:
                        if len(Nagpur_Bikes.users) != 0:
                            for i in Nagpur_Bikes.users.keys():
                                print(f"Ім'я користувача: {i}")
                            name = input("Хто ви з списку? ")
                            Nagpur_Bikes.issue_bill(name)
                        else:
                            print("Ще ніхто не орендував велосипед!")

                    else:
                        print("Invalid input!")
            print("\n----------------------------------------------------\n")
