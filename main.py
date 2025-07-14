from fastapi import FastAPI
from pydantic import BaseModel
import os
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [ "*" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

class user_prompt(BaseModel):
    prompt: str
    
class html_content(BaseModel):
    content: str
   
def generate_website(prompt):
    print(prompt)
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """
                You are a skilled portfolio website builder. Your task is to design and develop a visually appealing, highly functional, and colorful portfolio website using only HTML, CSS, and JavaScript. To enhance the UI, you can use icons, but make sure to import the required library first.

                Requirements:

                Use TailwindCSS: Utilize TailwindCSS to make the website responsive and to style the components. Import the TailwindCSS library by adding <script src='https://cdn.tailwindcss.com'></script> in the <head> section.
                Maximize TailwindCSS usage: Use TailwindCSS utility classes as much as possible to style the website. If a specific styling cannot be achieved with TailwindCSS, use custom CSS.
                Create a unique and colorful design: Elaborate on the design to create a unique, visually appealing, and colorful portfolio website. Use a variety of colors that are appropriate and attractive, and ensure that they complement each other.
                Proper alignments: Ensure that the content is properly aligned, and the layout is well-structured and easy to navigate.
                Text visibility: Make sure that the text is clearly visible and not hidden or obscured by the background or other elements. Ensure sufficient contrast between the text and background colors.
                Single HTML file: Provide the complete code in a single HTML file.
                Guidelines:

                Use HTML to structure the content.
                Use CSS (TailwindCSS and custom CSS) to style the website.
                Use JavaScript to add interactivity to the website.
                Make sure the website is responsive and works well on different devices and screen sizes.
                Pay attention to the alignment of the content, and use TailwindCSS utility classes to achieve proper alignment.
                Choose colors that are aesthetically pleasing and do not compromise the readability of the text.
                Deliverable:

                A single HTML file containing the complete code for the portfolio website.
                """
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="deepseek-r1-distill-llama-70b",
    )

    print(chat_completion.choices[0].message.content)

    with open("portfolio.html", "w") as f:
        f.write(chat_completion.choices[0].message.content) 
    
@app.post("/generate_portfolio")
def generate_portfolio(prompt: user_prompt):
    print(prompt.prompt)
    try:
        print("starting generation...")
        generate_website(prompt.prompt)
        print("Generation completed.")
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/get_html")
def get_html():
    if os.path.exists("portfolio.html"):
        with open("portfolio.html", "r") as f:
            content = f.read()
        return {"html_content": content}
    else:
        return {"error": "Portfolio HTML file not found."}



