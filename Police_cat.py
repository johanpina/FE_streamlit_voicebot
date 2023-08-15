import pandas as pd
import numpy as np
import argparse
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer

parser = argparse.ArgumentParser(description='Time series forecasting program')
parser.add_argument("--f", help="Sentence to compare with", default="me colabora que los vecinos hacen mucha bulla")
args = parser.parse_args()

# Coseine similarity for sentence comparison
def cos_sim (A,B):
  return np.dot(A,B)/(norm(A)*norm(B))

# Base sentence for classify
df = pd.read_excel('Policia_Cat.xlsx')
sentences = [item for row in df.values for item in row]

# Pretrained model on sentence similarity spanish
model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')
embeddings = model.encode(sentences)

#Embedding on the new sentence to compare
prueba = args.f
input = model.encode(prueba)

#Get cosine similarity of all sentences, sort and extract best 5
similarity = [cos_sim(input,x) for x in embeddings]
ind = np.argsort(similarity)[-5:]
ind[:] = ind[::-1]


#With the most similar get the class (Column name)
for col in df.columns:
    if sentences[ind[0]] in df[col].values:
        print(col)
