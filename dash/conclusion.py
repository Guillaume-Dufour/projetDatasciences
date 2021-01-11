import dash_html_components as html

content = html.Div([
    html.H4("Conclusion"),
    html.P(
        "Cette analyse nous a permis de montrer que contrairement à ce que l’on pourrait penser, il n’y a pas de type "
        "d’employés qui envoie plus de mails que d’autres (exemple: les personnes hautes placées délèguent cette "
        "tâche aux personnes en dessous dans la hiérarchie). En effet, il n’y a pas de lien entre le poste occupé par "
        "les employés et le nombre de mails qu’ils envoient et reçoivent.",
        style={'marginBottom': 20}
    ),
    html.P(
        "Concernant le temps de réponse, il semblait à première vue qu’il ne dépendait pas du type de poste. "
        "Cependant nous avons vu qu’il y avait des extrêmes, des personnes qui mettent plus d’un mois à répondre, "
        "ce qui n’est pas réaliste. Avec des données plus « sensées » nous montrons un lien entre ces deux variables. "
        "Nous voyons par exemple que les externes répondent plus vite que les associés.",
        style={'marginBottom': 20}
    ),
    html.P(
        "Finalement, nous avons remarqué que les personnes appartenant au même type de poste parlaient "
        "majoritairement entre elles et que les exécutifs sont légèrement exclus de la communication avec les autres "
        "types de poste. De plus, les associés et les employés communiquent beaucoup entre eux et peu avec les "
        "managers. Enfin, les externes communiquent majoritairement avec les associés, les employés et les managers "
        "mais pas du tout avec l'exécutif.",
        style={'marginBottom': 30}
    ),
    html.H4("Nos impressions sur le projet"),
    html.P(
        "Nous avons eu du mal à commencer le projet car nous ne trouvions pas de problématique à analyser.",
        style={'marginBottom': 20}
    ),
    html.P(
        "Nous avons eu des difficultés concernant le traitement des données. Nous ne comprenions pas la signification "
        "de certaines colonnes du csv, nous avons donc dû faire un choix sur la sélection de ces dernières. Nous "
        "avons donc décidé de les supprimer et avons fait de même avec les doublons. Une fois le csv “propre”, "
        "nous n’étions pas satisfait du nombre de mails que nous avions. En effet, nous sommes partis d’un csv qui ne "
        "contenait qu’un échantillon du dataset Enron. Nous avons donc décidé de récupérer le dossier complet des "
        "mails pour pouvoir réaliser nos analyses sur un plus grand échantillon. Cela a été une autre difficulté.",
        style={'marginBottom': 20}
    ),
    html.P(
        "Une fois le dataset propre et complet, nous avons commencé à réfléchir sur la manière de l’analyser en "
        "accord avec notre sujet. Nous tenions à faire des analyses en nous basant sur le niveau du poste de la "
        "personne au sein de l’entreprise. Cependant, nous n’avions aucun moyen simple d’avoir cette donnée pour tous "
        "les employés. Nous avons donc dû approfondir les recherches pour au final trouver, dans une librairie de R, "
        "un graphe de données comportant les emplois ainsi qu’un markdown à suivre pour rendre ce dernier  "
        "exploitable. Ceci nous a grandement débloqué dans notre avancement.",
        style={'marginBottom': 20}
    ),
    html.P(
        "Nous avons eu une autre difficulté au moment où nous avons dû trouver une librairie pour effectuer une AFC. "
        "Les deux librairies que nous avions choisies (fanalysis et Prince) ne permettent pas d’afficher les "
        "graphiques sur l’application Dash. Nous avons donc trouvé le moyen de nous même faire les différents "
        "diagrammes ainsi que les différents tableaux afin de présenter les résultats du mieux possible. De plus, "
        "la librairie que nous avons finalement utilisée (Prince) ne nous permettait pas, à notre connaissance, "
        "de retourner les contributions absolues et relatives de nos modalités.",
        style={'marginBottom': 20}
    ),
    html.P(
        "Finalement, nous sommes un peu déçus des conclusions auxquelles nous sommes arrivés. Nous nous attendions à "
        "des résultats plus marqués que ce que nous avons obtenus.",
        style={'marginBottom': 20}
    )
])
