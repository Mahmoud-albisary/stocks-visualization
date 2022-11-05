from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.resources import CDN
start = datetime.datetime(2020, 1, 20)
end = datetime.datetime(2020, 8, 7)

df = data.DataReader(name ="AAPL", data_source = "yahoo", start = start, end = end)

def which(o, c):
    if c > o:
        return "Increase"
    elif o > c:
        return "Decrease"
    else:
        return "Equal"

df["Status"] = [which(o, c) for o, c in zip(df.Open, df.Close)]
df["Middle"] = (df.Open + df.Close)/2
df["Difference"] = abs(df.Open - df.Close)
print(df)
p = figure(x_axis_type = "datetime", plot_width=2000, plot_height=1000)
p.grid.grid_line_alpha = 0.3
p.segment(df.index[df.Status == "Increase"],df.High[df.Status == "Increase"]
,df.index[df.Status == "Increase"], df.Low[df.Status == "Increase"], color = "Black")

p.segment(df.index[df.Status == "Decrease"],df.Low[df.Status == "Decrease"]
,df.index[df.Status == "Decrease"], df.High[df.Status == "Decrease"], color = "Black")
p.rect(df.index[df.Status == "Increase"],df.Middle[df.Status == "Increase"], 12*60*60*1000
, df.Difference[df.Status == "Increase"], fill_color = "green", line_color = "black")

p.rect(df.index[df.Status == "Decrease"],df.Middle[df.Status == "Decrease"], 12*60*60*1000
, df.Difference[df.Status == "Decrease"], fill_color = "red", line_color = "black")


show(p)
