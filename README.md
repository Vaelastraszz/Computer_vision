# Computer_vision

Ce repository contient les fichiers ci dessous :
- Le notebook avec toutes les procédures d'entraînement sur le dataset fourni
- Le modèle sous format h5 entrainé et stoppé en checkpoint durant l'entraînement
- Un script pour extraire les labels à partir des json envoyés 
- Un script pour récupérer une image en path et faire une prédiction avec le modèle
- une image test
- les plot durant l'entraînement

# Comment exécuter le code

- Installer les librairies du script
- Entrer les deux chemins du modèle et de l'image selon ou vous enregistrez
- exécuter le main

# Détails de l'entrainement

- Génération des labels grace au script réalisé
- Génération du dataset à partir des chemins des images et des labels créés
- Undersapling et équilibrage du dataset
- Splitting de manière stratifié du dataset train,validation,test
- Récupération du modèle Xception
- Création de generateurs et de data augmentation 
- Freezing des couches de convolutions
- Initialisation du modèle (optimizer, early stopping, FC Layers, dropout,loss, Batch Normalization...)
- 1 er entrainement du modèle sur les couches fully connected uniquement (warm up du modèle)
- Plotting de training acc, val acc, train loss, val loss
- Unfreezing des couches de convulutions
- diminution du learning rate de /10
- On réentraine le modèle en fine-tuning
- Optimisation du treshold tpr/fpr
- Evaluation du modèle sur le test generator
- Creation de la méthode has_tomatoes
- NB : On préfèrera mettre en avant un recall fort sur le modèle pour éviter le plus possible de tomber sur un produit allergène lors de la prédiction

# Credits

- Médium blog sur le fine tuning
- Une méthode pour plot la courbe ROC que je n'ai pas utilisé au final :)

