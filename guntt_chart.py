import plotly.express as px
import plotly.io as pio
import pandas as pd
import datetime 

dt = datetime.datetime(2021,11,1,9)
df = pd.DataFrame([
    dict(Task="Worker1", Start= dt, Finish= dt + datetime.timedelta(minutes = 20),resource = "Machine1",job = "JOB1"),
    dict(Task="Worker2", Start=dt + datetime.timedelta(minutes = 20), Finish= dt + datetime.timedelta(minutes = 40),resource = "Machine2",job = "JOB2"),
    dict(Task="Worker3", Start=dt + datetime.timedelta(minutes = 40), Finish= dt + datetime.timedelta(minutes = 60),resource = "Machine3",job = "JOB3")
])
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task",color = "resource",text = "job",title = "guntt chart")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
pio.write_html(fig,file="graduation-thesis/guntt-chart.html")