import dash_table
import dash_html_components as html
import dash_core_components as dcc

content = html.Div([
    html.H4("Conclusion"),
    html.P(
        "Cette analyse nous a permis de montrer que contrairement à ce que l’on pourrait penser, il n’y a pas de type d’employés qui envoie plus de mails que d’autres (exemple: les personnes hautes placées délèguent cette tâche aux personnes en dessous dans la hiérarchie). En effet, il n’y a pas de lien entre le poste occupé par les employés et le nombre de mails qu’ils envoient et reçoivent.",
        style={'marginBottom': 20}
    ),
    html.P(
        "Concernant le temps de réponse, il semblait à première vue qu’il ne dépendait pas du type de poste. Cependant nous avons vu qu’il y avait des extrêmes, des personnes qui mettent plus d’un mois à répondre, ce qui n’est pas réaliste. Avec des données plus « sensées » nous montrons un lien entre ces deux variables. Nous voyons par exemple que les externes répondent plus vite que les associés.",
        style={'marginBottom': 20}
    ),
    html.P(
        "Finalement, nous avons remarqué que les personnes appartenant au même type de poste parlaient majoritairement entre elles et que les exécutifs sont légèrement exclus de la communication avec les autres types de poste. De plus, les associés et les employés communiquent beaucoup entre eux et peu avec les managers. Enfin, les externes communiquent majoritairement avec les associés, les employés et les managers mais pas du tout avec l'exécutif.",
        style={'marginBottom': 30}
    ),
    html.H4("Nos impressions sur le projet"),
    html.P(
        "Nous avons eu du mal à commencer le projet car nous ne trouvions pas de problématique à analyser.",
        style={'marginBottom': 20}
    ),
    html.P(
        "P2",
        style={'marginBottom': 20}
    ),
    html.P(
        "P3",
        style={'marginBottom': 20}
    ),
    html.P(
        "P4",
        style={'marginBottom': 20}
    ),
    html.P(
        "P5",
        style={'marginBottom': 20}
    ),
    html.P(
        "P6",
        style={'marginBottom': 20}
    ),

])
