import dash_html_components as html

introduction = html.Div([
    html.H4("Présentation du projet"),
    html.Div([
        html.P(
            "Bonjour à tous, nous sommes un groupe de 4 composé de TEROITIN Marine, COUPRIE Aymeric, DUFOUR Guillaume "
            "et TRIBOT Mathilde.",
            style={'marginBottom': 20}),
        html.P("Pour réaliser ce projet, nous avons récupéré les mails échangés par les employés de la société Enron.",
               style={'marginBottom': 20}),
        html.P("Ces données vont nous permettre d’analyser la dynamique des échanges entre les différentes personnes.",
               style={'marginBottom': 20}),
        html.P(
            "Nous avons décidé de recentrer notre étude sur les postes des employés afin de traiter le sujet plus en "
            "profondeur. Nous nous sommes demandés si le poste avait une influence sur le temps de réponse et s’ils "
            "avaient une influence sur les personnes avec qui ils communiquent.",
            style={'marginBottom': 20})
    ]),
    html.Br(),
    html.H4("Méthodologie appliquée durant le projet"
            ),
    html.Div([
        html.P(
            "Dans cette partie, nous allons présenter les méthodes générales utilisées pour analyser ce projet ainsi "
            "que notre organisation globale.",
            style={'marginBottom': 30}
        ),

        html.H5("Découverte des données"),

        html.P(
            "Nous avons dans un premier temps récupéré le csv contenant les données incomplètes et nous avons essayé "
            "de nous familiariser avec le nom des variables. Certaines nous ont posé problème: cat_level et "
            "cat_weight. Nous avons ensuite récupéré les données brutes complètes et créé un algorithme pour pouvoir "
            "créer un csv avec ces données. Après de longues recherches, nous avons trouvé une librairie R contenant "
            "le job des employés.",
            style={'marginBottom': 20}
        ),

        html.H5("Nettoyage des données"),

        html.P(
            "Une fois que nous avons créé le csv à partir de tous les dossiers de tous les employés d’Enron (mails "
            "bruts), nous avons remarqué qu’il y avait des doublons dans les mails. En effet, certains étaient en "
            "plusieurs exemplaires car ils étaient présents dans plusieurs dossiers d’un employé. Nous avons donc "
            "supprimé tous ces doublons en fonction de trois champs : l’expéditeur (from), le destinataire (to) et la "
            "date d’envoi du mail (date). ",
            style={'marginBottom': 20}
        ),
        html.P(
            "Ensuite lorsque nous avons commencé notre analyse, nous avons remarqué que les mails avant 1999 ou après "
            "2003 étaient très rares et souvent des mails automatiques. Nous avons donc choisi de les ignorer lors "
            "des analyses.",
            style={'marginBottom': 20}
        ),
        html.P(
            "Lorsque nous avons calculé le temps de réponse, nous avons trouvé que certaines réponses étaient "
            "envoyées avant le mail d’origine, probablement dû au décalage horaire qui n’est pas noté dans l'horaire "
            "du mail de réponse. Nous avons donc supprimé ces mails pour réaliser les analyses. Nous avons également "
            "supprimé toutes les données pour lesquelles les dates avaient un format atypique que nous ne pouvions "
            "pas traiter. Il nous restait donc 8 235 mails à analyser sur les 57 306 mails ayant une réponse.",
            style={'marginBottom': 30}
        ),

        html.H5("Création de données supplémentaires"),

        html.P(
            "Afin de réaliser nos analyses, nous avions besoin de rajouter de nouvelles données dans le csv. Nous "
            "avons donc rajouté les colonnes suivantes : year, month, weekDay et hour en utilisant le champ ‘date’ "
            "déjà existant afin de pouvoir les regrouper par catégorie.",
            style={'marginBottom': 20}
        ),
        html.P(
            "Nous avons aussi calculé le temps de réponse pour chaque mail qui est une réponse (mail dont le corps "
            "contient le texte suivant : “-Original Message-”) afin de pouvoir l’analyser.",
            style={'marginBottom': 20}
        ),
        html.P(
            "Nous avons aussi trouvé une librairie sur R contenant la description des jobs avec le nom des personnes correspondant, que nous avons fusionné avec notre csv contenant toutes les données. Pour ce qui est du job 'externe' nous avons réalisé un algorithme qui récupère tous ceux qui n’ont pas une adresse mail contenant “@enron”."
        )
    ])
])
