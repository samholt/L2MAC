# Relentless GPT

To install

Install everything in the setup folder.












* Paper:
  * [https://github.com/samholt/RelentlessGPT](https://github.com/samholt/RelentlessGPT)
  * Overleaf: [https://www.overleaf.com/9764181785fxfjrtnwwwsn](https://www.overleaf.com/9764181785fxfjrtnwwwsn)
* Code: [https://github.com/samholt/RelentlessGPTCode](https://github.com/samholt/RelentlessGPTCode)

Claiming to be the first method to solve well how to execute large complex tasks.

By Sam, Paulius, and Max.

---

# Research Code Template
Research Code Template: Cutting-edge research code template with all the best practices

* Saving logs out?: Google Protobuf to text? Saving python dictionaries out?
* Hyperparameter config: Allow complex configuration and tracking of config to results. Hydra/My own/
* Multiprocessing: Joblib? Torch/Jax multiprocessing? Running with slugs/bash?
* Wandb integration: Automatic tuning of hyperparameters
* Automatic plotting and visualizing logs in real-time?
* Automatically creating Latex tables? / Processing random seed runs


---

* Latest repo is nice. Be able to run pipeline end to end in one file, run minimum of 3 seeds, quickly to find issues, then run for longer 100, 1000 seed runs!
* Also pipe to central log processing to give immediate results as would appear in the paper as tables / plots, without any intermediary processing.

---

* Research process, always use mathematics, and tie mathematics to code!
** Go step beyond, leverage automatic proof solvers, symbolic math understanding to understand control flows of programs, information propagation, and the mathematical reliance of parts, and how much they affect things too. Always strive to proove things, or at least sketch a proof. Use the computer to assist with all these proof solving abilities and a course to do this as well!

---

* Implementing all baselines
* Tracking all the metrics we want (All additional metrics---integrate into plotting library--visualise all things, in easy to see dashboard---save copies of these dashboards/processed results out---really want to render latex tables and have these ready in a report/pdf file so can easily see the output at a given stage---can even make this as a GitHub workflow action? Run all code in docker, make sure it is all replicable & insert all results into paper etc.---Could be overkill.).
* Visualizing videos for the RL env
* Visualize results in the native form, give you eyes into the process and the science. What other tools/best practices are there? There is GIT etc, be like a commander to investigate!


---

Eventual clean up and release

Find out what people want from public code? Well documented, a re-usable package. Unit tests they can use. Make it a very useful tool etc. Tutorials to show how to use it.

Can I look at other repo's? What about clean RL code algorithms to take inspiration or other libraries of clean code examples to mimic?

---

Reproducibility:
* Always check for reproducibility; how can I get this to run automatically on some form of scheduler?!
* Use github actions to run and re-verify code, perhaps even putting the plots into the figure in the main paper?!


---
Templates:
* https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/guide4/Research_Projects_with_JAX.html
* WandDB hyper param tuner
* https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/td3_continuous_action_jax.py

---
Release notes:

* Readme should be in this easily parseable format for SEO. https://github.com/paperswithcode/releasing-research-code/blob/master/templates/README.md


--------

Always submit something early, never leave to last minute to submit, even if doing typing fixes etc!! Can easily misunderstand things!!


----

Writing in general. Always put money in the bank, whether that is practice, or similar. Especially writing down the ideas, and spending an entire session writing, and or more importantly reading and trying to empathasize with the reader.
Never format things by hand, always auto format with code, as I end up doing it too many time over and over!

$\mathcal{D} = \frac{D}{x+1}$ 

To code quicker I can use the following: 


---------

Maxims, always optomize for efficiency over total output! And creative ways to reflect on efficiency. Time myself so I know how to complete something like that