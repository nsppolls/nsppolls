# NSPPolls

➡️ [Le flux JSON des sondages pour l'élection présidentielle](https://raw.githubusercontent.com/nsppolls/nsppolls/master/presidentielle.json)

➡️ [Le fichier CSV des sondages pour l'élection présidentielle](https://raw.githubusercontent.com/nsppolls/nsppolls/master/presidentielle.csv)

➡️ [Suivez-nous sur Twitter](http://twitter.com/nsppolls)

Ce projet a pour but de compiler les sondages produits à l'occasion des élections régionales et présidentielle en France et de les remettre en contexte. 

1. [À propos des sondages](#a-propos-des-sondages)
  - [Pourquoi les notes sont publiées ?](#pourquoi-les-notes-sont-publiées)
  - [Élections présidentielle](#élection-présidentielle)
2. [Compilation des sondages](#compilation-des-sondages)
  - [Flux JSON disponibles](#flux-json-disponibles)
3. [Bonus](#bonus)

Retrouvez-nous sur les réseaux sociaux, sur [Twitter](https://twitter.com/nsppolls), où nous postons notre veille et des infos sur les mises à jour du fichier, et [Medium](https://medium.com/nsppolls), pour des articles non réguliers.

Pour des questions ou des demandes : [contact@nsppolls.fr](mailto:contact@nsppolls.fr)

# À propos des sondages

## Pourquoi les notes sont publiées ?

La publication des sondages d'intentions de vote est encadrée depuis 1977. En 2016 est prévu que la première publication d'un sondage soit accompagnée de mentions obligatoires, et que soit mis en ligne [sur le site de la commission des sondages](http://www.commission-des-sondages.fr/notices/) une notice précisant, notamment, la méthode d'interrogation et le nombre de personnes ne s'étant pas exprimées.

<!--## Élections régionales

Les élections régionales devraient avoir lieu en juin 2021 dans 17 territoires. Elles devraient se tenir le même jour que les élections départementales. Début mars 2021, les différentes têtes de listes n'étaient pas certaines, les sondages multiplient les hypothèses, mais la situation n'est pas encore stabilisée.

Si aucune liste n'obtient la majorité absolue au premier tour, les listes qui recueillent plus de 10% des suffrages exprimés peuvent se qualifier pour le second tour. Celles qui recueillent entre 5% et 10% peuvent fusionner avec d'autres listes en vue du second tour. Pour l'assemblée de Corse, le seuil de maintien au second tour est abaissé à 7 %.

### Qu'est-ce qu'on peut faire avec ces sondages ?

Jusqu'au printemps 2021, la variété d'hypothèses rendent compliquées certaines analyses, notamment sur les têtes de liste à gauche, avec la multiplication des possibilités d'alliances ou d'incarnation. On peut noter cependant quelques évolutions personnelles au fil des mois, par exemple pour les présidents sortants, tels Valérie Pécresse ou Laurent Wauquiez.

S'ajoute également la faiblesse du corpus. Fin février, six sondages avaient été publiés pour la région Île-de-France, trois pour la région Nouvelle-Aquitaine, mais seulement deux ou moins dans toutes les autres régions, empêchant toute comparaison. Certaines régions n'ont pas vu de sondage publié officiellement, comme le Centre-Val-de-Loire ou la Corse, ou encore les outremers.

### Que valent les sondages nationaux ?

Il est coûteux de composer un panel de 1 000 électeurs pour chaque région, et la tentation est grande d'extrapoler des résultats à partir d'une population naitonale, représentative. C'est ce que fait Opinion Way, dans [son enquête « RégioTrack »](https://www.opinion-way.com/fr/sondage-d-opinion/regiotrack2021.html) pour _Les Echos_ et Radio Classique. Les questions de ce sondage sont adaptées à la région d'origine de la personne interrogée pour les têtes de listes seulement. 5 000 personnes sont interrogées.

> « La modélisation calcule, à partir de la structure démographique et politique de chaque électorat, le score potentiel de chaque force politique dans les 12 régions métropolitaines hors Corse. Il en déduit la configuration probable du second tour dans chaque région, puis, à l’aide de matrices de reports de voix basées sur les résultats de l’enquête, le résultat le plus probable au second tour ce qui permet d’identifier à ce jour le favori pour remporter la région en juin. »

Cette méthodologie repose sur de nombreuses hypothèses, que ce soit pour les alliances, ou le maintien au second tour. En l'état actuel, aucun intervalle de confiance n'est donné par Opinion Way, pas plus qu'une quantification du rapport de force. Ces résultats, surtout pour le second tour, sont donc à prendre avec précaution.-->

## Élection présidentielle

L'élection présidentielle devrait se dérouler au printemps 2022. Les candidat·es ne sont pas encore tous·tes connu·es, les différents sondages multiplient donc les hypothèses.

# Compilation des sondages

## Indicateurs collectés

Sont rassemblés ici les sondages ayant traits aux élections présidentielle et régionales demandant des *intentions de vote*, soit les sondages répondant à la question *« Si le premier tour avait lieu dimanche, pour qui voteriez-vous ? »*, ou approchant. Ne sont pas compilés les souhaits de victoire, les chances de l'emporter ou les prédictions. 

Pour chaque sondage est répertorié le nombre de personne ne donnant aucun avis, ou déclarant vouloir voter blanc ou nul. 

## Notes sur la méthodologie

* Seuls les sondages ayant été publiés sont compilés ici. Faute d'exhaustivité, il faut donc prendre avec précaution les interprétations sur les commandaitaires. 
* Le ou les partis des têtes de listes ou des candidat·es ne sont pas toujours précisés dans les sondages compilés. Si un ou plusieurs partis sont précisés, nous les avons renseignés tels que. Si rien n'est précisé, nous avons indiqué le parti de rattachement de la tête de liste ou des candidat·es. En revanche, quand aucune tête de liste n'est précisée, la case reste vide, et seul le parti (ou positionnement politique) est indiqué.
* Le calcul de l'intervalle de confiance, qui reste artificiel dans le cas de sondages avec la méthode par quota, est effectué sur les sous-échantillons des personnes ayant donné une intention de vote (soit les certain·es d'aller voter, soit les inscrit·es sur les listes, en fonction de ce qui est indiqué dans la colonne *population*).

## Flux JSON disponibles

Des flux JSON proposant l'ensemble des données compilées sont disponibles sous licence MIT ci-dessous. Si vous utilisez les chiffres, veuillez s'il vous plaît les créditer, et faire un lien vers NSPPolls.

L'architecture est plutôt simple et se décline par région (dans le cas des élections régionales), puis par sondage, par tour, par hypothèse et par candidat.

Les fichiers seront remis à jour dans la foulée de l'ajout d'une notice de sondage sur le site de la Commission des sondages, ou si on en obtient par d'autres moyens.

* [Élections régionales – toutes les régions](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales.json)
  * [Île-de-France](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_IDF.json)
  * [Provence-Alpes-Côte-d'Azur](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_PACA.json)
  * [Auvergne-Rhône-Alpes](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_ARA.json)
  * [Normandie](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_N.json)
  * [Nouvelle-Aquitaine](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_NA.json)
  * [Hauts-de-France](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_HDF.json)
  * [Occitanie](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_OCC.json)
  * [Pays de la Loire](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_PDL.json)
  * [Bretagne](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_BZH.json)
  * [Grand Est](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_GE.json)
  * [Centre-Val de Loire](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_CLV.json)
  * [Bretagne-Franche-Comté](https://raw.githubusercontent.com/nsppolls/nsppolls/master/regionales_BFC.json)
* [Élection présidentielle](https://raw.githubusercontent.com/nsppolls/nsppolls/master/presidentielle.json)

## Flux CSV

Un flux CSV est généré automatiquement à partir du fichier JSON, grâce à un script de Nicolas Mondon. Il reprend toutes les infos du JSON en affichant une ligne par intention de vote, détaillant le sondage, l'hypothèse, le candidat, etc.

* [Élection présidentielle (csv)](https://raw.githubusercontent.com/nsppolls/nsppolls/master/presidentielle.csv)

## Reprises

Les chiffres relatifs à l'élection présidentielle sont repris par plusieurs médias, dont [Le Figaro](https://www.lefigaro.fr/fig-data/sondages-programmes-candidats-discours-dates-deplacements-scrutin-20210906/), [Contexte](contexte.com/article/pouvoirs/agregateur-de-sondages-de-la-presidentielle-2022_128913.html), [The Guardian](https://www.theguardian.com/world/ng-interactive/2021/oct/25/french-election-polls-who-is-leading-the-race-to-be-the-next-president-of-france), [Le Télégramme](https://www.letelegramme.fr/elections/sondages/sondages-election-presidentielle-2022.php). Ils sont également repris sur d'autres sites comme [Datapolitics](https://datapolitics.fr/agregateur-sondages-presidentielle2022/) ou [datatracking.io](https://datatracking.io). 

# Bonus

Suivez les investitures aux élections législatives grâce à la compilation réalisée par NSPPolls ! [Un fichier CSV](https://github.com/nsppolls/nsppolls/blob/master/donnees/candidatures_legislatives.csv) reprend les candidatures annoncées, dans chaque circonscription. 

Pour l'instant, seul le parti Les Réplublicains a fait ses premières annonces. Le fichier sera amélioré au fil des annonces et du temps. Les élections législatives sont prévues pour le mois de juin 2022.

# Crédits

NSPPolls est proposé notamment par [Alexandre Léchenet](http://twitter.com/alphoenix). Pour des questions ou des demandes : [contact@nsppolls.fr](mailto:contact@nsppolls.fr)