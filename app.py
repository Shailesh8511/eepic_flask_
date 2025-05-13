from flask import Flask, render_template, send_file
from PIL import Image, ImageDraw
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process")
def process():
    input_path = "static/input/ssp.jpeg"
    output_path = "static/output/output.pdf"

    # Open the input image
    image = Image.open(input_path).convert("RGB")

    # Create a white rectangle over the text location
    draw = ImageDraw.Draw(image)
    draw.rectangle([(50, 140), (700, 180)], fill="white")  # Adjust based on exact location

    # Save as PDF
    image.save(output_path, "PDF")

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
