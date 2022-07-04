# Python e data neye kaj korar jonno most popular holo pandas
# Ai code korar jono kicu modiul Install korte hbe r akta file lagbe jeta holo csb excel file.
# .jekhane data thakbe( , )separeted

"""
    1. pip install pandas  [Data Gulo Access er jonno ei library install]
    2. pip install matplotlib [Data gulu ke scatter, pie ,bar,barh,Chart akare dekhanor jonno ai library install]
       But Import Korte Hobe   [ import matplotlib.pyplot ]
"""

import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv('iphone_price.csv')
plt.bar(data['version'],data['price'])
plt.show()
