# StringGroupingMethod

This repository is dedicated to sharing a string similarity grouping method that I have researched and developed using the Jaccard Index. While there is a plethora of information online about clustering strings with the Jaccard Index, I found a gap in practical Python implementations. My method, detailed here, fills this gap by providing a hands-on approach. Although K-means clustering is another viable technique, it requires specifying the number of groups upfront, which may not always be efficient.

The method is showcased through the classification of Medical Schools, a task undertaken as part of my economics research. The dataset includes three key variables: longitude, latitude, and school name. The challenge was to cluster repeated school entries, which was complicated by variations in school names due to the survey-based nature of the data. To address this, my approach involved two steps:

Address Retrieval: Using the geopy library to convert longitude and latitude into detailed addresses, offering more precision than school names alone.
Clustering: Implementing an initial rough grouping based on closely matching longitude and latitude (rounded to integers). Within these groups, I applied the Jaccard Index with a 70% threshold. The accuracy and precision of the results were impressive.

Repository Contents

StringSimilarityCode.ipynb: This Jupyter notebook contains the implementation of the Jaccard Index method and the classification process.
SampleSchoolData.csv: A sample dataset used in the application.
GeopyLatLong.py: A Python script for converting latitude and longitude into addresses.
Distribution_JaccardScore2.jpg: A visual representation showing the distribution of match scores across the dataset.

Feel free to explore the repository and utilize these resources in your projects.

Andrew


