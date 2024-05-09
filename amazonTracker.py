import requests
from bs4 import BeautifulSoup

amazonURL = "https://www.amazon.co.jp/?&tag=hydjpabky-22&ref=pd_sl_8eaqjij3p1_e&adgrpid=118839724067&hvadid=665927875573&hvqmt=e&hvdev=c&hvtargid=kwd-893523692&hydadcr=27920_14702046"

def amazonTrackingPrice():
    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.content,"html.parser")
    print(soup)

amazonTrackingPrice()
