from tqdm import tqdm
import ast
import pandas as pd
import numpy as np
from scipy import stats
import shelve
import glob
import random
from collections import defaultdict
import os, sys


method_map = {     'sindy': 'A-SINDy',
                        'wsindy': 'A-WSINDy',
                        'te-cde': 'TE-CDE',
                        'insite': r'\bf INSITE',
                        'crn': 'CRN',
                        'msm': 'MSM',
                        'gnet': 'G-Net',
                        'rmsn': 'RMSN',
                        'ct': 'CT',
                        'edct': 'EDCT'}


env_name_ordering = {'EQ_4_A': 0,
                        'EQ_4_B': 1,
                        'EQ_4_C': 2,
                        'EQ_4_D': 3,
                        'EQ_5_A': 4,
                        'EQ_5_B': 5,
                        'EQ_5_C': 6,
                        'EQ_5_D': 7}

method_ordering = {
                    'msm': 0,
                    'rmsn': 1,
                    'crn': 2,
                    'gnet': 3,
                    'te-cde': 4,
                    'ct': 5,
                    'edct': 6,
                    'sindy': 7,
                    'wsindy': 8,
                    'insite': 9,
                    }

STEP_AHEAD_NAME_MAP = {'encoder_test_rmse_orig': 1,
                        'decoder_test_rmse_2-step': 2,
                        'decoder_test_rmse_3-step': 3,
                        'decoder_test_rmse_4-step': 4,
                        'decoder_test_rmse_5-step': 5,
                        'decoder_test_rmse_6-step': 6}

    
def file_path_from_parent_directory(parent_dir):
    files = glob.glob(parent_dir + '/*')
    return files[-1]

def moving_average(x, N):
    return np.convolve(x, np.ones(N)/N, mode='valid')

def ci(data, confidence=0.95, axis=0):
    # https://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data
    a = 1.0 * np.array(data)
    n = a.shape[axis]
    m, se = np.mean(a, axis=axis), stats.sem(a, axis=axis)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return h

def configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE, use_autolayout=True):
    pd.set_option('mode.chained_assignment', None)
    sn.set(rc={'figure.figsize': (SCALE, int(HEIGHT_SCALE * SCALE)), 'figure.autolayout': use_autolayout, 'text.usetex': True, 
    'text.latex.preamble': '\n'.join([
       r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
       r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
       r'\usepackage{helvet}',    # set the normal font here
       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
                    ])  
    })
    sn.set(font_scale=2.0)
    sn.set_style('white', {'font.family':'serif',
                            'font.serif':'Times New Roman',
                            "pdf.fonttype": 42,
                            "ps.fonttype": 42,
                            "font.size": 14})
    sn.color_palette("colorblind")
    return sn

def load_df(path, remove_extra_columns=True, load_from_cache=False):
    if load_from_cache:
        try:
            with shelve.open("logs") as db:
                df = db[path]
        except KeyError:
            df = df_from_log(path, remove_extra_columns=remove_extra_columns)
            with shelve.open("logs") as db:
                db[path] = df
    else:
        df = df_from_log(path, remove_extra_columns=remove_extra_columns)
    return df

def df_from_log(path, remove_extra_columns=True, load_tensorboard_data=True):
    with open(path) as f:
        lines = f.readlines()
    pd_l = []
    for line in tqdm(lines):
        if '[Exp evaluation complete] {' in line:
            result_dict = line.split('[Policy evaluation complete] ')[1].strip()
            result_dict = result_dict.replace('nan', '\'nan\'')
            result_dict = result_dict.replace('array', '')
            result_dict = ast.literal_eval(result_dict)
            # try:
            if load_tensorboard_data:
                if 'run_name' in result_dict:
                    run_name = result_dict['run_name']
                    log_path = file_path_from_parent_directory(f'./runs/{run_name}')
                    tensorboard_data = load_metrics_from_tensorboard_file(log_path)
                    result_dict['episodic_return_all'] = tensorboard_data['charts/episodic_return']
                    # result_dict['episodic_length_all'] = tensorboard_data['charts/episodic_length']
            pd_l.append(result_dict)
            # except:
            #     pass
    dfm = pd.DataFrame(pd_l)
    if remove_extra_columns:
        columns_to_remove_if_exist = ['costs_std_stats', 'planner', 'observed_times', 'observed_times_diff', 'costs_std_median', 's', 'a', 'r', 'cost_std_plot', 'ri', 'telem_file_path']
        current_columns = list(dfm.columns)
        columns_to_drop = set(columns_to_remove_if_exist) & set(current_columns)
        columns_to_drop = list(columns_to_drop)
        dfm = dfm.drop(columns=columns_to_drop)
    else:
        columns_to_np_arrays_if_exist = ['observed_times', 'observed_times_diff', 's', 'a', 'r', 'cost_std_plot', 'ri']
        current_columns = list(dfm.columns)
        columns_to_np_arrays = set(columns_to_np_arrays_if_exist) & set(current_columns)
        columns_to_np_arrays = list(columns_to_np_arrays)
        dfm[columns_to_np_arrays] = dfm[columns_to_np_arrays].applymap(np.array)
    # numeric_columns = ['roll_outs',
    #                     'time_steps',
    #                     'episode_elapsed_time',
    #                     'episode_elapsed_time_per_it',
    #                     'dt_sim',
    #                     'dt_plan',
    #                     'total_reward',
    #                     'state_reward',
    #                     'state_reward_std',
    #                     'observation_reward',
    #                     'observations_taken',
    #                     'observing_var_threshold',
    #                     'observing_cost',
    #                     'observation_noise',
    #                     'seed']
    # dfm[numeric_columns] = dfm[numeric_columns].apply(pd.to_numeric, errors='coerce')
    # dfm['name'] = dfm.model_name + '+' + dfm.method
    return dfm

def normalize_means(df):
    df_means = df.groupby(['env_name', 'policy', 'network_specific']).agg(np.mean).reset_index()
    for env_name in df_means.env_name.unique():
        pass
        df_means_env = df_means[df_means.env_name == env_name]
        random_row = df_means_env[df_means_env.method == 'random'].iloc[0]
        best_row = df_means_env[df_means_env.method == 'continuous_planning'].iloc[0]

        df.loc[df.env_name==env_name, 'total_reward'] = ((df[df.env_name == env_name].total_reward - random_row.total_reward) / (best_row.total_reward - random_row.total_reward)) * 100.0
        df.loc[df.env_name==env_name, 'state_reward'] = ((df[df.env_name == env_name].state_reward - random_row.state_reward) / (best_row.state_reward - random_row.state_reward)) * 100.0
    return df

def remove_unneeded_columns(df):
    columns_to_remove_if_exist = ['errored', 'costs_std_stats', 'planner', 'observed_times', 'observed_times_diff', 'costs_std_median', 's', 'a', 'r', 'cost_std_plot', 'ri', 'telem_file_path', 'path']
    current_columns = list(df.columns)
    columns_to_drop = set(columns_to_remove_if_exist) & set(current_columns)
    columns_to_drop = list(columns_to_drop)
    if len(columns_to_drop) > 0:
        print('[WARNING] Dropping columns: ', columns_to_drop)
    df = df.drop(columns=columns_to_drop)
    return df

def compute_norm_metrics(df):
    cancer_norm = 1150
    single_eq_norm = 764
    env_name_norm_map = {'eq_1': single_eq_norm,
                            'eq_2': single_eq_norm,
                            'eq_3': single_eq_norm,
                            'eq_4': single_eq_norm,
                            'eq_5': cancer_norm,
                            'eq_6': cancer_norm,
                            'eq_7': cancer_norm,
                            'eq_8': cancer_norm,
                            'eq_9': cancer_norm}
    
    for env_name in df.env_name.unique():
        norm = env_name_norm_map[env_name]
        df.loc[df.env_name == env_name, 'test_rmse'] = df[df.env_name == env_name].test_rmse / norm
    return df

def generate_main_results_table_paper_format_tests_pass_with_all(df_results, wandb=None, use_95_ci=True, seeds_to_use=None, include_tests=True):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    df_results['features'] = np.minimum(df_results['features'], df_results['total_features'])
    df_results['features_percent'] = (df_results['features'] / df_results['total_features']) * 100.0
    df_results = df_results[df_results['env_name'] != 'dropbox']
    df_results['test_failed'] = df_results['test_total'] - df_results['test_passed']
    # df_results['test_percent'] = (df_results['test_passed'] / df_results['test_total']) * 100.0
    print('')
    # df_results[df_results['test_total'] == 0] = 0
    # df_results = df_results[df_results['env_name'] != 0]
    df_results['method'] = df_results['method'].replace('zeroshot', 'gpt4')
    # df_results['test_percent'] = df_results['test_percent'].apply(lambda x: x * 100.0)
    # print(df_results)
    # df_results['test_percent'].replace('NA', 0, inplace=True)

    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'


    df_out = df_out[df_out['method'].isin(['gptengineer', 'unleash']) == False]
    sf = 3
    env_name_map = {'whatsapp': 'Online Chat App',
                    'url_shortener': 'URL Shortener App',
                    'dropbox': 'Online File Sharing App',
                    'twitter': 'Online Social Media App',
                    'bookclub': 'Book Club App',
                    'finance': 'Financial Planner App',
                    'eventplanner': 'Event Planner App',
                    'recipe': 'Recipe App'}

    env_name_ordering = {'whatsapp': 2,
                        'url_shortener': 0,
                        'dropbox': 3,
                        'twitter': 1,
                        'bookclub': 7,
                        'finance': 5,
                        'eventplanner': 6,
                        'recipe': 4}
    
    method_name_ordering = {'llmatic': 4,
                            'gpt4': 0,
                            'unleash': 3,
                            'gptengineer': 1,
                            'autogpt': 2}

    method_name_map = {'llmatic': 'LLMatic',
                       'gpt4': 'GPT4',
                       'unleash': 'InfiniteReadMemory',
                       'gptengineer': 'GPT-Engineer',
                       'autogpt': 'AutoGPT'}
                             
    df_out = df_out.sort_values(by=['env_name', 'method'], 
                            key=lambda col: col.map(env_name_ordering) if col.name == 'env_name' else col.map(method_name_ordering))
    table_lines = []
    if include_tests:
        line = r'\begin{tabular}{@{}l' + '|cccc' * df_out.env_name.nunique() + '}'
    else:
        line = r'\begin{tabular}{@{}l' + '|ccc' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    if include_tests:
        table_lines.append(''.join([r'&  \multicolumn{4}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} & \textbf{Passing Tests}' * df_out.env_name.nunique() + r'\\' )
        table_lines.append(r'' + r'    & $\uparrow$ & $\downarrow$ & & $\uparrow$ ' * df_out.env_name.nunique() + r'\\' )
    else:
        table_lines.append(''.join([r'&  \multicolumn{3}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} ' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for method in df_out.method.unique():
        if method == 'llmatic':
            line = r'\midrule' + '\n' + method_name_map[method]
        else:
            line = method_name_map[method]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.method == method) & (df_out.env_name == env_name)]
            if method == 'llmatic':
                if include_tests:
                    line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.test_failed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_failed[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" 
            else:
                if include_tests:
                    line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.test_failed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_failed[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    print('')
    print('Latex Table::')
    print(table)
    print('')
    return df_out, table

def generate_main_results_table_paper_format_tests_pass_code_coverage(df_results, wandb=None, use_95_ci=True, seeds_to_use=None, include_tests=True):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    df_results = df_results[df_results['locs'] != 0]
    df_results['features'] = np.minimum(df_results['features'], df_results['total_features'])
    df_results['features_percent'] = (df_results['features'] / df_results['total_features']) * 100.0
    df_results = df_results[df_results['env_name'] != 'dropbox']
    # df_results['test_percent'] = (df_results['test_passed'] / df_results['test_total']) * 100.0
    print('')
    # df_results[df_results['test_total'] == 0] = 0
    # df_results = df_results[df_results['env_name'] != 0]
    df_results['method'] = df_results['method'].replace('zeroshot', 'gpt4')
    df_results['env_name'] = df_results['env_name'].replace('finance2', 'finance')
    df_results['env_name'] = df_results['env_name'].replace('bookclub2', 'bookclub')
    df_results = df_results[df_results['env_name'] != 'bookclub']
    # df_results['test_percent'] = df_results['test_percent'].apply(lambda x: x * 100.0)
    # print(df_results)
    # df_results['test_percent'].replace('NA', 0, inplace=True)

    if True: # Rebuttal
        df_results = df_results[df_results['env_name'] != 'url_shortener']
        df_results = df_results[df_results['env_name'] != 'whatsapp']
        df_results = df_results[df_results['env_name'] != 'twitter']
        unique_combinations_count = df_results.groupby(['env_name', 'method']).size().reset_index(name='count')
        sampled_df = df_results.groupby(['env_name', 'method']).apply(lambda x: x.sample(n=10, replace=False) if len(x) > 10 else x)
        sampled_df.reset_index(drop=True, inplace=True)
        sampled_df
        unique_combinations_count = sampled_df.groupby(['env_name', 'method']).size().reset_index(name='count')

        print(unique_combinations_count)

    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'


    df_out = df_out[df_out['method'].isin(['gptengineer', 'unleash']) == False]
    sf = 3
    env_name_map = {'whatsapp': 'Online Chat App',
                    'url_shortener': 'URL Shortener App',
                    'dropbox': 'Online File Sharing App',
                    'twitter': 'Online Social Media App',
                    'bookclub': 'Book Club App',
                    'finance': 'Financial Planner App',
                    'eventplanner': 'Event Planner App',
                    'recipe': 'Recipe App'}

    env_name_ordering = {'whatsapp': 2,
                        'url_shortener': 0,
                        'dropbox': 3,
                        'twitter': 1,
                        'bookclub': 7,
                        'finance': 6,
                        'eventplanner': 5,
                        'recipe': 4}
    
    method_name_ordering = {
                            'gpt4': 0,
                            'gptengineer': 1,
                            'codet': 2,
                            'selfrefine': 3,
                            'reflexion': 4,
                            'autogpt': 5,
                            'llmatic': 6,
                            'unleash': 7}

    method_name_map = {'llmatic': 'Code-L2MAC',
                       'gpt4': 'GPT4',
                       'unleash': 'InfiniteReadMemory',
                       'gptengineer': 'GPT-Engineer',
                       'autogpt': 'AutoGPT',
                       'codet': 'CodeT',
                       'selfrefine': 'Self-Refine',
                       'reflexion': 'Reflexion'}
                             
    df_out = df_out.sort_values(by=['env_name', 'method'], 
                            key=lambda col: col.map(env_name_ordering) if col.name == 'env_name' else col.map(method_name_ordering))
    table_lines = []
    if include_tests:
        line = r'\begin{tabular}{@{}l' + '|ccccc' * df_out.env_name.nunique() + '}'
    else:
        line = r'\begin{tabular}{@{}l' + '|cccc' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    if include_tests:
        table_lines.append(''.join([r'&  \multicolumn{5}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} & \textbf{Passing Tests}  & \textbf{Cov \%}' * df_out.env_name.nunique() + r'\\' )
        table_lines.append(r'' + r'    & $\uparrow$ & $\downarrow$ & & $\uparrow$ & $\uparrow$' * df_out.env_name.nunique() + r'\\' )
    else:
        table_lines.append(''.join([r'&  \multicolumn{3}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} ' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for method in df_out.method.unique():
        if method == 'llmatic':
            line = r'\midrule' + '\n' + method_name_map[method]
        else:
            line = method_name_map[method]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.method == method) & (df_out.env_name == env_name)]
            if method == 'llmatic':
                if include_tests:
                    if row is None or row.empty:
                        line += r'& ' +  r'& ' +  r'& ' + r'& ' + r'& ' 
                    else:
                        line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.coverage_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.coverage_percent[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" 
            else:
                if include_tests:
                    if row is None or row.empty:
                        line += r'& ' +  r'& ' +  r'& ' + r'& '  + r'& '
                    else:
                        line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.coverage_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.coverage_percent[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    print('')
    print('Latex Table::')
    print(table)
    print('')
    return df_out, table

def generate_main_results_table_paper_format_tests_pass(df_results, wandb=None, use_95_ci=True, seeds_to_use=None, include_tests=True, rebuttal=False, rebuttal_big=False, ablation_no_summarization=False):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    df_results = df_results[df_results['locs'] != 0]
    df_results['features'] = np.minimum(df_results['features'], df_results['total_features'])
    df_results['features_percent'] = (df_results['features'] / df_results['total_features']) * 100.0
    df_results = df_results[df_results['env_name'] != 'dropbox']
    # df_results['test_percent'] = (df_results['test_passed'] / df_results['test_total']) * 100.0
    print('')
    # df_results[df_results['test_total'] == 0] = 0
    # df_results = df_results[df_results['env_name'] != 0]
    df_results['method'] = df_results['method'].replace('zeroshot', 'gpt4')
    df_results['env_name'] = df_results['env_name'].replace('finance2', 'finance')
    df_results['env_name'] = df_results['env_name'].replace('bookclub2', 'bookclub')
    df_results = df_results[df_results['env_name'] != 'bookclub']
    # df_results['test_percent'] = df_results['test_percent'].apply(lambda x: x * 100.0)
    # print(df_results)
    # df_results['test_percent'].replace('NA', 0, inplace=True)

    if rebuttal: # Rebuttal
        df_results = df_results[df_results['env_name'] != 'bookclub']
        df_results = df_results[df_results['env_name'] != 'finance']
        df_results = df_results[df_results['env_name'] != 'eventplanner']
        df_results = df_results[df_results['env_name'] != 'recipe']
        unique_combinations_count = df_results.groupby(['env_name', 'method']).size().reset_index(name='count')
        sampled_df = df_results.groupby(['env_name', 'method']).apply(lambda x: x.sample(n=10, replace=False) if len(x) > 10 else x)
        sampled_df.reset_index(drop=True, inplace=True)
        # sampled_df
        df_results = sampled_df
        unique_combinations_count = sampled_df.groupby(['env_name', 'method']).size().reset_index(name='count')
        print(unique_combinations_count)
        print('')
    elif ablation_no_summarization:
        df_results = df_results[df_results['env_name'] != 'twitter']
        df_results = df_results[df_results['env_name'] != 'whatsapp']
        sampled_df = df_results.groupby(['env_name', 'method']).apply(lambda x: x.sample(n=10, replace=False) if len(x) > 10 else x)
        sampled_df.reset_index(drop=True, inplace=True)
        df_results = sampled_df

    if rebuttal_big:
        print('Rebuttal Big')
        df_results = df_results[df_results['locs'] > 1000]

    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'


    df_out = df_out[df_out['method'].isin(['gptengineer', 'unleash']) == False]
    sf = 3
    env_name_map = {'whatsapp': 'Online Chat App',
                    'url_shortener': 'URL Shortener App',
                    'dropbox': 'Online File Sharing App',
                    'twitter': 'Online Social Media App',
                    'bookclub': 'Book Club App',
                    'finance': 'Financial Planner App',
                    'eventplanner': 'Event Planner App',
                    'recipe': 'Recipe App'}

    env_name_ordering = {'whatsapp': 2,
                        'url_shortener': 0,
                        'dropbox': 3,
                        'twitter': 1,
                        'bookclub': 7,
                        'finance': 6,
                        'eventplanner': 5,
                        'recipe': 4}
    
    method_name_ordering = {
                            'gpt4': 0,
                            'gptengineer': 1,
                            'codet': 2,
                            'selfrefine': 3,
                            'reflexion': 4,
                            'autogpt': 5,
                            'llmatic': 6,
                            'unleash': 7}

    method_name_map = {'llmatic': 'Code-L2MAC',
                       'gpt4': 'GPT4',
                       'unleash': 'InfiniteReadMemory',
                       'gptengineer': 'GPT-Engineer',
                       'autogpt': 'AutoGPT',
                       'codet': 'CodeT',
                       'selfrefine': 'Self-Refine',
                       'reflexion': 'Reflexion'}
                             
    df_out = df_out.sort_values(by=['env_name', 'method'], 
                            key=lambda col: col.map(env_name_ordering) if col.name == 'env_name' else col.map(method_name_ordering))
    table_lines = []
    if include_tests:
        line = r'\begin{tabular}{@{}l' + '|cccc' * df_out.env_name.nunique() + '}'
    else:
        line = r'\begin{tabular}{@{}l' + '|ccc' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    if include_tests:
        table_lines.append(''.join([r'&  \multicolumn{4}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} & \textbf{Passing Tests}' * df_out.env_name.nunique() + r'\\' )
        table_lines.append(r'' + r'    & $\uparrow$ & $\downarrow$ & & $\uparrow$ ' * df_out.env_name.nunique() + r'\\' )
    else:
        table_lines.append(''.join([r'&  \multicolumn{3}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} ' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for method in df_out.method.unique():
        if method == 'llmatic':
            line = r'\midrule' + '\n' + method_name_map[method]
        else:
            line = method_name_map[method]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.method == method) & (df_out.env_name == env_name)]
            if method == 'llmatic':
                if include_tests:
                    if row is None or row.empty:
                        line += r'& ' +  r'& ' +  r'& ' + r'& ' 
                    else:
                        line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" 
            else:
                if include_tests:
                    if row is None or row.empty:
                        line += r'& ' +  r'& ' +  r'& ' + r'& ' 
                    else:
                        line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    print('')
    print('Latex Table::')
    print(table)
    print('')
    return df_out, table

def generate_main_results_table_paper_format_tests_pass_human_eval(df_results, wandb=None, use_95_ci=True, seeds_to_use=None, include_tests=False, rebuttal=False, rebuttal_big=False):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    # df_results = df_results[df_results['locs'] != 0]
    env_name_to_total_features = {'url_shortener': 17, 'whatsapp': 20, 'twitter': 21, 'recipe': 20}
    df_results['total_features'] = df_results['env_name'].map(env_name_to_total_features)
    df_results['features'] = df_results['features_counted']
    df_results['features'] = np.minimum(df_results['features'], df_results['total_features'])
    df_results['features_percent'] = (df_results['features'] / df_results['total_features']) * 100.0
    df_results = df_results[df_results['env_name'] != 'dropbox']
    df_results['method'] = df_results['method'].str.lower()
    df_results['method'] = df_results['method'].replace('l2mac', 'llmatic')
    # df_results['test_percent'] = (df_results['test_passed'] / df_results['test_total']) * 100.0
    print('')
    # df_results[df_results['test_total'] == 0] = 0
    # df_results = df_results[df_results['env_name'] != 0]
    df_results['method'] = df_results['method'].replace('zeroshot', 'gpt4')
    df_results['env_name'] = df_results['env_name'].replace('finance2', 'finance')
    df_results['env_name'] = df_results['env_name'].replace('bookclub2', 'bookclub')
    df_results = df_results[df_results['env_name'] != 'bookclub']
    # df_results['test_percent'] = df_results['test_percent'].apply(lambda x: x * 100.0)
    # print(df_results)
    # df_results['test_percent'].replace('NA', 0, inplace=True)

    if rebuttal: # Rebuttal
        df_results = df_results[df_results['env_name'] != 'bookclub']
        df_results = df_results[df_results['env_name'] != 'finance']
        df_results = df_results[df_results['env_name'] != 'eventplanner']
        df_results = df_results[df_results['env_name'] != 'recipe']
        unique_combinations_count = df_results.groupby(['env_name', 'method']).size().reset_index(name='count')
        sampled_df = df_results.groupby(['env_name', 'method']).apply(lambda x: x.sample(n=10, replace=False) if len(x) > 10 else x)
        sampled_df.reset_index(drop=True, inplace=True)
        sampled_df
        unique_combinations_count = sampled_df.groupby(['env_name', 'method']).size().reset_index(name='count')
        print(unique_combinations_count)
        print('')

    if rebuttal_big:
        print('Rebuttal Big')
        df_results = df_results[df_results['locs'] > 1000]

    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'


    df_out = df_out[df_out['method'].isin(['gptengineer', 'unleash']) == False]
    sf = 3
    env_name_map = {'whatsapp': 'Online Chat App',
                    'url_shortener': 'URL Shortener App',
                    'dropbox': 'Online File Sharing App',
                    'twitter': 'Online Social Media App',
                    'bookclub': 'Book Club App',
                    'finance': 'Financial Planner App',
                    'eventplanner': 'Event Planner App',
                    'recipe': 'Recipe App'}

    env_name_ordering = {'whatsapp': 2,
                        'url_shortener': 0,
                        'dropbox': 3,
                        'twitter': 1,
                        'bookclub': 7,
                        'finance': 6,
                        'eventplanner': 5,
                        'recipe': 4}
    
    method_name_ordering = {
                            'gpt4': 0,
                            'gptengineer': 1,
                            'codet': 2,
                            'selfrefine': 3,
                            'reflexion': 4,
                            'autogpt': 5,
                            'llmatic': 6,
                            'unleash': 7}

    method_name_map = {'llmatic': 'Code-L2MAC',
                       'gpt4': 'GPT4',
                       'unleash': 'InfiniteReadMemory',
                       'gptengineer': 'GPT-Engineer',
                       'autogpt': 'AutoGPT',
                       'codet': 'CodeT',
                       'selfrefine': 'Self-Refine',
                       'reflexion': 'Reflexion'}
                             
    df_out = df_out.sort_values(by=['env_name', 'method'], 
                            key=lambda col: col.map(env_name_ordering) if col.name == 'env_name' else col.map(method_name_ordering))
    table_lines = []
    if include_tests:
        line = r'\begin{tabular}{@{}l' + '|cccc' * df_out.env_name.nunique() + '}'
    else:
        line = r'\begin{tabular}{@{}l' + '|c' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    if include_tests:
        table_lines.append(''.join([r'&  \multicolumn{4}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} & \textbf{Passing Tests}' * df_out.env_name.nunique() + r'\\' )
        table_lines.append(r'' + r'    & $\uparrow$ & $\downarrow$ & & $\uparrow$ ' * df_out.env_name.nunique() + r'\\' )
    else:
        table_lines.append(''.join([r'&  \multicolumn{1}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Human Expert Features \%} ' * df_out.env_name.nunique() + r'\\' )
        table_lines.append(r'' + r'    & $\uparrow$' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for method in df_out.method.unique():
        if method == 'llmatic':
            line = r'\midrule' + '\n' + method_name_map[method]
        else:
            line = method_name_map[method]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.method == method) & (df_out.env_name == env_name)]
            if method == 'llmatic':
                if include_tests:
                    if row is None or row.empty:
                        line += r'& ' +  r'& ' +  r'& ' + r'& ' 
                    else:
                        line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}"
                else:
                    if row is None or row.empty:
                        line += r'& '
                    else:
                        line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}"
            else:
                if include_tests:
                    if row is None or row.empty:
                        line += r'& ' +  r'& ' +  r'& ' + r'& ' 
                    else:
                        line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}"
                else:
                    if row is None or row.empty:
                        line += r'& '
                    else:
                        line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    print('')
    print('Latex Table::')
    print(table)
    print('')
    return df_out, table

def generate_main_results_table_paper_format_tests_pass_human_eval_without_eb(df_results, wandb=None, use_95_ci=True, seeds_to_use=None, include_tests=False, rebuttal=False, rebuttal_big=False):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    # df_results = df_results[df_results['locs'] != 0]
    env_name_to_total_features = {'url_shortener': 17, 'whatsapp': 20, 'twitter': 21, 'recipe': 20}
    df_results['total_features'] = df_results['env_name'].map(env_name_to_total_features)
    df_results['features'] = df_results['features_counted']
    df_results['features'] = np.minimum(df_results['features'], df_results['total_features'])
    df_results['features_percent'] = (df_results['features'] / df_results['total_features']) * 100.0
    df_results = df_results[df_results['env_name'] != 'dropbox']
    df_results['method'] = df_results['method'].str.lower()
    df_results['method'] = df_results['method'].replace('l2mac', 'llmatic')
    # df_results['test_percent'] = (df_results['test_passed'] / df_results['test_total']) * 100.0
    print('')
    # df_results[df_results['test_total'] == 0] = 0
    # df_results = df_results[df_results['env_name'] != 0]
    df_results['method'] = df_results['method'].replace('zeroshot', 'gpt4')
    df_results['env_name'] = df_results['env_name'].replace('finance2', 'finance')
    df_results['env_name'] = df_results['env_name'].replace('bookclub2', 'bookclub')
    df_results = df_results[df_results['env_name'] != 'bookclub']
    # df_results['test_percent'] = df_results['test_percent'].apply(lambda x: x * 100.0)
    # print(df_results)
    # df_results['test_percent'].replace('NA', 0, inplace=True)

    if rebuttal: # Rebuttal
        df_results = df_results[df_results['env_name'] != 'bookclub']
        df_results = df_results[df_results['env_name'] != 'finance']
        df_results = df_results[df_results['env_name'] != 'eventplanner']
        df_results = df_results[df_results['env_name'] != 'recipe']
        unique_combinations_count = df_results.groupby(['env_name', 'method']).size().reset_index(name='count')
        sampled_df = df_results.groupby(['env_name', 'method']).apply(lambda x: x.sample(n=10, replace=False) if len(x) > 10 else x)
        sampled_df.reset_index(drop=True, inplace=True)
        sampled_df
        unique_combinations_count = sampled_df.groupby(['env_name', 'method']).size().reset_index(name='count')
        print(unique_combinations_count)
        print('')

    if rebuttal_big:
        print('Rebuttal Big')
        df_results = df_results[df_results['locs'] > 1000]

    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'


    df_out = df_out[df_out['method'].isin(['gptengineer', 'unleash']) == False]
    sf = 3
    env_name_map = {'whatsapp': 'Online Chat App',
                    'url_shortener': 'URL Shortener App',
                    'dropbox': 'Online File Sharing App',
                    'twitter': 'Online Social Media App',
                    'bookclub': 'Book Club App',
                    'finance': 'Financial Planner App',
                    'eventplanner': 'Event Planner App',
                    'recipe': 'Recipe App'}

    env_name_ordering = {'whatsapp': 2,
                        'url_shortener': 0,
                        'dropbox': 3,
                        'twitter': 1,
                        'bookclub': 7,
                        'finance': 6,
                        'eventplanner': 5,
                        'recipe': 4}
    
    method_name_ordering = {
                            'gpt4': 0,
                            'gptengineer': 1,
                            'codet': 2,
                            'selfrefine': 3,
                            'reflexion': 4,
                            'autogpt': 5,
                            'llmatic': 6,
                            'unleash': 7}

    method_name_map = {'llmatic': 'Code-L2MAC',
                       'gpt4': 'GPT4',
                       'unleash': 'InfiniteReadMemory',
                       'gptengineer': 'GPT-Engineer',
                       'autogpt': 'AutoGPT',
                       'codet': 'CodeT',
                       'selfrefine': 'Self-Refine',
                       'reflexion': 'Reflexion'}
                             
    df_out = df_out.sort_values(by=['env_name', 'method'], 
                            key=lambda col: col.map(env_name_ordering) if col.name == 'env_name' else col.map(method_name_ordering))
    table_lines = []
    if include_tests:
        line = r'\begin{tabular}{@{}l' + '|cccc' * df_out.env_name.nunique() + '}'
    else:
        line = r'\begin{tabular}{@{}l' + '|c' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    if include_tests:
        table_lines.append(''.join([r'&  \multicolumn{4}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} & \textbf{Passing Tests}' * df_out.env_name.nunique() + r'\\' )
        table_lines.append(r'' + r'    & $\uparrow$ & $\downarrow$ & & $\uparrow$ ' * df_out.env_name.nunique() + r'\\' )
    else:
        table_lines.append(''.join([r'&  \multicolumn{1}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Human Expert Features \%} ' * df_out.env_name.nunique() + r'\\' )
        table_lines.append(r'' + r'    & $\uparrow$' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for method in df_out.method.unique():
        if method == 'llmatic':
            line = r'\midrule' + '\n' + method_name_map[method]
        else:
            line = method_name_map[method]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.method == method) & (df_out.env_name == env_name)]
            if method == 'llmatic':
                if include_tests:
                    if row is None or row.empty:
                        line += r'& ' +  r'& ' +  r'& ' + r'& ' 
                    else:
                        line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}"
                else:
                    if row is None or row.empty:
                        line += r'& '
                    else:
                        line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}"
            else:
                if include_tests:
                    if row is None or row.empty:
                        line += r'& ' +  r'& ' +  r'& ' + r'& ' 
                    else:
                        line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}"
                else:
                    if row is None or row.empty:
                        line += r'& '
                    else:
                        line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" 
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    print('')
    print('Latex Table::')
    print(table)
    print('')
    return df_out, table

def generate_main_results_table_paper_format_tests_pass_unit_tests_apriori(df_results, wandb=None, use_95_ci=True, seeds_to_use=None, include_tests=True):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    df_results = df_results[df_results['locs'] != 0]
    df_results['features'] = np.minimum(df_results['features'], df_results['total_features'])
    df_results['features_percent'] = (df_results['features'] / df_results['total_features']) * 100.0
    unit_test_total_input_dict = {'url_shortener': 9, 'whatsapp': 19, 'twitter': 13, 'recipe': 20}
    df_results['unit_test_total_input'] = df_results['env_name'].map(unit_test_total_input_dict)
    df_results['human_unit_test_percent'] = (df_results['unit_test_passed'] / df_results['unit_test_total_input']) * 100.0
    df_results = df_results[df_results['env_name'] != 'dropbox']
    df_results = df_results[df_results['env_name'] != 'recipe']
    df_results = df_results[df_results['env_name'] != 'whatsapp']
    df_results = df_results[df_results['env_name'] != 'twitter']
    # df_results['test_percent'] = (df_results['test_passed'] / df_results['test_total']) * 100.0
    print('')
    # df_results[df_results['test_total'] == 0] = 0
    # df_results = df_results[df_results['env_name'] != 0]
    df_results['method'] = df_results['method'].replace('zeroshot', 'gpt4')
    # df_results['test_percent'] = df_results['test_percent'].apply(lambda x: x * 100.0)
    # print(df_results)
    # df_results['test_percent'].replace('NA', 0, inplace=True)

    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'


    df_out = df_out[df_out['method'].isin(['gptengineer', 'unleash']) == False]
    sf = 3
    env_name_map = {'whatsapp': 'Online Chat App',
                    'url_shortener': 'URL Shortener App',
                    'dropbox': 'Online File Sharing App',
                    'twitter': 'Online Social Media App',
                    'bookclub': 'Book Club App',
                    'finance': 'Financial Planner App',
                    'eventplanner': 'Event Planner App',
                    'recipe': 'Recipe App'}

    env_name_ordering = {'whatsapp': 2,
                        'url_shortener': 0,
                        'dropbox': 3,
                        'twitter': 1,
                        'bookclub': 7,
                        'finance': 5,
                        'eventplanner': 6,
                        'recipe': 4}
    
    method_name_ordering = {
                            'gpt4': 0,
                            'gptengineer': 1,
                            'codet': 2,
                            'selfrefine': 3,
                            'reflexion': 4,
                            'autogpt': 5,
                            'llmatic': 6,
                            'unleash': 7}

    method_name_map = {'llmatic': 'Code-L2MAC',
                       'gpt4': 'GPT4',
                       'unleash': 'InfiniteReadMemory',
                       'gptengineer': 'GPT-Engineer',
                       'autogpt': 'AutoGPT',
                       'codet': 'CodeT',
                       'selfrefine': 'Self-Refine',
                       'reflexion': 'Reflexion'}
                             
    df_out = df_out.sort_values(by=['env_name', 'method'], 
                            key=lambda col: col.map(env_name_ordering) if col.name == 'env_name' else col.map(method_name_ordering))
    table_lines = []
    if include_tests:
        line = r'\begin{tabular}{@{}l' + '|cccccc' * df_out.env_name.nunique() + '}'
    else:
        line = r'\begin{tabular}{@{}l' + '|ccc' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    if include_tests:
        table_lines.append(''.join([r'&  \multicolumn{6}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{HT \%} & \textbf{\# Errors} & \textbf{LOC} & \textbf{Passing Tests} & \textbf{Cov \%}' * df_out.env_name.nunique() + r'\\' )
        table_lines.append(r'' + r'    & $\uparrow$ & $\uparrow$ & $\downarrow$ & & $\uparrow$ & $\uparrow$ ' * df_out.env_name.nunique() + r'\\' )
    else:
        table_lines.append(''.join([r'&  \multicolumn{3}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} ' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for method in df_out.method.unique():
        if method == 'llmatic':
            line = r'\midrule' + '\n' + method_name_map[method]
        else:
            line = method_name_map[method]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.method == method) & (df_out.env_name == env_name)]
            if method == 'llmatic':
                if include_tests:
                    if row is None or len(row) == 0:
                        line += r'& ' + r'& ' + r'& ' +  r'& ' + r'& ' + r'& '
                    else:
                        line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.human_unit_test_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.human_unit_test_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.coverage_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.coverage_percent[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" 
            else:
                if include_tests:
                    if row is None or len(row) == 0:
                        line += r'& ' + r'& ' + r'& ' +  r'& ' + r'& ' + r'& '
                    else:
                        line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.human_unit_test_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.human_unit_test_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.test_passed['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_passed[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.coverage_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.coverage_percent[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    print('')
    print('Latex Table::')
    print(table)
    print('')
    return df_out, table

def generate_main_results_table_paper_format_tests_pass_unit_tests_apriori_without_errors_or_passing_tests(df_results, wandb=None, use_95_ci=True, seeds_to_use=None, include_tests=True):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    df_results = df_results[df_results['locs'] != 0]
    df_results['features'] = np.minimum(df_results['features'], df_results['total_features'])
    df_results['features_percent'] = (df_results['features'] / df_results['total_features']) * 100.0
    unit_test_total_input_dict = {'url_shortener': 9, 'whatsapp': 19, 'twitter': 13, 'recipe': 20}
    df_results['unit_test_total_input'] = df_results['env_name'].map(unit_test_total_input_dict)
    df_results['human_unit_test_percent'] = (df_results['unit_test_passed'] / df_results['unit_test_total_input']) * 100.0
    df_results = df_results[df_results['env_name'] != 'dropbox']
    df_results = df_results[df_results['env_name'] != 'recipe']
    # df_results['test_percent'] = (df_results['test_passed'] / df_results['test_total']) * 100.0
    print('')
    # df_results[df_results['test_total'] == 0] = 0
    # df_results = df_results[df_results['env_name'] != 0]
    df_results['method'] = df_results['method'].replace('zeroshot', 'gpt4')
    # df_results['test_percent'] = df_results['test_percent'].apply(lambda x: x * 100.0)
    # print(df_results)
    # df_results['test_percent'].replace('NA', 0, inplace=True)

    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'


    df_out = df_out[df_out['method'].isin(['gptengineer', 'unleash']) == False]
    sf = 3
    env_name_map = {'whatsapp': 'Online Chat App',
                    'url_shortener': 'URL Shortener App',
                    'dropbox': 'Online File Sharing App',
                    'twitter': 'Online Social Media App',
                    'bookclub': 'Book Club App',
                    'finance': 'Financial Planner App',
                    'eventplanner': 'Event Planner App',
                    'recipe': 'Recipe App'}

    env_name_ordering = {'whatsapp': 2,
                        'url_shortener': 0,
                        'dropbox': 3,
                        'twitter': 1,
                        'bookclub': 7,
                        'finance': 5,
                        'eventplanner': 6,
                        'recipe': 4}
    
    method_name_ordering = {
                            'gpt4': 0,
                            'gptengineer': 1,
                            'codet': 2,
                            'selfrefine': 3,
                            'reflexion': 4,
                            'autogpt': 5,
                            'llmatic': 6,
                            'unleash': 7}

    method_name_map = {'llmatic': 'Code-L2MAC',
                       'gpt4': 'GPT4',
                       'unleash': 'InfiniteReadMemory',
                       'gptengineer': 'GPT-Engineer',
                       'autogpt': 'AutoGPT',
                       'codet': 'CodeT',
                       'selfrefine': 'Self-Refine',
                       'reflexion': 'Reflexion'}
                             
    df_out = df_out.sort_values(by=['env_name', 'method'], 
                            key=lambda col: col.map(env_name_ordering) if col.name == 'env_name' else col.map(method_name_ordering))
    table_lines = []
    if include_tests:
        line = r'\begin{tabular}{@{}l' + '|cccc' * df_out.env_name.nunique() + '}'
    else:
        line = r'\begin{tabular}{@{}l' + '|ccc' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    if include_tests:
        table_lines.append(''.join([r'&  \multicolumn{4}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{HT \%} & \textbf{LOC} & \textbf{Cov \%}' * df_out.env_name.nunique() + r'\\' )
        table_lines.append(r'' + r'    & $\uparrow$ & $\uparrow$ & & $\uparrow$ ' * df_out.env_name.nunique() + r'\\' )
    else:
        table_lines.append(''.join([r'&  \multicolumn{3}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} ' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for method in df_out.method.unique():
        if method == 'llmatic':
            line = r'\midrule' + '\n' + method_name_map[method]
        else:
            line = method_name_map[method]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.method == method) & (df_out.env_name == env_name)]
            if method == 'llmatic':
                if include_tests:
                    if row is None or len(row) == 0:
                        line += r'& ' + r'& ' + r'& ' +  r'& ' 
                    else:
                        line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.human_unit_test_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.human_unit_test_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.coverage_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.coverage_percent[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" 
            else:
                if include_tests:
                    if row is None or len(row) == 0:
                        line += r'& ' + r'& ' + r'& ' +  r'& '
                    else:
                        line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.human_unit_test_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.human_unit_test_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.coverage_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.coverage_percent[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    print('')
    print('Latex Table::')
    print(table)
    print('')
    return df_out, table


def generate_main_results_table_paper_format(df_results, wandb=None, use_95_ci=True, seeds_to_use=None, include_tests=True):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    df_results['features'] = np.minimum(df_results['features'], df_results['total_features'])
    df_results['features_percent'] = (df_results['features'] / df_results['total_features']) * 100.0
    # df_results['test_percent'] = (df_results['test_passed'] / df_results['test_total']) * 100.0
    print('')
    # df_results[df_results['test_total'] == 0] = 0
    # df_results = df_results[df_results['env_name'] != 0]
    df_results['method'] = df_results['method'].replace('zeroshot', 'gpt4')
    # df_results['test_percent'] = df_results['test_percent'].apply(lambda x: x * 100.0)
    # print(df_results)
    # df_results['test_percent'].replace('NA', 0, inplace=True)

    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'


    df_out = df_out[df_out['method'].isin(['gptengineer', 'unleash']) == False]
    sf = 3
    env_name_map = {'whatsapp': 'Online Chat App',
                    'url_shortener': 'URL Shortener App',
                    'dropbox': 'Online File Sharing App',
                    'twitter': 'Online Social Media App'}

    env_name_ordering = {'whatsapp': 0,
                        'url_shortener': 1,
                        'dropbox': 2,
                        'twitter': 3}
    
    method_name_ordering = {'llmatic': 4,
                            'gpt4': 0,
                            'unleash': 3,
                            'gptengineer': 1,
                            'autogpt': 2}

    method_name_map = {'llmatic': 'LLMatic',
                       'gpt4': 'GPT4',
                       'unleash': 'InfiniteReadMemory',
                       'gptengineer': 'GPT-Engineer',
                       'autogpt': 'AutoGPT'}
                             
    df_out = df_out.sort_values(by=['env_name', 'method'], 
                            key=lambda col: col.map(env_name_ordering) if col.name == 'env_name' else col.map(method_name_ordering))
    table_lines = []
    if include_tests:
        line = r'\begin{tabular}{@{}l' + '|cccc' * df_out.env_name.nunique() + '}'
    else:
        line = r'\begin{tabular}{@{}l' + '|ccc' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    if include_tests:
        table_lines.append(''.join([r'&  \multicolumn{4}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} & \textbf{Test \%}' * df_out.env_name.nunique() + r'\\' )
    else:
        table_lines.append(''.join([r'&  \multicolumn{3}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
        table_lines.append(r'Method ' + r'& \textbf{Features \%} & \textbf{\# Errors} & \textbf{LOC} ' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for method in df_out.method.unique():
        if method == 'llmatic':
            line = r'\midrule' + '\n' + method_name_map[method]
        else:
            line = method_name_map[method]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.method == method) & (df_out.env_name == env_name)]
            if method == 'llmatic':
                if include_tests:
                    line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.test_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_percent[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&\bf' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&\bf' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" 
            else:
                if include_tests:
                    line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.test_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.test_percent[error_metric].iloc[0]:.{sf}g}"
                else:
                    line += r'&' + f"{row.features_percent['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.features_percent[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.errors['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.errors[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.locs['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.locs[error_metric].iloc[0]:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    print('')
    print('Latex Table::')
    print(table)
    print('')
    return df_out, table

class NoOpDict:
    def __getitem__(self, key):
        return key

    def __setitem__(self, key, value):
        pass # No-op for setting a value

    def __contains__(self, key):
        return True


def generate_main_results_table(df_results, wandb=None, use_95_ci=True, return_all_next_step_head_n_tables=True):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'

    sf = 3
    # env_name_map = {'oderl-cartpole': 'Cartpole',
    #                 'oderl-pendulum': 'Pendulum',
    #                 'oderl-acrobot': 'Acrobot',
    #                 'oderl-cancer': 'Cancer',
    #                 'oderl-glucose': 'Glucose',
    #                 'oderl-hiv': 'HIV',
    #                 'oderl-quadrotor': 'Quadcoptor'}
    env_name_map = NoOpDict()

    # env_name_ordering = {'oderl-cartpole': 2,
    #                 'oderl-pendulum': 3,
    #                 'oderl-acrobot': 1,
    #                 'oderl-cancer': 0,
    #                 'oderl-glucose': 4,
    #                 'oderl-hiv': 5,
    #                 'oderl-quadrotor': 6}
    env_name_ordering = NoOpDict()

    # method_map = {'discrete_monitoring': 'Discrete Monitoring',
    #                          'discrete_planning': 'Discrete Planning',
    #                          'continuous_planning': 'Continuous Planning',
    #                          'active_observing_control': r'\bf Active Sampling Control',
    #                          'random': 'Random'}
    method_map = NoOpDict()
                             
    # df_out = df_out.sort_values(by=['env_name'], key=lambda x: x.map(env_name_ordering))
    table_lines = []
    line = r'\begin{tabular}{@{}l' + 'c' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    table_lines.append(''.join([r'&  ' + env_name_map[env_name] for env_name in df_out.env_name.unique()]) + r'\\')
    table_lines.append(r'Policy ' + r'$\mathcal{R}$ ' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for method in df_out.method.unique():
        if method == 'active_observing_control':
            line = r'\midrule' + '\n' + method_map[method]
        else:
            line = method_map[method]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.method == method) & (df_out.env_name == env_name)]
            if method == 'relentless':
                line += r'&\bf' + f"{row.reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.reward[error_metric].iloc[0]:.{sf}g}"
            else:
                line += r'&' + f"{row.reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.reward[error_metric].iloc[0]:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    print('')
    print('Latex Table::')
    print(table)
    print('')
    return df_out, table

def custom_format(number, threshold=1e-2):
    if abs(number) < threshold:
        if number == 0:
            return '0.00'
        else:
            return f"{number:.2e}"
    else:
        return f"{number:.2f}"

def generate_n_step_graph(df_results, wandb=None, use_95_ci=True):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method', 'gamma']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method', 'gamma']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'

    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    # plt.rcParams["font.family"] = "Times New Roman"
    SCALE = 8
    HEIGHT_SCALE = 0.5
    LEGEND_Y_CORD = 0.5  # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}
    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    # plt.gcf().subplots_adjust(bottom=(1-1/HEIGHT_SCALE), left=0.15, top=0.99)
    plt.gcf().subplots_adjust(bottom=0.40, left=0.2) #, top=0.95)
    method_map = {'sindy': 'SINDY', 'te-cde': 'TE-CDE'}
                            #  'discrete_planning': 'Discrete Planning',
                            #  'continuous_planning': 'Continuous Planning',
                            #  'active_observing_control': r'\bf Active Sampling Control',
                            #  'random': 'Random'}

    y_metric = 'test_rmse'

    for env_name in df_out.env_name.unique():
        for method in df_out.method.unique():
            df = df_out[df_out.env_name == env_name]
            x = [1]
            # x = df[df.method == method]['gamma']
            y_mean = df[df.method == method][y_metric]['mean'].iloc[0]
            y_std = df[df.method == method][y_metric][error_metric].iloc[0]
            plt.plot(x, y_mean, '--o', label=method_map[method])
            plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)

        # cp_y_mean = df_t[df_t.method == 'continuous_planning'][y_metric]['mean'].iloc[0]
        # cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        # cp_y_std = df_t[df_t.method == 'continuous_planning'][y_metric][error_metric].iloc[0]
        # cp_y_std = np.ones_like(y_mean) * cp_y_std
        # plt.plot(x,cp_y_mean,'--o',label=method_map['continuous_planning'])
        # plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
        plt.xlabel(r'$n$-step')
        plt.ylabel(r'Normalized RMSE')
        plt.yscale('log')
        # plt.xscale('log')
        # plt.axvline(x=threshold_we_used, color='r')

        # plt.legend(loc="lower center", bbox_to_anchor=(
        #             LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
        plt.legend(loc="upper right", ncol=1, fancybox=True, shadow=True)
        plt.tight_layout()                    
        plt.savefig(f'./results/n_step_{env_name}.png')
        plt.savefig(f'./results/n_step_{env_name}.pdf')
        print(f'./results/n_step_{env_name}.png')
        plt.clf()


def generate_n_step_graph(df_results, wandb=None, use_95_ci=True):
    df_results = df_results.drop(columns=['global_equation_string', 'fine_tuned', 'method'])
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method', 'domain_conf']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method', 'domain_conf']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'

    # Grouped sorting
    df_out['env_name_order'] = df_out['env_name'].map(env_name_ordering)
    df_out['method_order'] = df_out['method'].map(method_ordering)
    df_out = df_out.sort_values(by=['env_name_order', 'method_order'])
    df_out = df_out.drop(columns=['env_name_order', 'method_order'])

    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    # plt.rcParams["font.family"] = "Times New Roman"
    SCALE = 10
    HEIGHT_SCALE =0.8
    LEGEND_Y_CORD = -1.2  # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}
    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    # plt.gcf().subplots_adjust(bottom=(1-1/HEIGHT_SCALE), left=0.15, top=0.99)
    
    y_metric = 'test_rmse'

    # Calculate global y-axis limits
    global_min_y = np.inf
    global_max_y = -np.inf

    for env_name in df_out.env_name.unique():
        for decoder_test_step in list(set(l[0] for l in list(df_out.columns) if 'decoder_test_rmse_' in l[0])):
            for method in df_out.method.unique():
                df = df_out[df_out.env_name == env_name]
                df = df[df.method == method]
                y_mean = df[decoder_test_step]['mean']
                y_std = df[decoder_test_step][error_metric]
                global_min_y = min(global_min_y, (y_mean - y_std).min())
                global_max_y = max(global_max_y, (y_mean + y_std).max())

    global_min_y = 0.5
    global_max_y = 10

    steps = list(set(l[0] for l in list(df_out.columns) if 'decoder_test_rmse_' in l[0]))
    steps.append('encoder_test_rmse_orig')
    steps.sort(key=lambda x: STEP_AHEAD_NAME_MAP[x])

    # n-step graph first
    env_name = 'EQ_4_D'
    # for env_name in df_out.env_name.unique():
    plt.figure()
    plt.gcf().subplots_adjust(bottom=0.40, left=0.2) #, top=0.95)
    data_dict = {}
    # res_l = []
    # std_l = []
    for method in df_out.method.unique():
        x, y_mean, y_std = [], [], []
        data_dict[method] = {'res': [], 'std': []}
        for decoder_test_step in steps:
            x.append(STEP_AHEAD_NAME_MAP[decoder_test_step])
            df = df_out[df_out.env_name == env_name]
            df = df[df.method == method] 
            y_mean.append(df[decoder_test_step]['mean'].to_numpy()[0])
            y_std.append(df[decoder_test_step][error_metric].to_numpy()[0])
        x = np.array(x)
        y_mean = np.array(y_mean)
        y_std = np.array(y_std)
        plt.plot(x, y_mean, '--o', label=method_map[method])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std, alpha=0.25)
        # plt.ylim(bottom=0)
        data_dict[method]['res'].append([(xi, yi) for xi, yi in zip(x, y_mean)])
        data_dict[method]['std'].append([(y_meani - y_stdi,y_meani + y_stdi) for y_meani, y_stdi in zip(y_mean, y_std)])

    # cp_y_mean = df_t[df_t.method == 'continuous_planning'][y_metric]['mean'].iloc[0]
    # cp_y_mean = np.ones_like(y_mean) * cp_y_mean
    # cp_y_std = df_t[df_t.method == 'continuous_planning'][y_metric][error_metric].iloc[0]
    # cp_y_std = np.ones_like(y_mean) * cp_y_std
    # plt.plot(x,cp_y_mean,'--o',label=method_map['continuous_planning'])
    # plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
    plt.xlabel(r'$\tau$-step ahead prediction')
    plt.ylabel(r'RMSE (normalized)')
    plt.xticks(x)
    plt.yscale('log')
    # plt.ylim(global_min_y, global_max_y)
    # plt.xscale('log')
    # plt.axvline(x=threshold_we_used, color='r')

    plt.legend(loc="lower center", bbox_to_anchor=(
            LEGEND_X_CORD, LEGEND_Y_CORD), ncol=2, fancybox=True, shadow=True)                 
    plt.savefig(f'./results/domain_conf_{env_name}_n-step-ahead.png')
    plt.savefig(f'./results/domain_conf_{env_name}_n-step-ahead.pdf')
    print(f'./results/domain_conf_{env_name}_n-step-ahead.png')
    plt.clf()
    plt.close()
    print('')
    print(decoder_test_step)
    print(data_dict)
    # print(std_l)
    print('')

def generate_overlap_graph(df_results, wandb=None, use_95_ci=True):
    df_results = df_results.drop(columns=['global_equation_string', 'fine_tuned', 'method'])
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'method', 'domain_conf']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'method', 'domain_conf']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'

    # Grouped sorting
    df_out['env_name_order'] = df_out['env_name'].map(env_name_ordering)
    df_out['method_order'] = df_out['method'].map(method_ordering)
    df_out = df_out.sort_values(by=['env_name_order', 'method_order'])
    df_out = df_out.drop(columns=['env_name_order', 'method_order'])

    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    # plt.rcParams["font.family"] = "Times New Roman"
    SCALE = 10
    HEIGHT_SCALE =0.8
    LEGEND_Y_CORD = -1.2  # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}
    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    # plt.gcf().subplots_adjust(bottom=(1-1/HEIGHT_SCALE), left=0.15, top=0.99)
    
    y_metric = 'test_rmse'

    # Calculate global y-axis limits
    global_min_y = np.inf
    global_max_y = -np.inf

    for env_name in df_out.env_name.unique():
        for decoder_test_step in list(set(l[0] for l in list(df_out.columns) if 'decoder_test_rmse_' in l[0])):
            for method in df_out.method.unique():
                df = df_out[df_out.env_name == env_name]
                df = df[df.method == method]
                y_mean = df[decoder_test_step]['mean']
                y_std = df[decoder_test_step][error_metric]
                global_min_y = min(global_min_y, (y_mean - y_std).min())
                global_max_y = max(global_max_y, (y_mean + y_std).max())

    global_min_y = 0.5
    global_max_y = 10

    steps = list(set(l[0] for l in list(df_out.columns) if 'decoder_test_rmse_' in l[0]))
    steps.append('encoder_test_rmse_orig')
    steps.sort(key=lambda x: STEP_AHEAD_NAME_MAP[x])

    # n-step graph first
    domain_conf_to_plot_for_n_step_graph = 2
    for env_name in df_out.env_name.unique():
        plt.figure()
        plt.gcf().subplots_adjust(bottom=0.40, left=0.2) #, top=0.95)
        data_dict = {}
        # res_l = []
        # std_l = []
        for method in df_out.method.unique():
            x, y_mean, y_std = [], [], []
            data_dict[method] = {'res': [], 'std': []}
            for decoder_test_step in steps:
                x.append(STEP_AHEAD_NAME_MAP[decoder_test_step])
                df = df_out[df_out.env_name == env_name]
                df = df[df.method == method] 
                x_d = df['domain_conf']
                d_idx = np.where(np.array(x_d == 2))[0]
                y_mean.append(df[decoder_test_step]['mean'].to_numpy()[d_idx][0])
                y_std.append(df[decoder_test_step][error_metric].to_numpy()[d_idx][0])
            x = np.array(x)
            y_mean = np.array(y_mean)
            y_std = np.array(y_std)
            plt.plot(x, y_mean, '--o', label=method_map[method])
            plt.fill_between(x,y_mean - y_std,y_mean + y_std, alpha=0.25)
            # plt.ylim(bottom=0)
            data_dict[method]['res'].append([(xi, yi) for xi, yi in zip(x, y_mean)])
            data_dict[method]['std'].append([(y_meani - y_stdi,y_meani + y_stdi) for y_meani, y_stdi in zip(y_mean, y_std)])

        # cp_y_mean = df_t[df_t.method == 'continuous_planning'][y_metric]['mean'].iloc[0]
        # cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        # cp_y_std = df_t[df_t.method == 'continuous_planning'][y_metric][error_metric].iloc[0]
        # cp_y_std = np.ones_like(y_mean) * cp_y_std
        # plt.plot(x,cp_y_mean,'--o',label=method_map['continuous_planning'])
        # plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
        plt.xlabel(r'$\tau$-step ahead prediction')
        plt.ylabel(r'RMSE (normalized)')
        plt.xticks(x)
        plt.yscale('log')
        # plt.ylim(global_min_y, global_max_y)
        # plt.xscale('log')
        # plt.axvline(x=threshold_we_used, color='r')

        plt.legend(loc="lower center", bbox_to_anchor=(
                LEGEND_X_CORD, LEGEND_Y_CORD), ncol=2, fancybox=True, shadow=True)                 
        plt.savefig(f'./results/domain_conf_{env_name}_n-step-ahead.png')
        plt.savefig(f'./results/domain_conf_{env_name}_n-step-ahead.pdf')
        print(f'./results/domain_conf_{env_name}_n-step-ahead.png')
        plt.clf()
        plt.close()
        print('')
        print(decoder_test_step)
        print(data_dict)
        # print(std_l)
        print('')


    for env_name in df_out.env_name.unique():
        for decoder_test_step in steps:
            plt.figure()
            plt.gcf().subplots_adjust(bottom=0.40, left=0.2) #, top=0.95)
            data_dict = {}
            # res_l = []
            # std_l = []

            for method in df_out.method.unique():
                data_dict[method] = {'res': [], 'std': []}
                df = df_out[df_out.env_name == env_name]
                df = df[df.method == method] 
                x = df['domain_conf']
                y_mean = df[decoder_test_step]['mean']
                y_std = df[decoder_test_step][error_metric]
                plt.plot(x, y_mean, '--o', label=method_map[method])
                plt.fill_between(x,y_mean - y_std,y_mean + y_std, alpha=0.25)
                # plt.ylim(bottom=0)
                data_dict[method]['res'].append([(xi, yi) for xi, yi in zip(x, y_mean)])
                data_dict[method]['std'].append([(y_meani - y_stdi,y_meani + y_stdi) for y_meani, y_stdi in zip(y_mean, y_std)])

            # cp_y_mean = df_t[df_t.method == 'continuous_planning'][y_metric]['mean'].iloc[0]
            # cp_y_mean = np.ones_like(y_mean) * cp_y_mean
            # cp_y_std = df_t[df_t.method == 'continuous_planning'][y_metric][error_metric].iloc[0]
            # cp_y_std = np.ones_like(y_mean) * cp_y_std
            # plt.plot(x,cp_y_mean,'--o',label=method_map['continuous_planning'])
            # plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
            plt.xlabel(r'Degree of time-dependent confounding $\gamma$')
            plt.ylabel(r'RMSE (normalized)')
            plt.xticks(x.values)
            plt.yscale('log')
            # plt.ylim(global_min_y, global_max_y)
            # plt.xscale('log')
            # plt.axvline(x=threshold_we_used, color='r')

            plt.legend(loc="lower center", bbox_to_anchor=(
                    LEGEND_X_CORD, LEGEND_Y_CORD), ncol=2, fancybox=True, shadow=True)                 
            plt.savefig(f'./results/domain_conf_{env_name}_{decoder_test_step}.png')
            plt.savefig(f'./results/domain_conf_{env_name}_{decoder_test_step}.pdf')
            print(f'./results/domain_conf_{env_name}_{decoder_test_step}.png')
            plt.clf()
            plt.close()
            print('')
            print(decoder_test_step)
            print(data_dict)
            # print(std_l)
            print('')


def plot_threshold_plots(df, use_95_ci=True):
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    # plt.rcParams["font.family"] = "Times New Roman"
    SCALE = 13
    HEIGHT_SCALE =0.8
    LEGEND_Y_CORD = -1.2  # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}

    if use_95_ci:
        error_metric = 'ci'
    else:
        error_metric = 'std'
    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    # plt.gcf().subplots_adjust(bottom=0.40, left=0.2, top=0.95)

    method_map = {'discrete_monitoring': 'Discrete Monitoring',
                             'discrete_planning': 'Discrete Planning',
                             'continuous_planning': r'Continuous Planning $\mathcal{O}=13$',
                             'active_observing_control': r'Active Sampling Control',
                             'random': 'Random'}


    thresholds_used = {'oderl-cancer': 6.760299902695876,
                        'oderl-pendulum': 0.012269268,
                        'oderl-acrobot': 0.08927406,
                        'oderl-cartpole': 0.029934801}

    print('')
    x_metric = 'observing_var_threshold' # 'observing_var_threshold'
    plots_total = 3
    for env_name in df.env_name.unique():
        threshold_we_used = thresholds_used[env_name]
        df_t = df[df.env_name==env_name]
        ax = plt.subplot(plots_total, 1, 1)
        y_metric = 'total_reward'
        x = df_t[df_t.method == 'active_observing_control'][x_metric]#['mean']
        y_mean = df_t[df_t.method == 'active_observing_control'][y_metric]['mean']
        y_std = df_t[df_t.method == 'active_observing_control'][y_metric][error_metric]
        plt.plot(x,y_mean,'--o',label=method_map['active_observing_control'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)
        cp_y_mean = df_t[df_t.method == 'continuous_planning'][y_metric]['mean'].iloc[0]
        cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        cp_y_std = df_t[df_t.method == 'continuous_planning'][y_metric][error_metric].iloc[0]
        cp_y_std = np.ones_like(y_mean) * cp_y_std
        plt.plot(x,cp_y_mean,'--o',label=method_map['continuous_planning'])
        plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
        plt.ylabel(r'$\mathcal{U}$')
        plt.axvline(x=threshold_we_used, color='r')

        ax = plt.subplot(plots_total, 1, 2, sharex=ax)
        y_metric = 'state_reward'
        x = df_t[df_t.method == 'active_observing_control'][x_metric]#['mean']
        y_mean = df_t[df_t.method == 'active_observing_control'][y_metric]['mean']
        y_std = df_t[df_t.method == 'active_observing_control'][y_metric][error_metric]
        plt.plot(x,y_mean,'--o',label=method_map['active_observing_control'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)
        cp_y_mean = df_t[df_t.method == 'continuous_planning'][y_metric]['mean'].iloc[0]
        cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        cp_y_std = df_t[df_t.method == 'continuous_planning'][y_metric][error_metric].iloc[0]
        cp_y_std = np.ones_like(y_mean) * cp_y_std
        plt.plot(x,cp_y_mean,'--o',label=method_map['continuous_planning'])
        plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
        plt.ylabel(r'$\mathcal{R}$')
        plt.axvline(x=threshold_we_used, color='r')
        # ax2 = ax.twinx()
        ax = plt.subplot(plots_total, 1, 3, sharex=ax)
        y_metric = 'observation_reward'
        x = df_t[df_t.method == 'active_observing_control'][x_metric]#['mean']
        y_mean = df_t[df_t.method == 'active_observing_control'][y_metric]['mean']
        y_std = df_t[df_t.method == 'active_observing_control'][y_metric][error_metric]
        plt.plot(x,y_mean,'--o',label=method_map['active_observing_control'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)
        cp_y_mean = df_t[df_t.method == 'continuous_planning'][y_metric]['mean'].iloc[0]
        cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        cp_y_std = df_t[df_t.method == 'continuous_planning'][y_metric][error_metric].iloc[0]
        cp_y_std = np.ones_like(y_mean) * cp_y_std
        plt.plot(x,cp_y_mean,'--o',label=method_map['continuous_planning'])
        plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
        plt.ylabel(r'$-\mathcal{C}$')
        plt.xlabel(r'Threshold $\tau$')
        plt.axvline(x=threshold_we_used, color='r')

        plt.legend(loc="lower center", bbox_to_anchor=(
                    LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
        # plt.tight_layout()                    
        plt.savefig(f'./plots/threshold_{env_name}.png')
        plt.savefig(f'./plots/threshold_{env_name}.pdf')
        print(f'./plots/threshold_{env_name}.png')
        plt.clf()
    print('')


# # https://stackoverflow.com/questions/42281844/what-is-the-mathematics-behind-the-smoothing-parameter-in-tensorboards-scalar#_=_
# def smooth(scalars, weight):  # Weight between 0 and 1
#     last = scalars[0]  # First value in the plot (first timestep)
#     smoothed = list()
#     for point in scalars:
#         smoothed_val = last * weight + (1 - weight) * point  # Calculate smoothed value
#         smoothed.append(smoothed_val)  # Save it
#         last = smoothed_val  # Anchor the last smoothed value

#     return smoothed


def load_df(path, remove_extra_columns=True):
    with open(path) as f:
        lines = f.readlines()
    pd_l = []
    for line in tqdm(lines):
        if '[Exp evaluation complete] {' in line:
            result_dict = line.split('[Exp evaluation complete] ')[1].strip()
            # result_dict = result_dict.replace('nan', '\'nan\'')
            result_dict = result_dict.replace('array', '')
            result_dict = ast.literal_eval(result_dict)
            pd_l.append(result_dict)
            # except:
            #     pass
    dfm = pd.DataFrame(pd_l)
    if remove_extra_columns:
        columns_to_remove_if_exist = ['costs_std_stats', 'planner', 'observed_times', 'observed_times_diff', 'costs_std_median', 's', 'a', 'r', 'cost_std_plot', 'ri', 'telem_file_path']
        current_columns = list(dfm.columns)
        columns_to_drop = set(columns_to_remove_if_exist) & set(current_columns)
        columns_to_drop = list(columns_to_drop)
        dfm = dfm.drop(columns=columns_to_drop)
    else:
        columns_to_np_arrays_if_exist = ['observed_times', 'observed_times_diff', 's', 'a', 'r', 'cost_std_plot', 'ri']
        current_columns = list(dfm.columns)
        columns_to_np_arrays = set(columns_to_np_arrays_if_exist) & set(current_columns)
        columns_to_np_arrays = list(columns_to_np_arrays)
        dfm[columns_to_np_arrays] = dfm[columns_to_np_arrays].applymap(np.array)
    return dfm

def extract_state_rewards(df):
    dd = {}
    for _, row in df.iterrows():
        k, v = row['observations_taken'], row['state_reward']
        if k in dd:
            dd[k].append(v)
        else:
            dd[k] = [v]
    return dd

def smooth(scalars: np.ndarray, weight: float) -> np.ndarray:
    """
    EMA implementation according to
    https://github.com/tensorflow/tensorboard/blob/34877f15153e1a2087316b9952c931807a122aa7/tensorboard/components/vz_line_chart2/line-chart.ts#L699
    """
    last = 0
    smoothed = []
    num_acc = 0
    for next_val in scalars:
        last = last * weight + (1 - weight) * next_val
        num_acc += 1
        # de-bias
        debias_weight = 1
        if weight != 1:
            debias_weight = 1 - np.power(weight, num_acc)
        smoothed_val = last / debias_weight
        smoothed.append(smoothed_val)

    return np.array(smoothed)

def seed_all(seed=None):
    """
    Set the torch, numpy, and random module seeds based on the seed
    specified in config. If there is no seed or it is None, a time-based
    seed is used instead and is written to config.
    """
    # Default uses current time in milliseconds, modulo 1e9
    if seed is None:
        seed = round(time() * 1000) % int(1e9)

    # Set the seeds using the shifted seed
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)