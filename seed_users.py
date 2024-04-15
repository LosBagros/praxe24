import requests
import random
import json

icon = [
    "fab fa-github",
    "fab fa-instagram",
    "fab fa-twitter",
    "fab fa-linkedin",
    "fab fa-youtube",
    "fab fa-facebook",
    "fab fa-tiktok",
    "fab fa-snapchat",
    "fab fa-pinterest",
    "fab fa-reddit-alien",
    "fab fa-tumblr",
    "fab fa-whatsapp",
    "fab fa-spotify",
    "fab fa-vimeo",
    "fab fa-soundcloud",
    "fab fa-discord",
    "fab fa-telegram-plane",
    "fab fa-slack-hash",
    "fab fa-medium-m",
    "fab fa-flickr",
    "fab fa-dribbble",
    "fab fa-behance",
    "fab fa-quora"
]

# You can change the number of users you want to seed
response = requests.get("https://randomuser.me/api/?results=10")
data = response.json()
users = []
for index, user_response in enumerate(data["results"]):
    num_socials = random.randint(1, 4)
    social_links = []
    for _ in range(num_socials):
        social_link = {"url": "https://placehold.co/200",
                       "icon": random.choice(icon)}
        social_links.append(social_link)

    user = {
        "id": index,
        "username": user_response["login"]["username"],
        "pfp_url": user_response["picture"]["large"],
        "links": social_links
    }
    users.append(user)


with open("user_seed.json", "w") as file:
    file.write(json.dumps(users, indent=4))
    print("Users seeded successfully")
