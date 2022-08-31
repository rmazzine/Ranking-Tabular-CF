# Ranking for Tabular Counterfactual Explanation Generators

This repository shows the benchmark of counterfactual generation algorithms in terms of (click for details):

<details>
  <summary>Coverage</summary>

    how many factuals are converted to counterfactuals?

</details>

<details>
  <summary>Sparsity</summary>

    how many features are unchanged?

</details>

<details>
  <summary>L2 distance</summary>

    how far are the counterfactuals from the factual data?

</details>

<details>
  <summary>Mean Absolute Deviation</summary>

    how different are the counterfactuals from the factual data considering feature variations?

</details>

<details>
  <summary>Mahalanobis distance</summary>

    how different are the counterfactuals from the factual data considering the data distribution?

</details>

<details>
  <summary>Time</summary>

    how long does it take to generate a counterfactual?

</details>

### How to include your CF generation algorithm
Follow the instructions on the [CounterfactualBenchmark repository](https://github.com/ADMAntwerp/CounterfactualBenchmark)

## RESULTS

All experiments consider a confidence level of 95%.

### Ranking Table
<details>
  <summary>Click here to see why we use ranking instead of the metrics itself</summary>

Most metrics cannot be directly compared as each algorithm has a different coverage. For example, if one algorithm 
only creates a single counterfactual and has a sparsity of 90%, we cannot say it is better than another algorithm 
that creates 1 000 counterfactuals and with sparsity of 88%. Therefore, the ranking consider these cases, giving a
better picture of the algorithms' performance.

</details>

The rankings below were created with Friedman's test to evaluate the null hypothesis that the algorithms are equal.
And Nemenyi's test to evaluate the significance of the difference between the algorithms.
The highlighted results are the ones that are statistically significant.

<div style="font-style: italic;" markdown="1">

### Ranking for all datasets

</div>

<style type="text/css">
#T_1b032_row0_col0, #T_1b032_row1_col1, #T_1b032_row2_col1, #T_1b032_row3_col1, #T_1b032_row4_col1 {
  background-color: gray;
}
</style>
<table id="T_1b032">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_1b032_level0_col0" class="col_heading level0 col0" >my_cf_generator</th>
      <th id="T_1b032_level0_col1" class="col_heading level0 col1" >new_generator_cf</th>
      <th id="T_1b032_level0_col2" class="col_heading level0 col2" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_1b032_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_1b032_row0_col0" class="data row0 col0" >1.48</td>
      <td id="T_1b032_row0_col1" class="data row0 col1" >1.52</td>
      <td id="T_1b032_row0_col2" class="data row0 col2" >3925</td>
    </tr>
    <tr>
      <th id="T_1b032_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_1b032_row1_col0" class="data row1 col0" >1.58</td>
      <td id="T_1b032_row1_col1" class="data row1 col1" >1.42</td>
      <td id="T_1b032_row1_col2" class="data row1 col2" >3925</td>
    </tr>
    <tr>
      <th id="T_1b032_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_1b032_row2_col0" class="data row2 col0" >1.65</td>
      <td id="T_1b032_row2_col1" class="data row2 col1" >1.35</td>
      <td id="T_1b032_row2_col2" class="data row2 col2" >3925</td>
    </tr>
    <tr>
      <th id="T_1b032_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_1b032_row3_col0" class="data row3 col0" >1.65</td>
      <td id="T_1b032_row3_col1" class="data row3 col1" >1.35</td>
      <td id="T_1b032_row3_col2" class="data row3 col2" >3925</td>
    </tr>
    <tr>
      <th id="T_1b032_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_1b032_row4_col0" class="data row4 col0" >1.60</td>
      <td id="T_1b032_row4_col1" class="data row4 col1" >1.40</td>
      <td id="T_1b032_row4_col2" class="data row4 col2" >3925</td>
    </tr>
    <tr>
      <th id="T_1b032_level0_row5" class="row_heading level0 row5" >cf_generation_time</th>
      <td id="T_1b032_row5_col0" class="data row5 col0" >1.50</td>
      <td id="T_1b032_row5_col1" class="data row5 col1" >1.50</td>
      <td id="T_1b032_row5_col2" class="data row5 col2" >3925</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for categorical datasets

</div>

<style type="text/css">
#T_2b2ee_row1_col1, #T_2b2ee_row2_col1, #T_2b2ee_row3_col1 {
  background-color: gray;
}
</style>
<table id="T_2b2ee">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_2b2ee_level0_col0" class="col_heading level0 col0" >my_cf_generator</th>
      <th id="T_2b2ee_level0_col1" class="col_heading level0 col1" >new_generator_cf</th>
      <th id="T_2b2ee_level0_col2" class="col_heading level0 col2" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_2b2ee_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_2b2ee_row0_col0" class="data row0 col0" >1.50</td>
      <td id="T_2b2ee_row0_col1" class="data row0 col1" >1.50</td>
      <td id="T_2b2ee_row0_col2" class="data row0 col2" >1327</td>
    </tr>
    <tr>
      <th id="T_2b2ee_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_2b2ee_row1_col0" class="data row1 col0" >1.63</td>
      <td id="T_2b2ee_row1_col1" class="data row1 col1" >1.37</td>
      <td id="T_2b2ee_row1_col2" class="data row1 col2" >1327</td>
    </tr>
    <tr>
      <th id="T_2b2ee_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_2b2ee_row2_col0" class="data row2 col0" >1.63</td>
      <td id="T_2b2ee_row2_col1" class="data row2 col1" >1.37</td>
      <td id="T_2b2ee_row2_col2" class="data row2 col2" >1327</td>
    </tr>
    <tr>
      <th id="T_2b2ee_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_2b2ee_row3_col0" class="data row3 col0" >1.63</td>
      <td id="T_2b2ee_row3_col1" class="data row3 col1" >1.37</td>
      <td id="T_2b2ee_row3_col2" class="data row3 col2" >1327</td>
    </tr>
    <tr>
      <th id="T_2b2ee_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_2b2ee_row4_col0" class="data row4 col0" >1.50</td>
      <td id="T_2b2ee_row4_col1" class="data row4 col1" >1.50</td>
      <td id="T_2b2ee_row4_col2" class="data row4 col2" >1327</td>
    </tr>
    <tr>
      <th id="T_2b2ee_level0_row5" class="row_heading level0 row5" >cf_generation_time</th>
      <td id="T_2b2ee_row5_col0" class="data row5 col0" >1.50</td>
      <td id="T_2b2ee_row5_col1" class="data row5 col1" >1.50</td>
      <td id="T_2b2ee_row5_col2" class="data row5 col2" >1327</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for numerical datasets

</div>

<style type="text/css">
#T_ae496_row2_col1, #T_ae496_row3_col1, #T_ae496_row4_col1 {
  background-color: gray;
}
</style>
<table id="T_ae496">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_ae496_level0_col0" class="col_heading level0 col0" >my_cf_generator</th>
      <th id="T_ae496_level0_col1" class="col_heading level0 col1" >new_generator_cf</th>
      <th id="T_ae496_level0_col2" class="col_heading level0 col2" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ae496_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_ae496_row0_col0" class="data row0 col0" >1.49</td>
      <td id="T_ae496_row0_col1" class="data row0 col1" >1.51</td>
      <td id="T_ae496_row0_col2" class="data row0 col2" >1598</td>
    </tr>
    <tr>
      <th id="T_ae496_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_ae496_row1_col0" class="data row1 col0" >1.49</td>
      <td id="T_ae496_row1_col1" class="data row1 col1" >1.51</td>
      <td id="T_ae496_row1_col2" class="data row1 col2" >1598</td>
    </tr>
    <tr>
      <th id="T_ae496_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_ae496_row2_col0" class="data row2 col0" >1.67</td>
      <td id="T_ae496_row2_col1" class="data row2 col1" >1.33</td>
      <td id="T_ae496_row2_col2" class="data row2 col2" >1598</td>
    </tr>
    <tr>
      <th id="T_ae496_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_ae496_row3_col0" class="data row3 col0" >1.68</td>
      <td id="T_ae496_row3_col1" class="data row3 col1" >1.32</td>
      <td id="T_ae496_row3_col2" class="data row3 col2" >1598</td>
    </tr>
    <tr>
      <th id="T_ae496_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_ae496_row4_col0" class="data row4 col0" >1.67</td>
      <td id="T_ae496_row4_col1" class="data row4 col1" >1.33</td>
      <td id="T_ae496_row4_col2" class="data row4 col2" >1598</td>
    </tr>
    <tr>
      <th id="T_ae496_level0_row5" class="row_heading level0 row5" >cf_generation_time</th>
      <td id="T_ae496_row5_col0" class="data row5 col0" >1.50</td>
      <td id="T_ae496_row5_col1" class="data row5 col1" >1.50</td>
      <td id="T_ae496_row5_col2" class="data row5 col2" >1598</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for mixed datasets

</div>

<style type="text/css">
#T_d9866_row0_col0, #T_d9866_row1_col1, #T_d9866_row2_col1, #T_d9866_row3_col1, #T_d9866_row4_col1 {
  background-color: gray;
}
</style>
<table id="T_d9866">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_d9866_level0_col0" class="col_heading level0 col0" >my_cf_generator</th>
      <th id="T_d9866_level0_col1" class="col_heading level0 col1" >new_generator_cf</th>
      <th id="T_d9866_level0_col2" class="col_heading level0 col2" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d9866_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_d9866_row0_col0" class="data row0 col0" >1.45</td>
      <td id="T_d9866_row0_col1" class="data row0 col1" >1.55</td>
      <td id="T_d9866_row0_col2" class="data row0 col2" >1000</td>
    </tr>
    <tr>
      <th id="T_d9866_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_d9866_row1_col0" class="data row1 col0" >1.65</td>
      <td id="T_d9866_row1_col1" class="data row1 col1" >1.35</td>
      <td id="T_d9866_row1_col2" class="data row1 col2" >1000</td>
    </tr>
    <tr>
      <th id="T_d9866_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_d9866_row2_col0" class="data row2 col0" >1.65</td>
      <td id="T_d9866_row2_col1" class="data row2 col1" >1.35</td>
      <td id="T_d9866_row2_col2" class="data row2 col2" >1000</td>
    </tr>
    <tr>
      <th id="T_d9866_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_d9866_row3_col0" class="data row3 col0" >1.63</td>
      <td id="T_d9866_row3_col1" class="data row3 col1" >1.37</td>
      <td id="T_d9866_row3_col2" class="data row3 col2" >1000</td>
    </tr>
    <tr>
      <th id="T_d9866_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_d9866_row4_col0" class="data row4 col0" >1.62</td>
      <td id="T_d9866_row4_col1" class="data row4 col1" >1.38</td>
      <td id="T_d9866_row4_col2" class="data row4 col2" >1000</td>
    </tr>
    <tr>
      <th id="T_d9866_level0_row5" class="row_heading level0 row5" >cf_generation_time</th>
      <td id="T_d9866_row5_col0" class="data row5 col0" >1.50</td>
      <td id="T_d9866_row5_col1" class="data row5 col1" >1.50</td>
      <td id="T_d9866_row5_col2" class="data row5 col2" >1000</td>
    </tr>
  </tbody>
</table>



### Coverage analysis

The results below consider **valid** counterfactuals. In other words, counterfactuals that: (1) have a different prediction class if compared to the factual and (2) respects binary and one-hot encoding rules.

<div style="font-style: italic; text-align: center;" markdown="1">

### Coverage (%) for all datasets

</div>

<p align="center">
<img src="./charts/validity_chart_all.png">
</p>

<div style="font-style: italic; text-align: center;" markdown="1">

### Coverage (%) for categorical datasets

</div>

<p align="center">
<img src="./charts/validity_chart_cat.png">
</p>

<div style="font-style: italic; text-align: center;" markdown="1">

### Coverage (%) for numerical continuous datasets

</div>

<p align="center">
<img src="./charts/validity_chart_num.png">
</p>

<div style="font-style: italic; text-align: center;" markdown="1">

### Coverage (%) for mixed datasets

</div>

<p align="center">
<img src="./charts/validity_chart_mix.png">
</p>

### Time Analysis
Time spent (in seconds) to generate a counterfactual explanation

<div style="font-style: italic; text-align: center;" markdown="1">

### Generation time (seconds) for all datasets

</div>

<p align="center">
<img src="./charts/cf_generation_time_chart_all.png">
</p>

<div style="font-style: italic; text-align: center;" markdown="1">

### Generation time (seconds) for categorical datasets

</div>

<p align="center">
<img src="./charts/cf_generation_time_chart_cat.png">
</p>

<div style="font-style: italic; text-align: center;" markdown="1">

### Generation time (seconds) for numerical continuous datasets

</div>

<p align="center">
<img src="./charts/cf_generation_time_chart_num.png">
</p>

<div style="font-style: italic; text-align: center;" markdown="1">

### Generation time (seconds) for mixed datasets

</div>

<p align="center">
<img src="./charts/cf_generation_time_chart_mix.png">
</p>



## Reference
If you used this package on your experiments, here's the reference paper:
```bibtex
@Article{app11167274,
AUTHOR = {de Oliveira, Raphael Mazzine Barbosa and Martens, David},
TITLE = {A Framework and Benchmarking Study for Counterfactual Generating Methods on Tabular Data},
JOURNAL = {Applied Sciences},
VOLUME = {11},
YEAR = {2021},
NUMBER = {16},
ARTICLE-NUMBER = {7274},
URL = {https://www.mdpi.com/2076-3417/11/16/7274},
ISSN = {2076-3417},
DOI = {10.3390/app11167274}
}
```
