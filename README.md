# Repository Name: Tiki-Data-Integration

## Description 
This repository encompasses a comprehensive data integration project involving the extraction, transformation, and loading (ETL) of product data from the Tiki.vn website into various data storage systems. The project is designed to achieve the following objectives:

1. Data Extraction and Storage in MongoDB:
Scrapes and captures all displayed products within the website's categories.
Stores the collected data in a MongoDB database for further analysis and processing.

2. Data Backup for Restoration:
Establishes a mechanism to create data backups, facilitating restoration on alternate MongoDB systems.

3. Data Extraction and Storage in MySQL:
Extracts specific fields from the product data, such as name, descriptions, URLs, ratings, quantities sold, prices, and category IDs.
Cleans and processes descriptions to remove unnecessary HTML tags.
Stores the processed data in a MySQL database for utilization by other teams.

3. Category Statistics:
Computes the number of products within each category, including sub-categories.
Generates visualizations to depict the origins of the products and their distribution, aiding in identifying trends and comparisons.

4. Top Performers Analysis:
Identifies the top 10 products based on sales, ratings, and price.

5. Ingredient Information Extraction:
Identifies products with ingredient information in their descriptions.
Extracts the product ID and ingredient details and stores them in CSV format for efficient querying.

6. Image Download and Storage:
Downloads all images associated with each product from their respective base URLs.
Stores the images on the local drive with filenames following the format: productID_number.

7. Future Recommendations:
Provides innovative ideas to team leaders regarding potential avenues for further analysis and utilization of the acquired data.