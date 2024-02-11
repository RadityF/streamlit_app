import streamlit as st
import pickle
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from pathlib import Path
import os


#lowercase words
def lowercase(str_text):
   return str_text.lower()

#normalize words
norm = {" dgn " : " dengan ", " gue ": " saya ", " dgn ":" dengan ", "bgmn ":" bagaimana ", ' tdk':' tidak ', ' blum ':' belum ', 'mantaaaaaaaappp':' bagus ', ' josss ':' bagus ', ' thanks ': ' terima kasih ', 'fast':' cepat ', ' dg ':' dengan ', 'trims':' terima kasih ', 'brg':' barang ', 'gx':' tidak ', ' dgn ':' dengan ', ' recommended':' rekomen ', 'recomend':' rekomen ', 'good':' bagus '}

def normalisasi(str_text):
  for i in norm:
    str_text = str_text.replace(i, norm[i])
  return str_text

#stop words
more_stop_words = []

stop_words = StopWordRemoverFactory().get_stop_words()
new_array = ArrayDictionary(stop_words)
stop_words_remover_new = StopWordRemover(new_array)

def stopword(str_text):
  str_text = stop_words_remover_new.remove(str_text)
  return str_text

#tokenized
def tokenized(str_text):
   str_text.split()

#masukkan tokenized ke stemming

#stemming 
def stemming(Ulasan):
  factory = StemmerFactory()
  stemmer = factory.create_stemmer()
  do = []
  for w in Ulasan:
    dt = stemmer.stem(w)
    do.append(dt)
  d_clean = []
  d_clean = " ".join(do)
  return d_clean

def text_processing(str_text):
    # Lowercase
    str_text = lowercase(str_text)
    # Normalisasi
    str_text = normalisasi(str_text)
    # Menghapus stop words
    str_text = stopword(str_text)
    # Tokenisasi
    tokens = tokenized(str_text)
    # Stemming
    stemmed_tokens = tokens.apply(stemming)
    return " ".join(stemmed_tokens)

model_vektor = "C:\samber\batch_1\streamlit_data_app\app\tfidf.pkl"
model_NB = 'C:\samber\batch_1\streamlit_data_app\app\nb.pkl'
# Load pickled files
with open(model_vektor, 'rb') as tfidf_file:
    tfidf = pickle.load(tfidf_file)

with open(model_NB, 'rb') as nb_file:
    nb = pickle.load(nb_file)


def main():
    st.title('REVIEW TOKOPEDIA SENTIMEN ANALYSIS CHECKER')

    ulasan = st.text_area('silahkan input ulasan')

    if st.button('submit'):
       if ulasan:
          clean_ulasan = text_processing(ulasan)
          #ulasan 
          vektor_ulasan = tfidf.transform(clean_ulasan)
          predict_ulasan = nb.predict(vektor_ulasan)
          hasil_sentimen = 'Positif' if predict_ulasan[0] == 1 else 'Negatif'
          st.write('Sentimen Ulasan:', hasil_sentimen)

if __name__ == '__main__':
    main()


