# NSPPolls

Ce projet a pour but de compiler les sondages produits à l'occasion des élections régionales et présidentielles en France et de les remettre en contexte. 

# À propos des sondages


# Compilation des sondages

## Chiffres collectés

Sont rassemblés ici les sondages ayant traits aux élections présidentielle et régionales demandant des *intentions de vote*, soit les sondages répondant à la question « Si le premier tour avait lieu dimanche, pour qui voteriez-vous », ou approchant. Ne sont pas compilés les souhaits de victoire, les chances de l'emporter ou les prédictions. 

Pour chaque sondage est répertorié le nombre de personne ne donnant aucun avis, ou déclarant vouloir voter blanc ou nul. 

## Notes sur la méthodologie

* Seuls les sondages ayant été publiés sont compilés ici. Faute d'exhaustivité, il faut donc prendre avec précaution les interprétations sur les commandaitaires. 
* Le ou les partis des têtes de listes ou des candidat·es ne sont pas toujours précisés dans les sondages compilés. Si un ou plusieurs partis sont précisés, nous les avons renseignés tels que. Si rien n'est précisé, nous avons indiqué le parti de rattachement de la tête de liste ou des candidat·es. En revanche, quand aucune tête de liste n'est précisée, la case reste vide, et seul le parti (ou positionnement politique) est indiqué.
* Le calcul des marges d'erreurs, qui restent artificielles dans le cas de sondages avec la méthode par quota sont effectués sur les sous-échantillons des personnes ayant donné une intention de vote (soit les certain·es d'aller voter, soit les inscrit·es sur les listes, en fonction de ce qui est indiqué dans la colonne _population_).

## Élections régionales

Les élections régionales devraient avoir lieu en juin 2021 dans 17 territoires. Elles devraient se tenir le même jour que les élections départementales. Début mars 2021, les différentes têtes de listes n'étaient pas certaines, les sondages multiplient les hypothèses, mais la situation n'est pas encore stabilisée.

### Qu'est-ce qu'on peut faire avec ces sondages ?

Jusqu'au printemps 2021, la variété d'hypothèses rendent compliquées certaines analyses, notamment sur les têtes de liste à gauche, avec la multiplication des possibilités d'alliances ou d'incarnation. On peut noter cependant quelques évolutions personnelles au fil des mois, par exemple pour les présidents sortants, tels Valérie Pécresse ou Laurent Wauquiez.

S'ajoute également la faiblesse du corpus. Fin février, six sondages avaient été publiés pour la région Île-de-France, trois pour la région Nouvelle-Aquitaine, mais seulement deux ou moins dans toutes les autres régions, empêchant toute comparaison. Certaines régions n'ont pas vu de sondage publié officiellement, comme le Centre-Val-de-Loire ou la Corse, ou encore les outremers.

### Qui commande des sondages ?

Début mars, la grande majorité des sondages publiés dans la presse ont été commandés par des partis politiques, EE-LV et le Parti socialiste en tête. Sept sondages ont été commandés par des médias.

### Que valent les sondages nationaux ?

Il est coûteux de composer un panel de 1000 électeurs dans une région, et la tentation est grande d'extrapoler des résultats à partir d'une population naitonale, représentative. C'est ce que fait Opinion Way, dans [son enquête « RégioTrack »](https://www.opinion-way.com/fr/sondage-d-opinion/regiotrack2021.html) pour _Les Echos_ et Radio Classique. 

## Élection présidentielle

L'élection présidentielle devrait se dérouler au printemps 2022. Les candidat·es ne sont pas encore clairement connu·es, les différents sondages multiplient donc les hypothèses.

### Flux JSON disponibles

Des flux JSON proposant l'ensemble des données compilées sont disponibles sous licence MIT ci-dessous. Si vous utilisez les chiffres, veuillez s'il vous plaît les créditer, et faire un lien vers NSPPolls.

L'architecture est plutôt simple et se décline par région (dans le cas des élections régionales), puis par sondage, par tour, par hypothèse et par candidat.

Les fichiers seront remis à jour dans la foulée de l'ajout d'une notice de sondage sur le site de la Commission des sondages, ou si on en obtient par d'autres moyens.

* [Élections régionales – toutes les régions](./regionales.json)
** [Île-de-France](./regionales_IDF.json)
** [Provence-Alpes-Côte-d'Azur](./regionales_PACA.json)
** [Auvergne-Rhône-Alpes](./regionales_ARA.json)
** [Normandie](./regionales_N.json)
** [Nouvelle-Aquitaine](./regionales_NA.json)
** [Hauts-de-France](./regionales_HDF.json)
** [Occitanie](./regionales_OCC.json)
** [Pays de la Loire](./regionales_PDL.json)
** [Bretagne](./regionales_B.json)
** [Grand Est](./regionales_GE.json)
* [Élection présidentielle](./presidentielle.json)


