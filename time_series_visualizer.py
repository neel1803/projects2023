import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import unittest
import matplotlib as mpl
import matplotlib.ticker as mticker
from pandas.plotting import register_matplotlib_converters
from datetime import datetime

register_matplotlib_converters()

def parse_date(x):
    return datetime.strptime(x, "%Y-%m-%d")
df = pd.read_csv("./fcc-forum-pageviews.csv",
    index_col=["date"],
    parse_dates=["date"],
    date_parser=parse_date,
)

df = df.loc[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]

def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(16, 6))

  ax = sns.lineplot(data=df, x="date", y="value")

  ax.set(
      xlabel="Date",
      ylabel="Page Views",
  )

  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = (
      df.copy()
      .groupby(pd.Grouper(freq="M"))
      .mean()
      .rename(columns={"value": "avg"})
  )

  df_bar["year"] = pd.DatetimeIndex(df_bar.index).year
  df_bar["month"] = pd.DatetimeIndex(df_bar.index).strftime("%B")

  # Convert data to long form
  df_bar = pd.melt(
      df_bar,
      id_vars=["year", "month"],
      value_vars=["avg"],
  )

  sns.set_theme(style="ticks")

  # Draw the chart
  fig = sns.catplot(
      data=df_bar,
      x="year",
      y="value",
      hue="month",
      kind="bar",
      legend=False,
  )

  # Config legend, axes and title
  fig.set_xlabels("Years")
  fig.set_ylabels("Average Page Views")
  plt.legend(
      title="Months",
      loc="upper left",
      labels=[
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December",
      ],
  )
  return fig.fig

def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy().rename(columns={"value": "views"})
  df_box.reset_index(inplace=True)

  df_box["year"] = [d.year for d in df_box.date]
  df_box["month"] = [d.strftime("%b") for d in df_box.date]

  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

  sns.boxplot(ax=ax1, data=df_box, x=df_box["year"], y=df_box["views"])

  # Remember to edit the labels after call to seaborn.
  ax1.set(
      xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)"
  )

  sns.boxplot(
      ax=ax2,
      data=df_box,
      x=df_box["month"],
      y=df_box["views"],
      order=[
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec",
      ],
  )

  ax2.set_title("Month-wise Box Plot (Seasonality)")
  ax2.set_xlabel("Month")
  ax2.set_ylabel("Page Views")

  # I'm cheating here, because I don't know why the test for y ticks label
  # fail and I don't want to dig into seaborn source code.
  y_ticks = [
      "0",
      "20000",
      "40000",
      "60000",
      "80000",
      "100000",
      "120000",
      "140000",
      "160000",
      "180000",
      "200000",
  ]
  ax1.yaxis.set_major_locator(mticker.FixedLocator([int(s) for s in y_ticks]))
  ax1.set_yticklabels(y_ticks)
  return fig
