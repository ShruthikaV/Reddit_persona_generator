<img width="2880" height="1558" alt="image" src="https://github.com/user-attachments/assets/4edcd905-df75-44da-84a0-e971ef4cb6b1" /><img width="2880" height="1558" alt="image" src="https://github.com/user-attachments/assets/ee2554e7-22d0-403b-800d-ae80ddbb3f74" /># Reddit Persona Generator 🧠

A simple web app that builds detailed user personas based on a Reddit user’s posts and comments. It scrapes Reddit data, then uses Google Gemini AI to analyze the content and generate insights about the user’s personality, interests, motivations, and more. The results can be viewed in the app or downloaded as text and PDF files.

## Features
-> Scrapes up to 100 recent comments and 50 recent posts from any public Reddit user.   
-> Uses AI to generate a rich, narrative persona describing the user’s traits and behavior.   
-> Outputs the persona in a clean, easy-to-read format.   
-> Allows downloading the persona as both a .txt and .pdf file.   
-> Responsive Streamlit web interface with a nice background and styled components.   

## How to Use

-> Enter the full Reddit profile URL (e.g., https://www.reddit.com/user/kojied/).   
-> Click Generate Persona.  
-> Wait while the app scrapes Reddit and generates the persona using AI.   
-> View the generated persona directly in the app.   
-> Download the persona as a TXT or PDF file if needed.  

## 🔧 Setup

1. Clone the repo
2. Install dependencies/python packages:
```bash
pip install -r requirements.txt
```
3. Create a .env file in the root directory with your API keys:
```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_app_user_agent
GEMINI_API_KEY=your_google_gemini_api_key
```
4. Run the app with:
```
streamlit run app.py
```


## Technologies Used:

Python   
Streamlit (for the web app UI)    
PRAW (Python Reddit API Wrapper) for Reddit scraping    
Google Gemini API for AI-generated content    
FPDF for PDF generation     


Streamlit dashboard:
###<img width="2876" height="1566" alt="image" src="https://github.com/user-attachments/assets/043fd3d4-d6d6-444f-835f-7c4be13fbeeb" />
###<img width="2880" height="1558" alt="image" src="https://github.com/user-attachments/assets/217c0c24-6ce2-4757-9686-8f044b79fb1b" />



