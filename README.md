## Introduction to Data Mining - Problem set 1

[![pipeline status](https://gitlab.com/Anaxilaus/bil3003-ps1/badges/master/pipeline.svg)](https://gitlab.com/Anaxilaus/bil3003-ps1/commits/master)

Goal is to generate frequent item sets and find association rules with Apriori algorithm. See [problem set description.](./DESCRIPTION.pdf)

Technologies used in this project:

- Python 3.7
- GitLab CI
- Git

## Research

Here's the what I generally used, [`a research paper from 1994 by IBM.`](http://www.vldb.org/conf/1994/P487.PDF)

**The Apriori Principle:**

> If an itemset is frequent, then all of its subsets must also be frequent. Conversely, if an subset is infrequent, then all of its supersets must be infrequent, too.
