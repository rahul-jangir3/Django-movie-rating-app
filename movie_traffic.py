import requests
from bs4 import BeautifulSoup
import random
import time

BASE_URL = "http://localhost:8000"  # Change to your EC2 public IP if needed
session = requests.Session()

# Helper to get CSRF token from a page
def get_csrf(url):
    r = session.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]
    return token

# Function to generate random movie names
def random_movie_name():
    adjectives = ["Dark", "Bright", "Silent", "Fast", "Epic", "Crazy", "Amazing"]
    nouns = ["Knight", "Hero", "Adventure", "Galaxy", "Dream", "Legend", "Saga"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

# Function to generate random rating
def random_rating():
    return round(random.uniform(1, 10), 1)

# ----------------------
# 1️⃣ User inputs
# ----------------------
while True:
    try:
        num_create = int(input("How many movies to create? "))
        if num_create < 1:
            raise ValueError
        break
    except ValueError:
        print("Enter a positive integer.")

while True:
    try:
        num_delete = int(input(f"How many movies to delete? (<= {num_create}) "))
        if num_delete < 0 or num_delete > num_create:
            raise ValueError
        break
    except ValueError:
        print(f"Enter an integer between 0 and {num_create}.")

# ----------------------
# 2️⃣ Create movies
# ----------------------
print(f"\nCreating {num_create} movies...")
for _ in range(num_create):
    title = random_movie_name()
    rating = random_rating()
    token = get_csrf(f"{BASE_URL}/add/")
    session.post(f"{BASE_URL}/add/", data={
        "csrfmiddlewaretoken": token,
        "title": title,
        "rating": rating
    })
    print(f"Added: {title} ({rating})")
    time.sleep(0.3)

# ----------------------
# 3️⃣ Delete movies
# ----------------------
print(f"\nDeleting {num_delete} movies...")
# Fetch home page and get delete links
r = session.get(BASE_URL)
soup = BeautifulSoup(r.text, "html.parser")
delete_links = [a['href'] for a in soup.select(".actions a") if 'delete' in a['href']]
to_delete = delete_links[:num_delete]

for link in to_delete:
    token = get_csrf(f"{BASE_URL}{link}")
    session.post(f"{BASE_URL}{link}", data={"csrfmiddlewaretoken": token})
    print(f"Deleted {link}")
    time.sleep(0.3)

# ----------------------
# 4️⃣ Refresh homepage
# ----------------------
for i in range(1):
    session.get(BASE_URL)
    print(f"Refreshed homepage")
    time.sleep(0.5)

print("\n✅ Traffic simulation completed!")

