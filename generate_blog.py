import requests
import os
from datetime import datetime

# Hämta API-nyckeln från miljövariabeln
API_KEY = os.getenv("GEMINI_API_KEY")

# Definiera API-endpoint
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# Uppdaterad prompt:
# Vi instruerar modellen att skriva ett SEO-optimerat blogginlägg direkt utan någon introduktion eller referens till AI-generering.
prompt = (
    "Skriv ett SEO-optimerat blogginlägg om lekplatssäkerhet för fastighetsägare och bostadsrättsföreningar. "
    "Artikeln ska inledas direkt med innehållet, utan någon inledande text som: 'Visst, här är ett SEO-optimerat blogginlägg ...'. "
    "Använd en tydlig struktur med underrubriker och inkludera eventuella relevanta länkar där det passar."
)

# Skapa payload för API-anropet
payload = {
    "contents": [{
        "parts": [{"text": prompt}]
    }]
}

# Skicka begäran till API:t
response = requests.post(API_URL, headers={"Content-Type": "application/json"}, json=payload)

# Hantera API-svaret
if response.status_code == 200:
    data = response.json()
    blog_content = data["candidates"][0]["content"]["parts"][0]["text"]

    # Se till att mappen "blog" finns, annars skapa den
    os.makedirs("blog", exist_ok=True)

    # Skapa en fil för inlägget med dagens datum
    today = datetime.today().strftime('%Y-%m-%d')
    filename = f"blog/{today}-lekplatssäkerhet.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"# Lekplatssäkerhet för fastighetsägare och bostadsrättsföreningar\n\n{blog_content}")

    print(f"Inlägg sparat som {filename}")
else:
    print("Fel vid API-anrop:", response.text)
