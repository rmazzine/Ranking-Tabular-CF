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


<table id="T_12102">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_12102_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_12102_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_12102_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_12102_level0_col3" class="col_heading level0 col3" >cadex</th>
      <th id="T_12102_level0_col4" class="col_heading level0 col4" >alibi_nograd</th>
      <th id="T_12102_level0_col5" class="col_heading level0 col5" >dice</th>
      <th id="T_12102_level0_col6" class="col_heading level0 col6" >growingspheres</th>
      <th id="T_12102_level0_col7" class="col_heading level0 col7" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_12102_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_12102_row0_col0" class="data row0 col0" >3.97</td>
      <td id="T_12102_row0_col1" class="data row0 col1" >4.62</td>
      <td id="T_12102_row0_col2" class="data row0 col2" >4.05</td>
      <td id="T_12102_row0_col3" class="data row0 col3" >3.49</td>
      <td id="T_12102_row0_col4" class="data row0 col4" >4.04</td>
      <td id="T_12102_row0_col5" class="data row0 col5" >🥇3.28</td>
      <td id="T_12102_row0_col6" class="data row0 col6" >4.55</td>
      <td id="T_12102_row0_col7" class="data row0 col7" >3925</td>
    </tr>
    <tr>
      <th id="T_12102_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_12102_row1_col0" class="data row1 col0" >3.28</td>
      <td id="T_12102_row1_col1" class="data row1 col1" >4.29</td>
      <td id="T_12102_row1_col2" class="data row1 col2" >4.16</td>
      <td id="T_12102_row1_col3" class="data row1 col3" >4.38</td>
      <td id="T_12102_row1_col4" class="data row1 col4" >4.08</td>
      <td id="T_12102_row1_col5" class="data row1 col5" >🥇2.85</td>
      <td id="T_12102_row1_col6" class="data row1 col6" >4.96</td>
      <td id="T_12102_row1_col7" class="data row1 col7" >3925</td>
    </tr>
    <tr>
      <th id="T_12102_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_12102_row2_col0" class="data row2 col0" >4.06</td>
      <td id="T_12102_row2_col1" class="data row2 col1" >5.00</td>
      <td id="T_12102_row2_col2" class="data row2 col2" >🥇3.74</td>
      <td id="T_12102_row2_col3" class="data row2 col3" >🥇3.61</td>
      <td id="T_12102_row2_col4" class="data row2 col4" >🥇3.66</td>
      <td id="T_12102_row2_col5" class="data row2 col5" >4.03</td>
      <td id="T_12102_row2_col6" class="data row2 col6" >3.90</td>
      <td id="T_12102_row2_col7" class="data row2 col7" >3925</td>
    </tr>
    <tr>
      <th id="T_12102_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_12102_row3_col0" class="data row3 col0" >4.04</td>
      <td id="T_12102_row3_col1" class="data row3 col1" >4.47</td>
      <td id="T_12102_row3_col2" class="data row3 col2" >3.88</td>
      <td id="T_12102_row3_col3" class="data row3 col3" >3.83</td>
      <td id="T_12102_row3_col4" class="data row3 col4" >🥇3.70</td>
      <td id="T_12102_row3_col5" class="data row3 col5" >🥇3.57</td>
      <td id="T_12102_row3_col6" class="data row3 col6" >4.50</td>
      <td id="T_12102_row3_col7" class="data row3 col7" >3925</td>
    </tr>
    <tr>
      <th id="T_12102_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_12102_row4_col0" class="data row4 col0" >4.01</td>
      <td id="T_12102_row4_col1" class="data row4 col1" >5.05</td>
      <td id="T_12102_row4_col2" class="data row4 col2" >3.70</td>
      <td id="T_12102_row4_col3" class="data row4 col3" >🥇3.55</td>
      <td id="T_12102_row4_col4" class="data row4 col4" >🥇3.67</td>
      <td id="T_12102_row4_col5" class="data row4 col5" >4.01</td>
      <td id="T_12102_row4_col6" class="data row4 col6" >4.01</td>
      <td id="T_12102_row4_col7" class="data row4 col7" >3925</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for categorical datasets

</div>


<table id="T_6246e">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_6246e_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_6246e_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_6246e_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_6246e_level0_col3" class="col_heading level0 col3" >cadex</th>
      <th id="T_6246e_level0_col4" class="col_heading level0 col4" >alibi_nograd</th>
      <th id="T_6246e_level0_col5" class="col_heading level0 col5" >dice</th>
      <th id="T_6246e_level0_col6" class="col_heading level0 col6" >growingspheres</th>
      <th id="T_6246e_level0_col7" class="col_heading level0 col7" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_6246e_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_6246e_row0_col0" class="data row0 col0" >3.66</td>
      <td id="T_6246e_row0_col1" class="data row0 col1" >5.37</td>
      <td id="T_6246e_row0_col2" class="data row0 col2" >4.55</td>
      <td id="T_6246e_row0_col3" class="data row0 col3" >2.88</td>
      <td id="T_6246e_row0_col4" class="data row0 col4" >4.31</td>
      <td id="T_6246e_row0_col5" class="data row0 col5" >🥇1.87</td>
      <td id="T_6246e_row0_col6" class="data row0 col6" >5.37</td>
      <td id="T_6246e_row0_col7" class="data row0 col7" >1327</td>
    </tr>
    <tr>
      <th id="T_6246e_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_6246e_row1_col0" class="data row1 col0" >3.26</td>
      <td id="T_6246e_row1_col1" class="data row1 col1" >5.37</td>
      <td id="T_6246e_row1_col2" class="data row1 col2" >4.42</td>
      <td id="T_6246e_row1_col3" class="data row1 col3" >3.53</td>
      <td id="T_6246e_row1_col4" class="data row1 col4" >4.10</td>
      <td id="T_6246e_row1_col5" class="data row1 col5" >🥇1.96</td>
      <td id="T_6246e_row1_col6" class="data row1 col6" >5.37</td>
      <td id="T_6246e_row1_col7" class="data row1 col7" >1327</td>
    </tr>
    <tr>
      <th id="T_6246e_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_6246e_row2_col0" class="data row2 col0" >3.26</td>
      <td id="T_6246e_row2_col1" class="data row2 col1" >5.37</td>
      <td id="T_6246e_row2_col2" class="data row2 col2" >4.42</td>
      <td id="T_6246e_row2_col3" class="data row2 col3" >3.53</td>
      <td id="T_6246e_row2_col4" class="data row2 col4" >4.10</td>
      <td id="T_6246e_row2_col5" class="data row2 col5" >🥇1.96</td>
      <td id="T_6246e_row2_col6" class="data row2 col6" >5.37</td>
      <td id="T_6246e_row2_col7" class="data row2 col7" >1327</td>
    </tr>
    <tr>
      <th id="T_6246e_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_6246e_row3_col0" class="data row3 col0" >3.82</td>
      <td id="T_6246e_row3_col1" class="data row3 col1" >5.17</td>
      <td id="T_6246e_row3_col2" class="data row3 col2" >4.74</td>
      <td id="T_6246e_row3_col3" class="data row3 col3" >3.25</td>
      <td id="T_6246e_row3_col4" class="data row3 col4" >4.23</td>
      <td id="T_6246e_row3_col5" class="data row3 col5" >🥇1.61</td>
      <td id="T_6246e_row3_col6" class="data row3 col6" >5.17</td>
      <td id="T_6246e_row3_col7" class="data row3 col7" >1327</td>
    </tr>
    <tr>
      <th id="T_6246e_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_6246e_row4_col0" class="data row4 col0" >3.28</td>
      <td id="T_6246e_row4_col1" class="data row4 col1" >5.37</td>
      <td id="T_6246e_row4_col2" class="data row4 col2" >4.41</td>
      <td id="T_6246e_row4_col3" class="data row4 col3" >3.54</td>
      <td id="T_6246e_row4_col4" class="data row4 col4" >4.09</td>
      <td id="T_6246e_row4_col5" class="data row4 col5" >🥇1.95</td>
      <td id="T_6246e_row4_col6" class="data row4 col6" >5.37</td>
      <td id="T_6246e_row4_col7" class="data row4 col7" >1327</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for numerical datasets

</div>


<table id="T_c6fc3">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_c6fc3_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_c6fc3_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_c6fc3_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_c6fc3_level0_col3" class="col_heading level0 col3" >cadex</th>
      <th id="T_c6fc3_level0_col4" class="col_heading level0 col4" >alibi_nograd</th>
      <th id="T_c6fc3_level0_col5" class="col_heading level0 col5" >dice</th>
      <th id="T_c6fc3_level0_col6" class="col_heading level0 col6" >growingspheres</th>
      <th id="T_c6fc3_level0_col7" class="col_heading level0 col7" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c6fc3_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_c6fc3_row0_col0" class="data row0 col0" >4.73</td>
      <td id="T_c6fc3_row0_col1" class="data row0 col1" >4.05</td>
      <td id="T_c6fc3_row0_col2" class="data row0 col2" >3.86</td>
      <td id="T_c6fc3_row0_col3" class="data row0 col3" >4.03</td>
      <td id="T_c6fc3_row0_col4" class="data row0 col4" >3.85</td>
      <td id="T_c6fc3_row0_col5" class="data row0 col5" >3.94</td>
      <td id="T_c6fc3_row0_col6" class="data row0 col6" >🥇3.55</td>
      <td id="T_c6fc3_row0_col7" class="data row0 col7" >1598</td>
    </tr>
    <tr>
      <th id="T_c6fc3_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_c6fc3_row1_col0" class="data row1 col0" >3.59</td>
      <td id="T_c6fc3_row1_col1" class="data row1 col1" >3.29</td>
      <td id="T_c6fc3_row1_col2" class="data row1 col2" >4.19</td>
      <td id="T_c6fc3_row1_col3" class="data row1 col3" >5.37</td>
      <td id="T_c6fc3_row1_col4" class="data row1 col4" >4.17</td>
      <td id="T_c6fc3_row1_col5" class="data row1 col5" >🥇2.86</td>
      <td id="T_c6fc3_row1_col6" class="data row1 col6" >4.54</td>
      <td id="T_c6fc3_row1_col7" class="data row1 col7" >1598</td>
    </tr>
    <tr>
      <th id="T_c6fc3_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_c6fc3_row2_col0" class="data row2 col0" >5.37</td>
      <td id="T_c6fc3_row2_col1" class="data row2 col1" >4.98</td>
      <td id="T_c6fc3_row2_col2" class="data row2 col2" >3.23</td>
      <td id="T_c6fc3_row2_col3" class="data row2 col3" >3.63</td>
      <td id="T_c6fc3_row2_col4" class="data row2 col4" >3.25</td>
      <td id="T_c6fc3_row2_col5" class="data row2 col5" >5.58</td>
      <td id="T_c6fc3_row2_col6" class="data row2 col6" >🥇1.95</td>
      <td id="T_c6fc3_row2_col7" class="data row2 col7" >1598</td>
    </tr>
    <tr>
      <th id="T_c6fc3_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_c6fc3_row3_col0" class="data row3 col0" >4.60</td>
      <td id="T_c6fc3_row3_col1" class="data row3 col1" >3.94</td>
      <td id="T_c6fc3_row3_col2" class="data row3 col2" >🥇3.28</td>
      <td id="T_c6fc3_row3_col3" class="data row3 col3" >4.63</td>
      <td id="T_c6fc3_row3_col4" class="data row3 col4" >🥇3.23</td>
      <td id="T_c6fc3_row3_col5" class="data row3 col5" >4.62</td>
      <td id="T_c6fc3_row3_col6" class="data row3 col6" >3.71</td>
      <td id="T_c6fc3_row3_col7" class="data row3 col7" >1598</td>
    </tr>
    <tr>
      <th id="T_c6fc3_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_c6fc3_row4_col0" class="data row4 col0" >5.15</td>
      <td id="T_c6fc3_row4_col1" class="data row4 col1" >5.04</td>
      <td id="T_c6fc3_row4_col2" class="data row4 col2" >3.25</td>
      <td id="T_c6fc3_row4_col3" class="data row4 col3" >3.55</td>
      <td id="T_c6fc3_row4_col4" class="data row4 col4" >3.23</td>
      <td id="T_c6fc3_row4_col5" class="data row4 col5" >5.55</td>
      <td id="T_c6fc3_row4_col6" class="data row4 col6" >🥇2.23</td>
      <td id="T_c6fc3_row4_col7" class="data row4 col7" >1598</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for mixed datasets

</div>


<table id="T_3e98d">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_3e98d_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_3e98d_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_3e98d_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_3e98d_level0_col3" class="col_heading level0 col3" >cadex</th>
      <th id="T_3e98d_level0_col4" class="col_heading level0 col4" >alibi_nograd</th>
      <th id="T_3e98d_level0_col5" class="col_heading level0 col5" >dice</th>
      <th id="T_3e98d_level0_col6" class="col_heading level0 col6" >growingspheres</th>
      <th id="T_3e98d_level0_col7" class="col_heading level0 col7" >N</th>
    </tr>
    <tr>
      <th class="index_name level0" >index</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_3e98d_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_3e98d_row0_col0" class="data row0 col0" >🥇3.18</td>
      <td id="T_3e98d_row0_col1" class="data row0 col1" >4.54</td>
      <td id="T_3e98d_row0_col2" class="data row0 col2" >3.69</td>
      <td id="T_3e98d_row0_col3" class="data row0 col3" >🥇3.44</td>
      <td id="T_3e98d_row0_col4" class="data row0 col4" >3.99</td>
      <td id="T_3e98d_row0_col5" class="data row0 col5" >4.09</td>
      <td id="T_3e98d_row0_col6" class="data row0 col6" >5.07</td>
      <td id="T_3e98d_row0_col7" class="data row0 col7" >1000</td>
    </tr>
    <tr>
      <th id="T_3e98d_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_3e98d_row1_col0" class="data row1 col0" >🥇2.81</td>
      <td id="T_3e98d_row1_col1" class="data row1 col1" >4.48</td>
      <td id="T_3e98d_row1_col2" class="data row1 col2" >3.78</td>
      <td id="T_3e98d_row1_col3" class="data row1 col3" >3.91</td>
      <td id="T_3e98d_row1_col4" class="data row1 col4" >3.92</td>
      <td id="T_3e98d_row1_col5" class="data row1 col5" >4.03</td>
      <td id="T_3e98d_row1_col6" class="data row1 col6" >5.07</td>
      <td id="T_3e98d_row1_col7" class="data row1 col7" >1000</td>
    </tr>
    <tr>
      <th id="T_3e98d_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_3e98d_row2_col0" class="data row2 col0" >🥇3.04</td>
      <td id="T_3e98d_row2_col1" class="data row2 col1" >4.55</td>
      <td id="T_3e98d_row2_col2" class="data row2 col2" >3.64</td>
      <td id="T_3e98d_row2_col3" class="data row2 col3" >3.68</td>
      <td id="T_3e98d_row2_col4" class="data row2 col4" >3.74</td>
      <td id="T_3e98d_row2_col5" class="data row2 col5" >4.28</td>
      <td id="T_3e98d_row2_col6" class="data row2 col6" >5.07</td>
      <td id="T_3e98d_row2_col7" class="data row2 col7" >1000</td>
    </tr>
    <tr>
      <th id="T_3e98d_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_3e98d_row3_col0" class="data row3 col0" >🥇3.45</td>
      <td id="T_3e98d_row3_col1" class="data row3 col1" >4.37</td>
      <td id="T_3e98d_row3_col2" class="data row3 col2" >3.70</td>
      <td id="T_3e98d_row3_col3" class="data row3 col3" >🥇3.33</td>
      <td id="T_3e98d_row3_col4" class="data row3 col4" >3.76</td>
      <td id="T_3e98d_row3_col5" class="data row3 col5" >4.51</td>
      <td id="T_3e98d_row3_col6" class="data row3 col6" >4.88</td>
      <td id="T_3e98d_row3_col7" class="data row3 col7" >1000</td>
    </tr>
    <tr>
      <th id="T_3e98d_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_3e98d_row4_col0" class="data row4 col0" >🥇3.15</td>
      <td id="T_3e98d_row4_col1" class="data row4 col1" >4.63</td>
      <td id="T_3e98d_row4_col2" class="data row4 col2" >3.50</td>
      <td id="T_3e98d_row4_col3" class="data row4 col3" >3.55</td>
      <td id="T_3e98d_row4_col4" class="data row4 col4" >3.81</td>
      <td id="T_3e98d_row4_col5" class="data row4 col5" >4.28</td>
      <td id="T_3e98d_row4_col6" class="data row4 col6" >5.07</td>
      <td id="T_3e98d_row4_col7" class="data row4 col7" >1000</td>
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
