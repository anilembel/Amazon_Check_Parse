import os
from flask import Flask, request, render_template, jsonify, send_file
import pandas as pd
import requests
from bs4 import BeautifulSoup
from openpyxl.drawing.image import Image

app = Flask(__name__, template_folder="templates", static_folder="templates/assets")

# Variables to hold uploaded data
data = pd.DataFrame(columns=["Product_Name", "Price_1", "Price_2"])

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        data = {}
        if 'file' not in request.files:
            return jsonify({"message": "No file part"})
        file = request.files['file']
        if file:
            df = pd.read_excel(file)
            df = df.drop(index=range(19))
            df = df.rename(columns={'香港红珊瑚国际货运代理有限公司' : "Article No.", 
                                    'Unnamed: 1' : "Description of goods", 
                                    'Unnamed: 2' : "HS Code",
                                    'Unnamed: 3' : "Unit Price",
                                    'Unnamed: 4' : "Description of goods",
                                    'Unnamed: 5' : "Material",
                                    'Unnamed: 6' : "Mark",
                                    'Unnamed: 7' : "Quantity",
                                    'Unnamed: 8' : "Total Value",
                                    'Unnamed: 9' : "Total Net Weight kg",
                                    'Unnamed: 10' : "Total Gross Weight kg",
                                    'Unnamed: 11' : "Links"})
            data["Product_Name"] = df["Description of goods"].dropna()
            data["Price"] = df["Unit Price"].dropna()
            data["Link_price"] = df["Links"].dropna()
            return jsonify({"message": "File uploaded successfully"})
    except Exception as e:
        app.logger.info(e.args)
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
