import requests
from bs4 import BeautifulSoup
import urllib3

# Disable SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://example.com"

try:
    response = requests.get(url, verify=False)
    response.raise_for_status()

    print("✅ Website accessed successfully!\n")

    soup = BeautifulSoup(response.text, "html.parser")

    print("Page Title:", soup.title.text)
    print("\nHeadings found on page:\n")

    headings = soup.find_all("h2")

    for heading in headings:
        print("-", heading.text)

    # Save to file
    with open("scraped_data.txt", "w", encoding="utf-8") as file:
        file.write("Page Title: " + soup.title.text + "\n\n")
        for heading in headings:
            file.write(heading.text + "\n")

    print("\n📁 Data saved to scraped_data.txt")

except requests.exceptions.RequestException as e:
    print("❌ Error accessing website:", e)
