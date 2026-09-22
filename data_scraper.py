import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

# Get the website
response = requests.get(url)

# Read the website
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Create CSV file
file = open("books.csv", "w", newline="", encoding="utf-8")

writer = csv.writer(file)

# Add headings
writer.writerow(["Book Name", "Price"])

# Get book details
for book in books:

    name = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    writer.writerow([name, price])

file.close()

print("Data scraped successfully!")
print("Saved in books.csv")