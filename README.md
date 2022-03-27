# E commerce app

### Voved

E commerce app e del od ednostaven e-commerce sistem,
so koj se ovozmozuva kreiranje i manipulacija na podatoci povrzani
so potrosuvaci i proizvodi.

### Funkcionalnosti

* Kreiranje na baza na podatoci so potrosuvaci i produkti
* Dodavanje i brisenje na podatoci od bazata preku soodvetni
API endpoints, i
* Prikazuvanje na site proizvodi od najeftin do najskap

### Voved za instalacija

* Vo requirements.txt se navedeni site potrebni moduli i paketi
koi e potrebno da se instaliraat kako bi rabotela aplikacijata.
* Python version: 3.80
* Run app.py za start
* Konekcijata so API-to i negovoto testiranje moze da se napravi
so pomos na Postman preku local host (http://127.0.0.1:5000/)
* Back up na bazata so podatoci (shop.db) e vo istiot folder
so ostanatite fajlovi.


### API Endpoints

| Resource      | Address         | http Protocol | Params                    |
|---------------|-----------------|---------------|---------------------------|
| AddUser       | /add_user       | POST          | {full json}*              |
| RemoveUser    | /remove_user    | DELETE        | {"email":"user@mail.com"} |
| AddProduct    | /add_product    | POST          | {full json}*              |
| RemoveProduct | /remove_product | DELETE        | {"name":"product_name"}   |
| ListProducts  | /list_products  | GET           |                           |

* AddUser ocekuva podatoci (body/raw/json) vo sledniot oblik:
```commandline
{
    "name": "ime",
    "last name": "prezime",
    "email": "mail@mail.com",
    "credit card": "",
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
    "price": 1900
}
```




