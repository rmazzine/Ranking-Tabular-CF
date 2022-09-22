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


<table id="T_b31b3">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_b31b3_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_b31b3_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_b31b3_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_b31b3_level0_col3" class="col_heading level0 col3" >cfnow_random_simple</th>
      <th id="T_b31b3_level0_col4" class="col_heading level0 col4" >cadex</th>
      <th id="T_b31b3_level0_col5" class="col_heading level0 col5" >cfnow_greedy</th>
      <th id="T_b31b3_level0_col6" class="col_heading level0 col6" >cfnow_random</th>
      <th id="T_b31b3_level0_col7" class="col_heading level0 col7" >alibi_nograd</th>
      <th id="T_b31b3_level0_col8" class="col_heading level0 col8" >cfnow_greedy_simple</th>
      <th id="T_b31b3_level0_col9" class="col_heading level0 col9" >dice</th>
      <th id="T_b31b3_level0_col10" class="col_heading level0 col10" >growingspheres</th>
      <th id="T_b31b3_level0_col11" class="col_heading level0 col11" >N</th>
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
      <th class="blank col8" >&nbsp;</th>
      <th class="blank col9" >&nbsp;</th>
      <th class="blank col10" >&nbsp;</th>
      <th class="blank col11" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_b31b3_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_b31b3_row0_col0" class="data row0 col0" >7.01</td>
      <td id="T_b31b3_row0_col1" class="data row0 col1" >8.03</td>
      <td id="T_b31b3_row0_col2" class="data row0 col2" >7.13</td>
      <td id="T_b31b3_row0_col3" class="data row0 col3" >🥇4.27</td>
      <td id="T_b31b3_row0_col4" class="data row0 col4" >5.79</td>
      <td id="T_b31b3_row0_col5" class="data row0 col5" >🥇4.27</td>
      <td id="T_b31b3_row0_col6" class="data row0 col6" >🥇4.27</td>
      <td id="T_b31b3_row0_col7" class="data row0 col7" >7.12</td>
      <td id="T_b31b3_row0_col8" class="data row0 col8" >🥇4.27</td>
      <td id="T_b31b3_row0_col9" class="data row0 col9" >5.91</td>
      <td id="T_b31b3_row0_col10" class="data row0 col10" >7.92</td>
      <td id="T_b31b3_row0_col11" class="data row0 col11" >3925</td>
    </tr>
    <tr>
      <th id="T_b31b3_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_b31b3_row1_col0" class="data row1 col0" >5.70</td>
      <td id="T_b31b3_row1_col1" class="data row1 col1" >7.26</td>
      <td id="T_b31b3_row1_col2" class="data row1 col2" >7.35</td>
      <td id="T_b31b3_row1_col3" class="data row1 col3" >5.28</td>
      <td id="T_b31b3_row1_col4" class="data row1 col4" >8.12</td>
      <td id="T_b31b3_row1_col5" class="data row1 col5" >🥇3.59</td>
      <td id="T_b31b3_row1_col6" class="data row1 col6" >3.99</td>
      <td id="T_b31b3_row1_col7" class="data row1 col7" >7.19</td>
      <td id="T_b31b3_row1_col8" class="data row1 col8" >🥇3.40</td>
      <td id="T_b31b3_row1_col9" class="data row1 col9" >5.51</td>
      <td id="T_b31b3_row1_col10" class="data row1 col10" >8.61</td>
      <td id="T_b31b3_row1_col11" class="data row1 col11" >3925</td>
    </tr>
    <tr>
      <th id="T_b31b3_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_b31b3_row2_col0" class="data row2 col0" >7.36</td>
      <td id="T_b31b3_row2_col1" class="data row2 col1" >8.76</td>
      <td id="T_b31b3_row2_col2" class="data row2 col2" >6.50</td>
      <td id="T_b31b3_row2_col3" class="data row2 col3" >4.80</td>
      <td id="T_b31b3_row2_col4" class="data row2 col4" >6.48</td>
      <td id="T_b31b3_row2_col5" class="data row2 col5" >3.71</td>
      <td id="T_b31b3_row2_col6" class="data row2 col6" >🥇3.24</td>
      <td id="T_b31b3_row2_col7" class="data row2 col7" >6.30</td>
      <td id="T_b31b3_row2_col8" class="data row2 col8" >4.44</td>
      <td id="T_b31b3_row2_col9" class="data row2 col9" >7.79</td>
      <td id="T_b31b3_row2_col10" class="data row2 col10" >6.62</td>
      <td id="T_b31b3_row2_col11" class="data row2 col11" >3925</td>
    </tr>
    <tr>
      <th id="T_b31b3_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_b31b3_row3_col0" class="data row3 col0" >7.42</td>
      <td id="T_b31b3_row3_col1" class="data row3 col1" >8.03</td>
      <td id="T_b31b3_row3_col2" class="data row3 col2" >7.22</td>
      <td id="T_b31b3_row3_col3" class="data row3 col3" >4.19</td>
      <td id="T_b31b3_row3_col4" class="data row3 col4" >7.28</td>
      <td id="T_b31b3_row3_col5" class="data row3 col5" >🥇2.94</td>
      <td id="T_b31b3_row3_col6" class="data row3 col6" >3.32</td>
      <td id="T_b31b3_row3_col7" class="data row3 col7" >6.99</td>
      <td id="T_b31b3_row3_col8" class="data row3 col8" >3.36</td>
      <td id="T_b31b3_row3_col9" class="data row3 col9" >7.11</td>
      <td id="T_b31b3_row3_col10" class="data row3 col10" >8.12</td>
      <td id="T_b31b3_row3_col11" class="data row3 col11" >3925</td>
    </tr>
    <tr>
      <th id="T_b31b3_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_b31b3_row4_col0" class="data row4 col0" >7.37</td>
      <td id="T_b31b3_row4_col1" class="data row4 col1" >8.92</td>
      <td id="T_b31b3_row4_col2" class="data row4 col2" >6.62</td>
      <td id="T_b31b3_row4_col3" class="data row4 col3" >4.49</td>
      <td id="T_b31b3_row4_col4" class="data row4 col4" >6.46</td>
      <td id="T_b31b3_row4_col5" class="data row4 col5" >🥇3.44</td>
      <td id="T_b31b3_row4_col6" class="data row4 col6" >🥇3.45</td>
      <td id="T_b31b3_row4_col7" class="data row4 col7" >6.53</td>
      <td id="T_b31b3_row4_col8" class="data row4 col8" >4.07</td>
      <td id="T_b31b3_row4_col9" class="data row4 col9" >7.73</td>
      <td id="T_b31b3_row4_col10" class="data row4 col10" >6.92</td>
      <td id="T_b31b3_row4_col11" class="data row4 col11" >3925</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for categorical datasets

</div>


<table id="T_a1763">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_a1763_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_a1763_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_a1763_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_a1763_level0_col3" class="col_heading level0 col3" >cfnow_random_simple</th>
      <th id="T_a1763_level0_col4" class="col_heading level0 col4" >cadex</th>
      <th id="T_a1763_level0_col5" class="col_heading level0 col5" >cfnow_greedy</th>
      <th id="T_a1763_level0_col6" class="col_heading level0 col6" >cfnow_random</th>
      <th id="T_a1763_level0_col7" class="col_heading level0 col7" >alibi_nograd</th>
      <th id="T_a1763_level0_col8" class="col_heading level0 col8" >cfnow_greedy_simple</th>
      <th id="T_a1763_level0_col9" class="col_heading level0 col9" >dice</th>
      <th id="T_a1763_level0_col10" class="col_heading level0 col10" >growingspheres</th>
      <th id="T_a1763_level0_col11" class="col_heading level0 col11" >N</th>
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
      <th class="blank col8" >&nbsp;</th>
      <th class="blank col9" >&nbsp;</th>
      <th class="blank col10" >&nbsp;</th>
      <th class="blank col11" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_a1763_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_a1763_row0_col0" class="data row0 col0" >6.68</td>
      <td id="T_a1763_row0_col1" class="data row0 col1" >9.37</td>
      <td id="T_a1763_row0_col2" class="data row0 col2" >8.08</td>
      <td id="T_a1763_row0_col3" class="data row0 col3" >🥇3.87</td>
      <td id="T_a1763_row0_col4" class="data row0 col4" >5.46</td>
      <td id="T_a1763_row0_col5" class="data row0 col5" >🥇3.87</td>
      <td id="T_a1763_row0_col6" class="data row0 col6" >🥇3.87</td>
      <td id="T_a1763_row0_col7" class="data row0 col7" >7.71</td>
      <td id="T_a1763_row0_col8" class="data row0 col8" >🥇3.87</td>
      <td id="T_a1763_row0_col9" class="data row0 col9" >🥇3.87</td>
      <td id="T_a1763_row0_col10" class="data row0 col10" >9.37</td>
      <td id="T_a1763_row0_col11" class="data row0 col11" >1327</td>
    </tr>
    <tr>
      <th id="T_a1763_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_a1763_row1_col0" class="data row1 col0" >6.27</td>
      <td id="T_a1763_row1_col1" class="data row1 col1" >9.37</td>
      <td id="T_a1763_row1_col2" class="data row1 col2" >8.02</td>
      <td id="T_a1763_row1_col3" class="data row1 col3" >🥇3.37</td>
      <td id="T_a1763_row1_col4" class="data row1 col4" >7.52</td>
      <td id="T_a1763_row1_col5" class="data row1 col5" >🥇3.07</td>
      <td id="T_a1763_row1_col6" class="data row1 col6" >🥇3.01</td>
      <td id="T_a1763_row1_col7" class="data row1 col7" >7.52</td>
      <td id="T_a1763_row1_col8" class="data row1 col8" >🥇3.07</td>
      <td id="T_a1763_row1_col9" class="data row1 col9" >5.40</td>
      <td id="T_a1763_row1_col10" class="data row1 col10" >9.37</td>
      <td id="T_a1763_row1_col11" class="data row1 col11" >1327</td>
    </tr>
    <tr>
      <th id="T_a1763_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_a1763_row2_col0" class="data row2 col0" >6.27</td>
      <td id="T_a1763_row2_col1" class="data row2 col1" >9.37</td>
      <td id="T_a1763_row2_col2" class="data row2 col2" >8.02</td>
      <td id="T_a1763_row2_col3" class="data row2 col3" >🥇3.37</td>
      <td id="T_a1763_row2_col4" class="data row2 col4" >7.52</td>
      <td id="T_a1763_row2_col5" class="data row2 col5" >🥇3.07</td>
      <td id="T_a1763_row2_col6" class="data row2 col6" >🥇3.01</td>
      <td id="T_a1763_row2_col7" class="data row2 col7" >7.52</td>
      <td id="T_a1763_row2_col8" class="data row2 col8" >🥇3.07</td>
      <td id="T_a1763_row2_col9" class="data row2 col9" >5.40</td>
      <td id="T_a1763_row2_col10" class="data row2 col10" >9.37</td>
      <td id="T_a1763_row2_col11" class="data row2 col11" >1327</td>
    </tr>
    <tr>
      <th id="T_a1763_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_a1763_row3_col0" class="data row3 col0" >7.19</td>
      <td id="T_a1763_row3_col1" class="data row3 col1" >9.17</td>
      <td id="T_a1763_row3_col2" class="data row3 col2" >8.55</td>
      <td id="T_a1763_row3_col3" class="data row3 col3" >🥇3.19</td>
      <td id="T_a1763_row3_col4" class="data row3 col4" >7.24</td>
      <td id="T_a1763_row3_col5" class="data row3 col5" >🥇2.90</td>
      <td id="T_a1763_row3_col6" class="data row3 col6" >🥇2.83</td>
      <td id="T_a1763_row3_col7" class="data row3 col7" >7.81</td>
      <td id="T_a1763_row3_col8" class="data row3 col8" >🥇2.90</td>
      <td id="T_a1763_row3_col9" class="data row3 col9" >5.05</td>
      <td id="T_a1763_row3_col10" class="data row3 col10" >9.17</td>
      <td id="T_a1763_row3_col11" class="data row3 col11" >1327</td>
    </tr>
    <tr>
      <th id="T_a1763_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_a1763_row4_col0" class="data row4 col0" >6.34</td>
      <td id="T_a1763_row4_col1" class="data row4 col1" >9.37</td>
      <td id="T_a1763_row4_col2" class="data row4 col2" >7.99</td>
      <td id="T_a1763_row4_col3" class="data row4 col3" >🥇3.44</td>
      <td id="T_a1763_row4_col4" class="data row4 col4" >7.52</td>
      <td id="T_a1763_row4_col5" class="data row4 col5" >🥇3.05</td>
      <td id="T_a1763_row4_col6" class="data row4 col6" >🥇3.11</td>
      <td id="T_a1763_row4_col7" class="data row4 col7" >7.45</td>
      <td id="T_a1763_row4_col8" class="data row4 col8" >🥇3.05</td>
      <td id="T_a1763_row4_col9" class="data row4 col9" >5.30</td>
      <td id="T_a1763_row4_col10" class="data row4 col10" >9.37</td>
      <td id="T_a1763_row4_col11" class="data row4 col11" >1327</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for numerical datasets

</div>


<table id="T_acc24">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_acc24_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_acc24_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_acc24_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_acc24_level0_col3" class="col_heading level0 col3" >cfnow_random_simple</th>
      <th id="T_acc24_level0_col4" class="col_heading level0 col4" >cadex</th>
      <th id="T_acc24_level0_col5" class="col_heading level0 col5" >cfnow_greedy</th>
      <th id="T_acc24_level0_col6" class="col_heading level0 col6" >cfnow_random</th>
      <th id="T_acc24_level0_col7" class="col_heading level0 col7" >alibi_nograd</th>
      <th id="T_acc24_level0_col8" class="col_heading level0 col8" >cfnow_greedy_simple</th>
      <th id="T_acc24_level0_col9" class="col_heading level0 col9" >dice</th>
      <th id="T_acc24_level0_col10" class="col_heading level0 col10" >growingspheres</th>
      <th id="T_acc24_level0_col11" class="col_heading level0 col11" >N</th>
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
      <th class="blank col8" >&nbsp;</th>
      <th class="blank col9" >&nbsp;</th>
      <th class="blank col10" >&nbsp;</th>
      <th class="blank col11" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_acc24_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_acc24_row0_col0" class="data row0 col0" >7.75</td>
      <td id="T_acc24_row0_col1" class="data row0 col1" >6.68</td>
      <td id="T_acc24_row0_col2" class="data row0 col2" >6.37</td>
      <td id="T_acc24_row0_col3" class="data row0 col3" >🥇4.95</td>
      <td id="T_acc24_row0_col4" class="data row0 col4" >6.64</td>
      <td id="T_acc24_row0_col5" class="data row0 col5" >🥇4.95</td>
      <td id="T_acc24_row0_col6" class="data row0 col6" >🥇4.95</td>
      <td id="T_acc24_row0_col7" class="data row0 col7" >6.37</td>
      <td id="T_acc24_row0_col8" class="data row0 col8" >🥇4.95</td>
      <td id="T_acc24_row0_col9" class="data row0 col9" >6.50</td>
      <td id="T_acc24_row0_col10" class="data row0 col10" >5.89</td>
      <td id="T_acc24_row0_col11" class="data row0 col11" >1598</td>
    </tr>
    <tr>
      <th id="T_acc24_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_acc24_row1_col0" class="data row1 col0" >5.72</td>
      <td id="T_acc24_row1_col1" class="data row1 col1" >4.97</td>
      <td id="T_acc24_row1_col2" class="data row1 col2" >6.79</td>
      <td id="T_acc24_row1_col3" class="data row1 col3" >7.60</td>
      <td id="T_acc24_row1_col4" class="data row1 col4" >9.21</td>
      <td id="T_acc24_row1_col5" class="data row1 col5" >4.28</td>
      <td id="T_acc24_row1_col6" class="data row1 col6" >4.96</td>
      <td id="T_acc24_row1_col7" class="data row1 col7" >6.75</td>
      <td id="T_acc24_row1_col8" class="data row1 col8" >🥇3.80</td>
      <td id="T_acc24_row1_col9" class="data row1 col9" >4.32</td>
      <td id="T_acc24_row1_col10" class="data row1 col10" >7.60</td>
      <td id="T_acc24_row1_col11" class="data row1 col11" >1598</td>
    </tr>
    <tr>
      <th id="T_acc24_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_acc24_row2_col0" class="data row2 col0" >8.86</td>
      <td id="T_acc24_row2_col1" class="data row2 col1" >8.41</td>
      <td id="T_acc24_row2_col2" class="data row2 col2" >4.69</td>
      <td id="T_acc24_row2_col3" class="data row2 col3" >6.57</td>
      <td id="T_acc24_row2_col4" class="data row2 col4" >5.36</td>
      <td id="T_acc24_row2_col5" class="data row2 col5" >4.71</td>
      <td id="T_acc24_row2_col6" class="data row2 col6" >4.27</td>
      <td id="T_acc24_row2_col7" class="data row2 col7" >4.68</td>
      <td id="T_acc24_row2_col8" class="data row2 col8" >6.33</td>
      <td id="T_acc24_row2_col9" class="data row2 col9" >9.42</td>
      <td id="T_acc24_row2_col10" class="data row2 col10" >🥇2.71</td>
      <td id="T_acc24_row2_col11" class="data row2 col11" >1598</td>
    </tr>
    <tr>
      <th id="T_acc24_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_acc24_row3_col0" class="data row3 col0" >7.64</td>
      <td id="T_acc24_row3_col1" class="data row3 col1" >6.81</td>
      <td id="T_acc24_row3_col2" class="data row3 col2" >5.86</td>
      <td id="T_acc24_row3_col3" class="data row3 col3" >5.98</td>
      <td id="T_acc24_row3_col4" class="data row3 col4" >8.13</td>
      <td id="T_acc24_row3_col5" class="data row3 col5" >🥇3.41</td>
      <td id="T_acc24_row3_col6" class="data row3 col6" >🥇3.35</td>
      <td id="T_acc24_row3_col7" class="data row3 col7" >5.83</td>
      <td id="T_acc24_row3_col8" class="data row3 col8" >4.44</td>
      <td id="T_acc24_row3_col9" class="data row3 col9" >7.88</td>
      <td id="T_acc24_row3_col10" class="data row3 col10" >6.67</td>
      <td id="T_acc24_row3_col11" class="data row3 col11" >1598</td>
    </tr>
    <tr>
      <th id="T_acc24_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_acc24_row4_col0" class="data row4 col0" >8.56</td>
      <td id="T_acc24_row4_col1" class="data row4 col1" >8.63</td>
      <td id="T_acc24_row4_col2" class="data row4 col2" >5.19</td>
      <td id="T_acc24_row4_col3" class="data row4 col3" >6.30</td>
      <td id="T_acc24_row4_col4" class="data row4 col4" >5.51</td>
      <td id="T_acc24_row4_col5" class="data row4 col5" >4.21</td>
      <td id="T_acc24_row4_col6" class="data row4 col6" >4.00</td>
      <td id="T_acc24_row4_col7" class="data row4 col7" >5.16</td>
      <td id="T_acc24_row4_col8" class="data row4 col8" >5.64</td>
      <td id="T_acc24_row4_col9" class="data row4 col9" >9.36</td>
      <td id="T_acc24_row4_col10" class="data row4 col10" >🥇3.45</td>
      <td id="T_acc24_row4_col11" class="data row4 col11" >1598</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for mixed datasets

</div>


<table id="T_d9ad1">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_d9ad1_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_d9ad1_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_d9ad1_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_d9ad1_level0_col3" class="col_heading level0 col3" >cfnow_random_simple</th>
      <th id="T_d9ad1_level0_col4" class="col_heading level0 col4" >cadex</th>
      <th id="T_d9ad1_level0_col5" class="col_heading level0 col5" >cfnow_greedy</th>
      <th id="T_d9ad1_level0_col6" class="col_heading level0 col6" >cfnow_random</th>
      <th id="T_d9ad1_level0_col7" class="col_heading level0 col7" >alibi_nograd</th>
      <th id="T_d9ad1_level0_col8" class="col_heading level0 col8" >cfnow_greedy_simple</th>
      <th id="T_d9ad1_level0_col9" class="col_heading level0 col9" >dice</th>
      <th id="T_d9ad1_level0_col10" class="col_heading level0 col10" >growingspheres</th>
      <th id="T_d9ad1_level0_col11" class="col_heading level0 col11" >N</th>
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
      <th class="blank col8" >&nbsp;</th>
      <th class="blank col9" >&nbsp;</th>
      <th class="blank col10" >&nbsp;</th>
      <th class="blank col11" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d9ad1_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_d9ad1_row0_col0" class="data row0 col0" >6.27</td>
      <td id="T_d9ad1_row0_col1" class="data row0 col1" >8.40</td>
      <td id="T_d9ad1_row0_col2" class="data row0 col2" >7.06</td>
      <td id="T_d9ad1_row0_col3" class="data row0 col3" >🥇3.73</td>
      <td id="T_d9ad1_row0_col4" class="data row0 col4" >4.88</td>
      <td id="T_d9ad1_row0_col5" class="data row0 col5" >🥇3.73</td>
      <td id="T_d9ad1_row0_col6" class="data row0 col6" >🥇3.73</td>
      <td id="T_d9ad1_row0_col7" class="data row0 col7" >7.53</td>
      <td id="T_d9ad1_row0_col8" class="data row0 col8" >🥇3.73</td>
      <td id="T_d9ad1_row0_col9" class="data row0 col9" >7.70</td>
      <td id="T_d9ad1_row0_col10" class="data row0 col10" >9.23</td>
      <td id="T_d9ad1_row0_col11" class="data row0 col11" >1000</td>
    </tr>
    <tr>
      <th id="T_d9ad1_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_d9ad1_row1_col0" class="data row1 col0" >4.92</td>
      <td id="T_d9ad1_row1_col1" class="data row1 col1" >8.11</td>
      <td id="T_d9ad1_row1_col2" class="data row1 col2" >7.34</td>
      <td id="T_d9ad1_row1_col3" class="data row1 col3" >4.12</td>
      <td id="T_d9ad1_row1_col4" class="data row1 col4" >7.18</td>
      <td id="T_d9ad1_row1_col5" class="data row1 col5" >🥇3.16</td>
      <td id="T_d9ad1_row1_col6" class="data row1 col6" >3.74</td>
      <td id="T_d9ad1_row1_col7" class="data row1 col7" >7.44</td>
      <td id="T_d9ad1_row1_col8" class="data row1 col8" >🥇3.20</td>
      <td id="T_d9ad1_row1_col9" class="data row1 col9" >7.55</td>
      <td id="T_d9ad1_row1_col10" class="data row1 col10" >9.23</td>
      <td id="T_d9ad1_row1_col11" class="data row1 col11" >1000</td>
    </tr>
    <tr>
      <th id="T_d9ad1_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_d9ad1_row2_col0" class="data row2 col0" >6.42</td>
      <td id="T_d9ad1_row2_col1" class="data row2 col1" >8.51</td>
      <td id="T_d9ad1_row2_col2" class="data row2 col2" >7.38</td>
      <td id="T_d9ad1_row2_col3" class="data row2 col3" >3.86</td>
      <td id="T_d9ad1_row2_col4" class="data row2 col4" >6.88</td>
      <td id="T_d9ad1_row2_col5" class="data row2 col5" >2.94</td>
      <td id="T_d9ad1_row2_col6" class="data row2 col6" >🥇1.89</td>
      <td id="T_d9ad1_row2_col7" class="data row2 col7" >7.28</td>
      <td id="T_d9ad1_row2_col8" class="data row2 col8" >3.25</td>
      <td id="T_d9ad1_row2_col9" class="data row2 col9" >8.37</td>
      <td id="T_d9ad1_row2_col10" class="data row2 col10" >9.23</td>
      <td id="T_d9ad1_row2_col11" class="data row2 col11" >1000</td>
    </tr>
    <tr>
      <th id="T_d9ad1_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_d9ad1_row3_col0" class="data row3 col0" >7.38</td>
      <td id="T_d9ad1_row3_col1" class="data row3 col1" >8.46</td>
      <td id="T_d9ad1_row3_col2" class="data row3 col2" >7.61</td>
      <td id="T_d9ad1_row3_col3" class="data row3 col3" >🥇2.67</td>
      <td id="T_d9ad1_row3_col4" class="data row3 col4" >6.00</td>
      <td id="T_d9ad1_row3_col5" class="data row3 col5" >🥇2.27</td>
      <td id="T_d9ad1_row3_col6" class="data row3 col6" >3.92</td>
      <td id="T_d9ad1_row3_col7" class="data row3 col7" >7.76</td>
      <td id="T_d9ad1_row3_col8" class="data row3 col8" >🥇2.27</td>
      <td id="T_d9ad1_row3_col9" class="data row3 col9" >8.62</td>
      <td id="T_d9ad1_row3_col10" class="data row3 col10" >9.04</td>
      <td id="T_d9ad1_row3_col11" class="data row3 col11" >1000</td>
    </tr>
    <tr>
      <th id="T_d9ad1_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_d9ad1_row4_col0" class="data row4 col0" >6.82</td>
      <td id="T_d9ad1_row4_col1" class="data row4 col1" >8.79</td>
      <td id="T_d9ad1_row4_col2" class="data row4 col2" >7.08</td>
      <td id="T_d9ad1_row4_col3" class="data row4 col3" >🥇3.01</td>
      <td id="T_d9ad1_row4_col4" class="data row4 col4" >6.56</td>
      <td id="T_d9ad1_row4_col5" class="data row4 col5" >🥇2.73</td>
      <td id="T_d9ad1_row4_col6" class="data row4 col6" >🥇3.00</td>
      <td id="T_d9ad1_row4_col7" class="data row4 col7" >7.50</td>
      <td id="T_d9ad1_row4_col8" class="data row4 col8" >🥇2.91</td>
      <td id="T_d9ad1_row4_col9" class="data row4 col9" >8.36</td>
      <td id="T_d9ad1_row4_col10" class="data row4 col10" >9.23</td>
      <td id="T_d9ad1_row4_col11" class="data row4 col11" >1000</td>
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
