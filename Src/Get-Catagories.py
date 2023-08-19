from bs4 import BeautifulSoup
import requests
import csv


def main():
    url = 'https://tiki.vn/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'} 
    response = requests.get(url, headers=header)
    source = response.text
    soup = BeautifulSoup(source,'html.parser')
    Specs = soup.find_all('div', class_='styles__StyledListItem-sc-w7gnxl-0 cjqkgR')
    for Spec in Specs:
        hrefs = Spec.find_all('a',href=True)
        rows = []
        for href in hrefs:    
            row = href['href']
            rows.append(row)

    print(rows)
    with open('1_href_category.txt', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(rows)
if __name__ == "__main__":
    main()