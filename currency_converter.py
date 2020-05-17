import json
import urllib.request

with urllib.request.urlopen(
        "https://free.currencyconverterapi.com/api/v5/convert?q=ILS_USD&compact=nultra&apiKey=a180c5be0fceeb14"
        "5f59") as url:
    data = json.loads(url.read().decode())
    results = data['results']
    ILS_USD = results['ILS_USD']
    currency_value = ILS_USD['val']
    print("Welcome to currency converter")
try:
    amount = float(input("Please enter an amount of Shekeles to convert:"))
    print("Result is: ", float(amount * currency_value))
    print("Thanks for using our currency converter")
except ValueError:
    print("Invalid Choice")
