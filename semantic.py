
## Code from Googles Semantic Encoder Toolkit



#@title Load the Universal Sentence Encoder's TF Hub module
from absl import logging

import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re
import seaborn as sns

module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/5" #@param ["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
model = hub.load(module_url)
print ("module %s loaded" % module_url)
def embed(input):
  return model(input)

# @A function to evaluate the semantic similarity of two sentences 
# @param v1, v2: 2 lists of strings with length 1 or greater
def semantic_similarity(v1, v2):
  embed_v1 = embed(v1)
  embed_v2 = embed(v2)
  return np.inner(embed_v1, embed_v2)

a = ["elephant"]
b = ["cheetah"]

print(semantic_similarity(a, b))