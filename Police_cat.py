import pandas as pd
import numpy as np
import argparse
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer


# Coseine similarity for sentence comparison
def cos_sim (A,B):
  return np.dot(A,B)/(norm(A)*norm(B))


# Base sentence for classify
df = pd.read_excel('Policia_Cat.xlsx')

sentences = [item for row in df.values for item in row]

def encode_DB(sentences):
  model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')
  embeddings = model.encode(sentences)
  return model,embeddings

def embed_sentence(model, sentence):
  return model.encode(sentence)


def best_similarity(input, embeddings,best_k:int):
  #Get cosine similarity of all sentences, sort and extract best 5
  similarity = [cos_sim(input,x) for x in embeddings]
  ind = np.argsort(similarity)[-best_k:]
  ind[:] = ind[::-1]
  return ind

def most_similar_class(ind, df, sentences):
  #With the most similar get the class (Column name)
  for col in df.columns:
      if sentences[ind[0]] in df[col].values:
          return col
  return "No identificado"