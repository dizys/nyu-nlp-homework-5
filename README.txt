NYU NLP Homework 5: Feature selection for Maxent Group tagger
    by Ziyang Zeng (zz2960)
    Spring 2022

Pre-requisites:
    - Python 3.8+

Install dependencies:
    `pip3 install -r requirements.txt`

Features selected:
    - word stem
    - POS tag
    - whether capitalized
    - previous BIO tag
    - previous word
    - previous POS tagger
    - previous previous word
    - previous previous POS tag
    - next word
    - next POS tag
    - next next word
    - next next POS tag


Score on the development set:
    31628 out of 32853 tags correct
        accuracy: 96.27
    8378 groups in key
    8609 groups in response
    7709 correct groups
        precision: 89.55
        recall:    92.01
        F1:        90.76

