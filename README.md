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


<table id="T_5f348">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_5f348_level0_col0" class="col_heading level0 col0" >alibi</th>
      <th id="T_5f348_level0_col1" class="col_heading level0 col1" >cadex</th>
      <th id="T_5f348_level0_col2" class="col_heading level0 col2" >alibi_nograd</th>
      <th id="T_5f348_level0_col3" class="col_heading level0 col3" >dice</th>
      <th id="T_5f348_level0_col4" class="col_heading level0 col4" >growingspheres</th>
      <th id="T_5f348_level0_col5" class="col_heading level0 col5" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_5f348_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_5f348_row0_col0" class="data row0 col0" >3.09</td>
      <td id="T_5f348_row0_col1" class="data row0 col1" >🥇2.69</td>
      <td id="T_5f348_row0_col2" class="data row0 col2" >3.08</td>
      <td id="T_5f348_row0_col3" class="data row0 col3" >🥇2.70</td>
      <td id="T_5f348_row0_col4" class="data row0 col4" >3.45</td>
      <td id="T_5f348_row0_col5" class="data row0 col5" >3925</td>
    </tr>
    <tr>
      <th id="T_5f348_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_5f348_row1_col0" class="data row1 col0" >2.99</td>
      <td id="T_5f348_row1_col1" class="data row1 col1" >3.70</td>
      <td id="T_5f348_row1_col2" class="data row1 col2" >2.70</td>
      <td id="T_5f348_row1_col3" class="data row1 col3" >🥇2.50</td>
      <td id="T_5f348_row1_col4" class="data row1 col4" >3.12</td>
      <td id="T_5f348_row1_col5" class="data row1 col5" >3925</td>
    </tr>
    <tr>
      <th id="T_5f348_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_5f348_row2_col0" class="data row2 col0" >3.34</td>
      <td id="T_5f348_row2_col1" class="data row2 col1" >3.39</td>
      <td id="T_5f348_row2_col2" class="data row2 col2" >2.99</td>
      <td id="T_5f348_row2_col3" class="data row2 col3" >3.82</td>
      <td id="T_5f348_row2_col4" class="data row2 col4" >🥇1.46</td>
      <td id="T_5f348_row2_col5" class="data row2 col5" >3925</td>
    </tr>
    <tr>
      <th id="T_5f348_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_5f348_row3_col0" class="data row3 col0" >3.13</td>
      <td id="T_5f348_row3_col1" class="data row3 col1" >3.19</td>
      <td id="T_5f348_row3_col2" class="data row3 col2" >🥇2.83</td>
      <td id="T_5f348_row3_col3" class="data row3 col3" >3.09</td>
      <td id="T_5f348_row3_col4" class="data row3 col4" >🥇2.76</td>
      <td id="T_5f348_row3_col5" class="data row3 col5" >3925</td>
    </tr>
    <tr>
      <th id="T_5f348_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_5f348_row4_col0" class="data row4 col0" >3.29</td>
      <td id="T_5f348_row4_col1" class="data row4 col1" >3.33</td>
      <td id="T_5f348_row4_col2" class="data row4 col2" >3.01</td>
      <td id="T_5f348_row4_col3" class="data row4 col3" >3.80</td>
      <td id="T_5f348_row4_col4" class="data row4 col4" >🥇1.57</td>
      <td id="T_5f348_row4_col5" class="data row4 col5" >3925</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for categorical datasets

</div>


<table id="T_2a264">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_2a264_level0_col0" class="col_heading level0 col0" >alibi</th>
      <th id="T_2a264_level0_col1" class="col_heading level0 col1" >cadex</th>
      <th id="T_2a264_level0_col2" class="col_heading level0 col2" >alibi_nograd</th>
      <th id="T_2a264_level0_col3" class="col_heading level0 col3" >dice</th>
      <th id="T_2a264_level0_col4" class="col_heading level0 col4" >growingspheres</th>
      <th id="T_2a264_level0_col5" class="col_heading level0 col5" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_2a264_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_2a264_row0_col0" class="data row0 col0" >3.54</td>
      <td id="T_2a264_row0_col1" class="data row0 col1" >2.34</td>
      <td id="T_2a264_row0_col2" class="data row0 col2" >3.37</td>
      <td id="T_2a264_row0_col3" class="data row0 col3" >🥇1.62</td>
      <td id="T_2a264_row0_col4" class="data row0 col4" >4.12</td>
      <td id="T_2a264_row0_col5" class="data row0 col5" >1327</td>
    </tr>
    <tr>
      <th id="T_2a264_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_2a264_row1_col0" class="data row1 col0" >3.83</td>
      <td id="T_2a264_row1_col1" class="data row1 col1" >3.46</td>
      <td id="T_2a264_row1_col2" class="data row1 col2" >3.12</td>
      <td id="T_2a264_row1_col3" class="data row1 col3" >🥇1.61</td>
      <td id="T_2a264_row1_col4" class="data row1 col4" >2.99</td>
      <td id="T_2a264_row1_col5" class="data row1 col5" >1327</td>
    </tr>
    <tr>
      <th id="T_2a264_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_2a264_row2_col0" class="data row2 col0" >4.07</td>
      <td id="T_2a264_row2_col1" class="data row2 col1" >3.86</td>
      <td id="T_2a264_row2_col2" class="data row2 col2" >3.45</td>
      <td id="T_2a264_row2_col3" class="data row2 col3" >2.62</td>
      <td id="T_2a264_row2_col4" class="data row2 col4" >🥇1.00</td>
      <td id="T_2a264_row2_col5" class="data row2 col5" >1327</td>
    </tr>
    <tr>
      <th id="T_2a264_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_2a264_row3_col0" class="data row3 col0" >4.20</td>
      <td id="T_2a264_row3_col1" class="data row3 col1" >3.29</td>
      <td id="T_2a264_row3_col2" class="data row3 col2" >3.30</td>
      <td id="T_2a264_row3_col3" class="data row3 col3" >🥇1.44</td>
      <td id="T_2a264_row3_col4" class="data row3 col4" >2.76</td>
      <td id="T_2a264_row3_col5" class="data row3 col5" >1327</td>
    </tr>
    <tr>
      <th id="T_2a264_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_2a264_row4_col0" class="data row4 col0" >4.07</td>
      <td id="T_2a264_row4_col1" class="data row4 col1" >3.87</td>
      <td id="T_2a264_row4_col2" class="data row4 col2" >3.44</td>
      <td id="T_2a264_row4_col3" class="data row4 col3" >2.61</td>
      <td id="T_2a264_row4_col4" class="data row4 col4" >🥇1.01</td>
      <td id="T_2a264_row4_col5" class="data row4 col5" >1327</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for numerical datasets

</div>


<table id="T_d6766">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_d6766_level0_col0" class="col_heading level0 col0" >alibi</th>
      <th id="T_d6766_level0_col1" class="col_heading level0 col1" >cadex</th>
      <th id="T_d6766_level0_col2" class="col_heading level0 col2" >alibi_nograd</th>
      <th id="T_d6766_level0_col3" class="col_heading level0 col3" >dice</th>
      <th id="T_d6766_level0_col4" class="col_heading level0 col4" >growingspheres</th>
      <th id="T_d6766_level0_col5" class="col_heading level0 col5" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d6766_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_d6766_row0_col0" class="data row0 col0" >3.02</td>
      <td id="T_d6766_row0_col1" class="data row0 col1" >3.14</td>
      <td id="T_d6766_row0_col2" class="data row0 col2" >3.01</td>
      <td id="T_d6766_row0_col3" class="data row0 col3" >3.04</td>
      <td id="T_d6766_row0_col4" class="data row0 col4" >🥇2.80</td>
      <td id="T_d6766_row0_col5" class="data row0 col5" >1598</td>
    </tr>
    <tr>
      <th id="T_d6766_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_d6766_row1_col0" class="data row1 col0" >2.89</td>
      <td id="T_d6766_row1_col1" class="data row1 col1" >4.11</td>
      <td id="T_d6766_row1_col2" class="data row1 col2" >2.88</td>
      <td id="T_d6766_row1_col3" class="data row1 col3" >🥇1.89</td>
      <td id="T_d6766_row1_col4" class="data row1 col4" >3.23</td>
      <td id="T_d6766_row1_col5" class="data row1 col5" >1598</td>
    </tr>
    <tr>
      <th id="T_d6766_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_d6766_row2_col0" class="data row2 col0" >2.92</td>
      <td id="T_d6766_row2_col1" class="data row2 col1" >3.06</td>
      <td id="T_d6766_row2_col2" class="data row2 col2" >2.93</td>
      <td id="T_d6766_row2_col3" class="data row2 col3" >4.32</td>
      <td id="T_d6766_row2_col4" class="data row2 col4" >🥇1.77</td>
      <td id="T_d6766_row2_col5" class="data row2 col5" >1598</td>
    </tr>
    <tr>
      <th id="T_d6766_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_d6766_row3_col0" class="data row3 col0" >🥇2.52</td>
      <td id="T_d6766_row3_col1" class="data row3 col1" >3.54</td>
      <td id="T_d6766_row3_col2" class="data row3 col2" >🥇2.51</td>
      <td id="T_d6766_row3_col3" class="data row3 col3" >3.55</td>
      <td id="T_d6766_row3_col4" class="data row3 col4" >2.87</td>
      <td id="T_d6766_row3_col5" class="data row3 col5" >1598</td>
    </tr>
    <tr>
      <th id="T_d6766_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_d6766_row4_col0" class="data row4 col0" >2.88</td>
      <td id="T_d6766_row4_col1" class="data row4 col1" >2.97</td>
      <td id="T_d6766_row4_col2" class="data row4 col2" >2.87</td>
      <td id="T_d6766_row4_col3" class="data row4 col3" >4.26</td>
      <td id="T_d6766_row4_col4" class="data row4 col4" >🥇2.02</td>
      <td id="T_d6766_row4_col5" class="data row4 col5" >1598</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for mixed datasets

</div>


<table id="T_c8656">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_c8656_level0_col0" class="col_heading level0 col0" >alibi</th>
      <th id="T_c8656_level0_col1" class="col_heading level0 col1" >cadex</th>
      <th id="T_c8656_level0_col2" class="col_heading level0 col2" >alibi_nograd</th>
      <th id="T_c8656_level0_col3" class="col_heading level0 col3" >dice</th>
      <th id="T_c8656_level0_col4" class="col_heading level0 col4" >growingspheres</th>
      <th id="T_c8656_level0_col5" class="col_heading level0 col5" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c8656_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_c8656_row0_col0" class="data row0 col0" >🥇2.60</td>
      <td id="T_c8656_row0_col1" class="data row0 col1" >🥇2.42</td>
      <td id="T_c8656_row0_col2" class="data row0 col2" >2.81</td>
      <td id="T_c8656_row0_col3" class="data row0 col3" >3.59</td>
      <td id="T_c8656_row0_col4" class="data row0 col4" >3.59</td>
      <td id="T_c8656_row0_col5" class="data row0 col5" >1000</td>
    </tr>
    <tr>
      <th id="T_c8656_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_c8656_row1_col0" class="data row1 col0" >🥇2.03</td>
      <td id="T_c8656_row1_col1" class="data row1 col1" >3.35</td>
      <td id="T_c8656_row1_col2" class="data row1 col2" >🥇1.85</td>
      <td id="T_c8656_row1_col3" class="data row1 col3" >4.64</td>
      <td id="T_c8656_row1_col4" class="data row1 col4" >3.12</td>
      <td id="T_c8656_row1_col5" class="data row1 col5" >1000</td>
    </tr>
    <tr>
      <th id="T_c8656_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_c8656_row2_col0" class="data row2 col0" >3.03</td>
      <td id="T_c8656_row2_col1" class="data row2 col1" >3.30</td>
      <td id="T_c8656_row2_col2" class="data row2 col2" >2.47</td>
      <td id="T_c8656_row2_col3" class="data row2 col3" >4.64</td>
      <td id="T_c8656_row2_col4" class="data row2 col4" >🥇1.57</td>
      <td id="T_c8656_row2_col5" class="data row2 col5" >1000</td>
    </tr>
    <tr>
      <th id="T_c8656_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_c8656_row3_col0" class="data row3 col0" >🥇2.66</td>
      <td id="T_c8656_row3_col1" class="data row3 col1" >🥇2.48</td>
      <td id="T_c8656_row3_col2" class="data row3 col2" >2.73</td>
      <td id="T_c8656_row3_col3" class="data row3 col3" >4.55</td>
      <td id="T_c8656_row3_col4" class="data row3 col4" >🥇2.57</td>
      <td id="T_c8656_row3_col5" class="data row3 col5" >1000</td>
    </tr>
    <tr>
      <th id="T_c8656_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_c8656_row4_col0" class="data row4 col0" >2.92</td>
      <td id="T_c8656_row4_col1" class="data row4 col1" >3.19</td>
      <td id="T_c8656_row4_col2" class="data row4 col2" >2.67</td>
      <td id="T_c8656_row4_col3" class="data row4 col3" >4.64</td>
      <td id="T_c8656_row4_col4" class="data row4 col4" >🥇1.58</td>
      <td id="T_c8656_row4_col5" class="data row4 col5" >1000</td>
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
