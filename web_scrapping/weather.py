import requests
import urllib.request
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&rlz=1C1CHBD_enIL865IL865&sxsrf=ALeKk01tTvPELNBDToIttU4t5hli87D3hQ%3A1621356170923&ei=iu6jYMbgN4jearGggoAL&oq={city}&gs_lcp=Cgdnd3Mtd2l6EAMyBwgjELADECcyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsANQwg1Ywg1gxA5oAXABeACAAW6IAdsBkgEDMC4ymAEAoAEBqgEHZ3dzLXdpesgBCcABAQ&sclient=gws-wiz&ved=0ahUKEwjGzfy01tPwAhUIrxoKHTGQALAQ4dUDCA4&uact=5',headers=headers)

    print("Searching in google......\n")
    soup = BeautifulSoup(res.text,'html.parser')
    print(soup.select("#wob_tm")[0].getText().strip(),"°C")

def main():
    print("Enter city name:")
    city = input()
    city = city + "weather"
    weather(city)





if __name__ == "__main__":
    main()