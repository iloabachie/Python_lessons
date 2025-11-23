from bs4 import BeautifulSoup
import requests

# Step 1: Fetch website content
url = "https://example.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Step 2: Extract headlines
headlines = [headline.text for headline in soup.find_all("h2")]

# Step 3: Save to file
with open("headlines.txt", "w") as file:
    for headline in headlines:
        file.write(headline + "\n")