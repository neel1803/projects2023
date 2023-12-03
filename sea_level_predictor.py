import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import unittest
def draw_plot():
  # Read data from file
  df = pd.read_csv("./epa-sea-level.csv", float_precision="legacy").rename(
      columns={
          "Year": "year",
          "CSIRO Adjusted Sea Level": "sea",
      }
  )
  plt.figure(1, figsize=(16, 9))
  plt.scatter(df["year"], df["sea"])
  regress = linregress(df["year"], df["sea"])
  last_year = df["year"].max()
  df = pd.concat([df, pd.DataFrame([{"year": y} for y in range(last_year + 1, 2050)])])
  plt.plot(
      df["year"],
      regress.intercept + regress.slope * df["year"],
      c="r",
      label="fit all",
  )
  df_recent = df.loc[(df["year"] >= 2000) & (df["year"] <= last_year)]
  bestfit = linregress(df_recent["year"], df_recent["sea"])
  df_recent = pd.concat([df_recent, pd.DataFrame(
      [{"year": y} for y in range(last_year + 1, 2050)])])
  plt.plot(
      df_recent["year"],
      bestfit.intercept + bestfit.slope * df_recent["year"],
      c="b",
      label="fit recent",
  )
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")

  return plt.gca()
