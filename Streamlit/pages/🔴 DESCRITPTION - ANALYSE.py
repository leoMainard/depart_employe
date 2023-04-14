import streamlit as st
from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# shapash pour l'interprétabilité des résultats


st.set_page_config(layout='wide')


data = pd.read_csv(r'./depart_employes.csv', sep=";")

# ----------------------------------------------------------------------- DESCRIPTION DES DONNEES
st.title('Description des données')
st.info('Objectif : comprendre le jeu de données.')



st.markdown('##### A travers notre fichier “depart_employes.csv” nous allons essayer d’expliquer et de prédire la variable “départ”.')
st.dataframe(data.head(10))
st.write("On a donc 9 variables explicatives et 1 variable à expliquer : depart. Cette variable prendre la valeur 0 si "
         "l'employé a quitté l'entreprise, 0 si ce n'est pas le cas")



st.markdown('***')
st.markdown('##### Regardons un peu nos données.')
st.dataframe(data.describe())

st.markdown("##### Etat des lieux")
st.markdown("Nous pouvons constater que :")
st.markdown("* Le nombre d'entrées est limité (14999 lignes)")
st.markdown("* Les variables sont des nombres décimaux, des entiers et des catégories")
st.markdown("* La description de data montre aussi qu'il n'y a à priori pas d'outliers")
st.markdown("A priori il n'y a donc pas de modifications importantes à réaliser avant de commencer à travailler.")


st.write("Nous aurions aussi pu afficher le graphique suivant pour visualiser notre jeu de données en entier, et visualiser"
         "les valeurs manquantes. Elles seraient affichées par une ligne blanche.")
fig = plt.figure(figsize=(10, 4))
sns.heatmap(data.isna(), cbar=False)
st.pyplot(fig)


st.markdown('***')
st.markdown("##### Quelle est la proportion de départ de maintient dans nos données ?")
proportion = data['depart'].value_counts(normalize=True)
prop1 , prop2 = st.columns(2)
prop1.metric('Employés qui restent', f"{round(proportion[0],2)}%")
prop2.metric('Employés qui partent', f"{round(proportion[1],2)}%")





# ----------------------------------------------------------------------- ANALYSE DES DONNEES
st.markdown('***')
st.title('Analyse des données')
st.info('Objectif : analyser le jeu de données, la distribution, leur relations.')

# La variable cible Y doit être de type binaire pour la Régréssion Logistique
data["target"] = data["depart"].astype('category')
data.drop("depart", axis=1,inplace=True)
positive_data= data[data['target']==1]
negative_data= data[data['target']==0]
col=list(data.columns)[:-1]
num_cols=list(data.columns)[:-3]
cat_cols=list(data.columns)[-3:-1]


st.markdown("##### Observons nos données numériques : ")
filtre_numerique = st.selectbox("Sélectionner une colonne numérique.", num_cols)

graph_num1, graph_num2 = st.columns(2)

fig_graphNum1 = plt.figure()
sns.distplot(positive_data[filtre_numerique], label='positive')
sns.distplot(negative_data[filtre_numerique], label='negative')
plt.legend()
graph_num1.pyplot(fig_graphNum1)


fig_graphNum2 = plt.figure()
sns.boxplot(data=data,y=filtre_numerique, x='target')
plt.legend()
graph_num2.pyplot(fig_graphNum2)

st.markdown('***')

