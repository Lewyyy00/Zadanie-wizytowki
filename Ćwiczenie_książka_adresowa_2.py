from faker import Faker

class WizytowkaBaseContact:
    def __init__(self, imie, nazwisko, telefon_prywatny, adres_email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon_prywatny = telefon_prywatny
        self.adres_email = adres_email

    def contact(self):
        print(f"Kontaktuję się z {self.imie} {self.nazwisko}, {self.telefon_prywatny}, {self.adres_email}")
    
    @property
    def label_length(self):
        return str(len(self.imie) + len(self.nazwisko))
    
    def __str__(self) -> str:
        return f"Imię: {self.imie}, Nazwisko: {self.nazwisko}, Telefon: {self.telefon_prywatny}, Email: {self.adres_email}"

    @classmethod
    def Losowanie_wizytówki(cls): 
        los = Faker()
        imie = los.first_name()
        nazwisko = los.last_name()
        telefon_prywatny  = los.phone_number()
        adres_email = los.email()

        return cls(imie, nazwisko, telefon_prywatny, adres_email)
    
class WizytowkaBusinesscontact(WizytowkaBaseContact):
    def __init__(self, imie, nazwisko, telefon_prywatny, adres_email, telefon_służbowy, stanowisko, nazwa_firmy):
        super().__init__(imie, nazwisko, telefon_prywatny, adres_email)
        self.telefon_slużbowy = telefon_służbowy
        self.stanowisko = stanowisko
        self.nazwa_firmy = nazwa_firmy
        
    def contact(self):
        return f"Imię: {self.imie}, Nazwisko: {self.nazwisko}, Email: {self.adres_email}\nDodatkowe informacje: Telefon służbowy: {self.telefon_slużbowy}, Stanowisko: {self.stanowisko}, Nazwa firmy: {self.nazwa_firmy}"
    
    @property
    def label_length(self):
        return super().label_length
    
    @classmethod
    def Losowanie_wizytówki(cls):
        los = Faker()
        imie = los.first_name()
        nazwisko = los.last_name()
        adres_email = los.email()
        telefon_slużbowy = los.phone_number()
        stanowisko = los.job()
        nazwa_firmy = los.company()

        return cls(imie, nazwisko, telefon_slużbowy, telefon_slużbowy, stanowisko, nazwa_firmy, adres_email)

def create_contacts(Rodzaj_wizytówki, ilość):
    Lista_wizytówek = [Rodzaj_wizytówki.Losowanie_wizytówki() for _ in range(ilość)]
    for i in Lista_wizytówek:
        print(i)
        print(f"Długość imienia i nazwiska: {i.label_length}")
        print(i.contact())
        print("-" * 75)

while True:
    Wybrana_wizytówka = input("Podaj jaki rodzaj wizytówki preferujesz. Możesz wpisać 'zwykła' lub 'biznesowa':\n")
    Wybrana_liczba_wizytówek = int(input("Podaj liczbę wizytówek:\n"))
    if Wybrana_wizytówka == 'zwykła':
        create_contacts(Rodzaj_wizytówki=WizytowkaBaseContact, ilość=Wybrana_liczba_wizytówek)
    elif Wybrana_wizytówka == 'biznesowa':
        create_contacts(Rodzaj_wizytówki=WizytowkaBusinesscontact, ilość=Wybrana_liczba_wizytówek)
    else:
        print('podaj parametry jeszcze raz')
        continue
   




