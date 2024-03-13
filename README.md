# pokemon_project

## Table of Contents

- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Tools](#tools)
- [Data Extraction and Collection](#data-extraction-and-collection)
- [Data Cleaning and Preparation](#data-cleaning-and-preparation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Analysis](#data-analysis)
- [Results and Findings](#results-and-findings)
- [Limitations](#limitations)
- [References](#references)
  
### Project Overview

I made this full data analysis project to test my abilities in every task that a data analyst work on, for example extracting and collecting data throught web scraping with Python Libraries, exporting the data to a CSV file and then cleaning the data in Excel to analyze it and finally designing dashboard for better data visualization.

### Data Source

Pokemon Stats: The data was extracted from the website [Wikidex](https://www.wikidex.net/wiki/Lista_de_Pok%C3%A9mon_con_sus_caracter%C3%ADsticas_base)

### Tools

- Python Libraries - Web Scraping 
  - [Requests](https://pypi.org/project/requests/)
  - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
  - [Pandas](https://pandas.pydata.org/docs/index.html)

- Excel - Data Cleaning and Data Analysis
  - [Download here](https://microsoft.com)

- PowerBI - Dashboard and Reports creation
  - [Download here](https://www.microsoft.com/en-us/power-platform/products/power-bi)

### Data Extraction and Collection

For the extraction of the data we use libraries from Python to request and parse the html file we need the data from
1. Import the libraries
2. Request the HTML file from the website
3. Parse the HTML file
4. Find the specific data you want to collect
   - For this we use an iterator to get every single data from a table  
``for pokemon in pokedex_table.find_all("tr"):``   
    ``  pokemon_cell = []``  
    ``  for cell in pokemon.find_all('td'):``  
        ``    pokemon_cell.append(cell.text)``  
    ``  pokedex.append(pokemon_cell)``  
6. Use Pandas to convert the data into a dataframe
7. Export it to CSV

### Data Cleaning and Preparation

In the initial data preparation phase, we performed the following tasks:
1. Import the CSV file into an Excel file
2. Data inspection
3. Handling and replacing typographic errors
4. Converting data types
5. Calculating average and standard deviation from the stats

### Exploratory Data Analysis

EDA involved exploring the stats data to answer key questions, such as:

- Who is the stronger Pokemon?
- Is there a correlation between the average and the standard deviation?
- Which pokemon is the best for each stat?

### Data Analysis

In this case the analysis was very simple using a table chart, gauge chart, donut chart and stacked column chart from Power Bi to analyze and get the EDA answers we needed

### Results and Findings

The analysis results are summarized as follows:
1. The stronger pokemon in all the franchise base on total stat is Eternatus Dynamax Form![Screenshot 2024-03-12 135343](https://github.com/yonnyliang/pokemon_project/assets/110066372/6717ffe1-9825-436e-9d54-581e7b126f3c)

2. There's a slightly positive correlation between average and standard deviation, but a high or low average doesn't mean that the standard deviation variability gets lower![Screenshot 2024-03-12 135712](https://github.com/yonnyliang/pokemon_project/assets/110066372/3b8a5668-95b6-4ff1-9941-ae1c850fc9dc)

3. The pokemons with the highest of each stat in their normal form and without being legendaries are Blissey, Rampardos, Shuckle (Two times), Chandelure and Ninjask![Screenshot 2024-03-12 135734](https://github.com/yonnyliang/pokemon_project/assets/110066372/55bcc1dc-a4e2-4575-9e25-1963b3f7a579)


### Limitations

Since every website and even every table of wikidex sort the pokemons in different ways (Some put the megas after their pre-evolution or their regional forms next to the normal forms and others not, was imposible to me to combine tables by their names or ID)

### References

1. [W3schools](https://www.w3schools.com/python/default.asp)
2. [Stack Overflow](https://stackoverflow.com/)


