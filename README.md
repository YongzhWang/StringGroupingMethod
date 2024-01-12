# StringGroupingMethod

The purpose of this repository is to share a string similarity grouping method I researched and developed with Jccard-Index. Online, there are lots of information related to clustering strings with Jccard-Index but none has developed a method in Python that actually puts the Jccard-Index into application. K-means clustering also works but it requires indication of number of groups which can be inefficient.

I will show my method with a application of classifying Medical Schools which I used for my economics research. In the data file, we already have three important variables Longtitude, Latitude, and School name. Our aim is to cluster the repeated schools. However, given the data came from surveys, the names of school often does not exactly match. Thus, we need a fuzzy type matching. My approach was first gain the address of these schools using geopy library to reverse from the Longtitude and Latitude, as those address are longer and thus more accurate than just the school names. Then, I did a rough grouping by using very close Longtitude and Latitude at the integer level. Within these groups, I applied the Jccard-Index at a threshold of 70%. The results are quite impressive and accurate.


This repository contains two main code and a data files:

