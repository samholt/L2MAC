* Implement a fuzzy logic unit tester of sorts to test all possible states of Finite State Machine orchestrator
* Can make this smarter over time as well.
* Purposely load large code bases, as an example and modify them, using the contained logic therein, to see if the orchestrator can handle it. 
* Can easily replay to re-construct all states ever achieved by such a system. And handle all edge cases.
* Much more productive. Can feature gate them too.


-----------

Implementation improvements:
* Need to have a way to control for token cut offs, rather than just controlling for character max cut offs, as the counts are not the same!

Improvement notes:
* Have an LLM manage the control loop, to avoid spurious repeating patterns, and help improve the FSM, such as when it gets stuck in loops where it runs out of context. Allow it to think and pass on data, and process within the limited memory that it has.
* Reflect on the plan allot, and check that all features are fully implemented.
* Support plans within plans.
* Support continual iteration, once executed it's plan, reflect and process all the code according to the original requirements and re-loop around to improve upon the code, perhaps with different roles and perspectives, such as a highly skilled and detailed UX designer, designing screens, then a highly skilled front end engineer etc, and perhaps even have a way to automatically test the frontend components, much like a human would and pass feedback from this. If we can construct a test for it, we can iterate and improve upon the generation of it.
* Support human feedback at stages.
* Support for different tasks, such as writing a novel, and use an LLM as a self reflector and evaluator to spot mistakes and lost context etc. Can do this for our task, to make sure that we stay aligned. Merge this with empirical trajectory optimization methods, if we can simulate randomly, however have a reward to evaluate the multiple versions then we can average and head in the right direction (equivalent would be PPO updates here), i.e. could evaluate many possible approaches then select the highest reward ones, RL, one-step, multi-step monte carlo methods here. Could also incorporate a terminal value reward for the best choice or action selected, can even roll this into with human feedback here.