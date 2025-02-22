import openai
import os
from datetime import datetime

# Se till att din API-nyckel är korrekt inställd som en miljövariabel
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY miljövariabeln är inte inställd.")

openai.api_key = api_key

# Definiera prompten för blogginlägget
prompt = (
    "Skriv ett detaljerat blogginlägg om de senaste framstegen inom artificiell intelligens, "
    "inklusive maskininlärning, djupinlärning och deras tillämpningar i olika industrier. "
    "Diskutera också framtida trender och etiska överväganden."
)

# Anropa OpenAI:s API för att generera text
try:
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Du är en expertbloggare inom artificiell intelligens."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,  # Justera antalet tokens baserat på önskad längd
        temperature=0.7,  # Justera kreativiteten i textgenereringen
    )
except openai.error.OpenAIError as e:
    print(f"Ett fel inträffade vid anropet till OpenAI API: {e}")
    raise

# Extrahera det genererade innehållet
generated_content = response.choices[0].message['content']

# Formatera dagens datum för filnamnet
today = datetime.now().strftime("%Y-%m-%d")

# Definiera filnamnet för blogginlägget
filename = f"_posts/{today}-ai-framsteg.md"

# Skapa innehållet i blogginlägget med YAML-metadata
blog_post = f"""---
layout: post
title: "De senaste framstegen inom artificiell intelligens"
date: {today}
categories: AI Utveckling
---

{generated_content}
"""

# Skriv blogginlägget till en fil
try:
    with open(filename, "w") as file:
        file.write(blog_post)
    print(f"Blogginlägget har skapats: {filename}")
except IOError as e:
    print(f"Ett fel inträffade vid skrivning till filen: {e}")
    raise
