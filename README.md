# Police_Similitud
Este algoritmo busca el poder clasificar texto proveniente de las llamadas a la policia por medio de frases que se enmarcan en cada categoria y la similitud semantica de estas.

## Requisitos
Se nesesita python, crear un ambiente e instalar las libreriass del **requirements.txt** con el siguiente codigo

`pip install -r requirements.txt`

## Uso
Se usa por medio del notebook **Sentense_similarity.ipynb** el cual utiliza las frases pre configuradas en el archivo **Policia_cat.xlsx** y extrae las 5 mas similares en comparacion a la frase que se ingreso en la variable `prueba`, aun esta version no categoriza.

Tambien puede ejecutarlo por medio del comando: 

`python Police_cat.py --f "la frase que desea probar"`

y este devolvera la categoria de la mas similar.


## Uso SaaS

para este se debe ejecutar

`streamlit run streamlit2.py`

de esta forma la aplicación empieza a ejecutarse como un FE

