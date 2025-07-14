from reddit_scraper import extract_username, scrape_reddit_user
from persona_generator import generate_persona
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python generate_persona.py <Reddit Profile URL>")
        exit()

    url = sys.argv[1]
    username = extract_username(url)

    print(f"Scraping Reddit user: {username}")
    scrape_reddit_user(username)

    print("Generating persona using Gemini...")
    result = generate_persona(username)
    print("Persona saved to output folder.")
