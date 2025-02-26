equests
import os
import random
from datetime import datetime

# Hämta API-nyckeln från miljövariabeln
API_KEY = os.getenv("GEMINI_API_KEY")

# Definiera API-endpoint
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# Lista med möjliga ämnen och relaterade SEO-parametrar
topics = [
    {
        "topic": "lekplatssäkerhet",
        "title": "Lekplatssäkerhet och underhåll för fastighetsägare",
        "link_text": "KPLN Lekplatser",
        "link_url": "https://www.kpln.se/category/klassisk-lek"
    },
    {
        "topic": "sport och träning utomhus",
        "title": "Utomhusträning: Tips för parkmiljöer",
        "link_text": "KPLN Sport",
        "link_url": "https://www.kpln.se/category/sport"
    },
    {
        "topic": "utomhusgym",
        "title": "Design och underhåll av utomhusgym",
        "link_text": "KPLN Utomhusgym",
        "link_url": "https://www.kpln.se/category/utomhusgym"
    },
    {
        "topic": "fitness",
        "title": "Fitness i friluftsmiljö: Inspiration och tips",
        "link_text": "KPLN Fitness",
        "link_url": "https://www.kpln.se/category/fitness"
    },
    {
        "topic": "parkmiljöer",
        "title": "Optimera parkmiljön för både rekreation och aktivitet",
        "link_text": "KPLN Parkmiljöer",
        "link_url": "https://www.kpln.se/category/parkmiljoter"  # Justera URL vid behov
    },
    {
        "topic": "skateparks",
        "title": "Säkerhet och design i moderna skateparks",
        "link_text": "KPLN Skate",
        "link_url": "https://www.kpln.se/category/skate"
    }
]

# Välj slumpmässigt ett ämne
chosen = random.choice(topics)

# Bygg en prompt som instruerar modellen att skriva ett SEO-optimerat inlägg
prompt = f"""Skriv ett SEO-optimerat blogginlägg om {chosen['topic']}. 
Inlägget ska vara minst 800 ord och ha en tydlig struktur med underrubriker. 
Inkludera naturliga länkar till KPLN.se och dess produkter, till exempel [{chosen['link_text']}]({chosen['link_url']}). 
Syftet är att driva trafik till KPLN.se och förbättra sökmotoroptimeringen. 
Fokusera på {chosen['title']}. 
Artikeln ska inledas direkt med innehållet, utan någon extra introduktion eller referens till att den är AI-genererad.
"""

# Skapa payload för API-anropet
payload = {
    "contents": [{
        "parts": [{"text": prompt}]
    }]
}

# Skicka anropet till Gemini API:t
response = requests.post(API_URL, headers={"Content-Type": "application/json"}, json=payload)

# Hantera svaret
if response.status_code == 200:
    data = response.json()
    blog_content = data["candidates"][0]["content"]["parts"][0]["text"]

    # Se till att mappen "blog" finns
    os.makedirs("blog", exist_ok=True)

    # Skapa ett filnamn baserat på datum och valt ämne (omvandlar mellanslag till bindestreck)
    today = datetime.today().strftime('%Y-%m-%d')
    slug = chosen['topic'].replace(" ", "-")
    filename = f"blog/{today}-{slug}.md"

    # Skriv rubrik och innehåll till filen
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"# {chosen['title']}\n\n{blog_content}")

    print(f"Inlägg sparat som {filename}")
else:
    print("Fel vid API-anrop:", response.text)
