from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from groq import Groq

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, origins=["*"], allow_headers=["*"], methods=["*"], supports_credentials=True)

def generate_website(prompt):
    print(prompt)
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
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

@app.route("/generate_portfolio", methods=["POST"])
def generate_portfolio():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate that prompt is provided
        if not data or 'prompt' not in data:
            return jsonify({"error": "Prompt is required"}), 400
        
        prompt = data['prompt']
        print(prompt)
        
        print("starting generation...")
        generate_website(prompt)
        print("Generation completed.")
        
        return jsonify({"message": "Portfolio generated successfully"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get_html", methods=["GET"])
def get_html():
    try:
        if os.path.exists("portfolio.html"):
            with open("portfolio.html", "r") as f:
                content = f.read()
            return jsonify({"html_content": content}), 200
        else:
            return jsonify({"error": "Portfolio HTML file not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
