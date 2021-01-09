import plotly.graph_objects as go


def topSenders(df):
    top10 = df['from'].value_counts().nlargest(10)
    top10_count = top10.values
    top10_names = top10.index.tolist()

    fig = go.Figure(
        data=[go.Bar(
            x=top10_names,
            y=top10_count)],
        layout_title_text="top 10 des expéditeurs"
    )
    return fig

def topReceiver (df) :
    top10 = df['to'].value_counts().nlargest(10)
    top10_count = top10.values
    top10_names = top10.index.tolist()

    fig = go.Figure(
        data=[go.Bar(
            x=top10_names,
            y=top10_count)],
        layout_title_text="top 10 des destinataire"
    )
    return fig