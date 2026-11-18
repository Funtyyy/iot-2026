class VacationPackage:
    
    def __init__(self, country="країна", duration=0, price=0, departure_city="Львів", hotel_stars= 0):
        self.__country = country
        self.__duration = duration
        self.__price = price
        
        self.departure_city = departure_city
        self.hotel_stars = hotel_stars
        
    def get_country(self):
        return self.__country
    
    def get_duration(self):
        return self.__duration
    
    def get_price(self):
        return self.__price
    
    def __str__(self):
        return (f"Путівка до країни {self.__country} на {self.__duration} днів, "
                f"ціна - {self.__price} євро."
                f"\nМісто відправлення - {self.departure_city}"
                f"\nЗірок готелю - {self.hotel_stars}")
    
    def __repr__(self):
        return (f"VacationPackage(country={self.__country}, "
                f"duration={self.__duration}, price={self.__price}, "
                f"departure_city={self.departure_city}, "
                f"hotel_stars={self.hotel_stars})")
    
    def __del__(self):
        print(f"деструктор путівки: {self.__country}, місто відправлення: {self.departure_city}")
    
    
def main():
    countries = [VacationPackage(), VacationPackage("Італія", 10, 1500, "Львів", 4), VacationPackage("Іспанія", 7, 1550, "Краків", 5)]  
    
    for country in countries:
        print("\n")
        print(country)
        print(repr(country))
        
        
if __name__ == "__main__":
    main()