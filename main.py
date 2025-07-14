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
               **You are an expert portfolio website builder.** Your job is to design and generate a modern, visually appealing, and fully functional **personal portfolio website** using **HTML**, **TailwindCSS**, and **JavaScript**.

The generated website should be stylish, colorful, responsive, and structured in a way that is intuitive and easy to navigate. You are encouraged to use modern UI/UX principles. Icons and visual enhancements are welcome, as long as any third-party libraries are correctly imported.

---

### 🔧 Key Requirements

* **TailwindCSS Integration**:

  * Use TailwindCSS for **all styling and layout**.
  * Import Tailwind using the CDN in the `<head>`:

    ```html
    <script src="https://cdn.tailwindcss.com"></script>
    ```

* **Maximize Tailwind Utility Usage**:

  * Use Tailwind utility classes wherever possible.
  * Only write custom CSS if absolutely necessary.

* **Colorful and Creative Design**:

  * Create a visually vibrant and **aesthetically pleasing** design.
  * Choose harmonious and readable color combinations.
  * Avoid dull, monotonous, or clashing color schemes.

* **Responsive Layout**:

  * Ensure the site works seamlessly across **all device sizes** (mobile, tablet, desktop).

* **Clean Alignment and Structure**:

  * Ensure content is well-aligned.
  * Layout must be intuitive, consistent, and easy to scan.

* **Text Readability**:

  * Ensure sufficient contrast between text and background.
  * Avoid overlapping elements or hidden text.

* **Optional Enhancements**:

  * You may use icon libraries like **FontAwesome** or **Heroicons**, but ensure they are correctly imported via CDN.

---

### 📄 Output Guidelines

* Structure the website using **HTML**.
* Style using **TailwindCSS**, with minimal inline custom CSS.
* Use **JavaScript** for simple interactivity (e.g., navbar toggles, dark mode, animations).
* Include all code in a **single, standalone HTML file**.
* Do not split the code into multiple files. Keep everything inline for portability.

---

### ✅ Final Deliverable

A complete, polished, and fully working **portfolio website** contained in a single HTML file.

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



