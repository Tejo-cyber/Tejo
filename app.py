from flask import Flask, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

# Root route for testing
@app.route('/')
def home():
    return "Welcome to the Food Blog Generator API! Use the /generate route to generate a blog."

# Route for generating a food blog
@app.route('/generate', methods=['POST'])
def generate_food_blog():
    data = request.json
    prompt = data.get("prompt", "Write a food blog about Italian cuisine.")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )
        return jsonify({"blog": response.choices[0].text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)})

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
