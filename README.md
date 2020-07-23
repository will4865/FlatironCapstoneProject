# Film Script Success Prediction Using NLP
## Flatiron Capstone Project

### Objective

The objective of this project was to use text data from movie scripts produced over the last 20 years to build a machine learning model to predict the success of future unproduced film scripts. This project has application for the film industry in that it can save the film industry hundreds of millions of dollars per year in wasted salary for script readers, wasted revenue for unproduced would-be-successful scripts, and avoided losses for producing film failures. 

### Data and Methodology

The data for the project was web-scraped using API Calls, Selenium, BeautifulSoup, PDFMiner from a variety of sources. 

- Film titles, production budgets, and box office gross information was web-scraped from TheNumbers.com using BeautifulSoup
- Genre, runtime, release date, and behind-the-camera talent information was obtained by making API calls to OMDBapi.com
- Scripts were webscraped using Selenium and BeautifulSoup from IMSDB.com, Scripts.com, and SubsLikeScript.com and cleaned using the TextHero library

For this project, I followed the ROSE-MED methodology to guide my data science workflow. 

<img src='/figures/df.png' />

### Cleaning and EDA

The biggest challenge I faced with this project was finding complete scripts online that I would be able to webscrape using Selenium or BeautifulSoup or extract from a PDF file using PDFMiner. By and large, successful movies with noteworthy scripts were available in full script form on IMSDB.com. However, scripts from less notable films were difficult to find as they are not the widely distributed collectibles. I had to settle for dialogue transcripts from sites like Scripts.com and SubsLikeAScript.com. The difference between the two types of scripts are shown below. 


#### Full Script from IMSDB.com
<img src='figures/bp_script.png' />


#### Dialogue Transcript from Scripts.com
<img src='figures/norbit_script.png' />

I used the TextHero library and Regex to clean and extract only the dialogue from the full scripts so that it matched the dialogue transcripts that I had for a majority of the scripts. TextHero was used to remove stop words, punctuation, whitespace, and tokenize script contents. This information was then used to build out additional features (total word count, words per minute, and vocabulary diversity). 

#### Succesful Film Script Word Cloud
<img src='figures/pos script word cloud.png' />

#### Failed Film Script Word Cloud
<img src='figures/neg script word cloud.png' />

### Modeling and Model Results
