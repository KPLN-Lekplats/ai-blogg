import os
import openai
from datetime import datetime

# Hämta API-nyckeln från miljövariabler
openai.api_key = os.getenv("OPENAI_API_KEY")

# Kontrollera att API-nyckeln är korrekt
if not openai.api_key:
    raise ValueError("Ingen giltig OpenAI API-nyckel hittades!")

# Skapa ett SEO-optimerat blogginlägg
prompt = "Skriv ett SEO-optimerat blogginlägg på svenska om lekplatser och dess betydelse för barns utveckling. Använd viktiga sökord relaterade till lekredskap och KPLN.se."

response = openai.chat.completions.create(
    model="gpt-40",
    messages=[{"role": "system", "content": "Du är en expert på att skriva SEO-optimerade blogginlägg."},
              {"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=1000
)

# Extrahera texten från OpenAI:s svar
blog_text = response.choices[0].message.content.strip()

# Skapa filnamn med dagens datum
date = datetime.today().strftime('%Y-%m-%d')
filename = f"_posts/{date}-seo-optimerat-lekplatser.md"

# Skriv ut till fil
with open(filename, "w", encoding="utf-8") as f:
    f.write(f"---\n")
    f.write(f"title: SEO-optimerade lekplatser\n")
    f.write(f"date: {date}\n")
    f.write(f"---\n\n")
    f.write(blog_text)

print(f"Blogginlägg genererat: {filename}")
