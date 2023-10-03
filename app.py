import os
from flask import Flask, request, render_template, jsonify, send_file
import pandas as pd
from bs4 import BeautifulSoup
import requests
import openpyxl
from openpyxl.drawing.image import Image

app = Flask(__name)

# Variables to hold uploaded data
data = pd.DataFrame(columns=["Product_Name", "Price_1", "Price_2"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"message": "No file part"})
        file = request.files['file']
        if file.filename == '':
            return jsonify({"message": "No selected file"})
        if file:
            df = pd.read_excel(file)
            data["Product_Name"] = df.loc[19:, "B"].dropna()
            data["Price_1"] = df.loc[19:, "D"].dropna()
            data["Price_2"] = data["Price_2"].apply(scrape_price)
            return jsonify({"message": "File uploaded successfully"})
    except Exception as e:
        return jsonify({"message": f"Error uploading file: {str(e)}"})

@app.route('/view_images', methods=['GET'])
def view_images():
    try:
        for idx, link in enumerate(data["Price_2"]):
            if link:
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'html.parser')
                img_src = soup.find('img')['src']
                img_response = requests.get(img_src, stream=True)
                with open(f'C:\\Users\\Office\\Desktop\\screenshot_{idx}.png', 'wb') as out_file:
                    out_file.write(img_response.content)
        return jsonify({"message": "Images saved successfully"})
    except Exception as e:
        return jsonify({"message": f"Error saving images: {str(e)}"})

@app.route('/compare', methods=['GET'])
def compare():
    data["Price_1"] = data["Price_1"].astype(float)
    data["Price_2"] = data["Price_2"].astype(float)
    data["Percentage"] = ((data["Price_2"] - data["Price_1"]) / data["Price_1"]) * 100
    data["Comparison"] = data["Percentage"] > 30
    return jsonify({"message": "Comparison completed"})

@app.route('/export', methods=['GET'])
def export():
    data.to_excel("output.xlsx", index=False)
    return send_file("output.xlsx")

if __name__ == '__main__':
    app.run(debug=True)
