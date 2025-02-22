import os
import openai
import datetime

# API-nyckel
openai.api_key = os.getenv("OPENAI_API_KEY")

# Kolla om det är en jämn vecka (ISO-veckonummer)
week_number = datetime.date.today().isocalendar()[1]
if week_number % 2 != 0:
    print("Hoppar över workflow: Det är en udda vecka.")
    exit(0)

# Datum och filnamn
today = datetime.date.today().strftime("%Y-%m-%d")
filename = f"_posts/{today}-seo-optimerat-inlagg.md"

# Fråga OpenAI om ett SEO-optimerat blogginlägg
prompt = """
Skapa ett SEO-optimerat blogginlägg för KPLN.se med fokus på lekplatser, säkerhet och hållbarhet. 
Använd relevanta sökord och inkludera interna länkar till KPLN.se.  
Rubrik, underrubriker och brödtext ska vara optimerade för sökmotorer.
"""

response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[{"role": "system", "content": "Du är en expert på SEO-optimerade blogginlägg."},
              {"role": "user", "content": prompt}]
)

content = response["choices"][0]["message"]["content"]

# Skapa blogginlägget
with open(filename, "w") as f:
    f.write(f"---\n")
    f.write(f"title: SEO-optimerat inlägg om lekplatser\n")
    f.write(f"date: {today}\n")
    f.write(f"---\n\n")
    f.write(content)

print(f"Blogginlägg sparat som {filename}")
