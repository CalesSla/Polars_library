---
jupyter:
  colab:
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

<div class="cell markdown" id="U08HDI2kOsSI">

# Polars quickstart

A quick overview of the polars library and the most common commands.

</div>

<div class="cell code" id="xIA3r4o0Mlrw">

``` python
# Import the library

import polars as pl
```

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:882}"
id="ITv_7P3LO7q3" outputId="532d9391-6204-41ac-9f23-9a5c170f22e0">

``` python
# Read a csv file

csv_file = 'Titanic.csv'
df = pl.read_csv(csv_file)
df
```

<div class="output execute_result" execution_count="10">

    shape: (891, 12)
    ┌─────────────┬──────────┬────────┬──────────────────┬───┬────────────┬─────────┬───────┬──────────┐
    │ PassengerId ┆ Survived ┆ Pclass ┆ Name             ┆ … ┆ Ticket     ┆ Fare    ┆ Cabin ┆ Embarked │
    │ ---         ┆ ---      ┆ ---    ┆ ---              ┆   ┆ ---        ┆ ---     ┆ ---   ┆ ---      │
    │ i64         ┆ i64      ┆ i64    ┆ str              ┆   ┆ str        ┆ f64     ┆ str   ┆ str      │
    ╞═════════════╪══════════╪════════╪══════════════════╪═══╪════════════╪═════════╪═══════╪══════════╡
    │ 1           ┆ 0        ┆ 3      ┆ Braund, Mr. Owen ┆ … ┆ A/5 21171  ┆ 7.25    ┆ null  ┆ S        │
    │             ┆          ┆        ┆ Harris           ┆   ┆            ┆         ┆       ┆          │
    │ 2           ┆ 1        ┆ 1      ┆ Cumings, Mrs.    ┆ … ┆ PC 17599   ┆ 71.2833 ┆ C85   ┆ C        │
    │             ┆          ┆        ┆ John Bradley     ┆   ┆            ┆         ┆       ┆          │
    │             ┆          ┆        ┆ (Flor…           ┆   ┆            ┆         ┆       ┆          │
    │ 3           ┆ 1        ┆ 3      ┆ Heikkinen, Miss. ┆ … ┆ STON/O2.   ┆ 7.925   ┆ null  ┆ S        │
    │             ┆          ┆        ┆ Laina            ┆   ┆ 3101282    ┆         ┆       ┆          │
    │ 4           ┆ 1        ┆ 1      ┆ Futrelle, Mrs.   ┆ … ┆ 113803     ┆ 53.1    ┆ C123  ┆ S        │
    │             ┆          ┆        ┆ Jacques Heath    ┆   ┆            ┆         ┆       ┆          │
    │             ┆          ┆        ┆ (Li…             ┆   ┆            ┆         ┆       ┆          │
    │ …           ┆ …        ┆ …      ┆ …                ┆ … ┆ …          ┆ …       ┆ …     ┆ …        │
    │ 888         ┆ 1        ┆ 1      ┆ Graham, Miss.    ┆ … ┆ 112053     ┆ 30.0    ┆ B42   ┆ S        │
    │             ┆          ┆        ┆ Margaret Edith   ┆   ┆            ┆         ┆       ┆          │
    │ 889         ┆ 0        ┆ 3      ┆ Johnston, Miss.  ┆ … ┆ W./C. 6607 ┆ 23.45   ┆ null  ┆ S        │
    │             ┆          ┆        ┆ Catherine Helen  ┆   ┆            ┆         ┆       ┆          │
    │             ┆          ┆        ┆ …                ┆   ┆            ┆         ┆       ┆          │
    │ 890         ┆ 1        ┆ 1      ┆ Behr, Mr. Karl   ┆ … ┆ 111369     ┆ 30.0    ┆ C148  ┆ C        │
    │             ┆          ┆        ┆ Howell           ┆   ┆            ┆         ┆       ┆          │
    │ 891         ┆ 0        ┆ 3      ┆ Dooley, Mr.      ┆ … ┆ 370376     ┆ 7.75    ┆ null  ┆ Q        │
    │             ┆          ┆        ┆ Patrick          ┆   ┆            ┆         ┆       ┆          │
    └─────────────┴──────────┴────────┴──────────────────┴───┴────────────┴─────────┴───────┴──────────┘

</div>

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:255}"
id="ag-6k4K0NAoX" outputId="c4841aae-c4af-4806-e7b2-f3bbe45edbc3">

``` python
# An overview of the dataset

df.head()
```

<div class="output execute_result" execution_count="12">

    shape: (5, 12)
    ┌─────────────┬──────────┬────────┬───────────────────┬───┬───────────┬─────────┬───────┬──────────┐
    │ PassengerId ┆ Survived ┆ Pclass ┆ Name              ┆ … ┆ Ticket    ┆ Fare    ┆ Cabin ┆ Embarked │
    │ ---         ┆ ---      ┆ ---    ┆ ---               ┆   ┆ ---       ┆ ---     ┆ ---   ┆ ---      │
    │ i64         ┆ i64      ┆ i64    ┆ str               ┆   ┆ str       ┆ f64     ┆ str   ┆ str      │
    ╞═════════════╪══════════╪════════╪═══════════════════╪═══╪═══════════╪═════════╪═══════╪══════════╡
    │ 1           ┆ 0        ┆ 3      ┆ Braund, Mr. Owen  ┆ … ┆ A/5 21171 ┆ 7.25    ┆ null  ┆ S        │
    │             ┆          ┆        ┆ Harris            ┆   ┆           ┆         ┆       ┆          │
    │ 2           ┆ 1        ┆ 1      ┆ Cumings, Mrs.     ┆ … ┆ PC 17599  ┆ 71.2833 ┆ C85   ┆ C        │
    │             ┆          ┆        ┆ John Bradley      ┆   ┆           ┆         ┆       ┆          │
    │             ┆          ┆        ┆ (Flor…            ┆   ┆           ┆         ┆       ┆          │
    │ 3           ┆ 1        ┆ 3      ┆ Heikkinen, Miss.  ┆ … ┆ STON/O2.  ┆ 7.925   ┆ null  ┆ S        │
    │             ┆          ┆        ┆ Laina             ┆   ┆ 3101282   ┆         ┆       ┆          │
    │ 4           ┆ 1        ┆ 1      ┆ Futrelle, Mrs.    ┆ … ┆ 113803    ┆ 53.1    ┆ C123  ┆ S        │
    │             ┆          ┆        ┆ Jacques Heath     ┆   ┆           ┆         ┆       ┆          │
    │             ┆          ┆        ┆ (Li…              ┆   ┆           ┆         ┆       ┆          │
    │ 5           ┆ 0        ┆ 3      ┆ Allen, Mr.        ┆ … ┆ 373450    ┆ 8.05    ┆ null  ┆ S        │
    │             ┆          ┆        ┆ William Henry     ┆   ┆           ┆         ┆       ┆          │
    └─────────────┴──────────┴────────┴───────────────────┴───┴───────────┴─────────┴───────┴──────────┘

</div>

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}"
id="jaMvosSVObVX" outputId="4799e1c1-9038-4f12-a728-ca8420849e63">

``` python
# An alternative command to have a glimpse of the data

print(df.glimpse())
```

<div class="output stream stdout">

    Rows: 891
    Columns: 12
    $ PassengerId <i64> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    $ Survived    <i64> 0, 1, 1, 1, 0, 0, 0, 0, 1, 1
    $ Pclass      <i64> 3, 1, 3, 1, 3, 3, 1, 3, 3, 2
    $ Name        <str> Braund, Mr. Owen Harris, Cumings, Mrs. John Bradley (Florence Briggs Thayer), Heikkinen, Miss. Laina, Futrelle, Mrs. Jacques Heath (Lily May Peel), Allen, Mr. William Henry, Moran, Mr. James, McCarthy, Mr. Timothy J, Palsson, Master. Gosta Leonard, Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg), Nasser, Mrs. Nicholas (Adele Achem)
    $ Sex         <str> male, female, female, female, male, male, male, male, female, female
    $ Age         <f64> 22.0, 38.0, 26.0, 35.0, 35.0, None, 54.0, 2.0, 27.0, 14.0
    $ SibSp       <i64> 1, 1, 0, 1, 0, 0, 0, 3, 0, 1
    $ Parch       <i64> 0, 0, 0, 0, 0, 0, 0, 1, 2, 0
    $ Ticket      <str> A/5 21171, PC 17599, STON/O2. 3101282, 113803, 373450, 330877, 17463, 349909, 347742, 237736
    $ Fare        <f64> 7.25, 71.2833, 7.925, 53.1, 8.05, 8.4583, 51.8625, 21.075, 11.1333, 30.0708
    $ Cabin       <str> None, C85, None, C123, None, None, E46, None, None, None
    $ Embarked    <str> S, C, S, S, S, Q, S, S, S, C

    None

</div>

</div>

<div class="cell markdown" id="QrM6PmEeOch_">

There are 2 main ways we can access the data in polars:

1.  Use the familiar pandas-like synthax with square brackets
2.  Using the native polars expression API. Typically this is a more
    performant approach that takes the full advantage of using polars.

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:192}"
id="KDmbes81PTc7" outputId="46a0fe9e-a200-4e74-aaca-fbf899dc63db">

``` python
# Option 1. Pandas synthax.

df[['Pclass', 'Name', 'Age']][:3]
```

<div class="output execute_result" execution_count="16">

    shape: (3, 3)
    ┌────────┬───────────────────────────────────┬──────┐
    │ Pclass ┆ Name                              ┆ Age  │
    │ ---    ┆ ---                               ┆ ---  │
    │ i64    ┆ str                               ┆ f64  │
    ╞════════╪═══════════════════════════════════╪══════╡
    │ 3      ┆ Braund, Mr. Owen Harris           ┆ 22.0 │
    │ 1      ┆ Cumings, Mrs. John Bradley (Flor… ┆ 38.0 │
    │ 3      ┆ Heikkinen, Miss. Laina            ┆ 26.0 │
    └────────┴───────────────────────────────────┴──────┘

</div>

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:882}"
id="UlxNAiR4PTf8" outputId="ca63143d-20af-476d-8492-bf66246c70c0">

``` python
# Option 2. Expression API.

df.select(pl.col('Pclass'), pl.col('Name'), pl.col('Age'))
```

<div class="output execute_result" execution_count="18">

    shape: (891, 3)
    ┌────────┬───────────────────────────────────┬──────┐
    │ Pclass ┆ Name                              ┆ Age  │
    │ ---    ┆ ---                               ┆ ---  │
    │ i64    ┆ str                               ┆ f64  │
    ╞════════╪═══════════════════════════════════╪══════╡
    │ 3      ┆ Braund, Mr. Owen Harris           ┆ 22.0 │
    │ 1      ┆ Cumings, Mrs. John Bradley (Flor… ┆ 38.0 │
    │ 3      ┆ Heikkinen, Miss. Laina            ┆ 26.0 │
    │ 1      ┆ Futrelle, Mrs. Jacques Heath (Li… ┆ 35.0 │
    │ …      ┆ …                                 ┆ …    │
    │ 1      ┆ Graham, Miss. Margaret Edith      ┆ 19.0 │
    │ 3      ┆ Johnston, Miss. Catherine Helen … ┆ null │
    │ 1      ┆ Behr, Mr. Karl Howell             ┆ 26.0 │
    │ 3      ┆ Dooley, Mr. Patrick               ┆ 32.0 │
    └────────┴───────────────────────────────────┴──────┘

</div>

</div>

<div class="cell markdown" id="kTt19ulMYShx">

The additional advantage of using the expression API is that we can
transform columns before returning them, which follows the
"Transformations and Actions" approach and is faster since it transforms
multiple columns in parallel.

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:882}"
id="LfhJQVp3Yfzz" outputId="aa90c20e-d97e-4367-ed1d-929b19cc2f29">

``` python
# An example of using the expression API with column transformations on the fly

df.select(pl.col('Pclass'), pl.col('Name').str.to_lowercase(), pl.col('Age').round(2))
```

<div class="output execute_result" execution_count="20">

    shape: (891, 3)
    ┌────────┬───────────────────────────────────┬──────┐
    │ Pclass ┆ Name                              ┆ Age  │
    │ ---    ┆ ---                               ┆ ---  │
    │ i64    ┆ str                               ┆ f64  │
    ╞════════╪═══════════════════════════════════╪══════╡
    │ 3      ┆ braund, mr. owen harris           ┆ 22.0 │
    │ 1      ┆ cumings, mrs. john bradley (flor… ┆ 38.0 │
    │ 3      ┆ heikkinen, miss. laina            ┆ 26.0 │
    │ 1      ┆ futrelle, mrs. jacques heath (li… ┆ 35.0 │
    │ …      ┆ …                                 ┆ …    │
    │ 1      ┆ graham, miss. margaret edith      ┆ 19.0 │
    │ 3      ┆ johnston, miss. catherine helen … ┆ null │
    │ 1      ┆ behr, mr. karl howell             ┆ 26.0 │
    │ 3      ┆ dooley, mr. patrick               ┆ 32.0 │
    └────────┴───────────────────────────────────┴──────┘

</div>

</div>

<div class="cell markdown" id="5GYP0E0SYf2V">

Another example of parallelization is when we use the expression API
with queries and/or aggregations.

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:286}"
id="4xJD5nefYf4j" outputId="f5494ba8-ed4b-45e8-85ca-624fa8c9a8eb">

``` python
df.groupby(['Survived', 'Pclass']).agg(pl.col('PassengerId').count().alias('counts'))
```

<div class="output execute_result" execution_count="24">

    shape: (6, 3)
    ┌──────────┬────────┬────────┐
    │ Survived ┆ Pclass ┆ counts │
    │ ---      ┆ ---    ┆ ---    │
    │ i64      ┆ i64    ┆ u32    │
    ╞══════════╪════════╪════════╡
    │ 1        ┆ 2      ┆ 87     │
    │ 1        ┆ 3      ┆ 119    │
    │ 0        ┆ 3      ┆ 372    │
    │ 0        ┆ 2      ┆ 97     │
    │ 1        ┆ 1      ┆ 136    │
    │ 0        ┆ 1      ┆ 80     │
    └──────────┴────────┴────────┘

</div>

</div>

<div class="cell markdown" id="AR2UV1IgYf6u">

Polars also supports the usage of visualization libraries directly on a
polars dataframe.

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:542}"
id="Er3_H5pRYf8n" outputId="8e18a3c8-3529-4e41-ddaf-9d33ce36264f">

``` python
# import plotly

import plotly.express as px

px.scatter(x = df['Age'], y = df['Fare'])
```

<div class="output display_data">

<html>
<head><meta charset="utf-8" /></head>
<body>
    <div>            <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG"></script><script type="text/javascript">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}</script>                <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script src="https://cdn.plot.ly/plotly-2.18.2.min.js"></script>                <div id="a3204cb2-c5f2-4fb3-83e6-2754d3bac8f9" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("a3204cb2-c5f2-4fb3-83e6-2754d3bac8f9")) {                    Plotly.newPlot(                        "a3204cb2-c5f2-4fb3-83e6-2754d3bac8f9",                        [{"hovertemplate":"x=%{x}<br>y=%{y}<extra></extra>","legendgroup":"","marker":{"color":"#636efa","symbol":"circle"},"mode":"markers","name":"","orientation":"v","showlegend":false,"x":[22.0,38.0,26.0,35.0,35.0,null,54.0,2.0,27.0,14.0,4.0,58.0,20.0,39.0,14.0,55.0,2.0,null,31.0,null,35.0,34.0,15.0,28.0,8.0,38.0,null,19.0,null,null,40.0,null,null,66.0,28.0,42.0,null,21.0,18.0,14.0,40.0,27.0,null,3.0,19.0,null,null,null,null,18.0,7.0,21.0,49.0,29.0,65.0,null,21.0,28.5,5.0,11.0,22.0,38.0,45.0,4.0,null,null,29.0,19.0,17.0,26.0,32.0,16.0,21.0,26.0,32.0,25.0,null,null,0.83,30.0,22.0,29.0,null,28.0,17.0,33.0,16.0,null,23.0,24.0,29.0,20.0,46.0,26.0,59.0,null,71.0,23.0,34.0,34.0,28.0,null,21.0,33.0,37.0,28.0,21.0,null,38.0,null,47.0,14.5,22.0,20.0,17.0,21.0,70.5,29.0,24.0,2.0,21.0,null,32.5,32.5,54.0,12.0,null,24.0,null,45.0,33.0,20.0,47.0,29.0,25.0,23.0,19.0,37.0,16.0,24.0,null,22.0,24.0,19.0,18.0,19.0,27.0,9.0,36.5,42.0,51.0,22.0,55.5,40.5,null,51.0,16.0,30.0,null,null,44.0,40.0,26.0,17.0,1.0,9.0,null,45.0,null,28.0,61.0,4.0,1.0,21.0,56.0,18.0,null,50.0,30.0,36.0,null,null,9.0,1.0,4.0,null,null,45.0,40.0,36.0,32.0,19.0,19.0,3.0,44.0,58.0,null,42.0,null,24.0,28.0,null,34.0,45.5,18.0,2.0,32.0,26.0,16.0,40.0,24.0,35.0,22.0,30.0,null,31.0,27.0,42.0,32.0,30.0,16.0,27.0,51.0,null,38.0,22.0,19.0,20.5,18.0,null,35.0,29.0,59.0,5.0,24.0,null,44.0,8.0,19.0,33.0,null,null,29.0,22.0,30.0,44.0,25.0,24.0,37.0,54.0,null,29.0,62.0,30.0,41.0,29.0,null,30.0,35.0,50.0,null,3.0,52.0,40.0,null,36.0,16.0,25.0,58.0,35.0,null,25.0,41.0,37.0,null,63.0,45.0,null,7.0,35.0,65.0,28.0,16.0,19.0,null,33.0,30.0,22.0,42.0,22.0,26.0,19.0,36.0,24.0,24.0,null,23.5,2.0,null,50.0,null,null,19.0,null,null,0.92,null,17.0,30.0,30.0,24.0,18.0,26.0,28.0,43.0,26.0,24.0,54.0,31.0,40.0,22.0,27.0,30.0,22.0,null,36.0,61.0,36.0,31.0,16.0,null,45.5,38.0,16.0,null,null,29.0,41.0,45.0,45.0,2.0,24.0,28.0,25.0,36.0,24.0,40.0,null,3.0,42.0,23.0,null,15.0,25.0,null,28.0,22.0,38.0,null,null,40.0,29.0,45.0,35.0,null,30.0,60.0,null,null,24.0,25.0,18.0,19.0,22.0,3.0,null,22.0,27.0,20.0,19.0,42.0,1.0,32.0,35.0,null,18.0,1.0,36.0,null,17.0,36.0,21.0,28.0,23.0,24.0,22.0,31.0,46.0,23.0,28.0,39.0,26.0,21.0,28.0,20.0,34.0,51.0,3.0,21.0,null,null,null,33.0,null,44.0,null,34.0,18.0,30.0,10.0,null,21.0,29.0,28.0,18.0,null,28.0,19.0,null,32.0,28.0,null,42.0,17.0,50.0,14.0,21.0,24.0,64.0,31.0,45.0,20.0,25.0,28.0,null,4.0,13.0,34.0,5.0,52.0,36.0,null,30.0,49.0,null,29.0,65.0,null,50.0,null,48.0,34.0,47.0,48.0,null,38.0,null,56.0,null,0.75,null,38.0,33.0,23.0,22.0,null,34.0,29.0,22.0,2.0,9.0,null,50.0,63.0,25.0,null,35.0,58.0,30.0,9.0,null,21.0,55.0,71.0,21.0,null,54.0,null,25.0,24.0,17.0,21.0,null,37.0,16.0,18.0,33.0,null,28.0,26.0,29.0,null,36.0,54.0,24.0,47.0,34.0,null,36.0,32.0,30.0,22.0,null,44.0,null,40.5,50.0,null,39.0,23.0,2.0,null,17.0,null,30.0,7.0,45.0,30.0,null,22.0,36.0,9.0,11.0,32.0,50.0,64.0,19.0,null,33.0,8.0,17.0,27.0,null,22.0,22.0,62.0,48.0,null,39.0,36.0,null,40.0,28.0,null,null,24.0,19.0,29.0,null,32.0,62.0,53.0,36.0,null,16.0,19.0,34.0,39.0,null,32.0,25.0,39.0,54.0,36.0,null,18.0,47.0,60.0,22.0,null,35.0,52.0,47.0,null,37.0,36.0,null,49.0,null,49.0,24.0,null,null,44.0,35.0,36.0,30.0,27.0,22.0,40.0,39.0,null,null,null,35.0,24.0,34.0,26.0,4.0,26.0,27.0,42.0,20.0,21.0,21.0,61.0,57.0,21.0,26.0,null,80.0,51.0,32.0,null,9.0,28.0,32.0,31.0,41.0,null,20.0,24.0,2.0,null,0.75,48.0,19.0,56.0,null,23.0,null,18.0,21.0,null,18.0,24.0,null,32.0,23.0,58.0,50.0,40.0,47.0,36.0,20.0,32.0,25.0,null,43.0,null,40.0,31.0,70.0,31.0,null,18.0,24.5,18.0,43.0,36.0,null,27.0,20.0,14.0,60.0,25.0,14.0,19.0,18.0,15.0,31.0,4.0,null,25.0,60.0,52.0,44.0,null,49.0,42.0,18.0,35.0,18.0,25.0,26.0,39.0,45.0,42.0,22.0,null,24.0,null,48.0,29.0,52.0,19.0,38.0,27.0,null,33.0,6.0,17.0,34.0,50.0,27.0,20.0,30.0,null,25.0,25.0,29.0,11.0,null,23.0,23.0,28.5,48.0,35.0,null,null,null,36.0,21.0,24.0,31.0,70.0,16.0,30.0,19.0,31.0,4.0,6.0,33.0,23.0,48.0,0.67,28.0,18.0,34.0,33.0,null,41.0,20.0,36.0,16.0,51.0,null,30.5,null,32.0,24.0,48.0,57.0,null,54.0,18.0,null,5.0,null,43.0,13.0,17.0,29.0,null,25.0,25.0,18.0,8.0,1.0,46.0,null,16.0,null,null,25.0,39.0,49.0,31.0,30.0,30.0,34.0,31.0,11.0,0.42,27.0,31.0,39.0,18.0,39.0,33.0,26.0,39.0,35.0,6.0,30.5,null,23.0,31.0,43.0,10.0,52.0,27.0,38.0,27.0,2.0,null,null,1.0,null,62.0,15.0,0.83,null,23.0,18.0,39.0,21.0,null,32.0,null,20.0,16.0,30.0,34.5,17.0,42.0,null,35.0,28.0,null,4.0,74.0,9.0,16.0,44.0,18.0,45.0,51.0,24.0,null,41.0,21.0,48.0,null,24.0,42.0,27.0,31.0,null,4.0,26.0,47.0,33.0,47.0,28.0,15.0,20.0,19.0,null,56.0,25.0,33.0,22.0,28.0,25.0,39.0,27.0,19.0,null,26.0,32.0],"xaxis":"x","y":[7.25,71.2833,7.925,53.1,8.05,8.4583,51.8625,21.075,11.1333,30.0708,16.7,26.55,8.05,31.275,7.8542,16.0,29.125,13.0,18.0,7.225,26.0,13.0,8.0292,35.5,21.075,31.3875,7.225,263.0,7.8792,7.8958,27.7208,146.5208,7.75,10.5,82.1708,52.0,7.2292,8.05,18.0,11.2417,9.475,21.0,7.8958,41.5792,7.8792,8.05,15.5,7.75,21.6792,17.8,39.6875,7.8,76.7292,26.0,61.9792,35.5,10.5,7.2292,27.75,46.9,7.2292,80.0,83.475,27.9,27.7208,15.2458,10.5,8.1583,7.925,8.6625,10.5,46.9,73.5,14.4542,56.4958,7.65,7.8958,8.05,29.0,12.475,9.0,9.5,7.7875,47.1,10.5,15.85,34.375,8.05,263.0,8.05,8.05,7.8542,61.175,20.575,7.25,8.05,34.6542,63.3583,23.0,26.0,7.8958,7.8958,77.2875,8.6542,7.925,7.8958,7.65,7.775,7.8958,24.15,52.0,14.4542,8.05,9.825,14.4583,7.925,7.75,21.0,247.5208,31.275,73.5,8.05,30.0708,13.0,77.2875,11.2417,7.75,7.1417,22.3583,6.975,7.8958,7.05,14.5,26.0,13.0,15.0458,26.2833,53.1,9.2167,79.2,15.2458,7.75,15.85,6.75,11.5,36.75,7.7958,34.375,26.0,13.0,12.525,66.6,8.05,14.5,7.3125,61.3792,7.7333,8.05,8.6625,69.55,16.1,15.75,7.775,8.6625,39.6875,20.525,55.0,27.9,25.925,56.4958,33.5,29.125,11.1333,7.925,30.6958,7.8542,25.4667,28.7125,13.0,0.0,69.55,15.05,31.3875,39.0,22.025,50.0,15.5,26.55,15.5,7.8958,13.0,13.0,7.8542,26.0,27.7208,146.5208,7.75,8.4042,7.75,13.0,9.5,69.55,6.4958,7.225,8.05,10.4625,15.85,18.7875,7.75,31.0,7.05,21.0,7.25,13.0,7.75,113.275,7.925,27.0,76.2917,10.5,8.05,13.0,8.05,7.8958,90.0,9.35,10.5,7.25,13.0,25.4667,83.475,7.775,13.5,31.3875,10.5,7.55,26.0,26.25,10.5,12.275,14.4542,15.5,10.5,7.125,7.225,90.0,7.775,14.5,52.5542,26.0,7.25,10.4625,26.55,16.1,20.2125,15.2458,79.2,86.5,512.3292,26.0,7.75,31.3875,79.65,0.0,7.75,10.5,39.6875,7.775,153.4625,135.6333,31.0,0.0,19.5,29.7,7.75,77.9583,7.75,0.0,29.125,20.25,7.75,7.8542,9.5,8.05,26.0,8.6625,9.5,7.8958,13.0,7.75,78.85,91.0792,12.875,8.85,7.8958,27.7208,7.2292,151.55,30.5,247.5208,7.75,23.25,0.0,12.35,8.05,151.55,110.8833,108.9,24.0,56.9292,83.1583,262.375,26.0,7.8958,26.25,7.8542,26.0,14.0,164.8667,134.5,7.25,7.8958,12.35,29.0,69.55,135.6333,6.2375,13.0,20.525,57.9792,23.25,28.5,153.4625,18.0,133.65,7.8958,66.6,134.5,8.05,35.5,26.0,263.0,13.0,13.0,13.0,13.0,13.0,16.1,15.9,8.6625,9.225,35.0,7.2292,17.8,7.225,9.5,55.0,13.0,7.8792,7.8792,27.9,27.7208,14.4542,7.05,15.5,7.25,75.25,7.2292,7.75,69.3,55.4417,6.4958,8.05,135.6333,21.075,82.1708,7.25,211.5,4.0125,7.775,227.525,15.7417,7.925,52.0,7.8958,73.5,46.9,13.0,7.7292,12.0,120.0,7.7958,7.925,113.275,16.7,7.7958,7.8542,26.0,10.5,12.65,7.925,8.05,9.825,15.85,8.6625,21.0,7.75,18.75,7.775,25.4667,7.8958,6.8583,90.0,0.0,7.925,8.05,32.5,13.0,13.0,24.15,7.8958,7.7333,7.875,14.4,20.2125,7.25,26.0,26.0,7.75,8.05,26.55,16.1,26.0,7.125,55.9,120.0,34.375,18.75,263.0,10.5,26.25,9.5,7.775,13.0,8.1125,81.8583,19.5,26.55,19.2583,30.5,27.75,19.9667,27.75,89.1042,8.05,7.8958,26.55,51.8625,10.5,7.75,26.55,8.05,38.5,13.0,8.05,7.05,0.0,26.55,7.725,19.2583,7.25,8.6625,27.75,13.7917,9.8375,52.0,21.0,7.0458,7.5208,12.2875,46.9,0.0,8.05,9.5875,91.0792,25.4667,90.0,29.7,8.05,15.9,19.9667,7.25,30.5,49.5042,8.05,14.4583,78.2667,15.1,151.55,7.7958,8.6625,7.75,7.6292,9.5875,86.5,108.9,26.0,26.55,22.525,56.4958,7.75,8.05,26.2875,59.4,7.4958,34.0208,10.5,24.15,26.0,7.8958,93.5,7.8958,7.225,57.9792,7.2292,7.75,10.5,221.7792,7.925,11.5,26.0,7.2292,7.2292,22.3583,8.6625,26.25,26.55,106.425,14.5,49.5,71.0,31.275,31.275,26.0,106.425,26.0,26.0,13.8625,20.525,36.75,110.8833,26.0,7.8292,7.225,7.775,26.55,39.6,227.525,79.65,17.4,7.75,7.8958,13.5,8.05,8.05,24.15,7.8958,21.075,7.2292,7.8542,10.5,51.4792,26.3875,7.75,8.05,14.5,13.0,55.9,14.4583,7.925,30.0,110.8833,26.0,40.125,8.7125,79.65,15.0,79.2,8.05,8.05,7.125,78.2667,7.25,7.75,26.0,24.15,33.0,0.0,7.225,56.9292,27.0,7.8958,42.4,8.05,26.55,15.55,7.8958,30.5,41.5792,153.4625,31.275,7.05,15.5,7.75,8.05,65.0,14.4,16.1,39.0,10.5,14.4542,52.5542,15.7417,7.8542,16.1,32.3208,12.35,77.9583,7.8958,7.7333,30.0,7.0542,30.5,0.0,27.9,13.0,7.925,26.25,39.6875,16.1,7.8542,69.3,27.9,56.4958,19.2583,76.7292,7.8958,35.5,7.55,7.55,7.8958,23.0,8.4333,7.8292,6.75,73.5,7.8958,15.5,13.0,113.275,133.65,7.225,25.5875,7.4958,7.925,73.5,13.0,7.775,8.05,52.0,39.0,52.0,10.5,13.0,0.0,7.775,8.05,9.8417,46.9,512.3292,8.1375,76.7292,9.225,46.9,39.0,41.5792,39.6875,10.1708,7.7958,211.3375,57.0,13.4167,56.4958,7.225,26.55,13.5,8.05,7.7333,110.8833,7.65,227.525,26.2875,14.4542,7.7417,7.8542,26.0,13.5,26.2875,151.55,15.2458,49.5042,26.55,52.0,9.4833,13.0,7.65,227.525,10.5,15.5,7.775,33.0,7.0542,13.0,13.0,53.1,8.6625,21.0,7.7375,26.0,7.925,211.3375,18.7875,0.0,13.0,13.0,16.1,34.375,512.3292,7.8958,7.8958,30.0,78.85,262.375,16.1,7.925,71.0,20.25,13.0,53.1,7.75,23.0,12.475,9.5,7.8958,65.0,14.5,7.7958,11.5,8.05,86.5,14.5,7.125,7.2292,120.0,7.775,77.9583,39.6,7.75,24.15,8.3625,9.5,7.8542,10.5,7.225,23.0,7.75,7.75,12.475,7.7375,211.3375,7.2292,57.0,30.0,23.45,7.05,7.25,7.4958,29.125,20.575,79.2,7.75,26.0,69.55,30.6958,7.8958,13.0,25.9292,8.6833,7.2292,24.15,13.0,26.25,120.0,8.5167,6.975,7.775,0.0,7.775,13.0,53.1,7.8875,24.15,10.5,31.275,8.05,0.0,7.925,37.0042,6.45,27.9,93.5,8.6625,0.0,12.475,39.6875,6.95,56.4958,37.0042,7.75,80.0,14.4542,18.75,7.2292,7.8542,8.3,83.1583,8.6625,8.05,56.4958,29.7,7.925,10.5,31.0,6.4375,8.6625,7.55,69.55,7.8958,33.0,89.1042,31.275,7.775,15.2458,39.4,26.0,9.35,164.8667,26.55,19.2583,7.2292,14.1083,11.5,25.9292,69.55,13.0,13.0,13.8583,50.4958,9.5,11.1333,7.8958,52.5542,5.0,9.0,24.0,7.225,9.8458,7.8958,7.8958,83.1583,26.0,7.8958,10.5167,10.5,7.05,29.125,13.0,30.0,23.45,30.0,7.75],"yaxis":"y","type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"x"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"y"}},"legend":{"tracegroupgap":0},"margin":{"t":60}},                        {"responsive": true}                    ).then(function(){
                            
var gd = document.getElementById('a3204cb2-c5f2-4fb3-83e6-2754d3bac8f9');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                            </script>        </div>
</body>
</html>

</div>

</div>

<div class="cell markdown" id="mbGuyY1JatXz">

# Lazy mode

Another key advantage of using polars is the lazy mode, in which polars
doesn't run each command line-by-line, but instead gathers the full
query together to run in one go. It is a more efficient way and is an
extention of the automatic query optimization.

In the example below we'll use the lazy query using scan_csv instead of
read_csv. Also instead of evaluating the query we use
describe_optimized_plan() method produced by polars query optimizer.

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}"
id="y--dSiKLay05" outputId="43fe87d8-f3e1-440a-b86b-4e1ed2456d8e">

``` python
print(pl.scan_csv(csv_file).groupby(['Survived', 'Pclass']).agg(pl.col('PassengerId').count().alias('counts')).describe_optimized_plan())
```

<div class="output stream stdout">

    AGGREGATE
    	[col("PassengerId").count().alias("counts")] BY [col("Survived"), col("Pclass")] FROM
    	
      CSV SCAN Titanic.csv
      PROJECT 3/12 COLUMNS

</div>

</div>

<div class="cell markdown" id="zU_JWPrPay3G">

In this example polars has identified that we only need 3 columns
instead of all 12.

Although most optimizations can be done manually, it is convenient that
polars is able to figure them out automatically. Also, it might apply
some optimizations that me might not know about.

</div>

<div class="cell markdown" id="R0AeLmjbay5I">

# Streaming

Streaming is another important feature of polars as it allows it to run
large datasets in batches so that we can work with the datasets that are
much larger than the available memory. A simple way to apply streaming
is to use the streaming=True argument in the collect method.

</div>

<div class="cell code"
colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:286}"
id="CK0o5WSKay7R" outputId="8c946e20-6d23-46bf-c906-a3a2b7f1e5d4">

``` python
pl.scan_csv(csv_file).groupby(['Survived', 'Pclass']).agg(pl.col('PassengerId').count().alias('counts')).collect(streaming = True)
```

<div class="output execute_result" execution_count="27">

    shape: (6, 3)
    ┌──────────┬────────┬────────┐
    │ Survived ┆ Pclass ┆ counts │
    │ ---      ┆ ---    ┆ ---    │
    │ i64      ┆ i64    ┆ u32    │
    ╞══════════╪════════╪════════╡
    │ 0        ┆ 3      ┆ 372    │
    │ 1        ┆ 3      ┆ 119    │
    │ 1        ┆ 1      ┆ 136    │
    │ 1        ┆ 2      ┆ 87     │
    │ 0        ┆ 2      ┆ 97     │
    │ 0        ┆ 1      ┆ 80     │
    └──────────┴────────┴────────┘

</div>

</div>

<div class="cell code" id="4O4tW9kddoIQ">

``` python
```

</div>

<div class="cell code" id="7iHK0Y1bdoKa">

``` python
```

</div>
