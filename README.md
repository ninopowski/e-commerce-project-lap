# E commerce app

### Voved

E commerce app e del od ednostaven e-commerce sistem,
so koj se ovozmozuva kreiranje i brisenje na podatoci povrzani
so potrosuvaci i proizvodi.

### Funkcionalnosti

* Kreiranje na baza na podatoci so potrosuvaci i produkti
* Dodavanje i brisenje na podatoci od bazata preku soodvetni
API endpoints,
* Verifikacija na validna creditna karticka pri zapis
* Prikazuvanje na site proizvodi od najeftin do najskap so izbor
razlicna valuta

### Voved za instalacija

* Vo requirements.txt se navedeni site potrebni moduli i paketi
koi e potrebno da se instaliraat kako bi rabotela aplikacijata.
* Python version: 3.80
* Run app.py za start
* Konekcijata so API-to i negovoto testiranje moze da se napravi
so pomos na Postman preku local host (http://127.0.0.1:5000/) 
i navedenite adresi vo tabelata podulu.
* Back up na bazata so podatoci (shop.db) e vo istiot folder
so ostanatite fajlovi.


### API Endpoints

| Resource      | Address         | http Protocol | Params                            |
|---------------|-----------------|---------------|-----------------------------------|
| AddUser       | /add_user       | POST          | {full json}*                      |
| RemoveUser    | /remove_user    | DELETE        | {"email":"user@mail.com"}         |
| AddProduct    | /add_product    | POST          | {full json}*                      |
| RemoveProduct | /remove_product | DELETE        | {"name":"product_name"}           |
| ListProducts  | /list_products  | GET           | KEY: "currency"<br/> VALUE: "XXX" |



* AddUser ocekuva podatoci (body/raw/json) vo sledniot oblik:
```commandline
{
    "name": "ime",
    "last name": "prezime",
    "email": "mail@mail.com",
    "credit card": 4567897658973215,
    "street and number": "ulica i broj",
    "post code": 1000,
    "city": "grad",
    "country": "drzava"
}

```
* AddProduct ocekuva podatoci (body/raw/json) vo sledniot oblik:
```commandline
{
    "name": "ime na product",
    "category": "pizami",
    "amount": 2,
    "size": "XL",
    "price": 1900,
    "currency": "MKD"
}
```
* RemoveUser ocekuva (body/raw/json), vo oblik:

```
{
    "email": "user@mail.com"
}
```
* RemoveProduct ocekuva (body/raw/json), vo oblik:
```commandline
{
    "name": "ime na product"
}
```


* ListProducts ocekuva (Params/Query Params), KEY: "currency", VALUE: "XXX";
kade XXX e nekoj od: ("MKD", "USD", "EUR").


### Zabeleski

* Verifikacijata na dozvolenite vrednosti koi mozat da se zacuvaat
kaj modelot na Product (category, size) se vrsi na nivo na aplikacija. 
Ova znaci deka nekoj so direkten pristap do data bazata moze da vnese i
drugi vrednosti od predlozenite. Toa bi mozelo da se spreci so nesto nalik:
```commandline
db.Column(db.Enum(Choices, values=[]))
```


### Izrabotil:
### Perkovikj Nino


