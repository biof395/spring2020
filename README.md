# Syllabus
## BIOF395 Introduction to Text Mining

**Spring 2020**

**Time: Thursday 5:30PM - 7:30PM**

Important notes
---------------
This is a tentative outline for the course and may be updated throughout the quarter.


<!---
To interact with the materials in the repo using [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) (via [Binder](https://mybinder.org/)), please click the button below.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/marskar/biof309_fall2018/master?urlpath=lab)

Additionally, the [Jupyter Notebooks (`ipynb` files)](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html) in this repo can be opened in [Google colab](https://colab.research.google.com) by clicking the icon below.

<a href="http://colab.research.google.com/github/marskar/biof309_fall2018/blob/master/index.ipynb"><img src="https://colab.research.google.com/img/colab_favicon_256px.png" width="48"></a>
-->

Instructors
-----------

* Dr Qingyu Chen (lead instructor) - qingyu dot chen at nih dot com
* Dr Yifan Peng (co-instructor) - yifan dot peng at nih dot com
* Dr Martin Skarzynski (co-instructor) - marskar at gmail dot com





Course description
------------------
Between Electronic Medical Records and Electronic Health Records, PubMed, and collections of biomedical grant
applications, there exist large quantities of medical information stored in databases waiting to be explored.
Besides tables of numbers, medical records also contain a great amount of free-text paragraphs that are
comprehensible by human readers but challenging to the computers. Text mining is an interdisciplinary area that
primarily combines advances in Natural Language Processing (NLP), Information Retrieval (IR), and Machine
Learning (ML) to help the computers understand human written language, and thus extract medical and clinical
information from free-text records. 

This class aims at introducing fundamental applications in text mining such as
named entity recognition (NER), relation extraction, passage retrieval and document classification.
The class is oriented towards hands-on experience with Python, popular text mining packages such as NLTK and spaCy, and popular machine learning packages suc as scikit-learn.

Learning Objectives
-------------------
By the end of this course you should be able to:
1. Develop Python functions for text processing
2. Understand fundamental building blocks of text mining
3. Understand fundamental building blocks of machine learning regarding with text mining applications 
4. Build fundamental text mining applications (hands-on experience with Python, NLTK, spaCy and scikit-learn)

Prerequisites
-------------

Prior exposure to programming and Python is highly recommended, but not required to attend this class. We will provide a crash tutorial on Python for the first three weeks.

Logistics
---------

This is a one-semester course starting on the 6th of February 2020 and finishing on 7th of May 2020.

**Class Location: B1C206, Building 10, NIH Bethesda campus**

Attendance in class is strongly recommended; however, we realize other commitments may occasionally prevent attendance. If you miss a class, please review the materials available at the course and keep up with activities and homework.

Important FAES Fall 2020 semester dates:
* January 31: online registration deadline 
* February 14: late registration deadline (10 dollar late fee per course applies)
* February 6: classes begin
* May 7: classes end

Schedule
--------

| #  | Date       | Topic                                        | Lead              |
|----|------------|----------------------------------------------|-------------------|
| 1  | 2020-02-06 | Course Intro and Python crash course part I  | All Instructors   |
| 2  | 2020-02-13 | Python crash course part II                  | Martin & Qingyu   |
| 3  | 2020-02-20 | Python revision, text processing pipeline, and project intro | Qingyu|
| 4  | 2020-02-27 | Regular expressions, parsing and pos tagging | Yifan             |
| 5  | 2020-03-05 | Machine learning on text part I              | Qingyu            |
| 6  | 2020-03-12 | Machine learning on text part II             | Yifan             |
| 7  | 2020-03-19 | Text mining applications: NER and relation extraction | Yifan    |
| 8  | 2020-03-26 | Text mining applications: sentence similarity and document classification | Qingyu|
| 9  | 2020-04-02 | Mid-term revision and early project feedback | Qingyu & Yifan    |
| 10 | 2020-04-09 | Deep learning on text part I                 | Qingyu            |
| 11 | 2020-04-16 | Deep learning on text part II                | Yifan             |
| 12 | 2020-04-23 | Text mining applications: other applications and project feedback  | Qingyu & Yifan|
| 13 | 2020-04-30 | Requested Topics/review/final project feedback | Qingyu & Yifan    |
| 14 | 2020-05-07 | Student Presentations                        |                   |


Assessment
--------
The assessment focuses on (1) practicing python and machine learning skills and (2) hands-on experience of text mining on real-world datasets. Details are as follows.

1. Python and machine learning skills
By the end of the semester, you must complete [Python Programming Skill Track](https://www.datacamp.com/tracks/python-programming) and [Machine Learning Fundamentals with Python Skill Track](https://www.datacamp.com/tracks/machine-learning-fundamentals-with-python). 
This will take about 35 hours in total to complete. Note that you could also do other tracks if you are interested, but they are optional. **Please start the tracks as soon as possible and work towards the certificate(s) throughout the semester. This may require substantial work! Do not wait until the end of the semester!**

2. Text mining on real-world datasets
By the end of the semester, you must also develop a text mining application on real-world datasets. You will (1) submit the codes and models to a github repository, (2) write up a report to describe the method, and (3) present in the final week. More details will be released in Week 3. 


Required Materials
------------------

**Each student is encouraged to bring their own laptop to each class.**

*Programing without a computer would be an exceptional feat.*

For installing Python or Python related queries, please refer to [BIOF309 Introduction to Python Programming](https://github.com/marskar/biof309_fall2018/). 


Recommended Books
-----------------
**There is no required textbook for this course.**

We do, however, highly recommend [Natural Language Processing with Python](https://www.nltk.org/book/) and [Applied Text Analysis with Python](http://shop.oreilly.com/product/0636920052555.do) for understanding text mining in more depth. If you are also interested in exploring Python in more detail, we recommend [Python for Data Science](https://github.com/jakevdp/PythonDataScienceHandbook) and its companion text [A Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython) by Jake Vanderplas.

Communication
------------

**Before contacting us**, please check to see if your question has already been answered elsewhere, e.g. [StackOverflow](https://stackoverflow.com/).

If you cannot find the answer, please make sure to ask your question thoughtfully (https://stackoverflow.com/help/how-to-ask) and provide everything needed to answer e.g. code, error message, dataset, etc.

In general, please use the [course Slack workspace](https://biof395.slack.com) to communicate with classmates and instructors. If you have a course-relevant question or something to share, [Slack](https://biof395.slack.com) is simply better than email. In case of personal/private question/concerns, please use [Slack](https://biof395.slack.com) direct message (DM).

In case of an emergency, please send a DM on [Slack](https://biof395.slack.com) *and* an email.



Optional Materials
------------------

1. A [UNIX-like system](https://en.wikipedia.org/wiki/Unix-like)

    If you use Windows 10, please try to set up the [Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). If you use MacOS or Linux, you are all set.

2. [GitHub student pack](https://education.github.com/pack)

    [GitHub](https://github.com) is offering some free awesome resources to students, that might be of interest to you, depending on your background:
