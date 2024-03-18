import pandas as pd
import numpy as np
import random
from utils.results_utils import normalize_means, generate_main_results_table, df_from_log, ci, moving_average, configure_plotting_sn_params, load_df, compute_norm_metrics, generate_overlap_graph, seed_all, generate_n_step_graph, generate_main_results_table_paper_format, generate_n_step_graph, generate_main_results_table_paper_format_tests_pass_with_all, generate_main_results_table_paper_format_tests_pass, generate_main_results_table_paper_format_tests_pass_unit_tests_apriori, generate_main_results_table_paper_format_tests_pass_unit_tests_apriori_without_errors_or_passing_tests, generate_main_results_table_paper_format_tests_pass_code_coverage, generate_main_results_table_paper_format_tests_pass_human_eval, generate_main_results_table_paper_format_tests_pass_human_eval_without_eb
from time import time
import shelve
from enum import Enum
seed_all(0)
class Experiment(Enum):
    MAIN_TABLE = 1
    REBUTTAL_UNIT_TESTS = 2
    REBUTTAL_NEW_BASELINES_SAME_TASKS = 3
    REBUTTAL_NEW_RESULTS_NEW_TASKS = 4
    REBUTTAL_BIG_TASKS = 5
    REBUTTAL_HUMAN_EVAL = 6
    ABLATION_NO_SUMMARIZATION = 7

experiment = Experiment.MAIN_TABLE

if experiment == Experiment.MAIN_TABLE:
    # Main results table - before rebuttal
    # LOG_PATH = './results/final_final_results/combined.txt'
    # LOG_PATH = './repo_results/run-20240308-125808_LLMatic-ZeroShot-CodeT-SelfRefine-Reflexion-ZeroShot_donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-twitter-donnemartin-system-design-oop-whatsapp_0_20-runs_log/evaluator-20240312-021452_LLMatic-ZeroShot-CodeT-SelfRefine-Reflexion-ZeroShot_donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-twitter-donnemartin-system-design-oop-whatsapp_0_20-runs_log.txt'
    # LOG_PATH = './repo_results/run-20240308-125808_LLMatic-ZeroShot-CodeT-SelfRefine-Reflexion-ZeroShot_donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-twitter-donnemartin-system-design-oop-whatsapp_0_20-runs_log/evaluator-20240312-124410_LLMatic-ZeroShot-CodeT-SelfRefine-Reflexion-ZeroShot_donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-twitter-donnemartin-system-design-oop-whatsapp_0_20-runs_log.txt'
    # LOG_PATH = './repo_results_2/evaluator-20240315-204434_LLMatic-ZeroShot-CodeT-SelfRefine-Reflexion-ZeroShot_donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-twitter-donnemartin-system-design-oop-whatsapp_0_20-runs_log.txt'
    LOG_PATH = './repo_results_2/evaluator-20240316-012810_LLMatic-ZeroShot-CodeT-SelfRefine-Reflexion-ZeroShot_donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-twitter-donnemartin-system-design-oop-whatsapp_0_20-runs_log-AutoGPT.txt'
    # New rebuttal results table on additional environments
    # LOG_PATH = './results/rebuttal/evaluator-20231112-224059_CodeT-SelfRefine-Reflexion-ZeroShot_donnemartin-system-design-oop-finance-donnemartin-system-design-oop-bookclub_0_20-runs_log.txt'
    df = load_df(LOG_PATH)
    _, table = generate_main_results_table_paper_format_tests_pass(df)
    print('')
    print(table)
elif experiment == Experiment.REBUTTAL_UNIT_TESTS:
    # Main results table - before rebuttal
    LOG_PATH = "./results/rebuttal_processed_results/unit_tests_aprori/evaluator_r_unit_tests-20231114-182918_LLMatic_donnemartin-system-design-oop-whatsapp_0_20-runs_log_final_version.txt"
    df = load_df(LOG_PATH)
    _, table = generate_main_results_table_paper_format_tests_pass_unit_tests_apriori(df)
    # _, table = generate_main_results_table_paper_format_tests_pass_unit_tests_apriori_without_errors_or_passing_tests(df)
    print('')
    print(table)
elif experiment == Experiment.REBUTTAL_NEW_BASELINES_SAME_TASKS:
    # Main results table - before rebuttal
    # LOG_PATH = "./results/rebuttal_processed_results/new_baselines/evaluator-20231114-200934_LLMatic_donnemartin-system-design-oop-bookclub2_0_20-runs_log.txt"
    LOG_PATH = "./results/rebuttal_processed_results/new_baselines/combined_only_new_baselines_existing_tasks.txt"
    df = load_df(LOG_PATH)
    _, table = generate_main_results_table_paper_format_tests_pass(df, rebuttal=True)
    # _, table = generate_main_results_table_paper_format_tests_pass_unit_tests_apriori_without_errors_or_passing_tests(df)
    print('')
    print(table)
elif experiment == Experiment.REBUTTAL_BIG_TASKS:
    # Main results table - before rebuttal
    # LOG_PATH = "./results/rebuttal_processed_results/new_baselines/evaluator-20231114-200934_LLMatic_donnemartin-system-design-oop-bookclub2_0_20-runs_log.txt"
    LOG_PATH = "./results/rebuttal_big_tasks/evaluator-20231115-033314_LLMatic_insight-large-code-base-indico_0_20-runs_log.txt"
    df = load_df(LOG_PATH)
    _, table = generate_main_results_table_paper_format_tests_pass(df, rebuttal_big=True)
    # _, table = generate_main_results_table_paper_format_tests_pass_unit_tests_apriori_without_errors_or_passing_tests(df)
    print('')
    print(table)
elif experiment == Experiment.REBUTTAL_NEW_RESULTS_NEW_TASKS:
    # Main results table - before rebuttal
    # LOG_PATH = "./results/rebuttal_processed_results/new_baselines/evaluator-20231114-200934_LLMatic_donnemartin-system-design-oop-bookclub2_0_20-runs_log.txt"
    LOG_PATH = "./results/rebuttal_processed_results/new_baselines/combined.txt"
    df = load_df(LOG_PATH)
    _, table = generate_main_results_table_paper_format_tests_pass_code_coverage(df)
    # _, table = generate_main_results_table_paper_format_tests_pass_unit_tests_apriori_without_errors_or_passing_tests(df)
    print('')
    print(table)
elif experiment == Experiment.REBUTTAL_HUMAN_EVAL:
    # Main results table - before rebuttal
    # LOG_PATH = "./results/rebuttal_processed_results/new_baselines/evaluator-20231114-200934_LLMatic_donnemartin-system-design-oop-bookclub2_0_20-runs_log.txt"
    
    # Load df from csv using pandas
    df = pd.read_csv("./results/rebuttal_human_feature_count/HumanFeatureCount.csv")

    # LOG_PATH = "./results/rebuttal_processed_results/new_baselines/combined.txt"
    # df = load_df(LOG_PATH)
    _, table = generate_main_results_table_paper_format_tests_pass_human_eval_without_eb(df)
    # _, table = generate_main_results_table_paper_format_tests_pass_unit_tests_apriori_without_errors_or_passing_tests(df)
    print('')
    print(table)
elif experiment == Experiment.ABLATION_NO_SUMMARIZATION:
    # Main results table - before rebuttal
    # LOG_PATH = "./results/rebuttal_processed_results/new_baselines/evaluator-20231114-200934_LLMatic_donnemartin-system-design-oop-bookclub2_0_20-runs_log.txt"
    LOG_PATH = "./results/rebuttal_ablation_no_summarization/evaluator-20231116-045608_LLMatic_donnemartin-system-design-oop-twitter_0_20-runs_log.txt"
    df = load_df(LOG_PATH)
    _, table = generate_main_results_table_paper_format_tests_pass(df, ablation_no_summarization=True)
    # _, table = generate_main_results_table_paper_format_tests_pass_unit_tests_apriori_without_errors_or_passing_tests(df)
    print('')
    print(table)