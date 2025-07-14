import google.generativeai as genai
import os
import time
import json
from dotenv import load_dotenv
from generate_pdf import save_persona_as_pdf

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_persona(username):
    with open(f'sample_data/{username}_raw.json') as f:
        raw = json.load(f)

    content = ""
    char_limit = 10000
    for comment in raw["comments"]:
        snippet = f"COMMENT: {comment['text']} (source: {comment['permalink']})\n"
        if len(content) + len(snippet) > char_limit:
            break
        content += snippet

    for post in raw["posts"]:
        snippet = f"POST: {post['title']} - {post['body']} (source: {post['permalink']})\n"
        if len(content) + len(snippet) > char_limit:
            break
        content += snippet

    prompt = f"""
Your task is to generate a detailed **user persona** based on a Reddit user's posts and comments.

Please include:
- Name (fictional)
- Age (guess from content)
- Occupation
- Personality Traits
- Behaviors & Habits
- Motivations
- Frustrations
- Goals & Needs

Cite the original post/comment URLs that support your inferences. Be honest when unsure.

Here is the data:
{content}
"""

    model = genai.GenerativeModel('gemini-1.5-flash')

    try:
        response = model.generate_content(prompt)
    except Exception as e:
        if "429" in str(e):
            print("⚠️ Rate limit hit. Retrying after delay...")
            time.sleep(15)
            response = model.generate_content(prompt)
        else:
            raise e

    persona = response.text

    os.makedirs("output", exist_ok=True)
    with open(f'output/{username}_persona.txt', 'w', encoding='utf-8') as f:
        f.write(persona)


    save_persona_as_pdf(username, persona)

    return persona
