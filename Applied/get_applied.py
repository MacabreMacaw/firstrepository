from bs4 import BeautifulSoup
import csv
# import numpy as np

txt = open("source.txt")
soup = BeautifulSoup(txt, 'lxml')
listings = soup.find_all("li", {"class":"list-item list_rows"})    
txt.close()

lsts=[]

for listing in listings:
    lst=[]
    print(listing)
    h3 = listing.find_all("a")
    for h in h3:
        # sus conditional I think I'm doing this wrong
        if h.text!='' and h.text[:4]!='View' and h.text != 'Withdraw' and h.text != 'javascript:;:':
            lst.append(h.text)
            lst.append(h.get("href"))
    lsts.append(lst)

print(lsts)

with open('applied_at.csv', 'w', newline='') as f:

    write = csv.writer(f)
    write.writerows(lsts)