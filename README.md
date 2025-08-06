# Salary Comparison of Tech Positions

This data analysis project is designed to compare salaries by job title and seniority level in tech industry. This project was interesting to me as I evaluate my career options, given my remaining working years and my long-term professional goals.  This project allows me to use real-world labor market data to assess opportunities within tech roles, the salaries and seniority level required to achieve a desired salary range.  This project provides insight into career pathing alternatives that balance earning potential and required seniority level to reach desired earning potential. 

## Project Overview
The objective of this project is to analyze salary trends in various tech positions by combining two datasets, see below, that are joined and stored in a SQLite database.
1. Data Science, AI, and Machine Learning Job Salaries (2025) 
2. Machine Learning Job Postings in the U.S.  

The project aimed to answer the following questions: 
1.  How do salaries vary by job role and seniority level?
2. What is the spread of salaries for each role?
3. How do salaries compare across company sizes?

My methods include cleaning and merging datasets found in Kaggle.  I normalized job titles as well as seniority levels using Pandas.   In addition, I removed extraneous columns and information so I can clearly and concisely examine and compare salaries by position and seniority level.

## Project Setup Instructions
The requirements to run this project are included in the 'Requirements.txt' folder.

I created this project in Jupyter Notebook using Python (3.13.1) in a virtual environment within VS Code.   It was created on a Windows system.  Utilizing the Jupyter Notebook allowed for clear markdowns to be added for narrative-driven presentation of both code and results.

The project file, LHS_DataAnalysisCapstoneProject.ipynb, can be run with these steps: 
1. Clone the repository (https://github.com/lsmith1968/data_analysis_capstone_project)
    Step 1:  Install Git (if not already installed, download from https://git-scm.com/downloads)
    Step 2:  Open a terminal or PowerShell
    Step 3:  Navigate to the folder where you want to store the project
    Step 4:  Clone the repository by typing the following:  git clone https://github.com/lsmith1968/data_analysis_capstone_project.git
    Step 5:  Navigate into the project folder

2. Create a virtual environment and activate it
    - if running on Windows:  
        from your terminal run python -m venv env
        activate by running .\venv\Scripts\activate 
            -If PowerShell blocks activation, type: /k venv\Scripts\activate.bat
    - if running on a Mac or Linux:  
        from your terminal run python3 -m venv env
        activate by running source venv/bin/activate

3. Install required dependencies as shown in the requirements.txt file

4. Install Jupyter Notebook if you don't already have it installed:  pip install notebook

5.  Start Jupyter Notebook

6.  Open LHS_DataAnalysisCapstoneProject.ipynb

7.  Run each cell in the notebook in order or click Run All.

Once the notebook is running, you will see: 
1. Data Import using Kaggle CLI to access two .csv files:
    - https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs/data
    - https://www.kaggle.com/datasets/ivankmk/thousand-ml-jobs-in-usa
2. Data Cleaning
    - Standardized job titles (e.g. "ML Engineer" to "machine learning engineer")
    - Standardized seniority levels (e.g. "EN" to "entry level")
    - Filtering to focus on four key job titles:  data engineer, machine learning enginner, data  scientist,and software engineer.  
3. SQLite Database Creation
    - Combining two database tables (jobs_db and salaries_db) into jobs_salaries_db
    - Tables linked via job_title + seniority level
4. Data Analysis
    - Salary averages and spread by role and seniority level
    - Salary variation across company sizes
5. Visualizations
    - Bar Chart:  Average Salary by Role and Seniority Level
    - Box Plot:  Salary Distribution by Role and Seniority Level
    - Scatterplot:  Salary Distribution by Company Size and Role/Seniority Level
    - Heatmap:  Average Salary Heatmap by Role/Seniority and Company Size

## Technologies Used

Python (3.13.1) was used as the primary programming language.
SQLite3 was used for joining and querying.
Pandas was used for data cleaning.
Matplotlib and Seaborn were used as the base library for creating visualizations.
Jupyter Notebook was used for narrative-driven coding and results presentation.
VS Code was the code editor used.
Git and GitHub - used for version control and project hosting.
Windows - the operating system used.
PowerPoint - used for Project Presentation

### Jobs.csv Data Dictionary

| Column Name              | Description | Data Type |
| -------------------------|-------------|-----------|
| Job Posted Date          | The date the job was posted | Object |
| Company Address Locality | The city or locality of the job or company | Object |
| Company Address Region   | The U.S. state or region where the job is located | Object |
| Company Name             | The name of the company posting the job | Object |
| Company Website          | The official website of the company | Object |
| Company Description      | A short description or mission statement of the company | Object |
| Job Description Text     | The full job description text as listed in original post | Object |
| Seniority Level          | The required seniority level | Object |
| Job Title                | The ful job title listed in the posting | Object | 

### Salaries.csv Data Dictionary

| Column Name              | Description | Data Type |
| -------------------------|-------------|-----------|
| WOrk Year                | The year the salary was reported | Integer |
| Experience Level         | The seniority level of the employee at the time of reporting | Object |
| Employment Type          | The type of employment contract | Object |
| Job Title                | The employee's specific job title | Object |
| Salary                   | The employee's annual salary in the original reported currency | Integer |
| Salary Currency          | The currency in which the salary was originally paid | Object |
| Salary in US Dollars     | The employee's salary coverted to USD using 2025 exchange rates | Integer | 
| Employee Residence       | The country where the employee resides | Object |
| Remote Ratio             | Indicates the percentage of remote work | Integer | 
| Company Location         | The country where the company is headquartered | Object |
| Company Size             | The size of the employing organization | Object |

## Project Summary

In summary, this project showed that Machine Learning Engineer (Executive/Director level) and Software Engineer (Executive/Directive level) had the highest average salaries among the four analyzed roles. Even the Senior level positions in these two roles had average salaries above the Data Scientist and Data Engineer Executive/Director level roles. Also, the average entry level salary for Machine Learning Engineer is substantially higher than the entry level average salaries for Data Scientist and Data Engineer positions. Senior level roles had wider salary ranges while entry level positions offered more consistent pay with had narrower ranges.  Smaller companies tend to have lower salaries across all job titles and seniority levels, while the medium-sized companies had higher salaries.  It's important to note that of the salaries dataset, 97.22% were reported as employed in a medium-sized company, 2.63% were employee by a large company and .15% were employed at a small company.  The very small sample sizes from the small and large employers could lend to less reliable averages. This is a limitation to the data and future analysis should include a more balanced dataset to more accurately compare average salaries across company sizes.    





 
