I started this project to improve myself at 03/10/23.


**EN**

Hello, I would like you to create an application. The application will have four buttons side by side, labeled "Upload," "Compare," "View Images," and "Download" in that order. You can use a simple front-end template for the application.

Step 1:

- Create an "Upload" button to upload an Excel file.
    - If the file is successfully uploaded, display a success message.
    - If it fails to upload, print an error message.

Step 2:

- Create an empty dataframe and retrieve data from the uploaded Excel file as follows:
    - Start from cell B20 in the Excel file and go to the last filled cell in column B. Store this data in the dataframe under the column "Product_Name."
    - Start from cell D20 in the Excel file and go to the last filled cell in column D. Store this data in the dataframe under the column "Price_1."
    - Start from cell L20 and go to the last filled cell in column L. Follow the links in these cells and scrape the price tag data from the linked pages, storing it in the dataframe under the column "Price_2."
    - In cell L20, there are links to websites like Amazon, eBay, etc. For each filled cell in column L, visit the link address and take a screenshot, saving it to the local PC at C:\Users\Office\Desktop. This should be done when the "View Images" button is clicked.
- For the "Compare" button,
    - When clicked, compare Price_1 and Price_2. Create two new columns in the dataframe (Comparison and Percentage). Use the formula percentage_change = ((Price_2 - Price_1) / Price_1) * 100 to calculate the percentage change. Rows where the percentage_change is greater than 30% should have "True" in the Comparison column, and "False" otherwise. The percentage change value should be written in the Percentage column.

Finally,

- Create an export button that saves the newly created dataframe as an Excel file to a local location chosen by the user.

If you have question Please contact With me. 

# FR

Bonjour, je souhaiterais que vous créiez une application. L'application comportera quatre boutons côte à côte, étiquetés "Télécharger", "Comparer", "Voir les images" et "Télécharger" dans cet ordre. Vous pouvez utiliser un modèle front-end simple pour l'application.

Étape 1 :

- Créez un bouton "Télécharger" pour télécharger un fichier Excel.
    - Si le fichier est téléchargé avec succès, affichez un message de réussite.
    - En cas d'échec du téléchargement, imprimez un message d'erreur.

Étape 2 :

- Créez un dataframe vide et récupérez les données du fichier Excel téléchargé comme suit :
    - Démarrez à partir de la cellule B20 du fichier Excel et allez jusqu'à la dernière cellule remplie de la colonne B. Stockez ces données dans le dataframe sous la colonne "Product_Name".
    - Démarrez à partir de la cellule D20 du fichier Excel et allez jusqu'à la dernière cellule remplie de la colonne D. Stockez ces données dans le dataframe sous la colonne "Price_1".
    - Démarrez à partir de la cellule L20 et allez jusqu'à la dernière cellule remplie de la colonne L. Suivez les liens dans ces cellules et extrayez les données de l'étiquette de prix des pages liées, en les stockant dans le dataframe sous la colonne "Price_2".
    - Dans la cellule L20, il y a des liens vers des sites web tels qu'Amazon, eBay, etc. Pour chaque cellule remplie de la colonne L, visitez l'adresse du lien et prenez une capture d'écran, en la sauvegardant sur l'ordinateur local à C:\Users\Office\Desktop. Ceci doit être fait lorsque le bouton "Voir les images" est cliqué.
- Pour le bouton "Comparer",
    - Lorsqu'il est cliqué, comparez Price_1 et Price_2. Créez deux nouvelles colonnes dans le dataframe (Comparaison et Pourcentage). Utilisez la formule pour calculer la variation en pourcentage : percentage_change = ((Price_2 - Price_1) / Price_1) * 100. Les lignes où percentage_change est supérieur à 30 % devraient avoir "True" dans la colonne Comparaison, et "False" sinon. La valeur de la variation en pourcentage doit être écrite dans la colonne Pourcentage.

Enfin,

- Créez un bouton d'exportation qui enregistre le dataframe nouvellement créé sous forme de fichier Excel dans un emplacement local choisi par l'utilisateur.