from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np


"""
연습중
"""
import os

if os.name == 'nt':
    font_family = "Malgun Gothic"
else:
    font_family = "AppleGothic"
    
sns.set(font=font_family, rc={"axes.unicode_minus" : False })

from IPython.display import set_matplotlib_formats

set_matplotlib_formats("retina")
