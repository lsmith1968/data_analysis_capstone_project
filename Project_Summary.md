# Project Summary

This project researches the tech industry job market by analyzing two datasets - one with salary information and the other with machine learning job postings.  After cleaning the normalizing the data, the datasets were joined and stored in a SQLite database.  Data was analyzed to identify salary trends by job title and seniority levels for four key roles:  Data Engineer, Software Engineer, Machine Learning Engineer and Data Scientist. Seniority levels were normalized into:  Entry level, Mid-level/Intermediate, Senior level and Executive/Director level.

The analysis is presented through visualizations including a bar chart, box plot, scatter plot and a heatmap. This project showed that Machine Learning Engineer (Executive/Director level) and Software Engineer (Executive/Directive level) had the highest average salaries among the four analyzed roles. Even the Senior level positions in these two roles had average salaries above the Data Scientist and Data Engineer Executive/Director level roles. Also, the average entry level salary for Machine Learning Engineer is substantially higher than the entry level average salaries for Data Scientist and Data Engineer positions. Senior level roles had wider salary ranges while entry level positions offered more consistent pay with had narrower ranges.  Smaller companies tend to have lower salaries across all job titles and seniority levels, while the medium-sized companies had higher salaries. 

It's important to note that of the salaries dataset, 97.22% were reported as employed in a medium-sized company, 2.63% were employee by a large company and .15% were employed at a small company.  The very small sample sizes from the small and large employers could lend to less reliable averages. This is a limitation to the data and future analysis should include a more balanced dataset to more accurately compare average salaries across company sizes.

Other possibilities for future analysis include:
    - Salary comparison by % of remote work
    - % of job posting by state
    - Most frequently used "keywords" in job descriptions
    - Using company description, categorize employer by type and compare salaries accordingly
