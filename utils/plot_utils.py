from tqdm import tqdm
import ast
import pandas as pd
import numpy as np
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ci(data, confidence=0.95):
    # https://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return h

def configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE, use_autolayout=True):
    pd.set_option('mode.chained_assignment', None)
    sn.set(rc={'figure.figsize': (SCALE, int(HEIGHT_SCALE * SCALE)), 'figure.autolayout': use_autolayout, 'text.usetex': True, 'text.latex.preamble': '\n'.join([
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

def get_normalized_policy_values_delay_zero():
    random_policy = {'oderl-acrobot': -2948.636826752257, 'oderl-cartpole': -14246.301963850627, 'oderl-pendulum': -616.7659306662474}
    best_policy = {'oderl-acrobot': -571.1055129432718, 'oderl-cartpole': -139.68956484338668, 'oderl-pendulum': -121.04611233502484}
    return random_policy, best_policy

def df_from_log(path, remove_extra_columns=True):
    with open(path) as f:
        lines = f.readlines()
    pd_l = []
    for line in tqdm(lines):
        if '[Policy evaluation complete] {' in line:
            result_dict = line.split('[Policy evaluation complete] ')[1].strip()
            result_dict = result_dict.replace('nan', '\'nan\'')
            result_dict = result_dict.replace('array', '')
            result_dict = ast.literal_eval(result_dict)
            pd_l.append(result_dict)

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
    numeric_columns = ['roll_outs',
                        'time_steps',
                        'episode_elapsed_time',
                        'episode_elapsed_time_per_it',
                        'dt_sim',
                        'dt_plan',
                        'total_reward',
                        'state_reward',
                        'state_reward_std',
                        'observation_reward',
                        'observations_taken',
                        'observing_var_threshold',
                        'observing_cost',
                        'observation_noise',
                        'seed']
    dfm[numeric_columns] = dfm[numeric_columns].apply(pd.to_numeric, errors='coerce')
    # dfm['name'] = dfm.model_name + '+' + dfm.sampling_policy
    return dfm

def normalize_means(df):
    df_means = df.groupby(['env_name', 'sampling_policy', 'model_name']).agg(np.mean).reset_index()
    for env_name in df_means.env_name.unique():
        pass
        df_means_env = df_means[df_means.env_name == env_name]
        random_row = df_means_env[df_means_env.sampling_policy == 'random'].iloc[0]
        best_row = df_means_env[df_means_env.sampling_policy == 'continuous_planning'].iloc[0]

        df.loc[df.env_name==env_name, 'total_reward'] = ((df[df.env_name == env_name].total_reward - random_row.total_reward) / (best_row.total_reward - random_row.total_reward)) * 100.0
        df.loc[df.env_name==env_name, 'state_reward'] = ((df[df.env_name == env_name].state_reward - random_row.state_reward) / (best_row.state_reward - random_row.state_reward)) * 100.0
    return df

def normalize_means_cp_matching_obs(df_in):
    df = df_in[df_in.fixed_continuous_planning_observations.isnull()]
    df_means = df.groupby(['env_name', 'sampling_policy', 'model_name']).agg(np.mean).reset_index()
    for env_name in df_means.env_name.unique():
        df_means_env = df_means[df_means.env_name == env_name]
        random_row = df_means_env[df_means_env.sampling_policy == 'random'].iloc[0]
        best_row = df_means_env[df_means_env.sampling_policy == 'continuous_planning'].iloc[0]

        df_in.loc[df_in.env_name==env_name, 'total_reward'] = ((df_in[df_in.env_name == env_name].total_reward - random_row.total_reward) / (best_row.total_reward - random_row.total_reward)) * 100.0
        df_in.loc[df_in.env_name==env_name, 'state_reward'] = ((df_in[df_in.env_name == env_name].state_reward - random_row.state_reward) / (best_row.state_reward - random_row.state_reward)) * 100.0
    return df_in

def remove_unneeded_columns(df):
    columns_to_remove_if_exist = ['costs_std_stats', 'planner', 'observed_times', 'observed_times_diff', 'costs_std_median', 's', 'a', 'r', 'cost_std_plot', 'ri', 'telem_file_path']
    current_columns = list(df.columns)
    columns_to_drop = set(columns_to_remove_if_exist) & set(current_columns)
    columns_to_drop = list(columns_to_drop)
    df = df.drop(columns=columns_to_drop)
    return df

def generate_main_results_table_cp_with_unique_obs(df_results, wandb=None):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    df_out = df_results.groupby(['env_name', 'sampling_policy', 'model_name']).agg([np.mean, np.std]).reset_index()
    df_out.loc[df_out.sampling_policy == 'random', 'total_reward'] = 0
    df_out.loc[df_out.sampling_policy == 'random', 'state_reward'] = 0

    sf = 3
    env_name_map = {'oderl-cartpole': 'Cartpole',
                    'oderl-pendulum': 'Pendulum',
                    'oderl-acrobot': 'Acrobot',
                    'oderl-cancer': 'Cancer'}

    env_name_ordering = {'oderl-cartpole': 2,
                    'oderl-pendulum': 3,
                    'oderl-acrobot': 1,
                    'oderl-cancer': 0}

    sampling_policy_map = {'discrete_monitoring': 'Discrete Monitoring',
                             'discrete_planning': 'Discrete Planning',
                             'continuous_planning': 'Continuous Planning',
                             'active_observing_control': r'\bf Active Sampling Control',
                             'random': 'Random'}
                             
    df_out = df_out.sort_values(by=['env_name'], key=lambda x: x.map(env_name_ordering))
    table_lines = []
    line = r'\begin{tabular}{@{}l' + '|ccc' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    table_lines.append(''.join([r'&  \multicolumn{3}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
    table_lines.append(r'Policy ' + r'& $\mathcal{U}$ & $\mathcal{R}$ & $\mathcal{O}$' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for sampling_policy in df_out.sampling_policy.unique():
        line = sampling_policy_map[sampling_policy]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.sampling_policy == sampling_policy) & (df_out.env_name == env_name)]
            line += r'&' + f"{row.total_reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.total_reward['std'].iloc[0]:.{sf}g}" + r'&' + f"{row.state_reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.state_reward['std'].iloc[0]:.{sf}g}" + r'&' + f"{row.observations_taken['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.observations_taken['std'].iloc[0]:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    # print('')
    # print('Latex Table::')
    # print(table)
    # print('')
    return df_out, table

def generate_main_results_table(df_results, wandb=None, use_95_ci=True):
    # Process seeds here
    df_results = remove_unneeded_columns(df_results)
    if use_95_ci:
        df_out = df_results.groupby(['env_name', 'sampling_policy', 'model_name']).agg([np.mean, ci]).reset_index()
        error_metric = 'ci'
    else:
        df_out = df_results.groupby(['env_name', 'sampling_policy', 'model_name']).agg([np.mean, np.std]).reset_index()
        error_metric = 'std'
    df_out.loc[df_out.sampling_policy == 'random', 'total_reward'] = 0
    df_out.loc[df_out.sampling_policy == 'random', 'state_reward'] = 0

    sf = 3
    env_name_map = {'oderl-cartpole': 'Cartpole',
                    'oderl-pendulum': 'Pendulum',
                    'oderl-acrobot': 'Acrobot',
                    'oderl-cancer': 'Cancer',
                    'oderl-glucose': 'Glucose',
                    'oderl-hiv': 'HIV',
                    'oderl-quadrotor': 'Quadcoptor'}

    env_name_ordering = {'oderl-cartpole': 2,
                    'oderl-pendulum': 3,
                    'oderl-acrobot': 1,
                    'oderl-cancer': 0,
                    'oderl-glucose': 4,
                    'oderl-hiv': 5,
                    'oderl-quadrotor': 6}

    sampling_policy_map = {'discrete_monitoring': 'Discrete Monitoring',
                             'discrete_planning': 'Discrete Planning',
                             'continuous_planning': 'Continuous Planning',
                             'active_observing_control': r'\bf Active Sampling Control',
                             'random': 'Random'}
                             
    df_out = df_out.sort_values(by=['env_name'], key=lambda x: x.map(env_name_ordering))
    table_lines = []
    line = r'\begin{tabular}{@{}l' + '|ccc' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    table_lines.append(''.join([r'&  \multicolumn{3}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
    table_lines.append(r'Policy ' + r'& $\mathcal{U}$ & $\mathcal{R}$ & $\mathcal{O}$' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for sampling_policy in df_out.sampling_policy.unique():
        if sampling_policy == 'active_observing_control':
            line = r'\midrule' + '\n' + sampling_policy_map[sampling_policy]
        else:
            line = sampling_policy_map[sampling_policy]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.sampling_policy == sampling_policy) & (df_out.env_name == env_name)]
            if sampling_policy == 'active_observing_control':
                line += (r'&\bf' if row.total_reward['mean'].iloc[0] > 100.0 else r'&') + f"{row.total_reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.total_reward[error_metric].iloc[0]:.{sf}g}" + (r'&\bf' if row.state_reward['mean'].iloc[0] > 100.0 else r'&') + f"{row.state_reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.state_reward[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.observations_taken['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.observations_taken[error_metric].iloc[0]:.{sf}g}"
            else:
                line += r'&' + f"{row.total_reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.total_reward[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.state_reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.state_reward[error_metric].iloc[0]:.{sf}g}" + r'&' + f"{row.observations_taken['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.observations_taken[error_metric].iloc[0]:.{sf}g}"
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


def plot_error_plots(results):
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    # plt.rcParams["font.family"] = "Times New Roman"
    # SCALE = 13
    SCALE = 8
    HEIGHT_SCALE =0.8
    LEGEND_Y_CORD = -1.2  # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}

    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    # plt.gcf().subplots_adjust(bottom=0.40, left=0.2, top=0.95)

    sampling_policy_map = {'discrete_monitoring': 'Discrete Monitoring',
                             'discrete_planning': 'Discrete Planning',
                             'continuous_planning': r'Continuous Planning $\mathcal{O}=13$',
                             'active_observing_control': r'Active Sampling Control',
                             'random': 'Random'}


    thresholds_used = {'oderl-cancer': 6.760299902695876,
                        'oderl-pendulum': 0.012269268,
                        'oderl-acrobot': 0.08927406,
                        'oderl-cartpole': 0.029934801}
    
    method_name_map = {'llmatic': 'Code-L2MAC',
                       'autogpt': 'AutoGPT',
                       'gpt4': 'GPT4'}
    
    autogpt = results[results['method'] == 'autogpt']
    llmatic = results[results['method'] == 'llmatic']
    gpt4 = results[results['method'] == 'gpt4']

    print('')
    max_x = autogpt.change_count.max()
    plt.plot((llmatic.change_count / llmatic.change_count.max())*100.0, llmatic.errors, '--o', label='Code-L2MAC', alpha=0.7)
    plt.plot((autogpt.change_count / autogpt.change_count.max())*100.0, autogpt.errors, '--o', label='AutoGPT', alpha=0.7)
    plt.plot(gpt4.change_count, gpt4.errors, '--o', label='GPT4', alpha=0.7)
    plt.ylabel(r'\# Errors')
    plt.xlabel(r'\% Episode Completion (Normalized Steps)')
    # plt.legend(loc="lower center", bbox_to_anchor=(
                # LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
    # plt.legend(loc="upper center", ncol=1, fancybox=True, shadow=True)
    # plt.tight_layout()                    
    plt.savefig(f'./results/errors.png')
    plt.savefig(f'./results/errors.pdf')
    print(f'./results/errors.png')
    plt.clf()

    print('')

    llmatic_f_c = np.ones(llmatic.change_count.shape[0])*100.0 * (19 / 20)
    llmatic_f_c[0] = 100.0
    plt.plot((llmatic.change_count / llmatic.change_count.max())*100.0, llmatic_f_c, '--o', label='Code-L2MAC', alpha=0.7)
    auto_gpt_f = np.ones(autogpt.change_count.shape[0]) * (8 / 20) * 100.0
    auto_gpt_f[0] = 100.0
    plt.plot((autogpt.change_count / autogpt.change_count.max())*100.0, auto_gpt_f, '--o', label='AutoGPT', alpha=0.7)
    plt.plot(gpt4.change_count, 100.0, '--o', label='GPT4', alpha=0.7)
    # plt.plot(autogpt.change_count, np.ones(autogpt.change_count.shape[0]) * 100.0, '--o', label='L2MAC', alpha=0.7)
    # plt.plot(autogpt.change_count, auto_gpt_f, '--o', label='AutoGPT', alpha=0.7)
    # plt.plot(autogpt.change_count[0], np.ones(autogpt.change_count.shape[0])[0] * 100.0, '--o', label='GPT4', alpha=0.7)
    plt.ylim([0,105.0])
    # plt.ylabel(r'\% Feature Req. in Context')
    plt.ylabel(r'\% Feature Req. Retained')
    plt.xlabel(r'\% Episode Completion (Normalized Steps)')
    # plt.legend(loc="upper center", ncol=1, fancybox=True, shadow=True)
    # plt.tight_layout()                    
    plt.savefig(f'./results/features.png')
    plt.savefig(f'./results/features.pdf')
    print(f'./results/features.png')
    plt.clf()


    print('')

    print('')
    max_x = autogpt.change_count.max()
    plt.plot((llmatic.change_count / llmatic.change_count.max())*100.0, llmatic.errors, '--o', label='Code-L2MAC', alpha=0.7)
    plt.plot((autogpt.change_count / autogpt.change_count.max())*100.0, autogpt.errors, '--o', label='AutoGPT', alpha=0.7)
    plt.plot(gpt4.change_count, gpt4.errors, '--o', label='GPT4', alpha=0.7)
    plt.ylabel(r'\# Errors')
    plt.xlabel(r'\% Episode Completion (Normalized Steps)')
    # plt.legend(loc="lower center", bbox_to_anchor=(
                # LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
    plt.legend(loc="upper left", ncol=1, fancybox=True, shadow=True)
    # plt.tight_layout()                    
    plt.savefig(f'./results/errors_legend.png')
    plt.savefig(f'./results/errors_legend.pdf')
    print(f'./results/errors_legend.png')
    plt.clf()


    print('')
    # import pandas as pd
    # import matplotlib.pyplot as plt
    # import seaborn as sns

    # # Concatenate dataframes
    # df = results

    # # Plotting
    # plt.figure(figsize=(10,6))

    # # Stacked bar plot for total tests and tests passed
    # df_grouped = df.groupby('method').max()[['tests_total', 'tests_passed']]
    # df_grouped.plot(kind='bar', stacked=True, ax=plt.gca())

    # # Line plot for the progression of tests passed
    # for method, group in df.groupby('method'):
    #     plt.plot(group['change_count'], group['tests_passed'], label=f"{method} progression", marker='o')

    # plt.title("Performance Comparison of Three Methods in Test Generation and Solution")
    # plt.ylabel("Number of Tests")
    # plt.xlabel("Methods")
    # plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    # plt.tight_layout()
    df = results



    # Assuming you've already concatenated the dataframes into df
    # fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True, sharey=True)
    fig, axes = plt.subplots(3, 1, sharex=True)

    methods = ["llmatic", "autogpt", "gpt4"]

    # Set total horizontal space range between 0 and 1
    horizontal_space = 1.0

    # Beautiful colors
    beautiful_green = "#28A745"
    beautiful_red = "#DC3545"

    # Find the overall maximum value for 'tests_total' across all methods
    ymax = df['tests_total'].max() + 5  # Added 5 for some padding at the top

    for ax, method in zip(axes, methods):
        subset = df[df['method'] == method]
        
        # Calculate the number of bars
        n_bars = len(subset)
        
        # Calculate width of each bar
        # bar_width = (horizontal_space / n_bars) - 0.02  # subtracting a small value for spacing
        bar_width = (horizontal_space / n_bars)
        
        # Adjust x-values so they lie uniformly between 0 and 1
        x_values = np.linspace(0, horizontal_space - bar_width, n_bars)
        
        # Bar for passed tests
        ax.bar(x_values, subset['tests_passed'], width=bar_width, label='Tests Passed', color=beautiful_green, alpha=0.7, align='edge')
        
        # Bar for tests not passed stacked on top
        ax.bar(x_values, subset['tests_total'] - subset['tests_passed'], width=bar_width, label='Tests Failed', color=beautiful_red, bottom=subset['tests_passed'], alpha=0.7, align='edge')
        
        ax.set_title(method_name_map[method])
        # ax.set_ylabel('Number of Tests')
        # ax.legend()
        # ax.set_ylim(0, ymax)  # Set the common y-axis limit
        if method == 'llmatic':
            ax.set_ylim(0, 50)  # Set the common y-axis limit
        ax.set_xlim(0, 1)  # Ensure x-axis starts from 0 and goes up to 1
        if method == 'autogpt':
            ax.set_ylabel('Number of Tests')


    # Common x label
    # axes[-1].set_xlabel('Adjusted Change Count')
    axes[-1].set_xlabel(r'\% Episode Completion (Normalized Steps)')
    # axes[-1].set_ylabel('Number of Tests')  # This sets the y-label for the main axis
    # axes.set_ylabel('Number of Tests')  # This sets the y-label for the main axis
    plt.tight_layout()
    plt.show()



    plt.savefig(f'./results/chatgpt.png')
    plt.savefig(f'./results/chatgpt.pdf')
    print(f'./results/chatgpt.png')
    plt.clf()

    # Save legend


    # Assuming you've already concatenated the dataframes into df
    # fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True, sharey=True)
    fig, axes = plt.subplots(1, 1, sharex=True)

    methods = ["autogpt", "llmatic", "gpt4"]

    # Set total horizontal space range between 0 and 1
    horizontal_space = 1.0

    # Beautiful colors
    beautiful_green = "#28A745"
    beautiful_red = "#DC3545"

    # Find the overall maximum value for 'tests_total' across all methods
    ymax = df['tests_total'].max() + 5  # Added 5 for some padding at the top

    # for ax, method in zip(axes, methods):
    ax = axes
    method = methods[0]
    subset = df[df['method'] == method]
    
    # Calculate the number of bars
    n_bars = len(subset)
    
    # Calculate width of each bar
    # bar_width = (horizontal_space / n_bars) - 0.02  # subtracting a small value for spacing
    bar_width = (horizontal_space / n_bars)
    
    # Adjust x-values so they lie uniformly between 0 and 1
    x_values = np.linspace(0, horizontal_space - bar_width, n_bars)
    
    # Bar for passed tests
    ax.bar(x_values, subset['tests_passed'], width=bar_width, label='Tests Passed', color=beautiful_green, alpha=0.7, align='edge')
    
    # Bar for tests not passed stacked on top
    ax.bar(x_values, subset['tests_total'] - subset['tests_passed'], width=bar_width, label='Tests Failed', color=beautiful_red, bottom=subset['tests_passed'], alpha=0.7, align='edge')
    
    # ax.set_title(method)
    # ax.set_ylabel('Number of Tests')
    ax.legend(fancybox=True, shadow=True)
    ax.set_ylim(0, ymax)  # Set the common y-axis limit
    ax.set_xlim(0, 1)  # Ensure x-axis starts from 0 and goes up to 1

    # Common x label
    # axes[-1].set_xlabel('Adjusted Change Count')
    # axes[-1].set_xlabel(r'\% Episode Completion (Normalized Steps)')
    # plt.tight_layout()
    # plt.show()



    plt.savefig(f'./results/chatgpt_legend.png')
    plt.savefig(f'./results/chatgpt_legend.pdf')
    print(f'./results/chatgpt_legend.png')
    plt.clf()


    print('')
    return


    # # Temps 2
    # # Concatenate the dataframes into df

    # methods = ["autogpt", "llmatic", "gpt4"]

    # # Colors for passed and not passed tests
    # beautiful_green = "#28A745"
    # beautiful_red = "#DC3545"

    # # Patterns for different methods
    # patterns = ['/', '\\', 'x']

    # # Create a merged dataframe with all unique 'change_count' values
    # all_change_counts = df['change_count'].unique()
    # merged_df = pd.DataFrame(all_change_counts, columns=['change_count'])

    # for method in methods:
    #     subset = df[df['method'] == method].copy()
    #     subset = subset.rename(columns={'tests_passed': f'{method}_passed', 'tests_total': f'{method}_total'})
    #     subset = subset[['change_count', f'{method}_passed', f'{method}_total']]
    #     merged_df = merged_df.merge(subset, on='change_count', how='left').fillna(0)

    # # Setting up the plot
    # fig, ax = plt.subplots(figsize=(12, 8))
    # bar_width = 0.2

    # for idx, method in enumerate(methods):
    #     x_values = np.arange(len(all_change_counts)) + idx * bar_width

    #     passed_col = f'{method}_passed'
    #     total_col = f'{method}_total'

    #     ax.bar(x_values, merged_df[passed_col], width=bar_width, color=beautiful_green, label=f'{method} - Tests Passed', alpha=0.7, hatch=patterns[idx])
    #     ax.bar(x_values, merged_df[total_col] - merged_df[passed_col], width=bar_width, bottom=merged_df[passed_col], color=beautiful_red, label=f'{method} - Tests Not Passed', alpha=0.7, hatch=patterns[idx])

    # ax.set_title('Comparison of Methods on Test Performance')
    # ax.set_ylabel('Number of Tests')
    # ax.set_xlabel('Change Count')
    # ax.set_xticks(np.arange(len(all_change_counts)) + bar_width)
    # ax.set_xticklabels(all_change_counts)
    # ax.set_ylim(0, merged_df[[f'{method}_total' for method in methods]].max().max() + 5)  # Adjusting y-axis limit

    # # Creating a legend
    # handles, labels = ax.get_legend_handles_labels()
    # ax.legend(handles[:6:2] + handles[1:6:2], labels[:6:2] + labels[1:6:2], loc='upper left')

    # plt.tight_layout()
    # plt.show()



    # plt.savefig(f'./results/chatgpt2.png')
    # plt.savefig(f'./results/chatgpt2.pdf')
    # print(f'./results/chatgpt2.png')
    # plt.clf()




    plt.plot(llmatic.change_count, llmatic.errors, '--o', label='LLMatic')
    plt.plot(autogpt.change_count, autogpt.errors, '--o', label='AutoGPT')
    plt.plot(gpt4.change_count, gpt4.errors, '--o', label='GPT4')
    plt.ylabel(r'\textbf{\# Errors}')
    plt.xlabel(r'\textbf{\# Code writes}')
    # plt.legend(loc="lower center", bbox_to_anchor=(
                # LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
    plt.legend(loc="lower center", ncol=1, fancybox=True, shadow=True)
    # plt.tight_layout()                    
    plt.savefig(f'./results/errors.png')
    plt.savefig(f'./results/errors.pdf')
    print(f'./results/errors.png')
    plt.clf()

    return 

    x_metric = 'observing_var_threshold' # 'observing_var_threshold'
    plots_total = 3
    for env_name in df.env_name.unique():
        threshold_we_used = thresholds_used[env_name]
        df_t = df[df.env_name==env_name]
        ax = plt.subplot(plots_total, 1, 1)
        y_metric = 'total_reward'
        x = df_t[df_t.sampling_policy == 'active_observing_control'][x_metric]#['mean']
        y_mean = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric]['mean']
        y_std = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric][error_metric]
        plt.plot(x,y_mean,'--o',label=sampling_policy_map['active_observing_control'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)
        cp_y_mean = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric]['mean'].iloc[0]
        cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        cp_y_std = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric][error_metric].iloc[0]
        cp_y_std = np.ones_like(y_mean) * cp_y_std
        plt.plot(x,cp_y_mean,'--o',label=sampling_policy_map['continuous_planning'])
        plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
        plt.ylabel(r'$\mathcal{U}$')
        plt.axvline(x=threshold_we_used, color='r')

        ax = plt.subplot(plots_total, 1, 2, sharex=ax)
        y_metric = 'state_reward'
        x = df_t[df_t.sampling_policy == 'active_observing_control'][x_metric]#['mean']
        y_mean = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric]['mean']
        y_std = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric][error_metric]
        plt.plot(x,y_mean,'--o',label=sampling_policy_map['active_observing_control'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)
        cp_y_mean = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric]['mean'].iloc[0]
        cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        cp_y_std = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric][error_metric].iloc[0]
        cp_y_std = np.ones_like(y_mean) * cp_y_std
        plt.plot(x,cp_y_mean,'--o',label=sampling_policy_map['continuous_planning'])
        plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
        plt.ylabel(r'$\mathcal{R}$')
        plt.axvline(x=threshold_we_used, color='r')
        # ax2 = ax.twinx()
        ax = plt.subplot(plots_total, 1, 3, sharex=ax)
        y_metric = 'observation_reward'
        x = df_t[df_t.sampling_policy == 'active_observing_control'][x_metric]#['mean']
        y_mean = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric]['mean']
        y_std = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric][error_metric]
        plt.plot(x,y_mean,'--o',label=sampling_policy_map['active_observing_control'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)
        cp_y_mean = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric]['mean'].iloc[0]
        cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        cp_y_std = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric][error_metric].iloc[0]
        cp_y_std = np.ones_like(y_mean) * cp_y_std
        plt.plot(x,cp_y_mean,'--o',label=sampling_policy_map['continuous_planning'])
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





def plot_write_heatmaps(data):
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    import matplotlib.colors as mcolors
    import matplotlib.patches as mpatches
    # plt.rcParams["font.family"] = "Times New Roman"
    # SCALE = 13
    SCALE = 8
    HEIGHT_SCALE =0.8
    LEGEND_Y_CORD = -1.2  # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}

    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    # plt.gcf().subplots_adjust(bottom=0.40, left=0.2, top=0.95)

    sampling_policy_map = {'discrete_monitoring': 'Discrete Monitoring',
                             'discrete_planning': 'Discrete Planning',
                             'continuous_planning': r'Continuous Planning $\mathcal{O}=13$',
                             'active_observing_control': r'Active Sampling Control',
                             'random': 'Random'}


    thresholds_used = {'oderl-cancer': 6.760299902695876,
                        'oderl-pendulum': 0.012269268,
                        'oderl-acrobot': 0.08927406,
                        'oderl-cartpole': 0.029934801}
    fig_size = (SCALE, 3)
    plt.figure(figsize=fig_size)

    for k, v in data.items():
        # Create a figure and axis
        # fig, ax = plt.subplots()

        # Plot the first heatmap
        plt.imshow(v['indx_files_exist'].transpose(), cmap=mcolors.ListedColormap(['black', 'white']), interpolation='nearest', origin='lower', aspect='auto')

        # Add a colorbar for the first heatmap
        # cbar1 = fig.colorbar(cax1, ax=ax, orientation='vertical', fraction=.1)

        # Plot the second heatmap with a degree of transparency using the alpha parameter
        # Mask the 0 values in the second matrix so they become transparent
        matrix2 = v['indx_files_written'].transpose() >= 1.0
        masked_matrix2 = np.ma.masked_where(matrix2 == 0, matrix2)
        # Define the colormap for the second matrix (0 is ignored due to masking, 1 is red)
        cmap2 = mcolors.ListedColormap(['red'])
        # Overlay the masked second binary matrix
        plt.imshow(masked_matrix2, cmap=cmap2, interpolation='nearest', origin='lower', alpha=0.7, aspect='auto')
        plt.xlabel(r'Episode Steps')
        plt.ylabel(r'File No.')
        plt.title('AutoGPT')

        if k == 'llmatic':
            matrix3 = v['indx_files_read'].transpose() >= 1.0
            masked_matrix3 = np.ma.masked_where(matrix3 == 0, matrix3)
            # Define the colormap for the second matrix (0 is ignored due to masking, 1 is red)
            cmap2 = mcolors.ListedColormap(['blue'])
            # Overlay the masked second binary matrix
            plt.imshow(masked_matrix3, cmap=cmap2, interpolation='nearest', origin='lower', alpha=0.7, aspect='auto')
            plt.title('Code-L2MAC')
            # plt.xlabel(r'Episode Steps')
            # plt.ylabel(r'File No.')




        # cax2 = ax.imshow(v['indx_files_written'].transpose() >= 1.0, cmap='Reds', interpolation='nearest', origin='lower', alpha=0.5)

        # cax3 = ax.imshow(v['indx_files_read'].transpose() >= 1.0, cmap='Blues', interpolation='nearest', origin='lower', alpha=0.5)

        # Optionally, if you want a colorbar for the second heatmap as well:
        # cbar2 = fig.colorbar(cax2, ax=ax, orientation='vertical', fraction=.1, pad=0.05)

        # Display the plot
        # plt.show()
        plt.savefig(f'./results/{k}_memory.png')
        plt.savefig(f'./results/{k}_memory.pdf')
        print(f'./results/{k}_memory.png')
        plt.clf()

    # Custom legend using patches
    black_patch = mpatches.Patch(color='black', label='File not created')
    white_patch = mpatches.Patch(color='white', label='File exists')
    red_patch = mpatches.Patch(color='red', label='File written to',  alpha=0.7)
    blue_patch = mpatches.Patch(color='blue', label='File read from', alpha=0.7)

    fig_size = (8, 8)
    plt.figure(figsize=fig_size)


    # Add the legend to the plot
    plt.legend(handles=[black_patch, white_patch, red_patch, blue_patch], fancybox=True, shadow=True)

    plt.savefig(f'./results/legend_memory.png')
    plt.savefig(f'./results/legend_memory.pdf')
    print(f'./results/legend_memory.png')
    plt.clf()
    print('')



    autogpt = results[results['method'] == 'autogpt']
    llmatic = results[results['method'] == 'llmatic']
    gpt4 = results[results['method'] == 'gpt4']

    print('')
    max_x = autogpt.change_count.max()
    plt.plot((llmatic.change_count / llmatic.change_count.max())*100.0, llmatic.errors, '--o', label='Code-L2MAC', alpha=0.7)
    plt.plot((autogpt.change_count / autogpt.change_count.max())*100.0, autogpt.errors, '--o', label='AutoGPT', alpha=0.7)
    plt.plot(gpt4.change_count, gpt4.errors, '--o', label='GPT4', alpha=0.7)
    plt.ylabel(r'\# Errors')
    plt.xlabel(r'\% Episode Completion (Normalized Steps)')
    # plt.legend(loc="lower center", bbox_to_anchor=(
                # LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
    # plt.legend(loc="upper center", ncol=1, fancybox=True, shadow=True)
    # plt.tight_layout()                    
    plt.savefig(f'./results/errors.png')
    plt.savefig(f'./results/errors.pdf')
    print(f'./results/errors.png')
    plt.clf()

    print('')

    plt.plot((llmatic.change_count / llmatic.change_count.max())*100.0, np.ones(llmatic.change_count.shape[0])*100.0, '--o', label='Code-L2MAC', alpha=0.7)
    auto_gpt_f = np.ones(autogpt.change_count.shape[0]) * (8 / 27) * 100.0
    auto_gpt_f[0] = 100.0
    plt.plot((autogpt.change_count / autogpt.change_count.max())*100.0, auto_gpt_f, '--o', label='AutoGPT', alpha=0.7)
    plt.plot(gpt4.change_count, 100.0, '--o', label='GPT4', alpha=0.7)
    # plt.plot(autogpt.change_count, np.ones(autogpt.change_count.shape[0]) * 100.0, '--o', label='L2MAC', alpha=0.7)
    # plt.plot(autogpt.change_count, auto_gpt_f, '--o', label='AutoGPT', alpha=0.7)
    # plt.plot(autogpt.change_count[0], np.ones(autogpt.change_count.shape[0])[0] * 100.0, '--o', label='GPT4', alpha=0.7)
    plt.ylim([0,105.0])
    plt.ylabel(r'\% Feature Req. in Context')
    plt.xlabel(r'\% Episode Completion (Normalized Steps)')
    # plt.legend(loc="upper center", ncol=1, fancybox=True, shadow=True)
    # plt.tight_layout()                    
    plt.savefig(f'./results/features.png')
    plt.savefig(f'./results/features.pdf')
    print(f'./results/features.png')
    plt.clf()


    print('')

    print('')
    max_x = autogpt.change_count.max()
    plt.plot((llmatic.change_count / llmatic.change_count.max())*100.0, llmatic.errors, '--o', label='Code-L2MAC', alpha=0.7)
    plt.plot((autogpt.change_count / autogpt.change_count.max())*100.0, autogpt.errors, '--o', label='AutoGPT', alpha=0.7)
    plt.plot(gpt4.change_count, gpt4.errors, '--o', label='GPT4', alpha=0.7)
    plt.ylabel(r'\# Errors')
    plt.xlabel(r'\% Episode Completion (Normalized Steps)')
    # plt.legend(loc="lower center", bbox_to_anchor=(
                # LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
    plt.legend(loc="upper left", ncol=1, fancybox=True, shadow=True)
    # plt.tight_layout()                    
    plt.savefig(f'./results/errors_legend.png')
    plt.savefig(f'./results/errors_legend.pdf')
    print(f'./results/errors_legend.png')
    plt.clf()


    print('')
    # import pandas as pd
    # import matplotlib.pyplot as plt
    # import seaborn as sns

    # # Concatenate dataframes
    # df = results

    # # Plotting
    # plt.figure(figsize=(10,6))

    # # Stacked bar plot for total tests and tests passed
    # df_grouped = df.groupby('method').max()[['tests_total', 'tests_passed']]
    # df_grouped.plot(kind='bar', stacked=True, ax=plt.gca())

    # # Line plot for the progression of tests passed
    # for method, group in df.groupby('method'):
    #     plt.plot(group['change_count'], group['tests_passed'], label=f"{method} progression", marker='o')

    # plt.title("Performance Comparison of Three Methods in Test Generation and Solution")
    # plt.ylabel("Number of Tests")
    # plt.xlabel("Methods")
    # plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    # plt.tight_layout()
    df = results



    # Assuming you've already concatenated the dataframes into df
    # fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True, sharey=True)
    fig, axes = plt.subplots(3, 1, sharex=True)

    methods = ["llmatic", "autogpt", "gpt4"]

    # Set total horizontal space range between 0 and 1
    horizontal_space = 1.0

    # Beautiful colors
    beautiful_green = "#28A745"
    beautiful_red = "#DC3545"

    # Find the overall maximum value for 'tests_total' across all methods
    ymax = df['tests_total'].max() + 5  # Added 5 for some padding at the top

    for ax, method in zip(axes, methods):
        subset = df[df['method'] == method]
        
        # Calculate the number of bars
        n_bars = len(subset)
        
        # Calculate width of each bar
        # bar_width = (horizontal_space / n_bars) - 0.02  # subtracting a small value for spacing
        bar_width = (horizontal_space / n_bars)
        
        # Adjust x-values so they lie uniformly between 0 and 1
        x_values = np.linspace(0, horizontal_space - bar_width, n_bars)
        
        # Bar for passed tests
        ax.bar(x_values, subset['tests_passed'], width=bar_width, label='Tests Passed', color=beautiful_green, alpha=0.7, align='edge')
        
        # Bar for tests not passed stacked on top
        ax.bar(x_values, subset['tests_total'] - subset['tests_passed'], width=bar_width, label='Tests Failed', color=beautiful_red, bottom=subset['tests_passed'], alpha=0.7, align='edge')
        
        # ax.set_title(method)
        # ax.set_ylabel('Number of Tests')
        # ax.legend()
        # ax.set_ylim(0, ymax)  # Set the common y-axis limit
        if method == 'llmatic':
            ax.set_ylim(0, 50)  # Set the common y-axis limit
        ax.set_xlim(0, 1)  # Ensure x-axis starts from 0 and goes up to 1
        if method == 'autogpt':
            ax.set_ylabel('Number of Tests')


    # Common x label
    # axes[-1].set_xlabel('Adjusted Change Count')
    axes[-1].set_xlabel(r'\% Episode Completion (Normalized Steps)')
    # axes[-1].set_ylabel('Number of Tests')  # This sets the y-label for the main axis
    # axes.set_ylabel('Number of Tests')  # This sets the y-label for the main axis
    plt.tight_layout()
    plt.show()



    plt.savefig(f'./results/chatgpt.png')
    plt.savefig(f'./results/chatgpt.pdf')
    print(f'./results/chatgpt.png')
    plt.clf()

    # Save legend


    # Assuming you've already concatenated the dataframes into df
    # fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True, sharey=True)
    fig, axes = plt.subplots(1, 1, sharex=True)

    methods = ["autogpt", "llmatic", "gpt4"]

    # Set total horizontal space range between 0 and 1
    horizontal_space = 1.0

    # Beautiful colors
    beautiful_green = "#28A745"
    beautiful_red = "#DC3545"

    # Find the overall maximum value for 'tests_total' across all methods
    ymax = df['tests_total'].max() + 5  # Added 5 for some padding at the top

    # for ax, method in zip(axes, methods):
    ax = axes
    method = methods[0]
    subset = df[df['method'] == method]
    
    # Calculate the number of bars
    n_bars = len(subset)
    
    # Calculate width of each bar
    # bar_width = (horizontal_space / n_bars) - 0.02  # subtracting a small value for spacing
    bar_width = (horizontal_space / n_bars)
    
    # Adjust x-values so they lie uniformly between 0 and 1
    x_values = np.linspace(0, horizontal_space - bar_width, n_bars)
    
    # Bar for passed tests
    ax.bar(x_values, subset['tests_passed'], width=bar_width, label='Tests Passed', color=beautiful_green, alpha=0.7, align='edge')
    
    # Bar for tests not passed stacked on top
    ax.bar(x_values, subset['tests_total'] - subset['tests_passed'], width=bar_width, label='Tests Failed', color=beautiful_red, bottom=subset['tests_passed'], alpha=0.7, align='edge')
    
    # ax.set_title(method)
    # ax.set_ylabel('Number of Tests')
    ax.legend(fancybox=True, shadow=True)
    ax.set_ylim(0, ymax)  # Set the common y-axis limit
    ax.set_xlim(0, 1)  # Ensure x-axis starts from 0 and goes up to 1

    # Common x label
    # axes[-1].set_xlabel('Adjusted Change Count')
    # axes[-1].set_xlabel(r'\% Episode Completion (Normalized Steps)')
    # plt.tight_layout()
    # plt.show()



    plt.savefig(f'./results/chatgpt_legend.png')
    plt.savefig(f'./results/chatgpt_legend.pdf')
    print(f'./results/chatgpt_legend.png')
    plt.clf()


    print('')
    return


    # # Temps 2
    # # Concatenate the dataframes into df

    # methods = ["autogpt", "llmatic", "gpt4"]

    # # Colors for passed and not passed tests
    # beautiful_green = "#28A745"
    # beautiful_red = "#DC3545"

    # # Patterns for different methods
    # patterns = ['/', '\\', 'x']

    # # Create a merged dataframe with all unique 'change_count' values
    # all_change_counts = df['change_count'].unique()
    # merged_df = pd.DataFrame(all_change_counts, columns=['change_count'])

    # for method in methods:
    #     subset = df[df['method'] == method].copy()
    #     subset = subset.rename(columns={'tests_passed': f'{method}_passed', 'tests_total': f'{method}_total'})
    #     subset = subset[['change_count', f'{method}_passed', f'{method}_total']]
    #     merged_df = merged_df.merge(subset, on='change_count', how='left').fillna(0)

    # # Setting up the plot
    # fig, ax = plt.subplots(figsize=(12, 8))
    # bar_width = 0.2

    # for idx, method in enumerate(methods):
    #     x_values = np.arange(len(all_change_counts)) + idx * bar_width

    #     passed_col = f'{method}_passed'
    #     total_col = f'{method}_total'

    #     ax.bar(x_values, merged_df[passed_col], width=bar_width, color=beautiful_green, label=f'{method} - Tests Passed', alpha=0.7, hatch=patterns[idx])
    #     ax.bar(x_values, merged_df[total_col] - merged_df[passed_col], width=bar_width, bottom=merged_df[passed_col], color=beautiful_red, label=f'{method} - Tests Not Passed', alpha=0.7, hatch=patterns[idx])

    # ax.set_title('Comparison of Methods on Test Performance')
    # ax.set_ylabel('Number of Tests')
    # ax.set_xlabel('Change Count')
    # ax.set_xticks(np.arange(len(all_change_counts)) + bar_width)
    # ax.set_xticklabels(all_change_counts)
    # ax.set_ylim(0, merged_df[[f'{method}_total' for method in methods]].max().max() + 5)  # Adjusting y-axis limit

    # # Creating a legend
    # handles, labels = ax.get_legend_handles_labels()
    # ax.legend(handles[:6:2] + handles[1:6:2], labels[:6:2] + labels[1:6:2], loc='upper left')

    # plt.tight_layout()
    # plt.show()



    # plt.savefig(f'./results/chatgpt2.png')
    # plt.savefig(f'./results/chatgpt2.pdf')
    # print(f'./results/chatgpt2.png')
    # plt.clf()




    plt.plot(llmatic.change_count, llmatic.errors, '--o', label='LLMatic')
    plt.plot(autogpt.change_count, autogpt.errors, '--o', label='AutoGPT')
    plt.plot(gpt4.change_count, gpt4.errors, '--o', label='GPT4')
    plt.ylabel(r'\textbf{\# Errors}')
    plt.xlabel(r'\textbf{\# Code writes}')
    # plt.legend(loc="lower center", bbox_to_anchor=(
                # LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
    plt.legend(loc="lower center", ncol=1, fancybox=True, shadow=True)
    # plt.tight_layout()                    
    plt.savefig(f'./results/errors.png')
    plt.savefig(f'./results/errors.pdf')
    print(f'./results/errors.png')
    plt.clf()

    return 

    x_metric = 'observing_var_threshold' # 'observing_var_threshold'
    plots_total = 3
    for env_name in df.env_name.unique():
        threshold_we_used = thresholds_used[env_name]
        df_t = df[df.env_name==env_name]
        ax = plt.subplot(plots_total, 1, 1)
        y_metric = 'total_reward'
        x = df_t[df_t.sampling_policy == 'active_observing_control'][x_metric]#['mean']
        y_mean = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric]['mean']
        y_std = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric][error_metric]
        plt.plot(x,y_mean,'--o',label=sampling_policy_map['active_observing_control'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)
        cp_y_mean = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric]['mean'].iloc[0]
        cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        cp_y_std = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric][error_metric].iloc[0]
        cp_y_std = np.ones_like(y_mean) * cp_y_std
        plt.plot(x,cp_y_mean,'--o',label=sampling_policy_map['continuous_planning'])
        plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
        plt.ylabel(r'$\mathcal{U}$')
        plt.axvline(x=threshold_we_used, color='r')

        ax = plt.subplot(plots_total, 1, 2, sharex=ax)
        y_metric = 'state_reward'
        x = df_t[df_t.sampling_policy == 'active_observing_control'][x_metric]#['mean']
        y_mean = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric]['mean']
        y_std = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric][error_metric]
        plt.plot(x,y_mean,'--o',label=sampling_policy_map['active_observing_control'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)
        cp_y_mean = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric]['mean'].iloc[0]
        cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        cp_y_std = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric][error_metric].iloc[0]
        cp_y_std = np.ones_like(y_mean) * cp_y_std
        plt.plot(x,cp_y_mean,'--o',label=sampling_policy_map['continuous_planning'])
        plt.fill_between(x,cp_y_mean - cp_y_std,cp_y_mean + cp_y_std,alpha=0.25)
        plt.ylabel(r'$\mathcal{R}$')
        plt.axvline(x=threshold_we_used, color='r')
        # ax2 = ax.twinx()
        ax = plt.subplot(plots_total, 1, 3, sharex=ax)
        y_metric = 'observation_reward'
        x = df_t[df_t.sampling_policy == 'active_observing_control'][x_metric]#['mean']
        y_mean = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric]['mean']
        y_std = df_t[df_t.sampling_policy == 'active_observing_control'][y_metric][error_metric]
        plt.plot(x,y_mean,'--o',label=sampling_policy_map['active_observing_control'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)
        cp_y_mean = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric]['mean'].iloc[0]
        cp_y_mean = np.ones_like(y_mean) * cp_y_mean
        cp_y_std = df_t[df_t.sampling_policy == 'continuous_planning'][y_metric][error_metric].iloc[0]
        cp_y_std = np.ones_like(y_mean) * cp_y_std
        plt.plot(x,cp_y_mean,'--o',label=sampling_policy_map['continuous_planning'])
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



def state_cancer_hist_v2(df):
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn

    # Hack
    import sys
    import os
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    from config import load_observing_var_thresholds

    pd.set_option('mode.chained_assignment', None)
    SCALE = 7
    HEIGHT_SCALE =1.0
    LEGEND_Y_CORD = -1.1  # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}
    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    time_multiplier = 5.0
    # plt.gcf().subplots_adjust(bottom=0.40, left=0.2, top=0.95)

    print('')
    x_metric = 'observing_var_threshold' # 'observing_var_threshold'
    plots_total = 3
    number_of_hist_bins = 4

    state_bins = np.linspace(0,1,number_of_hist_bins)*1140
    timelen = 5.0
    df_cp = df[df.sampling_policy == 'continuous_planning']
    df_cp_row = df_cp.iloc[0]
    iter_ = timelen / df_cp_row.dt_sim

    observing_var_thresholds = load_observing_var_thresholds()
    observing_var_threshold = observing_var_thresholds[df_cp_row.dt_plan][df_cp_row.env_name]['continuous']


    obs_count, state_bins_out = np.histogram(df_cp_row.s[df_cp_row.observed_times,0], bins=state_bins)
    s = df_cp_row.s[:,0]
    t = np.arange(iter_) * df_cp_row.dt_sim * time_multiplier
    times = t * time_multiplier
    iter_ = timelen / df_cp_row.dt_sim
    prev_time = 0.0
    dts_l = []
    for i, state_boundary in enumerate(state_bins[::-1][1:]):
        if i < (state_bins[::-1][1:].shape[0]-1):
            time_indx = (s < state_boundary).nonzero()[0][0]
            dt = times[time_indx] - prev_time
            prev_time = times[time_indx]
            dts_l.append(dt)
        else: # Final bin
            dt = times[-1] - prev_time
            dts_l.append(dt)
    dts = np.array(dts_l)
    dts = dts[::-1]
    obs_count_per_time = obs_count / dts
    obs_count_per_time[:] = obs_count_per_time.mean()
    state_mid_points = state_bins + (np.diff(state_bins)[0] / 2.0)
    state_mid_points = state_mid_points[:-1]
    state_width = np.diff(state_bins)[0]

    ax = plt.subplot(3, 1, 1)
    plt.plot(t, df_cp_row.s[:,0])
    plt.ylabel('$v$ ($cm^3$)')
    plt.xlabel('$t$ (days)')
    for obs_t in t[df_cp_row.observed_times]:
        plt.axvline(x=obs_t, color='g')
    ax = plt.subplot(3, 1, 2, sharex=ax)
    plt.plot(t, df_cp_row.cost_std_plot)
    plt.ylim([0,4.0])
    plt.axhline(y=observing_var_threshold, color='r')
    for obs_t in t[df_cp_row.observed_times]:
        plt.axvline(x=obs_t, color='g')
    plt.ylabel('$\\sigma(r)$')
    plt.xlabel('$t$ (days)')
    ax = plt.subplot(3, 1, 3)
    plt.bar(state_mid_points, obs_count_per_time, width=state_width)
    # plt.ylim([0,4.5])
    plt.xlabel(r'$v$ $(\mathrm{cm}^3)$')
    plt.ylabel(r'$\frac{\mathcal{O}}{t}$ $(\frac{\mathrm{obs}}{\mathrm{day}})$')
    plt.savefig(f'./plots/{df_cp_row.env_name}_hist_with_state_{df_cp_row.sampling_policy}.png')
    plt.savefig(f'./plots/{df_cp_row.env_name}_hist_with_state_{df_cp_row.sampling_policy}.pdf')
    plt.clf()
    file_path = f'./plots/{df_cp_row.env_name}_hist_with_state_{df_cp_row.sampling_policy}.png'
    print(file_path)


    df_aoc = df[df.sampling_policy == 'active_observing_control']
    # Same as above, average over all seed runs though.
    # Should see massive improvement
    observed_states_l = []
    for j, row in df_aoc.iterrows():
        observed_states_l.append(row.s[row.observed_times,0])
    observed_states = np.concatenate(observed_states_l)
    obs_count, state_bins_out = np.histogram(observed_states, bins=state_bins)
    s = df_cp_row.s[:,0]
    iter_ = timelen / df_cp_row.dt_sim
    times = np.arange(iter_) * df_cp_row.dt_sim
    prev_time = 0.0
    dts_l = []
    for i, state_boundary in enumerate(state_bins[::-1][1:]):
        if i < (state_bins[::-1][1:].shape[0]-1):
            time_indx = (s < state_boundary).nonzero()[0][0]
            dt = times[time_indx] - prev_time
            prev_time = times[time_indx]
            dts_l.append(dt)
        else: # Final bin
            dt = times[-1] - prev_time
            dts_l.append(dt)
    dts = np.array(dts_l)
    dts = dts[::-1]
    obs_count_per_time = obs_count / dts
    obs_count_per_time = obs_count_per_time / df_aoc.shape[0]
    state_mid_points = state_bins + (np.diff(state_bins)[0] / 2.0)
    state_mid_points = state_mid_points[:-1]
    state_width = np.diff(state_bins)[0]


    ax = plt.subplot(3, 1, 1)
    plt.plot(t, row.s[:,0])
    plt.ylabel('$v$ ($cm^3$)')
    plt.xlabel('$t$ (days)')
    for obs_t in t[row.observed_times]:
        plt.axvline(x=obs_t, color='g')
    ax = plt.subplot(3, 1, 2, sharex=ax)
    plt.plot(t, row.cost_std_plot)
    plt.axhline(y=observing_var_threshold, color='r')
    plt.ylim([0,4.0])
    for obs_t in t[row.observed_times]:
        plt.axvline(x=obs_t, color='g')
    plt.ylabel('$\\sigma(r)$')
    plt.xlabel('$t$ (days)')
    ax = plt.subplot(3, 1, 3)
    plt.bar(state_mid_points, obs_count_per_time, width=state_width)
    plt.ylim([0,6.2])
    plt.xlabel(r'$v$ $(\mathrm{cm}^3)$')
    plt.ylabel(r'$\frac{\mathcal{O}}{t}$ $(\frac{\mathrm{obs}}{\mathrm{day}})$')
    plt.savefig(f'./plots/{row.env_name}_hist_with_state_{row.sampling_policy}.png')
    plt.savefig(f'./plots/{row.env_name}_hist_with_state_{row.sampling_policy}.pdf')
    plt.clf()
    file_path = f'./plots/{row.env_name}_hist_with_state_{row.sampling_policy}.png'
    print(file_path)
    print('')

def state_cancer_hist(df):
    # cancer timelen = 1.25 for this to work
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    pd.set_option('mode.chained_assignment', None)
    SCALE = 7
    HEIGHT_SCALE =1.0
    LEGEND_Y_CORD = -1.1  # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}

    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    # plt.gcf().subplots_adjust(bottom=0.40, left=0.2, top=0.95)

    print('')
    x_metric = 'observing_var_threshold' # 'observing_var_threshold'
    plots_total = 3

    state_when_obs_taken_l = []
    for i, row in df.iterrows():
        state_when_obs_taken_l.append(row.s[row.observed_times,0])
    states_observed = np.concatenate(state_when_obs_taken_l)
    count, values = np.histogram(states_observed, bins=np.linspace(0,1,5)*1140)
    count = count / df.shape[0]
    a = values + (np.diff(values)[0] / 2.0)
    a = a[:-1]
    width = np.diff(values)[0]
    plt.bar(a, count, width=width)
    plt.xlabel(r'$c$')
    plt.ylabel(r'$\mathcal{O}/\Delta_c$')
    plt.savefig(f'./plots/state_cancer_hist.png')
    plt.savefig(f'./plots/state_cancer_hist.pdf')
    print(f'./plots/state_cancer_hist.png')
    plt.clf()
    print('')
    # import matplotlib.pyplot as plt
    # plt.hist(states_observed, bins=np.linspace(0,1,5)*1140)
    # # plt.hist(states_observed, bins=((np.exp(np.linspace(0,1,6))-1.0)/(np.exp(1)-1))*1140)
    # # plt.hist(states_observed, bins=(np.log(np.linspace(1,np.exp(1),10)))*1140)
    # plt.savefig('out.png')
    # plt.clf()

def plot_pendulum_state(df):
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    pd.set_option('mode.chained_assignment', None)
    # import seaborn_image as isns
    SCALE = 7
    HEIGHT_SCALE =0.75
    LEGEND_Y_CORD = -1.1  # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}

    TRANSFORMED_TRIG_STATES = False

    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    # sn.color_palette("viridis", as_cmap=True)
    # plt.gcf().subplots_adjust(bottom=0.40, left=0.2, top=0.95)

    print('')
    x_metric = 'observing_var_threshold' # 'observing_var_threshold'
    plots_total = 3
    hist_bins = 16
    len_up_to = 500

    state_when_obs_taken_l = []
    all_states_l = []
    for i, row in df.iterrows():
        s = row.s
        if TRANSFORMED_TRIG_STATES:
            cos_th, sin_th, theta_dot = s[...,0],s[...,1],s[...,2]
            C = (cos_th**2 + sin_th**2)
            cos_th,sin_th = cos_th/C, sin_th/C
            theta = np.arctan2(sin_th/C,cos_th/C)
            st = np.stack([theta, theta_dot], axis=1)
        else:
            st = row.s[:len_up_to,:]
        observed_times = np.array(row.observed_times)
        observed_times = observed_times[observed_times<len_up_to]
        state_when_obs_taken_l.append(st[observed_times])
        if i<=1:
            plt.plot(st[:,0],st[:,1], color='k', linewidth=2.0)#, marker='o', alpha=.5,)
        all_states_l.append(st)
    states_observed = np.concatenate(state_when_obs_taken_l)
    all_states = np.concatenate(all_states_l)
    # plt.scatter([0,2*np.pi],[0,0], color='r', marker='x', s=500, zorder=2, linewidth=5.0)
    # plt.scatter([np.pi],[0], color='g', marker='x', s=500, zorder=2, linewidth=5.0)
    theta_min = all_states[:,0].min()
    theta_max = all_states[:,0].max()
    theta_dot_min = all_states[:,1].min()
    theta_dot_max = all_states[:,1].max()
    theta_bins = np.linspace(theta_min, theta_max, hist_bins)
    theta_dot_bins = np.linspace(theta_dot_min, theta_dot_max, hist_bins)
    # plt.scatter(states_observed[:,0],states_observed[:,1], marker='o', alpha=.5,)
    # plt.plot(all_states[:10,0],all_states[:10,1], color='k')#, marker='o', alpha=.5,)
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$\dot{\theta}$')
    plt.savefig(f'./plots/pendulum_state_obs_phase.png')
    plt.savefig(f'./plots/pendulum_state_obs_phase.pdf')
    print(f'./plots/pendulum_state_obs_phase.png')
    # plt.clf()

    h_obs, xedges_obs, yedged_obs = np.histogram2d(x=states_observed[:,0], y=states_observed[:,1], bins=(theta_bins, theta_dot_bins))
    # np.histogram2d(x=all_states[:,0], y=all_states[:,1], bins=hist_bins)
    h_all, xedges_all, yedged_all = np.histogram2d(x=all_states[:,0], y=all_states[:,1], bins=(theta_bins, theta_dot_bins))
    h_obs_per_time = np.nan_to_num((h_obs / h_all))
    plt.imshow(h_obs_per_time, cmap="Blues", interpolation="none", extent=[theta_min,theta_max,theta_dot_max,theta_dot_min], aspect="auto")
    # sn.heatmap(h_obs_per_time) 
    # sn.heatmap(h_obs)
    # isns.imshow(h_obs)

    # plt.hist2d(states_observed[:,0],states_observed[:,1], bins=hist_bins)
    # sn.displot(x=states_observed[:,0], y=states_observed[:,1], bins=hist_bins) #, kind="kde", fill=True)
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$\dot{\theta}$')
    plt.savefig(f'./plots/pendulum_state_obs_phase_hist.png')
    plt.savefig(f'./plots/pendulum_state_obs_phase_hist.pdf')
    print(f'./plots/pendulum_state_obs_phase_hist.png')
    plt.clf()



    state_when_obs_taken_l = []
    all_states_l = []
    for i, row in df.iterrows():
        s = row.s
        state_when_obs_taken_l.append(s[row.observed_times])
        all_states_l.append(s)
        # if i<=1:
        #     plt.plot(np.cos(st[:,0]),np.sin(st[:,0]), color='k', linewidth=2.0)#, marker='o', alpha=.5,)
    states_observed = np.concatenate(state_when_obs_taken_l)
    all_states = np.concatenate(all_states_l)
    # plt.scatter([0],[1], color='r', marker='x', s=500, zorder=2, linewidth=5.0)
    # plt.scatter([0],[0], color='g', marker='x', s=500, zorder=2, linewidth=5.0)
    x_obs, y_obs = np.cos(states_observed[:,0]), np.sin(states_observed[:,0])
    x_all, y_all = np.cos(all_states[:,0]), np.sin(all_states[:,0])
    # plt.scatter(x_obs,y_obs, marker='o', alpha=.5,)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.savefig(f'./plots/pendulum_state_obs_location.png')
    plt.savefig(f'./plots/pendulum_state_obs_location.pdf')
    print(f'./plots/pendulum_state_obs_location.png')
    # plt.clf()

    # plt.hist2d(states_observed[:,0],states_observed[:,1], bins=hist_bins)
    # fig, ax = plt.subplots()

    x_bins = np.linspace(-1.0, 1.0, hist_bins)
    y_bins = np.linspace(-1.0, 1.0, hist_bins)
    h_obs, xedges_obs, yedged_obs = np.histogram2d(x=x_obs, y=y_obs, bins=(x_bins, y_bins))
    # np.histogram2d(x=all_states[:,0], y=all_states[:,1], bins=hist_bins)
    h_all, xedges_all, yedged_all = np.histogram2d(x=x_all, y=y_all, bins=(x_bins, y_bins))
    h_obs_per_time = np.nan_to_num((h_obs / h_all))
    plt.imshow(h_obs_per_time, cmap="Blues", interpolation="none", extent=[-1.0,1.0,1.0,-1.0], aspect="auto")

    # sn.displot(x=states_observed[:,0], y=states_observed[:,1], bins=hist_bins, cbar=True) #, kind="kde", fill=True)
    # sn.displot(x=states_observed[:,0], y=states_observed[:,1], bins=hist_bins) #, kind="kde", fill=True)
    # plt.legend(loc="lower center", bbox_to_anchor=(LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
    plt.xlim([-1,1])
    plt.ylim([-1,1])
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.savefig(f'./plots/pendulum_state_obs_location_hist.png')
    plt.savefig(f'./plots/pendulum_state_obs_location_hist.pdf')
    print(f'./plots/pendulum_state_obs_location_hist.png')
    plt.clf()

    theta_obs = np.arctan2(y_obs,x_obs)
    theta_all = np.arctan2(y_all,x_all)


    theta_bins = np.linspace(-np.pi, np.pi, hist_bins)
    h_obs, h_bin_edges = np.histogram(theta_obs, bins=theta_bins)
    h_all, h_bin_edges = np.histogram(theta_all, bins=theta_bins)
    h_obs_per_time = np.nan_to_num((h_obs / h_all))

    theta_mid_points = theta_bins + (np.diff(theta_bins)[0] / 2.0)
    theta_mid_points = theta_mid_points[:-1]
    theta_width = np.diff(theta_bins)[0]




    print('')
    # Compute pie slices
    N = 20
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    width = (2 * np.pi) / N

    ax = plt.subplot(111, projection='polar')
    ax.set_theta_zero_location("N")
    bars = ax.bar(theta_mid_points, h_obs_per_time, width=theta_width, bottom=0.0)
    ax.set_xlabel('$\phi$')

    plt.savefig(f'./plots/pendulum_state_obs_location_hist_polar.png')
    plt.savefig(f'./plots/pendulum_state_obs_location_hist_polar.pdf')
    plt.clf()
    print(f'./plots/pendulum_state_obs_location_hist_polar.png')
    print('')

    # count, values = np.histogram(states_observed, bins=np.linspace(0,1,5)*1140)
    # count = count / df.shape[0]
    # a = values + (np.diff(values)[0] / 2.0)
    # a = a[:-1]
    # width = np.diff(values)[0]
    # plt.bar(a, count, width=width)
    # plt.xlabel(r'$c$')
    # plt.ylabel(r'$\mathcal{O}/\Delta_c$')
    # plt.savefig(f'./plots/state_cancer_hist.png')
    # plt.savefig(f'./plots/state_cancer_hist.pdf')
    # print(f'./plots/state_cancer_hist.png')
    # plt.clf()
    # print('')



    # import matplotlib.pyplot as plt
    # plt.hist(states_observed, bins=np.linspace(0,1,5)*1140)
    # # plt.hist(states_observed, bins=((np.exp(np.linspace(0,1,6))-1.0)/(np.exp(1)-1))*1140)
    # # plt.hist(states_observed, bins=(np.log(np.linspace(1,np.exp(1),10)))*1140)
    # plt.savefig('out.png')
    # plt.clf()


def gen_match_cp_obs_table(df, use_95_ci=True):
    print('')
    cp_with_different_obs = df[~df.fixed_continuous_planning_observations.isnull()]
    aoc_with_normalization_reference_baselines = df[df.fixed_continuous_planning_observations.isnull()]

    if use_95_ci:
        df_out = aoc_with_normalization_reference_baselines.groupby(['env_name', 'sampling_policy', 'model_name', 'observing_var_threshold']).agg([np.mean, ci]).reset_index()
        cp_dif_obs = cp_with_different_obs.groupby(['env_name', 'sampling_policy', 'model_name', 'fixed_continuous_planning_observations']).agg([np.mean, ci]).reset_index()
    else:
        df_out = aoc_with_normalization_reference_baselines.groupby(['env_name', 'sampling_policy', 'model_name', 'observing_var_threshold']).agg([np.mean, np.std]).reset_index()
        cp_dif_obs = cp_with_different_obs.groupby(['env_name', 'sampling_policy', 'model_name', 'fixed_continuous_planning_observations']).agg([np.mean, np.std]).reset_index()

    df_out.loc[df_out.sampling_policy == 'random', 'total_reward'] = 0
    df_out.loc[df_out.sampling_policy == 'random', 'state_reward'] = 0


    sf = 3
    env_name_map = {'oderl-cartpole': 'Cartpole',
                    'oderl-pendulum': 'Pendulum',
                    'oderl-acrobot': 'Acrobot',
                    'oderl-cancer': 'Cancer'}

    env_name_ordering = {'oderl-cartpole': 2,
                    'oderl-pendulum': 3,
                    'oderl-acrobot': 1,
                    'oderl-cancer': 0}

    sampling_policy_map = {'discrete_monitoring': 'Discrete Monitoring',
                             'discrete_planning': 'Discrete Planning',
                             'continuous_planning': 'Continuous Planning',
                             'active_observing_control': r'\bf Active Sampling Control',
                             'random': 'Random'}
                             
    table_lines = []
    line = r'\begin{tabular}{@{}l' + '|ccc' * df_out.env_name.nunique() + '}'
    table_lines.append(line)
    table_lines.append(r'\toprule')
    table_lines.append(''.join([r'&  \multicolumn{3}{c|}{' + env_name_map[env_name] + '}' for env_name in df_out.env_name.unique()]) + r'\\')
    table_lines.append(r'Policy ' + r'& $\mathcal{U}$ & $\mathcal{R}$ & $\mathcal{O}$' * df_out.env_name.nunique() + r'\\' )
    table_lines.append(r'\midrule')
    for sampling_policy in df_out.sampling_policy.unique():
        line = sampling_policy_map[sampling_policy]
        for env_name in df_out.env_name.unique():
            row = df_out[(df_out.sampling_policy == sampling_policy) & (df_out.env_name == env_name)]
            if use_95_ci:
                line += r'&' + f"{row.total_reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.total_reward['ci'].iloc[0]:.{sf}g}" + r'&' + f"{row.state_reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.state_reward['ci'].iloc[0]:.{sf}g}" + r'&' + f"{row.observations_taken['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.observations_taken['ci'].iloc[0]:.{sf}g}"
            else:
                line += r'&' + f"{row.total_reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.total_reward['std'].iloc[0]:.{sf}g}" + r'&' + f"{row.state_reward['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.state_reward['std'].iloc[0]:.{sf}g}" + r'&' + f"{row.observations_taken['mean'].iloc[0]:.{sf}g}" + r'$\pm$' + f"{row.observations_taken['std'].iloc[0]:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    for i, row in cp_dif_obs.iterrows():
        line = sampling_policy_map[row.sampling_policy.iloc[0]]
        for env_name in cp_dif_obs.env_name.unique():
            if use_95_ci:
                line += r'&' + f"{row.total_reward['mean']:.{sf}g}" + r'$\pm$' + f"{row.total_reward['ci']:.{sf}g}" + r'&' + f"{row.state_reward['mean']:.{sf}g}" + r'$\pm$' + f"{row.state_reward['ci']:.{sf}g}" + r'&' + f"{row.observations_taken['mean']:.{sf}g}" + r'$\pm$' + f"{row.observations_taken['ci']:.{sf}g}"
            else:
                line += r'&' + f"{row.total_reward['mean']:.{sf}g}" + r'$\pm$' + f"{row.total_reward['std']:.{sf}g}" + r'&' + f"{row.state_reward['mean']:.{sf}g}" + r'$\pm$' + f"{row.state_reward['std']:.{sf}g}" + r'&' + f"{row.observations_taken['mean']:.{sf}g}" + r'$\pm$' + f"{row.observations_taken['std']:.{sf}g}"
        line += r'\\'
        table_lines.append(line)
    table_lines.append(r'\bottomrule')
    table_lines.append(r'\end{tabular}')
    table = '\n'.join(table_lines)
    # print('')
    # print('Latex Table::')
    # print(table)
    # print('')
    # print('')
    return df_out, table

def plot_match_cp_obs_plots(df):
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    pd.set_option('mode.chained_assignment', None)
    SCALE = 13
    HEIGHT_SCALE =0.5
    LEGEND_Y_CORD = -0.7 # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}

    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    plt.gcf().subplots_adjust(bottom=0.4, top=0.95)

    sampling_policy_map = {'discrete_monitoring': 'Discrete Monitoring',
                             'discrete_planning': 'Discrete Planning',
                             'continuous_planning': 'Continuous Planning',
                             'active_observing_control': r'Active Sampling Control',
                             'random': 'Random'}

    cp_with_different_obs = df[~df.fixed_continuous_planning_observations.isnull()]
    aoc_with_normalization_reference_baselines = df[df.fixed_continuous_planning_observations.isnull()]

    df_standard = aoc_with_normalization_reference_baselines.groupby(['env_name', 'sampling_policy', 'model_name', 'observing_var_threshold']).agg([np.mean, np.std]).reset_index()
    cp_dif_obs = cp_with_different_obs.groupby(['env_name', 'sampling_policy', 'model_name', 'fixed_continuous_planning_observations']).agg([np.mean, np.std]).reset_index()

    print('')
    x_metric = 'observations_taken'
    for env_name in df_standard.env_name.unique():
        y_metric = 'total_reward'

        df_standard_t = df_standard[df_standard.env_name==env_name]
        x = df_standard_t[df_standard_t.sampling_policy == 'active_observing_control'][x_metric]['mean']
        y_mean = df_standard_t[df_standard_t.sampling_policy == 'active_observing_control'][y_metric]['mean']
        y_std = df_standard_t[df_standard_t.sampling_policy == 'active_observing_control'][y_metric]['std']
        plt.plot(x,y_mean,'--o',label=sampling_policy_map['active_observing_control'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)

        cp_dif_obs_t = cp_dif_obs[cp_dif_obs.env_name==env_name]
        x = cp_dif_obs_t[cp_dif_obs_t.sampling_policy == 'continuous_planning'][x_metric]['mean']
        print(x)
        y_mean = cp_dif_obs_t[cp_dif_obs_t.sampling_policy == 'continuous_planning'][y_metric]['mean']
        y_std = cp_dif_obs_t[cp_dif_obs_t.sampling_policy == 'continuous_planning'][y_metric]['std']
        plt.plot(x, y_mean, '--o', label=sampling_policy_map['continuous_planning'])
        plt.fill_between(x,y_mean - y_std,y_mean + y_std,alpha=0.25)

        plt.ylabel(r'$\mathcal{U}$')
        plt.xlabel(r'$\mathcal{O}$')

        # plt.legend(loc="lower center", ncol=1, fancybox=True, shadow=True)
        plt.legend(loc="lower center", bbox_to_anchor=(LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
        plt.tight_layout()                    
        plt.savefig(f'./plots/cp_same_obs_as_aoc_{env_name}.png')
        plt.savefig(f'./plots/cp_same_obs_as_aoc_{env_name}.pdf')
        print(f'./plots/cp_same_obs_as_aoc_{env_name}.png')
        plt.clf()
    print('')

def cost_std_comparison(df):
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    pd.set_option('mode.chained_assignment', None)
    SCALE = 10
    HEIGHT_SCALE =0.30
    LEGEND_Y_CORD = -0.72 # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}
    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE, use_autolayout=False)
    plt.gcf().subplots_adjust(bottom=0.40, left=0.2, top=0.95)

    sampling_policy_map = {'discrete_monitoring': r'Discrete Monitoring \quad\quad\quad $\mathcal{R}=85.7\pm0.526$',
                            'discrete_planning': r'Discrete Planning',
                            'continuous_planning': r'Continuous Planning',
                            'active_observing_control': r'Active Sampling Control \quad $\mathcal{R}=98.8\pm0.174$',
                            'random': 'Random'}

    timelen = 5.0
    df_cp_row = df.iloc[0]
    iter_ = timelen / df_cp_row.dt_sim
    t = np.arange(iter_) * df_cp_row.dt_sim
    if df_cp_row.env_name == 'oderl-cancer':
        time_multiplier = 5.0
        t = t * time_multiplier

    length_to_plot = 0.4


    start_cost_std = None
    for i, row in df.iterrows():
        costs_std = row.costs_std
        min_length = min(t.shape[0],costs_std.shape[0])
        min_length = int(length_to_plot * min_length)
        if row.sampling_policy == 'discrete_monitoring':
            costs_std = costs_std / 14.775529274573692
        elif row.sampling_policy == 'active_observing_control':
            costs_std = costs_std / 6.760299902695876
        # if start_cost_std is None:
        #     start_cost_std = costs_std[0]
        plt.plot(t[:min_length], costs_std[:min_length], label=sampling_policy_map[row.sampling_policy])
        plt.axhline(y=1.0, color='r')
    plt.ylabel(r'$\frac{\sigma(r)}{\tau}$')
    plt.xlabel(r'Time $t$ (days)')
    # plt.legend(loc="lower center", bbox_to_anchor=(
    #         LEGEND_X_CORD, LEGEND_Y_CORD), ncol=1, fancybox=True, shadow=True)
    plt.savefig(f'./plots/{row.env_name}_cost_std_compare.png')
    plt.savefig(f'./plots/{row.env_name}_cost_std_compare.pdf')
    print(f'./plots/{row.env_name}_cost_std_compare.png')
    plt.clf()
    print('') 
    



def plot_telem_standard(result):
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import pandas as pd
    import seaborn as sn
    import os
    pd.set_option('mode.chained_assignment', None)
    SCALE = 13
    HEIGHT_SCALE = 0.5
    LEGEND_Y_CORD = -0.75  # * (HEIGHT_SCALE / 2.0)
    SUBPLOT_ADJUST = 1 / HEIGHT_SCALE  # -(0.05 + LEGEND_Y_CORD)
    LEGEND_X_CORD = 0.45
    PLOT_FROM_CACHE = False
    PLOT_SAFTEY_MARGIN = 1.25
    MODEL_NAME_MAP = {}

    plot_actions = True
    plot_reward = True

    sn = configure_plotting_sn_params(sn, SCALE, HEIGHT_SCALE)
    # plt.gcf().subplots_adjust(bottom=0.40, left=0.2, top=0.95)

    s = result['s'].copy()
    r = result['ri'].copy()
    a = result['a'].copy()
    cost_std_plot = result['cost_std_plot'].copy()
    observed_times = result['observed_times'].copy()
    t = np.arange(s.shape[0]) * result['dt_sim']
    observing_var_threshold = result['observing_var_threshold']
    env_name = result['env_name']
    sampling_policy = result['sampling_policy']
    observation_noise = result['observation_noise']
    plot_seed = result['plot_seed']
    # for obs_t_i in observed_times:
    #     cost_std_plot[obs_t_i] = observing_var_threshold # Same as clipping

    plots_total = s.shape[1] + 1
    plots_total += a.shape[1] if plot_actions else 0
    plots_total += 1 if plot_reward else 0

    plot_index = 1
    si = 0
    ai = 0

    for plot_index in range(1,plots_total+1):
        if plot_index == 1:
            ax = plt.subplot(plots_total, 1, plot_index)
            plt.title(f'{env_name}')
        else:
            ax = plt.subplot(plots_total, 1, plot_index, sharex=ax)
        if si < s.shape[1]:
            plt.plot(t, s[:,si])
            plt.ylabel(f'$s_{si}$')
            for obs_t in t[observed_times]:
                plt.axvline(x=obs_t, color='g')
            # elif env_name == 'oderl-cancer' and si == 0:
            #     plt.ylim([0,10])
            si += 1
        elif plot_actions and ai < a.shape[1]:
            plt.plot(t, a[:,ai])
            plt.ylabel(f'$a_{ai}$')
            for obs_t in t[observed_times]:
                plt.axvline(x=obs_t, color='g')
            ai += 1
        elif plot_reward and plot_index == (plots_total - 1):
            plt.plot(t, r)
            plt.ylabel('$r$')
            for obs_t in t[observed_times]:
                plt.axvline(x=obs_t, color='g')
        elif plot_index == plots_total:
            if cost_std_plot.size != 0:
                plt.plot(t, cost_std_plot)
                plt.ylabel('$\\sigma(r)$')
                plt.xlabel('$t$ (days)')
                for obs_t in t[observed_times]:
                    plt.axvline(x=obs_t, color='g')

    if not os.path.exists("./plots/telem/"):
        os.makedirs("./plots/telem/")

    plt.savefig(f'./plots/telem/telem_{env_name}_{sampling_policy}_{observation_noise}_{plot_seed}.png')
    plt.savefig(f'./plots/telem/telem_{env_name}_{sampling_policy}_{observation_noise}_{plot_seed}.pdf')
    plt.clf()
    file_path = f'./plots/telem/telem_{env_name}_{sampling_policy}_{observation_noise}_{plot_seed}.png'
    print(file_path)
    print(np.median(cost_std_plot))
    return file_path



# if __name__ == '__main__':
#     env_name = 'oderl-cartpole'
#     val = -242.2

#     random_policy, best_policy = get_normalized_policy_values_delay_zero()
#     print((val - random_policy[env_name]) / (best_policy[env_name] - random_policy[env_name])*100.00)
#     print('')
