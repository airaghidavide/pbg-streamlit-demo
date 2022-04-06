import altair as alt

def make_heatmap(df,anno):
    heatmap = alt.Chart(df[(df.review_date == anno)] ).mark_rect().encode(
    alt.X('cocoa_percent',scale=alt.Scale(zero=False),bin=True),
    alt.Y('rating',bin=True),
    alt.Tooltip(['count()','cocoa_percent','rating','rating_value']),
    alt.Color('rating_value', scale=alt.Scale(scheme='browns')),
).properties(
    title='Conteggio in relazione a percentuale di cacao e rating per '+ str(anno)
)
    return heatmap