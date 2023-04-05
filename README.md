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

::: {.cell .markdown id="rBGq9T9efPVR"}
![Polars_vs_pandas_img.jpg](vertopal_f09c658f3d9a4d00a0fae16b6cd97a47/3eba185d313bce7484730a47e02852237cda7b97.jpg)
:::

::: {.cell .markdown id="fssVmHOb-l4v"}
# What is polars?

-   Polars is a library for working with and manipulating dataframe that
    is typically used for data loading, transformation and analysis.
-   It works conveniently with CSV files, Excel spreadsheets, json
    etc\...
-   It is a faster alternative to pandas
:::

::: {.cell .markdown id="hEm_mFRK-xls"}
# Why polars vs pandas?

-   Polars is much faster.
-   Polars implements under-the-hood code optimization, including native
    parallelization.
-   Polars code is easy and pandas-like.
:::

::: {.cell .code id="JRVyu6xi_soj"}
``` python
# Import both libraries

import polars as pl
import pandas as pd
```
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":362}" id="56XJmt9B_srC" outputId="f598f867-d7a0-45ec-e8d9-d68ca8bfa822"}
``` python
# Sample dataset ~ 14000 rows and 20 columns

csv_file = 'RankingsCombined.csv'
pl.scan_csv(csv_file, ignore_errors=True).head(5).collect()
```

::: {.output .execute_result execution_count="55"}
```{=html}
<div><style>
.dataframe > thead > tr > th,
.dataframe > tbody > tr > td {
  text-align: right;
}
</style>
<small>shape: (5, 25)</small><table border="1" class="dataframe"><thead><tr><th></th><th>rank_order</th><th>rank</th><th>name</th><th>scores_overall</th><th>scores_overall_rank</th><th>scores_teaching</th><th>scores_teaching_rank</th><th>scores_international_outlook</th><th>scores_international_outlook_rank</th><th>scores_industry_income</th><th>scores_industry_income_rank</th><th>scores_research</th><th>scores_research_rank</th><th>scores_citations</th><th>scores_citations_rank</th><th>location</th><th>aliases</th><th>subjects_offered</th><th>closed</th><th>unaccredited</th><th>stats_number_students</th><th>stats_student_staff_ratio</th><th>stats_pc_intl_students</th><th>stats_female_male_ratio</th></tr><tr><td>i64</td><td>i64</td><td>i64</td><td>str</td><td>f64</td><td>i64</td><td>f64</td><td>i64</td><td>str</td><td>i64</td><td>str</td><td>i64</td><td>f64</td><td>i64</td><td>f64</td><td>i64</td><td>str</td><td>str</td><td>str</td><td>bool</td><td>bool</td><td>str</td><td>str</td><td>str</td><td>str</td></tr></thead><tbody><tr><td>0</td><td>1</td><td>1</td><td>&quot;Harvard Univer…</td><td>96.1</td><td>1</td><td>99.7</td><td>1</td><td>&quot;72.4&quot;</td><td>49</td><td>&quot;34.5&quot;</td><td>105</td><td>98.7</td><td>2</td><td>98.8</td><td>8</td><td>&quot;United States&quot;</td><td>&quot;Harvard Univer…</td><td>&quot;Mathematics &amp; …</td><td>false</td><td>false</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>1</td><td>2</td><td>2</td><td>&quot;California Ins…</td><td>96.0</td><td>2</td><td>97.7</td><td>4</td><td>&quot;54.6&quot;</td><td>93</td><td>&quot;83.7&quot;</td><td>24</td><td>98.0</td><td>4</td><td>99.9</td><td>1</td><td>&quot;United States&quot;</td><td>&quot;California Ins…</td><td>&quot;Languages, Lit…</td><td>false</td><td>false</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>2</td><td>3</td><td>3</td><td>&quot;Massachusetts …</td><td>95.6</td><td>3</td><td>97.8</td><td>3</td><td>&quot;82.3&quot;</td><td>36</td><td>&quot;87.5&quot;</td><td>21</td><td>91.4</td><td>11</td><td>99.9</td><td>2</td><td>&quot;United States&quot;</td><td>&quot;Massachusetts …</td><td>&quot;Mathematics &amp; …</td><td>false</td><td>false</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>3</td><td>4</td><td>4</td><td>&quot;Stanford Unive…</td><td>94.3</td><td>4</td><td>98.3</td><td>2</td><td>&quot;29.5&quot;</td><td>156</td><td>&quot;64.3&quot;</td><td>33</td><td>98.1</td><td>3</td><td>99.2</td><td>6</td><td>&quot;United States&quot;</td><td>&quot;Stanford Unive…</td><td>&quot;Physics &amp; Astr…</td><td>false</td><td>false</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>4</td><td>5</td><td>5</td><td>&quot;Princeton Univ…</td><td>94.2</td><td>5</td><td>90.9</td><td>6</td><td>&quot;70.3&quot;</td><td>53</td><td>&quot;-&quot;</td><td>164</td><td>95.4</td><td>5</td><td>99.9</td><td>3</td><td>&quot;United States&quot;</td><td>&quot;Princeton Univ…</td><td>&quot;Languages, Lit…</td><td>false</td><td>false</td><td>null</td><td>null</td><td>null</td><td>null</td></tr></tbody></table></div>
```
:::
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="OWK748wC_stb" outputId="836694ae-f78e-4d84-8b52-90afd3eb5614"}
``` python
# Polars data read performance

%%timeit -n1 -r1
pl.read_csv(csv_file, ignore_errors=True)
```

::: {.output .stream .stdout}
    60.8 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
:::
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="547jvSrs_sv0" outputId="de52f645-308a-438a-8134-ee9d6146c3d7"}
``` python
# Pandas data read performance

%%timeit -n1 -r1
pd.read_csv(csv_file)
```

::: {.output .stream .stdout}
    158 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
:::
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="w4VbWNBgDiQF" outputId="ddd16d22-8022-461b-e91d-79bd411c27a0"}
``` python
# Optimized pandas data read performance

%%timeit -n1 -r1
pd.read_csv(csv_file, engine = 'pyarrow')
```

::: {.output .stream .stdout}
    114 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
:::
:::

::: {.cell .markdown id="wm_Qks1uE51C"}
### Query optimization

By default, polars also optimizes queries, which makes them easier to
read and write.

For example, here is a comparinsong of getting an average and maximum
values grouping by the location.
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="MdZ09htfE9M4" outputId="45840eb8-5b68-41c8-bc71-982419a0b9a8"}
``` python
# Polars aggregation

%%timeit -n1 -r1
(
    pl.scan_csv(csv_file, ignore_errors = True)
    .groupby('location')
    .agg(
        [
            pl.col('scores_industry_income_rank').mean().suffix('_mean'),
            pl.col('scores_industry_income_rank').mean().suffix('_max')
        ]
    )
    .collect()
)
```

::: {.output .stream .stdout}
    28 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
:::
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="9jfRo1v_IPZq" outputId="a793de88-8ab9-4609-f966-c97561d39145"}
``` python
 # Pandas aggregation

%%timeit -n1 -r1
(
    pd.read_csv(csv_file)
    .groupby('location')
    .agg({'scores_industry_income_rank': ['mean', 'max']})
)
```

::: {.output .stream .stdout}
    150 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
:::
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="JhlaaflOIPcT" outputId="705123f7-abf9-488d-ba34-7153725a2097"}
``` python
# Polars vs pandas aggregation

%%timeit -n1 -r1
(
    pd.read_csv(csv_file, engine = 'pyarrow', usecols = ['location', 'scores_industry_income_rank'])
    .groupby('location')
    .agg({'scores_industry_income_rank':['mean', 'max']})
)
```

::: {.output .stream .stdout}
    41.7 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
:::
:::

::: {.cell .markdown id="mloFuUKYIPel"}
# Conclusion

Even on a relatively small dataset polars is about 3 times faster than
pandas and about 2 times faster than using pandas with optimization.
:::

::: {.cell .code id="2MEtiE8mIPhN"}
``` python
```
:::
