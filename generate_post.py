import openai
import os
from datetime import datetime

# Hämta API-nyckeln från miljövariabel
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY är inte inställd som en miljövariabel.")

# Initiera OpenAI-klienten med den nya syntaxen
client = openai.OpenAI(api_key=api_key)

# Skapa en prompt för blogginlägget
prompt = (
    "Skriv ett detaljerat och SEO-optimerat blogginlägg om vikten av lekplatser för barns utveckling. "
    "Inkludera fakta om fysisk aktivitet, social interaktion och mental stimulans. "
    "Ge exempel på bra lekplatsutrustning och hur den bidrar till barns hälsa och välbefinnande."
)

# Anropa OpenAI API med den uppdaterade metoden
try:
    response = client.chat.completions.create(
        model="gpt-4o",  # Använd den senaste tillgängliga modellen
        messages=[
            {"role": "system", "content": "Du är en expert på lekplatser och barnutveckling."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0.7
    )
except Exception as e:
    print(f"Ett fel uppstod vid anropet till OpenAI API: {e}")
    raise

# Extrahera genererat innehåll
generated_content = response.choices[0].message.content

# Skapa filnamn baserat på dagens datum
today = datetime.now().strftime("%Y-%m-%d")
filename = f"_posts/{today}-lekplatser-barns-utveckling.md"

# Skapa blogginläggsfilens innehåll med YAML-metadata
blog_post = f"""---
layout: post
title: "Lekplatsers betydelse för barns utveckling"
date: {today}
categories: Lek & Utveckling
---

{generated_content}
"""

# Spara blogginlägget i en fil
try:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(blog_post)
    print(f"Blogginlägget har sparats: {filename}")
except IOError as e:
    print(f"Fel vid skrivning till filen: {e}")
    raise
