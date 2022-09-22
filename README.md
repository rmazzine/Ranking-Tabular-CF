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


<table id="T_a8e07">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_a8e07_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_a8e07_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_a8e07_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_a8e07_level0_col3" class="col_heading level0 col3" >cadex</th>
      <th id="T_a8e07_level0_col4" class="col_heading level0 col4" >cfnow_greedy</th>
      <th id="T_a8e07_level0_col5" class="col_heading level0 col5" >cfnow_random</th>
      <th id="T_a8e07_level0_col6" class="col_heading level0 col6" >alibi_nograd</th>
      <th id="T_a8e07_level0_col7" class="col_heading level0 col7" >cfnow_greedy_simple</th>
      <th id="T_a8e07_level0_col8" class="col_heading level0 col8" >dice</th>
      <th id="T_a8e07_level0_col9" class="col_heading level0 col9" >growingspheres</th>
      <th id="T_a8e07_level0_col10" class="col_heading level0 col10" >N</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_a8e07_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_a8e07_row0_col0" class="data row0 col0" >6.26</td>
      <td id="T_a8e07_row0_col1" class="data row0 col1" >7.19</td>
      <td id="T_a8e07_row0_col2" class="data row0 col2" >6.37</td>
      <td id="T_a8e07_row0_col3" class="data row0 col3" >5.15</td>
      <td id="T_a8e07_row0_col4" class="data row0 col4" >🥇3.77</td>
      <td id="T_a8e07_row0_col5" class="data row0 col5" >🥇3.77</td>
      <td id="T_a8e07_row0_col6" class="data row0 col6" >6.36</td>
      <td id="T_a8e07_row0_col7" class="data row0 col7" >🥇3.77</td>
      <td id="T_a8e07_row0_col8" class="data row0 col8" >5.27</td>
      <td id="T_a8e07_row0_col9" class="data row0 col9" >7.09</td>
      <td id="T_a8e07_row0_col10" class="data row0 col10" >3925</td>
    </tr>
    <tr>
      <th id="T_a8e07_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_a8e07_row1_col0" class="data row1 col0" >5.11</td>
      <td id="T_a8e07_row1_col1" class="data row1 col1" >6.56</td>
      <td id="T_a8e07_row1_col2" class="data row1 col2" >6.68</td>
      <td id="T_a8e07_row1_col3" class="data row1 col3" >7.17</td>
      <td id="T_a8e07_row1_col4" class="data row1 col4" >🥇3.33</td>
      <td id="T_a8e07_row1_col5" class="data row1 col5" >3.69</td>
      <td id="T_a8e07_row1_col6" class="data row1 col6" >6.54</td>
      <td id="T_a8e07_row1_col7" class="data row1 col7" >🥇3.15</td>
      <td id="T_a8e07_row1_col8" class="data row1 col8" >4.90</td>
      <td id="T_a8e07_row1_col9" class="data row1 col9" >7.86</td>
      <td id="T_a8e07_row1_col10" class="data row1 col10" >3925</td>
    </tr>
    <tr>
      <th id="T_a8e07_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_a8e07_row2_col0" class="data row2 col0" >6.58</td>
      <td id="T_a8e07_row2_col1" class="data row2 col1" >7.86</td>
      <td id="T_a8e07_row2_col2" class="data row2 col2" >5.85</td>
      <td id="T_a8e07_row2_col3" class="data row2 col3" >5.74</td>
      <td id="T_a8e07_row2_col4" class="data row2 col4" >3.37</td>
      <td id="T_a8e07_row2_col5" class="data row2 col5" >🥇3.04</td>
      <td id="T_a8e07_row2_col6" class="data row2 col6" >5.68</td>
      <td id="T_a8e07_row2_col7" class="data row2 col7" >4.03</td>
      <td id="T_a8e07_row2_col8" class="data row2 col8" >6.88</td>
      <td id="T_a8e07_row2_col9" class="data row2 col9" >5.96</td>
      <td id="T_a8e07_row2_col10" class="data row2 col10" >3925</td>
    </tr>
    <tr>
      <th id="T_a8e07_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_a8e07_row3_col0" class="data row3 col0" >6.59</td>
      <td id="T_a8e07_row3_col1" class="data row3 col1" >7.20</td>
      <td id="T_a8e07_row3_col2" class="data row3 col2" >6.44</td>
      <td id="T_a8e07_row3_col3" class="data row3 col3" >6.35</td>
      <td id="T_a8e07_row3_col4" class="data row3 col4" >🥇2.60</td>
      <td id="T_a8e07_row3_col5" class="data row3 col5" >2.99</td>
      <td id="T_a8e07_row3_col6" class="data row3 col6" >6.24</td>
      <td id="T_a8e07_row3_col7" class="data row3 col7" >3.02</td>
      <td id="T_a8e07_row3_col8" class="data row3 col8" >6.28</td>
      <td id="T_a8e07_row3_col9" class="data row3 col9" >7.30</td>
      <td id="T_a8e07_row3_col10" class="data row3 col10" >3925</td>
    </tr>
    <tr>
      <th id="T_a8e07_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_a8e07_row4_col0" class="data row4 col0" >6.57</td>
      <td id="T_a8e07_row4_col1" class="data row4 col1" >8.00</td>
      <td id="T_a8e07_row4_col2" class="data row4 col2" >5.94</td>
      <td id="T_a8e07_row4_col3" class="data row4 col3" >5.71</td>
      <td id="T_a8e07_row4_col4" class="data row4 col4" >🥇3.08</td>
      <td id="T_a8e07_row4_col5" class="data row4 col5" >🥇3.10</td>
      <td id="T_a8e07_row4_col6" class="data row4 col6" >5.87</td>
      <td id="T_a8e07_row4_col7" class="data row4 col7" >3.65</td>
      <td id="T_a8e07_row4_col8" class="data row4 col8" >6.84</td>
      <td id="T_a8e07_row4_col9" class="data row4 col9" >6.24</td>
      <td id="T_a8e07_row4_col10" class="data row4 col10" >3925</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for categorical datasets

</div>


<table id="T_bec19">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_bec19_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_bec19_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_bec19_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_bec19_level0_col3" class="col_heading level0 col3" >cadex</th>
      <th id="T_bec19_level0_col4" class="col_heading level0 col4" >cfnow_greedy</th>
      <th id="T_bec19_level0_col5" class="col_heading level0 col5" >cfnow_random</th>
      <th id="T_bec19_level0_col6" class="col_heading level0 col6" >alibi_nograd</th>
      <th id="T_bec19_level0_col7" class="col_heading level0 col7" >cfnow_greedy_simple</th>
      <th id="T_bec19_level0_col8" class="col_heading level0 col8" >dice</th>
      <th id="T_bec19_level0_col9" class="col_heading level0 col9" >growingspheres</th>
      <th id="T_bec19_level0_col10" class="col_heading level0 col10" >N</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_bec19_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_bec19_row0_col0" class="data row0 col0" >5.92</td>
      <td id="T_bec19_row0_col1" class="data row0 col1" >8.37</td>
      <td id="T_bec19_row0_col2" class="data row0 col2" >7.20</td>
      <td id="T_bec19_row0_col3" class="data row0 col3" >4.81</td>
      <td id="T_bec19_row0_col4" class="data row0 col4" >🥇3.37</td>
      <td id="T_bec19_row0_col5" class="data row0 col5" >🥇3.37</td>
      <td id="T_bec19_row0_col6" class="data row0 col6" >6.86</td>
      <td id="T_bec19_row0_col7" class="data row0 col7" >🥇3.37</td>
      <td id="T_bec19_row0_col8" class="data row0 col8" >🥇3.37</td>
      <td id="T_bec19_row0_col9" class="data row0 col9" >8.37</td>
      <td id="T_bec19_row0_col10" class="data row0 col10" >1327</td>
    </tr>
    <tr>
      <th id="T_bec19_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_bec19_row1_col0" class="data row1 col0" >5.52</td>
      <td id="T_bec19_row1_col1" class="data row1 col1" >8.37</td>
      <td id="T_bec19_row1_col2" class="data row1 col2" >7.12</td>
      <td id="T_bec19_row1_col3" class="data row1 col3" >6.53</td>
      <td id="T_bec19_row1_col4" class="data row1 col4" >🥇2.63</td>
      <td id="T_bec19_row1_col5" class="data row1 col5" >🥇2.58</td>
      <td id="T_bec19_row1_col6" class="data row1 col6" >6.67</td>
      <td id="T_bec19_row1_col7" class="data row1 col7" >🥇2.63</td>
      <td id="T_bec19_row1_col8" class="data row1 col8" >4.58</td>
      <td id="T_bec19_row1_col9" class="data row1 col9" >8.37</td>
      <td id="T_bec19_row1_col10" class="data row1 col10" >1327</td>
    </tr>
    <tr>
      <th id="T_bec19_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_bec19_row2_col0" class="data row2 col0" >5.52</td>
      <td id="T_bec19_row2_col1" class="data row2 col1" >8.37</td>
      <td id="T_bec19_row2_col2" class="data row2 col2" >7.12</td>
      <td id="T_bec19_row2_col3" class="data row2 col3" >6.53</td>
      <td id="T_bec19_row2_col4" class="data row2 col4" >🥇2.63</td>
      <td id="T_bec19_row2_col5" class="data row2 col5" >🥇2.58</td>
      <td id="T_bec19_row2_col6" class="data row2 col6" >6.67</td>
      <td id="T_bec19_row2_col7" class="data row2 col7" >🥇2.63</td>
      <td id="T_bec19_row2_col8" class="data row2 col8" >4.58</td>
      <td id="T_bec19_row2_col9" class="data row2 col9" >8.37</td>
      <td id="T_bec19_row2_col10" class="data row2 col10" >1327</td>
    </tr>
    <tr>
      <th id="T_bec19_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_bec19_row3_col0" class="data row3 col0" >6.35</td>
      <td id="T_bec19_row3_col1" class="data row3 col1" >8.17</td>
      <td id="T_bec19_row3_col2" class="data row3 col2" >7.60</td>
      <td id="T_bec19_row3_col3" class="data row3 col3" >6.24</td>
      <td id="T_bec19_row3_col4" class="data row3 col4" >🥇2.45</td>
      <td id="T_bec19_row3_col5" class="data row3 col5" >🥇2.40</td>
      <td id="T_bec19_row3_col6" class="data row3 col6" >6.92</td>
      <td id="T_bec19_row3_col7" class="data row3 col7" >🥇2.46</td>
      <td id="T_bec19_row3_col8" class="data row3 col8" >4.23</td>
      <td id="T_bec19_row3_col9" class="data row3 col9" >8.17</td>
      <td id="T_bec19_row3_col10" class="data row3 col10" >1327</td>
    </tr>
    <tr>
      <th id="T_bec19_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_bec19_row4_col0" class="data row4 col0" >5.58</td>
      <td id="T_bec19_row4_col1" class="data row4 col1" >8.37</td>
      <td id="T_bec19_row4_col2" class="data row4 col2" >7.09</td>
      <td id="T_bec19_row4_col3" class="data row4 col3" >6.53</td>
      <td id="T_bec19_row4_col4" class="data row4 col4" >🥇2.63</td>
      <td id="T_bec19_row4_col5" class="data row4 col5" >🥇2.68</td>
      <td id="T_bec19_row4_col6" class="data row4 col6" >6.61</td>
      <td id="T_bec19_row4_col7" class="data row4 col7" >🥇2.63</td>
      <td id="T_bec19_row4_col8" class="data row4 col8" >4.50</td>
      <td id="T_bec19_row4_col9" class="data row4 col9" >8.37</td>
      <td id="T_bec19_row4_col10" class="data row4 col10" >1327</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for numerical datasets

</div>


<table id="T_e3d47">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_e3d47_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_e3d47_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_e3d47_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_e3d47_level0_col3" class="col_heading level0 col3" >cadex</th>
      <th id="T_e3d47_level0_col4" class="col_heading level0 col4" >cfnow_greedy</th>
      <th id="T_e3d47_level0_col5" class="col_heading level0 col5" >cfnow_random</th>
      <th id="T_e3d47_level0_col6" class="col_heading level0 col6" >alibi_nograd</th>
      <th id="T_e3d47_level0_col7" class="col_heading level0 col7" >cfnow_greedy_simple</th>
      <th id="T_e3d47_level0_col8" class="col_heading level0 col8" >dice</th>
      <th id="T_e3d47_level0_col9" class="col_heading level0 col9" >growingspheres</th>
      <th id="T_e3d47_level0_col10" class="col_heading level0 col10" >N</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e3d47_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_e3d47_row0_col0" class="data row0 col0" >6.99</td>
      <td id="T_e3d47_row0_col1" class="data row0 col1" >6.02</td>
      <td id="T_e3d47_row0_col2" class="data row0 col2" >5.75</td>
      <td id="T_e3d47_row0_col3" class="data row0 col3" >5.99</td>
      <td id="T_e3d47_row0_col4" class="data row0 col4" >🥇4.45</td>
      <td id="T_e3d47_row0_col5" class="data row0 col5" >🥇4.45</td>
      <td id="T_e3d47_row0_col6" class="data row0 col6" >5.74</td>
      <td id="T_e3d47_row0_col7" class="data row0 col7" >🥇4.45</td>
      <td id="T_e3d47_row0_col8" class="data row0 col8" >5.86</td>
      <td id="T_e3d47_row0_col9" class="data row0 col9" >5.31</td>
      <td id="T_e3d47_row0_col10" class="data row0 col10" >1598</td>
    </tr>
    <tr>
      <th id="T_e3d47_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_e3d47_row1_col0" class="data row1 col0" >5.21</td>
      <td id="T_e3d47_row1_col1" class="data row1 col1" >4.64</td>
      <td id="T_e3d47_row1_col2" class="data row1 col2" >6.44</td>
      <td id="T_e3d47_row1_col3" class="data row1 col3" >8.33</td>
      <td id="T_e3d47_row1_col4" class="data row1 col4" >4.19</td>
      <td id="T_e3d47_row1_col5" class="data row1 col5" >4.84</td>
      <td id="T_e3d47_row1_col6" class="data row1 col6" >6.40</td>
      <td id="T_e3d47_row1_col7" class="data row1 col7" >🥇3.73</td>
      <td id="T_e3d47_row1_col8" class="data row1 col8" >🥇4.02</td>
      <td id="T_e3d47_row1_col9" class="data row1 col9" >7.20</td>
      <td id="T_e3d47_row1_col10" class="data row1 col10" >1598</td>
    </tr>
    <tr>
      <th id="T_e3d47_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_e3d47_row2_col0" class="data row2 col0" >8.05</td>
      <td id="T_e3d47_row2_col1" class="data row2 col1" >7.63</td>
      <td id="T_e3d47_row2_col2" class="data row2 col2" >4.39</td>
      <td id="T_e3d47_row2_col3" class="data row2 col3" >4.99</td>
      <td id="T_e3d47_row2_col4" class="data row2 col4" >4.44</td>
      <td id="T_e3d47_row2_col5" class="data row2 col5" >4.22</td>
      <td id="T_e3d47_row2_col6" class="data row2 col6" >4.38</td>
      <td id="T_e3d47_row2_col7" class="data row2 col7" >5.89</td>
      <td id="T_e3d47_row2_col8" class="data row2 col8" >8.48</td>
      <td id="T_e3d47_row2_col9" class="data row2 col9" >🥇2.53</td>
      <td id="T_e3d47_row2_col10" class="data row2 col10" >1598</td>
    </tr>
    <tr>
      <th id="T_e3d47_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_e3d47_row3_col0" class="data row3 col0" >6.92</td>
      <td id="T_e3d47_row3_col1" class="data row3 col1" >6.22</td>
      <td id="T_e3d47_row3_col2" class="data row3 col2" >5.36</td>
      <td id="T_e3d47_row3_col3" class="data row3 col3" >7.27</td>
      <td id="T_e3d47_row3_col4" class="data row3 col4" >🥇3.18</td>
      <td id="T_e3d47_row3_col5" class="data row3 col5" >🥇3.29</td>
      <td id="T_e3d47_row3_col6" class="data row3 col6" >5.34</td>
      <td id="T_e3d47_row3_col7" class="data row3 col7" >4.19</td>
      <td id="T_e3d47_row3_col8" class="data row3 col8" >7.14</td>
      <td id="T_e3d47_row3_col9" class="data row3 col9" >6.10</td>
      <td id="T_e3d47_row3_col10" class="data row3 col10" >1598</td>
    </tr>
    <tr>
      <th id="T_e3d47_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_e3d47_row4_col0" class="data row4 col0" >7.79</td>
      <td id="T_e3d47_row4_col1" class="data row4 col1" >7.82</td>
      <td id="T_e3d47_row4_col2" class="data row4 col2" >4.81</td>
      <td id="T_e3d47_row4_col3" class="data row4 col3" >5.12</td>
      <td id="T_e3d47_row4_col4" class="data row4 col4" >3.94</td>
      <td id="T_e3d47_row4_col5" class="data row4 col5" >3.81</td>
      <td id="T_e3d47_row4_col6" class="data row4 col6" >4.79</td>
      <td id="T_e3d47_row4_col7" class="data row4 col7" >5.25</td>
      <td id="T_e3d47_row4_col8" class="data row4 col8" >8.45</td>
      <td id="T_e3d47_row4_col9" class="data row4 col9" >🥇3.22</td>
      <td id="T_e3d47_row4_col10" class="data row4 col10" >1598</td>
    </tr>
  </tbody>
</table>


<div style="font-style: italic;" markdown="1">

### Ranking for mixed datasets

</div>


<table id="T_63af4">
  <thead>
    <tr>
      <th class="index_name level0" >framework</th>
      <th id="T_63af4_level0_col0" class="col_heading level0 col0" >synas</th>
      <th id="T_63af4_level0_col1" class="col_heading level0 col1" >sedc</th>
      <th id="T_63af4_level0_col2" class="col_heading level0 col2" >alibi</th>
      <th id="T_63af4_level0_col3" class="col_heading level0 col3" >cadex</th>
      <th id="T_63af4_level0_col4" class="col_heading level0 col4" >cfnow_greedy</th>
      <th id="T_63af4_level0_col5" class="col_heading level0 col5" >cfnow_random</th>
      <th id="T_63af4_level0_col6" class="col_heading level0 col6" >alibi_nograd</th>
      <th id="T_63af4_level0_col7" class="col_heading level0 col7" >cfnow_greedy_simple</th>
      <th id="T_63af4_level0_col8" class="col_heading level0 col8" >dice</th>
      <th id="T_63af4_level0_col9" class="col_heading level0 col9" >growingspheres</th>
      <th id="T_63af4_level0_col10" class="col_heading level0 col10" >N</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_63af4_level0_row0" class="row_heading level0 row0" >validity</th>
      <td id="T_63af4_row0_col0" class="data row0 col0" >5.54</td>
      <td id="T_63af4_row0_col1" class="data row0 col1" >7.48</td>
      <td id="T_63af4_row0_col2" class="data row0 col2" >6.26</td>
      <td id="T_63af4_row0_col3" class="data row0 col3" >4.27</td>
      <td id="T_63af4_row0_col4" class="data row0 col4" >🥇3.23</td>
      <td id="T_63af4_row0_col5" class="data row0 col5" >🥇3.23</td>
      <td id="T_63af4_row0_col6" class="data row0 col6" >6.68</td>
      <td id="T_63af4_row0_col7" class="data row0 col7" >🥇3.23</td>
      <td id="T_63af4_row0_col8" class="data row0 col8" >6.84</td>
      <td id="T_63af4_row0_col9" class="data row0 col9" >8.23</td>
      <td id="T_63af4_row0_col10" class="data row0 col10" >1000</td>
    </tr>
    <tr>
      <th id="T_63af4_level0_row1" class="row_heading level0 row1" >sparsity</th>
      <td id="T_63af4_row1_col0" class="data row1 col0" >4.41</td>
      <td id="T_63af4_row1_col1" class="data row1 col1" >7.24</td>
      <td id="T_63af4_row1_col2" class="data row1 col2" >6.47</td>
      <td id="T_63af4_row1_col3" class="data row1 col3" >6.18</td>
      <td id="T_63af4_row1_col4" class="data row1 col4" >🥇2.89</td>
      <td id="T_63af4_row1_col5" class="data row1 col5" >3.34</td>
      <td id="T_63af4_row1_col6" class="data row1 col6" >6.60</td>
      <td id="T_63af4_row1_col7" class="data row1 col7" >🥇2.92</td>
      <td id="T_63af4_row1_col8" class="data row1 col8" >6.72</td>
      <td id="T_63af4_row1_col9" class="data row1 col9" >8.23</td>
      <td id="T_63af4_row1_col10" class="data row1 col10" >1000</td>
    </tr>
    <tr>
      <th id="T_63af4_level0_row2" class="row_heading level0 row2" >L2</th>
      <td id="T_63af4_row2_col0" class="data row2 col0" >5.64</td>
      <td id="T_63af4_row2_col1" class="data row2 col1" >7.57</td>
      <td id="T_63af4_row2_col2" class="data row2 col2" >6.49</td>
      <td id="T_63af4_row2_col3" class="data row2 col3" >5.89</td>
      <td id="T_63af4_row2_col4" class="data row2 col4" >2.66</td>
      <td id="T_63af4_row2_col5" class="data row2 col5" >🥇1.74</td>
      <td id="T_63af4_row2_col6" class="data row2 col6" >6.45</td>
      <td id="T_63af4_row2_col7" class="data row2 col7" >2.93</td>
      <td id="T_63af4_row2_col8" class="data row2 col8" >7.39</td>
      <td id="T_63af4_row2_col9" class="data row2 col9" >8.23</td>
      <td id="T_63af4_row2_col10" class="data row2 col10" >1000</td>
    </tr>
    <tr>
      <th id="T_63af4_level0_row3" class="row_heading level0 row3" >MAD</th>
      <td id="T_63af4_row3_col0" class="data row3 col0" >6.39</td>
      <td id="T_63af4_row3_col1" class="data row3 col1" >7.46</td>
      <td id="T_63af4_row3_col2" class="data row3 col2" >6.62</td>
      <td id="T_63af4_row3_col3" class="data row3 col3" >5.03</td>
      <td id="T_63af4_row3_col4" class="data row3 col4" >🥇1.88</td>
      <td id="T_63af4_row3_col5" class="data row3 col5" >3.29</td>
      <td id="T_63af4_row3_col6" class="data row3 col6" >6.77</td>
      <td id="T_63af4_row3_col7" class="data row3 col7" >🥇1.89</td>
      <td id="T_63af4_row3_col8" class="data row3 col8" >7.63</td>
      <td id="T_63af4_row3_col9" class="data row3 col9" >8.04</td>
      <td id="T_63af4_row3_col10" class="data row3 col10" >1000</td>
    </tr>
    <tr>
      <th id="T_63af4_level0_row4" class="row_heading level0 row4" >MD</th>
      <td id="T_63af4_row4_col0" class="data row4 col0" >5.95</td>
      <td id="T_63af4_row4_col1" class="data row4 col1" >7.79</td>
      <td id="T_63af4_row4_col2" class="data row4 col2" >6.21</td>
      <td id="T_63af4_row4_col3" class="data row4 col3" >5.57</td>
      <td id="T_63af4_row4_col4" class="data row4 col4" >🥇2.29</td>
      <td id="T_63af4_row4_col5" class="data row4 col5" >🥇2.53</td>
      <td id="T_63af4_row4_col6" class="data row4 col6" >6.61</td>
      <td id="T_63af4_row4_col7" class="data row4 col7" >🥇2.44</td>
      <td id="T_63af4_row4_col8" class="data row4 col8" >7.38</td>
      <td id="T_63af4_row4_col9" class="data row4 col9" >8.23</td>
      <td id="T_63af4_row4_col10" class="data row4 col10" >1000</td>
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
