# **EN**

Hello, I would like you to create an application. Today I tried to write codes about it but I’m so shitty in this area. The application Idea I will upload one excel documents and I will use the data and links for cheking amazon prices.  In the application will have four buttons in the user interface. they could be side by side, labeled "Upload", "Run", "Compare" and "Export" in that order. You can use a simple front-end template for the application. Also there is No front end needed for it. 

Also if you could look at the Example(.xlsx) there will be shitty datas. I just need the cells whic is starting from  **B19 as a header and B20 to All Valuable B cells**  & **L20 to all valuable L cells** Where is the links are wrotten for web scraping. 

Step 1:

- Create an "Upload" button to upload an Excel file.
    - If the file is successfully uploaded, display a success message.
    - If it fails to upload, print an error message.
    

Step 2:

- Create an empty dataframe and retrieve data from the uploaded Excel file as follows:
    - Start from cell B20 in the Excel file and go to the last filled cell in column B. Store this data in the dataframe under the column "Product_Name."
    - Start from cell D20 in the Excel file and go to the last filled cell in column D. Store this data in the dataframe under the column "Price_1." ( Unit Price Column In the Excel file)
    - Start from cell L20 and go to the last filled cell in column L. Follow the links in these cells and scrape the price tag data from the linked pages, storing it in the dataframe under the column "Price_2."
    - In cell L20, there are links to websites like Amazon, eBay, etc. For each filled cell in column L, visit the link address and take a screenshot, saving it to the local PC at C:\Users\Office\Desktop. This should be done when the "View Images" button is clicked.
- For the "Compare" button,
    - When clicked, compare Price_1 and Price_2. Create two new columns in the dataframe (Comparison and Percentage). Use the formula percentage_change = ((Price_2 - Price_1) / Price_1) * 100 to calculate the percentage change. Rows where the percentage_change is greater than 30% should have "True" in the Comparison column, and "False" otherwise. The percentage change value should be written in the Percentage column.

Finally,

- Create an export button that saves the newly created dataframe as an Excel file to a local location chosen by the user.


![Buttons Picture]([https://github.com/anilembel/Amazon_Check_Parse/blob/main/buttons.png]))
