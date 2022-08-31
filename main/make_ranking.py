import os
import copy
from collections import defaultdict

import scipy as sp
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cvnt005 = { 2: 1.960, 3: 2.344, 4: 2.569, 5: 2.728, 6: 2.850, 7: 2.948, 8: 3.031, 9: 3.102, 10: 3.164, 11: 3.219,
            12: 3.268, 13: 3.313, 14: 3.354, 15: 3.391, 16: 3.426, 17: 3.458, 18: 3.489, 19: 3.517, 20: 3.544,
            21: 3.569, 22: 3.593, 23: 3.616, 24: 3.637, 25: 3.658, 26: 3.678, 27: 3.696, 28: 3.714, 29: 3.732,
            30: 3.749, 31: 3.765, 32: 3.780, 33: 3.795, 34: 3.810, 35: 3.824, 36: 3.837, 37: 3.850, 38: 3.863,
            39: 3.876, 40: 3.888, 41: 3.899, 42: 3.911, 43: 3.922, 44: 3.933, 45: 3.943, 46: 3.954, 47: 3.964,
            48: 3.973, 49: 3.983, 50: 3.992, }


def generate_color_pallete(feat_names):
    pallete_list = []
    for f in feat_names:
        if f == 'CGS':
            pallete_list.append('#4a3270')
        elif f == 'CGL':
            pallete_list.append('#9882b5')
        elif f == 'CRS':
            pallete_list.append('#57c840')
        elif f == 'CRL':
            pallete_list.append('#9ada86')
        else:
            pallete_list.append('gray')

    return pallete_list

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

algorithms_names = []
for f in os.listdir(f'{SCRIPT_DIR}/../results'):
    if f == '__init__.py':
        continue
    algorithms_names.append(f)

all_dstypes = defaultdict(list)
all_dsnames = []
dict_results = {}
for algname in algorithms_names:
    alg_data = pd.read_pickle(f'{SCRIPT_DIR}/../results/{algname}/{algname}_analysis.pkl')
    for factual_class in ['0', '1']:
        dataset_names = alg_data[alg_data['factual_class'] == factual_class].dsname.unique()
        for dsname in dataset_names:

            dstype = alg_data[alg_data['dsname'] == dsname].ds_type.unique()[0]
            if dsname not in all_dsnames:
                all_dsnames.append(dsname)
            if dsname not in [ds for sl in all_dstypes.values() for ds in sl]:
                all_dstypes[dstype].append(dsname)

            # If the dataset is not in the dict, create it
            if dsname not in dict_results:
                dict_results[dsname] = {}
            # If the factual class is not in the dict, create it
            if factual_class not in dict_results[dsname]:
                dict_results[dsname][factual_class] = []
            row_data = alg_data[(alg_data['dsname'] == dsname) & (alg_data['factual_class'] == factual_class)]
            dict_results[dsname][factual_class].append(
                {
                    'framework': row_data['framework'].tolist()[0],
                    'n': factual_class,
                    'validity': row_data['validity'].tolist()[0],
                    'validityFound': row_data['validityFound'].tolist()[0],
                    'sparsity': row_data['sparsity'].tolist()[0],
                    'L2': row_data['l2'].tolist()[0],
                    'RUC': row_data['RUC'].tolist()[0],
                    'RMC': row_data['RMC'].tolist()[0],
                    'MAD': row_data['MAD'].tolist()[0],
                    'MD': row_data['MD'].tolist()[0],
                    'cf_generation_time': row_data['cf_generation_time'].tolist()[0],
                }
            )


def get_dataset_names(ds_type):
    # Select the correct dataframes to be analyzed
    if ds_type == 'all':
        selected_ds = [ds for sl in all_dstypes.values() for ds in sl]
        chart_title = 'ALL DATASETS'
    if ds_type == 'num':
        selected_ds = [v for k, v in all_dstypes.items() if k == 'numerical'][0]
        chart_title = 'NUMERICAL DATASETS'
    if ds_type == 'cat':
        selected_ds = [v for k, v in all_dstypes.items() if k == 'categorical'][0]
        chart_title = 'CATEGORICAL DATASETS'
    if ds_type == 'mix':
        selected_ds = [v for k, v in all_dstypes.items() if k == 'mixed'][0]
        chart_title = 'MIXED DATASETS'

    return selected_ds, chart_title


# Function that creates a dataframe with all results
def create_full_dataframe(dict_results):
    # Create a list to store the initial results
    all_results = []

    # For each dataset
    for dsname in all_dsnames:
        # For each class
        for n in ['0', '1']:

            # Create a list to store the specific dataset and class result
            dsname_results = []

            # Create variable to measure the number of rows
            n_rows = 0

            # For each dataset result in the result dictionary
            for dsname_r in dict_results[dsname][n]:

                # Load it into a DataFrame
                sdf = pd.DataFrame(dsname_r)
                # Include the dataset name on the DataFrame
                sdf['dataset'] = dsname
                # Append the result into the output list
                dsname_results.append(sdf)

                # If the number of rows is zero (first run)
                if n_rows == 0:
                    # Update the number of rows
                    n_rows = sdf.shape[0]
                else:
                    # If it's not the first run, verify if the number of rows is the same across frameworks
                    assert n_rows == sdf.shape[0]

            # Concatenate the results into a single DataFrame
            dsname_f = pd.concat(dsname_results)

            # Get all framework names that were found in the results
            afw = list(dsname_f['framework'].unique())

            # Get the frameworks that were not found in the results and create empty results for it
            for algo_name in list(set(algorithms_names) - set(afw)):
                adf = pd.DataFrame(
                    {
                        'framework': [algo_name] * n_rows,
                        'n': [n] * n_rows,
                        'validity': [False] * n_rows,
                        'validityFound': [False] * n_rows,
                        'sparsity': [np.nan] * n_rows,
                        'L2': [np.nan] * n_rows,
                        'RUC': [0] * n_rows,
                        'RMC': [0] * n_rows,
                        'MAD': [np.nan] * n_rows,
                        'MD': [np.nan] * n_rows,
                        'cf_generation_time': [np.nan] * n_rows,
                        'dataset': [dsname] * n_rows
                    })

                # Append the not found result into our output
                dsname_results.append(adf)

            # Concatenate again to have the results for all frameworks
            dsname_f = pd.concat(dsname_results)

            # Then append the final DataFrame in the all results list
            all_results.append(dsname_f)

    # Create the DataFrame with the all results obtained
    df_all_results = pd.concat(all_results)
    df_all_results = df_all_results.reset_index()

    return df_all_results


def generate_rank_analysis(df_all_results, ds_type, n_list=['0', '1']):

    # Select the correct dataframes to be analyzed
    selected_ds, chart_title = get_dataset_names(ds_type)

    # Create a list to store row results
    rank_rows = []

    # For each dataset in the selection
    for ds in selected_ds:
        # For each class in the class selection
        for n in n_list:

            # Select a subframe with the specified dataset and class
            df_s = df_all_results[(df_all_results['dataset'] == ds) & (df_all_results['n'] == n)]

            # For each unique row index (that is a factual instance)
            for ds_idx in list(df_s['index'].unique()):
                # Select the rows for each framework
                df_s_idx = df_s[df_s['index'] == ds_idx]

                # Calculate the ranking where minimum values are the best (L2, MAD, MD)
                rank_max_row = df_s_idx.set_index('framework') \
                    .drop(columns=['index', 'n', 'validityFound', 'dataset', 'L2', 'MAD', 'MD'])\
                    .T.rank(na_option='bottom', axis=1, ascending=False)

                # Calculate the ranking where maximum values are the best (validity, sparsity, RUC, RMC)
                rank_min_row = df_s_idx.set_index('framework') \
                    .drop(columns=['index', 'n', 'validityFound', 'dataset', 'validity', 'sparsity', 'RUC', 'RMC']) \
                    .T.rank(na_option='bottom', axis=1)

                # Concatenate the two types of rankings
                rank_row = pd.concat([rank_max_row, rank_min_row])

                # Include the row index and dataset name and class
                rank_row['index'] = ds_idx
                rank_row['dataset'] = ds
                rank_row['n'] = n

                # Append the result row to output list
                rank_rows.append(rank_row)

    # Create DataFrame for all rows
    result_df_rows = pd.concat(rank_rows)

    # Create DataFrame with mean result for the selected set
    result_df_mean = result_df_rows.drop(columns=['index', 'dataset', 'n']) \
        .reset_index().groupby('index').mean()

    # Insert the number of instances that were analyzed
    result_df_mean['N'] = len(rank_rows)

    # Adjust to standard column and row order
    result_df_mean = result_df_mean[algorithms_names + ['N']].loc[
        ['validity', 'sparsity', 'L2', 'MAD', 'MD', 'cf_generation_time']]

    table_ranking_styled = result_df_mean.style.apply(highlight_group_best, axis=1)
    table_ranking_styled.data = table_ranking_styled.data.applymap(lambda x: round(x, 2))
    table_ranking_styled.to_html(f'{SCRIPT_DIR}/../tables/ranking_table_{ds_type}.html')
    # Read and modify the HTML file to remove extra 000
    with open(f'{SCRIPT_DIR}/../tables/ranking_table_{ds_type}.html', 'r') as f:
        html_table = f.read()
        html_table = html_table.replace('0000</td>', f'</td>')
        html_table = html_table.replace('<style type="text/css">', f'')
        html_table = html_table.replace('</style>', f'')
    # Write the modified HTML file
    with open(f'{SCRIPT_DIR}/../tables/ranking_table_{ds_type}.html', 'w') as f:
        f.write(html_table)

    return html_table


def highlight_group_best(s):
    # Calculate the number of frameworks analyzed, -1 because N column
    k = len(s.index) - 1

    # Get the number of rows analyzed
    N = s['N']

    # Remove the number of rows, having only the framework rankings
    s_clean = s.drop('N')

    # Calculate the Friedman's test
    spx2f = sum([(R - (k + 1) / 2) ** 2 for R in s_clean.values])
    x2f = 12 * N / (k * (k + 1)) * spx2f
    ff = (N - 1) * x2f / (N * (k - 1) - x2f)

    # Calculate the critical value for a 95% confidence interval
    critical_f_value = sp.stats.f.ppf(q=1 - .05, dfn=k - 1, dfd=N - 1)

    # Check if the null hypothesis (all frameworks perform the same) was rejected
    reject_h0 = True if ff >= critical_f_value else False

    # If rejected, calculate the critical difference and highlight the best frameworks
    if reject_h0:

        # Critical difference
        cd = cvnt005[k] * (k * (k + 1) / (6 * N)) ** 0.5

        # Get best frameworks
        bests_fws = list(s_clean[s_clean <= (s_clean.min() + cd)].index)

        # Highlight the best frameworks
        return ['background-color: gray' if v in bests_fws else '' for v in list(s.index)]
    else:
        # If all frameworks perform the same (null hypothesis), do not highlight anything
        return ['' for v in list(s.index)]


# Function to create coverage charts with raw results
def generate_charts(df_all_results, ds_type, metric, max_y=None):

    # Select the correct dataframes to be analyzed
    selected_ds, chart_title = get_dataset_names(ds_type)

    # Make a deepcopy just to be sure we will not modify the results
    realistic_analysis = copy.deepcopy(
        df_all_results[df_all_results['dataset'].isin(selected_ds)][['framework', metric]])

    fws = realistic_analysis['framework'].unique()

    df_result_coverage = pd.concat(
        [realistic_analysis[realistic_analysis['framework'] == fw].reset_index(drop=True)[metric] for fw in fws],
        axis=1)
    df_result_coverage.columns = fws

    sns.set_theme(style="whitegrid")
    ax, fig = plt.subplots(dpi=150)

    # Now create the chart
    ax = sns.barplot(data=df_result_coverage, ci=95)
    if max_y is not None:
        ax.set_ylim(0, max_y)
    #     show_values_on_bars(ax, np.array(realistic_analysis_mean['coverage'].tolist()))
    ax.set_title(chart_title)
    #     ax.figure.set_size_inches(10,6)

    plt.savefig(f'{SCRIPT_DIR}/../charts/{metric}_chart_{ds_type}.png')

if len(dict_results) > 0:
    df_all_results = create_full_dataframe(dict_results)
    generate_charts(df_all_results, 'all', 'validity', 1.0)
    generate_charts(df_all_results, 'num', 'validity', 1.0)
    generate_charts(df_all_results, 'cat', 'validity', 1.0)
    generate_charts(df_all_results, 'mix', 'validity', 1.0)

    generate_charts(df_all_results, 'all', 'cf_generation_time')
    generate_charts(df_all_results, 'num', 'cf_generation_time')
    generate_charts(df_all_results, 'cat', 'cf_generation_time')
    generate_charts(df_all_results, 'mix', 'cf_generation_time')

    # Copy README_template.md to README.md
    with open(f'{SCRIPT_DIR}/../README_template.md', 'r') as f:
        template = f.read()
    with open(f'{SCRIPT_DIR}/../README.md', 'w') as f:
        f.write(template)

    html_table_all = generate_rank_analysis(df_all_results, 'all')
    html_table_num = generate_rank_analysis(df_all_results, 'num')
    html_table_cat = generate_rank_analysis(df_all_results, 'cat')
    html_table_mix = generate_rank_analysis(df_all_results, 'mix')

    # Replace the tables with the new ones in the README.md file
    with open(f'{SCRIPT_DIR}/../README.md', 'r') as f:
        readme = f.read()
        readme = readme.replace('@RANKING_ALL_DATASETS@', html_table_all)
        readme = readme.replace('@RANKING_NUMERICAL_DATASETS@', html_table_num)
        readme = readme.replace('@RANKING_CATEGORICAL_DATASETS@', html_table_cat)
        readme = readme.replace('@RANKING_MIXED_DATASETS@', html_table_mix)

    with open(f'{SCRIPT_DIR}/../README.md', 'w') as f:
        f.write(readme)
