# Syllabus
## BIOF395 Introduction to Text Mining

**Spring 2020**

**Time: Thursday 6:00PM - 8:00PM**

**Class Location: B1C206, Building 10, NIH Bethesda campus**

Important Notes
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

* Dr Qingyu Chen, NCBI/NLM/NIH (lead instructor) - qingyu dot chen at nih dot gov
* Dr Yifan Peng, NCBI/NLM/NIH (co-instructor) - yifan dot peng at nih dot gov
* Dr Martin Skarzynski (co-instructor) - marskar at gmail dot com

Office Hours
------------
* Office Hours: Wednesdays and Fridays, 4:00 – 5:00 PM.
* Please do not hesitate to reach out to me to discuss your questions and concerns about the
course policies, course material, and anything else. I will do my very best to make myself
available to you via email and via the course Canvas site. However, if you feel that you are not
getting adequate feedback, or if you are uncertain about any aspect of the course or my
expectations, please contact me (qingyu dot chen at nih dot gov) ASAP.

Course Information
------------------
Prerequisites
-------------
Prior exposure to programming and Python is highly recommended, but not required to attend this class. We will provide a crash tutorial on Python in the first three weeks.

Course Description
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
The class is oriented towards hands-on experience with Python, popular text mining packages such as NLTK and spaCy, and popular machine learning packages such as scikit-learn.

Course Goals
------------
By the end of this course you should be able to:

1. Understand fundamental building blocks of text mining
2. Understand fundamental building blocks of machine learning regarding text mining applications 
3. Develop Python functions for text processing
4. Build fundamental text mining applications (hands-on experience with Python, [NLTK](https://www.nltk.org/), [spaCy](https://spacy.io/) and [scikit-learn](https://scikit-learn.org/stable/))

Required Materials
------------------

**Each student is encouraged to bring their laptop to each class.**

*Programing without a computer would be an exceptional feat.*

For installing Python or Python related queries, please refer to [BIOF309 Introduction to Python Programming](https://github.com/marskar/biof309_fall2018/). 


Text Books
-----------------
**There is no required textbook for this course.**

We do, however, highly recommend [Natural Language Processing with Python](https://www.nltk.org/book/) and [Applied Text Analysis with Python](http://shop.oreilly.com/product/0636920052555.do) for understanding text mining in more depth. If you are also interested in exploring Python in more details, we recommend [Python for Data Science](https://github.com/jakevdp/PythonDataScienceHandbook) and its companion text [A Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython) by Jake Vanderplas.

Optional Materials
------------------

1. A [UNIX-like system](https://en.wikipedia.org/wiki/Unix-like)

    If you use Windows 10, please try to set up the [Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). If you use MacOS or Linux, you are all set.

2. [GitHub student pack](https://education.github.com/pack)

    [GitHub](https://github.com) is offering some free awesome resources to students, that might be of interest to you, depending on your background.

Learning Philosophy
-------------------
In this course, emphasis is placed on your active engagement with the course material and with the
other members of the learning environment – that is, US (your teachers) and your peers. We will guide and
support you through the course, but the onus will be on you to take responsibility for your learning. 

The course is designed
for understanding primary concepts of machine learning and text mining, and more importantly, having in-depth practice on these topics. It will
require you to draw connections among these main topics; critically analyze, evaluate and reflect upon
course concepts; synthesize course concepts; and apply the course concepts in novel ways. For these topics,
having hands-on exprience is essential; you should be able to develop primary text mining applications
on your own after completing the course. The course materials will enable you to develop progressively more advanced
learning skills while obtaining feedback that will allow you to make adjustments and improvements – in
other words, to become a self-regulated learner.
It’s important to be self-aware and to know our learning preferences. If you are not a self-directed,
active learner, then that’s ok – but this course might not be the best fit for you. Please contact me with
your questions or concerns about the learning philosophy for this course.

Course Structure
----------------
* The course Canvas site operates according to the eastern time zone.
* The weeks in this course run Monday – Sunday.
* The course materials will be uploaded to Canvas and also in github for version control (will be cross-referenced).

Course Communication
--------------------
* Weekly Canvas Announcements: before the class each week, I will post a weekly announcement
in Canvas outlining the primary course information for that week. 
* Other Canvas Announcements: In addition to the weekly announcement, I will also periodically
post mid-week announcements when I have important updates and reminders to share with
you. It is a good habit to check the Announcements area in Canvas whenever you access the
course.
* Email From Me: In accordance with program regulations, any emails that I send to you will be
sent to the email address that the program has on file for you; this will be the email address that
you used when you registered for this course. Please check this email address regularly.
* Email To Me: As previously mentioned, you are strongly encouraged to contact me at
qingyu dot chen at nih dot org with questions about the course policies, course material, and anything
else.

Important Dates
---------------
* Course Start Date: February 6, 2020
* Course End Date: May 7, 2020

Policies
--------
Academic Policies
-----------------
This course adheres to all FAES policies described in the academic catalog and student handbook,
including the Academic Integrity policy listed on page 11 of the academic catalog and student handbook.
Be certain that you are knowledgeable about all of the policies listed in this syllabus, in the academic
catalog and student handbook, and on the FAES website. As a student in this program, you are bound by
those policies.

Copyright
---------
All course materials are the property of FAES and are to be used for the student’s individual academic
purpose only. Any dissemination, copying, reproducing, modification, displaying, or transmitting of any
course material for any other purpose is prohibited, will be considered misconduct, and may be cause
for disciplinary action. In addition, encouraging academic dishonesty by distributing information about
course materials or assignments which would give an unfair advantage to others may violate the FAES
Academic Integrity policy. Course materials may not be exchanged or distributed for commercial
purposes, for compensation, or for any purpose other than use by students enrolled in the course.
Distributions of course materials may be subject to disciplinary action.

Guidelines for Disability Accommodations
----------------------------------------
FAES is committed to providing reasonable and appropriate accommodations to students with
disabilities. Students with documented disabilities should contact Dr. Mindy Maris, Assistant Dean of
Education.

Dropping the Course
-------------------
Students are responsible for understanding FAES policies, procedures, and deadlines regarding dropping
or withdrawing from the course or switching to audit status.
Harassment:
FAES adheres to the NIH’s harassment policies, which can be found at the following link:
https://hr.nih.gov/working-nih/civil/statement-workplace-harassment
Faculty and students in FAES courses are responsible for being familiar with the NIH’s harassment
policies and adhering to them.

Attendance and Participation Expectations; Policies on Late or Missed Assignments
---------------------------------------------------------------------------------
* Attendance in class is strongly recommended; however, we realize other commitments may occasionally prevent attendance. If you miss a class, please review the materials available at the course and keep up with activities and homework.
* If you are having difficulty organizing your
workload and making a schedule for yourself, please contact me for advice and assistance. 
* It is understood that illnesses, work or family obligations, and other unexpected issues may
occur. If you have an issue that will cause you to be unable to submit an assignment on time or
is impacting your ability to participate actively in the course, please notify me by email as early
as possible so that we can work out alternative arrangements. In general, the earlier you inform
me about issues, the more options we have available to us, so please do not hesitate to inform
me about any issues that are impacting your ability to successfully participate in the course and
complete your work. I strongly encourage you to communicate with me, and I am committed to
finding solutions that will enable you to be successful in the course (within the framework of
program policies). However, the longer you wait to communicate with me, the more our options
will be constrained by program policies.
* If you do not make alternate arrangements with me, or if you fail to communicate with me
about issues ahead of time, then you will receive a zero for assignments that are not
submitted on time. I do not mean to be harsh, but I am obligated to follow program policies,
and it is important that program and course policies are applied in a consistent and transparent
manner. Consider the following: if you are submitting a grant proposal and you do not follow all
of the instructions exactly as they are written or if you do not meet the deadline, then your
proposal will be rejected. If you have grant funding and are expected to produce deliverables by
a certain point and you do not communicate with the funding agency about any hardships that
are preventing you from being productive, then your funding will be rescinded. Unfortunately,
you will rarely receive second chances in real world scenarios, so it is important to start building
good habits now.

Grading Policies
--------
The assessment focuses on (1) practicing python and machine learning skills and (2) hands-on experience of text mining on real-world datasets. Details are as follows.

1. Python and machine learning skills (50%)

    By the end of the semester, you must complete [Python Programming Skill Track](https://www.datacamp.com/tracks/python-programming) and [Machine Learning Fundamentals with Python Skill Track](https://www.datacamp.com/tracks/machine-learning-fundamentals-with-python). 
This will take about 35 hours in total to complete. Note that you could also do other tracks if you are interested, but they are optional. **Please start the tracks as soon as possible and work towards the certificate(s) throughout the semester. This may require substantial work! Do not wait until the end of the semester!**

2. Text mining on real-world datasets (50%)

    By the end of the semester, you must also develop a text mining application on real-world datasets. You will (1) submit the codes to a [GitHub](https://github.com] repository, (2) write up a report to describe the method, and (3) present in the final week. More details will be released in Week 3. 

Grading Scales
--------------

| Grade | Score |   
|----|------------|
| A+  | 97-100 | 
| A  | 94-96 | 
| A-  | 90-93 | 
| B+  | 87-89| 
| B  | 84-86 | 
| B-  | 80-83 | 
| C  | 70-79 | 
| D  | 60-69 | 
| F  | 59 and below|

Please refer to the academic catalog and program website for additional policies on grading and degree
requirements.

Weekly Schedule
--------

| #  | Date       | Topic                                        | Lead              |
|----|------------|----------------------------------------------|-------------------|
| 1  | 2020-02-06 | Course Intro and Python crash course part I  | All Instructors   |
| 2  | 2020-02-13 | Python crash course part II                  | Martin & Qingyu   |
| 3  | 2020-02-20 | Python revision, text processing I, and project intro | Qingyu|
| 4  | 2020-02-27 | Text processing II | Yifan             |
| 5  | 2020-03-05 | Intro to machine learning              | Qingyu            |
| 6  | 2020-03-12 | Text mining applications I: classification           | Yifan             |
| 7  | 2020-03-19 | Text mining applications II: sequence labelling | Yifan    |
| 8  | 2020-03-26 | Text mining applications III: text retrieval | Qingyu|
| 9  | 2020-04-02 | Mid-term revision and early project feedback | Qingyu & Yifan    |
| 10 | 2020-04-09 | Intro to deep learning                | Qingyu            |
| 11 | 2020-04-16 | Deep learning on text mining I               | Yifan             |
| 12 | 2020-04-23 | Deep learning on text mining II  | Qingyu & Yifan|
| 13 | 2020-04-30 | Requested Topics/review/final project feedback | Qingyu & Yifan    |
| 14 | 2020-05-07 | Student Presentations                        |                   |


