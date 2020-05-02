# To make result rapid, recommend cut the files to front 1 thousand lines


# libs
import string
import numpy as np 
import random
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from plotly import graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from collections import Counter

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


from tqdm import tqdm
import os
import random

import warnings
warnings.filterwarnings("ignore")


# read_file
train = pd.read_csv('./train1000.csv')
test = pd.read_csv('./test1000.csv')
sample_submission = pd.read_csv('./sample_submission.csv')

# print basic info
print(train.shape)
print(test.shape)

train.info()

train.dropna(inplace=True)
test.info()

train.head()

train.describe()
















