# Myfirst-AI-project-Star-Wars
Dans la bordure extérieure, un satellite non identifié a été repéré dans le ciel autour de la planète
Tatouine se déplaçant en orbite haute à très grande vitesse constante. Les analystes de l’alliance
sont sur le coup. Ce satellite ne répond à aucune injonction; le premier problème est d’éviter toute
collision entre ce satellite et la flotte de satellites de l’alliance déjà en opération. Mais surtout, il
s’agit de se préparer à une destruction imminente du satellite par un tir de plasma pulsé.
Malheureusement, au sol, l’énergie nécessaire à son atomisation est trop limitée et un seul tir
sera possible. Vous n’avez donc pas le droit à l’erreur. Il va falloir préparer ce tir au mieux avec les
rares moyens disponibles.
Le satellite suit une orbite dı̂te de Lissajous 1 définit comme suit:
x(t) = p 1 × sin(p 2 × t + p 3 )
y(t) = p 4 × sin(p 5 × t + p 6 )
Avec x(t) et y(t) la position du satellite à un instant t donnée. Les p i , i ∈ [1; 6] sont les paramètres
qu’il va falloir découvrir afin de pouvoir anticiper au mieux les mouvements du satellite à un instant
t donné (t ∈ [0; 2π]).
A l’aide de lunettes à visée laser, la rébellion a pu relever avec une certaine précision la position
du satellite à plusieurs instants. Cette liste vous est fournie dans le fichier position sample.csv
2
Plan d’action
Afin de réussir la mission, vous allez devoir déployer un algorithme génétique capable de trouver
une bonne combinaison de paramètres expliquant au mieux la trajectoire du satellite. Afin de
restreindre la recherche, nous allons supposer que chaque paramètre est compris entre [−100; 100].
En parallèle de votre programme, vous devrez fournir un rapport expliquant vos différents choix:
1 https://fr.wikipedia.org/wiki/Orbite_de_Lissajous
11. Quelle est la taille de l’espace de recherche (utiliser une notation scientifique)?
2. Quelle est votre fonction fitness?
3. Décrivez les opérateurs mis en œuvre (mutation, croissement)?
4. Décrivez votre processus de sélection.
5. Quel est la taille de votre population, combien de générations sont nécessaires avant de con-
verger vers une solution stable?
6. Combien de temps votre programme prend en moyenne (sur plusieurs runs)?
7. Si vous avez testé différentes solutions qui ont moins bien fonctionnées, décrivez-les et discutez-
les.
Merci de recopier chacune des questions ci-dessus dans votre rapport précédant chacune de vos
réponses (en respectant leur numérotation).
3
Protocole
Vous devrez fournir votre rapport (au format PDF), votre programme ainsi que votre combinaison
trouvée, le tout sur DVO pour le 25 mars. Vous êtes libre d’utiliser le langage de votre choix (mais
il est recommandé d’utiliser Python). Ce projet est un travail individuel.
Pour vous mettre sur un pied d’égalité en terme de ressource de calcul, vous pouvez utiliser
Google Colab: https://colab.research.google.com. Celui-ci est gratuit est nécessite unique-
ment un compte gmail.
Pour simplifier le travail d’évaluation, des dépôts séparés seront crées. Un dépôt pour votre
rapport et votre programme et un dépôt pour votre solution. Votre solution devra respecter le
format spécifique suivant (Tout écart à ce format sera pénalisé): chaque paramètre devra être
séparé par un point-virgule le tout sauvegardé dans un fichier à l’extension txt. Le nom du fichier
sera composé de votre nom, prénom et groupe séparés par un underscore: Un exemple de fichier
solution est donnée en annexe.
