# Concepts

After this tutorial, you will be able to:

- Understand L2MAC's concept of a prompt program and how it works
- How it uses memory to store the intermediate outputs from completing each step instruction in the prompt program, and re-use this growing memory for subsequent step instructions

The goal is to provide an intuitive and <b>simplified</b> explanation of the concepts so that users have a background to further explore the tutorial series. While we aim for clarity, we also recognize simplifications can produce inaccuracy or omission. Therefore, we encourage more navigation over subsequent documents for complete comprehension.

You may also jump to [L2MAC 101](./l2mac_101) if you want hands-on coding first.

Check out our [ICLR 2024 paper](https://openreview.net/forum?id=EhrzQwsV4K) for a complete, rigorous explanation.

## High-Level Overview

![BlockDiagram](/l2mac-block-diagram.png)

**L2MAC Overview**. Here the LLM-automatic Computer Framework is instantiated for extensive code generation tasks. First, it takes in a **single user input prompt**, for example, `"Create an online chat app..."`, and the underlying LLM understands the user task and breaks it down into sequential instructions, a **prompt program** to execute to complete the task. We note that self-generating a prompt program is a form of bootstrapping, and L2MAC also supports being given the prompt program explicitly as input. Mirroring the operation of a computer, each instruction of the prompt program is sequentially loaded into a new instance of an LLM agent, where we make the LLM an agent by providing it with tools and the ability to perform actions sequentially.

The **Control Unit (CU)** manages the LLM agent's *context window* for each instruction (agent) and empowers the LLM agent to interact with an *external memory file store* through read, write, and evaluate tools. Crucially, this *external memory file store* stores the *prompt program*, as well as the intermediate and final outputs of the execution of following the prompt program to solve the given task; this follows the stored-program computer, or von Neumann architecture approach of storing both the program and the program output in memory. It identifies and reads relevant files from the memory to generate or update files per instruction. This ensures proper conditioning of existing files without losing vital context. Automatic checks evaluate the LLM's outputs for correctness and completion, with iterative error corrections involving both code syntactical checks of the code and running self-generated unit tests to check desired functionality. Overall, this produces a complete large codebase that fulfills the detailed user task in the file store.

## Benefits of the LLM-automatic Computer

By using the LLM-automatic computer framework, we gain the immediate strong benefits of:

* Strong empirical performance beating existing LLMs and other leading LLM multi-agent and LLM compound AI frameworks for [codebase generation tasks](https://arxiv.org/pdf/2310.02003.pdf), and [single coding tasks, such as HumanEval.](https://paperswithcode.com/sota/code-generation-on-humaneval).
* Can augment *any existing LLM* with the ability to follow a near-infinite length and complex *prompt program* to solve a given task.
* Can generate a near-infinite amount of output for a given task when following a prompt program.
* Can generate intermediate outputs, either from thinking and solving parts of the difficult task already or from the use of tools, and re-use these intermediate thoughts at later stages of its operation to solve more complex and difficult tasks that require many LLM thinking steps to solve, for example, generating an entire codebase for a complex application, refires conditioning, understanding and potentially modifying many of the previously generated code files in the code base.
* By creating and following a prompt program, we can create large unbounded outputs that align exactly with what the user desires rather than autonomously think and forget what the original user input requirements were, which is the case of [AutoGPT (page 8)](https://arxiv.org/pdf/2310.02003.pdf).
* By breaking a large task into a sequential prompt program, we can generate the final output as one part at a time, enabling LLMs with fixed context windows to generate significant unbounded outputs that are significantly greater than their underlying context window. We note that this also helps large context LLM models, as prior work has shown that even when using a large context LLM model, their attention is largely restricted to the most recent [small percentage of the context window](https://arxiv.org/abs/2307.03172).
* [Mirroring the development of the computer](../mission), we believe that the advancement of the LLM-automatic Computer Framework enables a general-purpose task-solving framework, where it can solve any task by simply re-programming the prompt program, whereas many existing multi-agent systems today, specialize for only one task, which is reminisnicnt of the first computing machines, where the [breakthrough was a re-programmable automatic or Universal automatic computing machine](https://arxiv.org/pdf/2310.02003.pdf).


## Low-Level details

All transformer-based LLMs have a fixed context window, limiting the number of tokens and characters they can process. Therefore, this restricts a single LLM from generating any larger output than its fixed context window constraint, such as a large codebase or entire books. A natural solution is to extend an LLM agent with external memory. However, existing methods use too simplistic memory stores, such as an external corpus of previous summarizations, which is append-only or maintains precise values for variables with databases or a dictionary without any provision for in-place updates. Compounding this, the existing works do not include mechanisms for maintaining syntactic or semantic consistency within the memory store, a vital requirement for the generation of coherent and interdependent large code structures.

Considering these issues, we introduce the LLM-automatic computer (L2MAC) framework, which is the first practical LLM-based general-purpose stored-program automatic computer (von Neumann architecture) framework, an LLM-based multi-agent system for long and consistent output generation. Here we mean *automatic* in the sense that it can automatically follow the internal prompt program without human intervention, mirroring early computers, such as [Turing's (Automatic-)machine (page 17)](https://arxiv.org/pdf/2310.02003.pdf).

A Control Unit (CU) orchestrates the execution of the individual LLM agents and their interaction with the memory store. As outlined in the above Figure, an LLM agent first generates a task-oriented *prompt program* from a detailed user-specified task. The CU tailors the LLM agent's context, so it always includes the next unresolved instruction in the *prompt program* and information about the execution of past iterations (agents), and declutters the context when approaching its limit. It also endows the LLM agent with the ability to read and update any existing region of the memory store or extend it with new outputs. Furthermore, the CU plays a crucial role in checking the generated output. It feeds the LLM agent with syntactical checker errors and requests the LLM agent to generate checks alongside generating output, here unit tests when generating code, which are verified at each update of the memory file store to trigger corrective actions if needed, thereby ensuring that the extensive output in memory is both syntactically and functionally consistent.

### L2MAC Framework

Now we outline the L2MAC framework for the first practical LLM-based stored-program computer, with an instantiation for coding illustrated in the above Figure. L2MAC consists of three main components: the LLM processor, the memory file store, and the Control Unit (CU) that controls the flow of the execution, thus endowing the LLM agent with read-and-write capabilities, among other capacities---this is illustrated in the below Figure.

#### LLM-based Processor

An LLM can be viewed as a more complex atomic unit of computation with a fixed context window input; this allows for a flexible and powerful computation unit that can be used to solve a range of different tasks. Additionally, the LLM is empowered with tools forming an LLM agent, where it can select which action to execute next or provide an output. Critically, the LLM produces a probabilistic output; it is regarded as a hallucination when it makes an erroneous output. Thus, crucial to effectively updating an interrelated memory is the ability to enforce periodic checks on the LLM output to ensure correctness and consistency.

#### Memory

Following a stored-program computer, we define two types of memory: that of the prompt program (or instructions) and that of the file store. Here, the file store stores information relevant for the processor to read, write, and evaluate, with the final output ultimately stored in the file store.

#### Control Unit

The control unit is responsible for managing the context window for the LLM, encompassing both its inputs and outputs, executing the LLM, checking its outputs for errors, and enabling it to call tools (functions), which include reading and writing to the memory file store. We provide the following figure to detail its operation.

![ControlFlow](/control_flow.png)
**Control Unit**-Control flow diagram for one dialog turn $t$. Here this executes one current instruction $\mathcal{I}^{(k)}$ of the *prompt program*. It starts by loading the first instruction into the context window $C^0\leftarrow \{\mathcal{I}^{(0)}\}$ and iterates it automatically until all instructions in the *prompt program* $\mathcal{I}$ have been executed. First, the LLMs context window $C^t$ is processed by the LLM Processor $\mathcal{P}_{\text{LLM}}(C^t)$ to output a response $M_r$. The CU stores this in a buffer $\Delta_{C^{t+1}} \leftarrow \{M_r\}$, and checks if $M_r$ has called a tool, and if so, it executes the tool with the specified input in $M_r$, which includes reading, writing and evaluating $\mathcal{E}(D)$ the file store $\mathcal{D}$-outputting the tool response $M_f$, which is appended to the buffer $\Delta_{C^{t+1}}$. The CU performs additional control flow (as outlined below) to check if an instruction has been completed, continue an instruction beyond the context window, and continue executing the current instruction.

##### Task-Oriented Context Management

The Control Unit (CU) uses the LLM as a multi-turn dialog system, filling its context window $C$ with a combination of messages $m$ which can come from the user $M_u$, an LLM response $M_r$, a function (tool) output $M_f$, or the CU $M_c$, so that $m \in \{ M_u, M_r, M_f, M_c\}$.
Consequently, at turn $t$ then the context window $C^t\in \text{List}(M)$ is of the form $C^t = (m^1, m^2, \dots, m^{n_t})$.


To make L2MAC an automatic computer, the CU prompts the LLM to fill the initially empty instruction registry $\mathcal{I}$ with a list of instructions $\{\mathcal{I}^{(1)},\dots,\mathcal{I}^{(K)}\}$ where each will be executed in the LLM processor. We consider the simplest case of sequential instructions of a prompt program and however we realize more complicated control flow paradigms are possible, and leave this for [contributors to add](../roadmap). L2MAC then loads an empty context window of an LLM agent with the first instruction $C^0\leftarrow\{\mathcal{I}^{(0)}\}$ and iterates the CU control flow loop until all instructions have been achieved. 
The LLM can signal when the current instruction $\mathcal{I}^{(i)}$ has been completed through calling a special tool `step\_complete' at which point the CU evaluates the file store $\mathcal{D}$ using its evaluator module $\mathcal{E}$ (discussed below) to check for any introduced errors. If none are found, it asks the LLM to summarize the generated output in the current context window $C^t$ as a message $M_{rs}$ and resets the context window as $C^{t+1}\leftarrow \{\mathcal{I}^{(k+1)},M_{rs}\}$.


**Overcoming the fixed context window constraint**. The input to the LLM cannot exceed the context window constraint $c$: the combined length of the initial context $C^t$ and the additional messages buffer $\Delta_{C^{t+1}}=\{m^0,\dots,m^n\}$ must fit in the context window, that is\footnote{We use $\oplus: \text{List}(A)\times \text{List}(A) \rightarrow \text{List}(A)$ as the concatenation of two lists on the set $A$. We abuse notation by considering any $a\in A$ as a singleton $\{a\}$.}, $|C^t \oplus \Delta_{C^{t+1}}| \leq c$.
However, the length of $\Delta_{C^{t+1}}$ is not known a priori, so the CU should have a way of handling the cases where $\Delta_{C^{t+1}}$ exceeds the context margin $c-|C^{t}|$.
This can be achieved through a combination of three different strategies: (1) minimize the occurrence by promoting the task at each time step to be small enough and economizing the filling of the context $C$; 
and if the situation occurs, (2) store in the file store $\mathcal{D}$ as much relevant output as possible from the current $C^t$ and (3) update or include a new summary message with $\mathcal{I}^{(k)}$ as in-context tuning for the next iteration.

Regarding (1), through appropriate crafting $C^t$, the CU can prompt the LLM to plan sub-steps for the current instruction (most likely the original task prompt given by the user) and then target each sub-step in the following iterations. For illustration, in a coding setting, (2) can be achieved by storing the generated code so far to avoid rewriting it in the next iteration, and (3) by initializing a new prompt with a summary $M_{rs}$ of the current progress and helpful information to complete the current instruction, e.g., which files should be read or modified, or the current progress made fixing errors-(3) is further detailed at the bottom right of the above Figure.

##### Precise Read/Write tools for entire memory

The need for a reading mechanism that retrieves the relevant information at each iteration is evident and has been reasonably explored in previous literature.
In contrast, previous work on memory has paid little attention to the writing component, which gets mostly reduced to the [appending of new prompts and LLM outputs](https://arxiv.org/abs/2307.08191) or updating the values of very structured and thus [restrictive forms of memory](https://arxiv.org/abs/2305.14322), e.g., variables or [tables](https://arxiv.org/abs/2306.03901).

These approaches make sense for summarization, dialogs, and database manipulation tasks but are not suitable for long interconnected output generation tasks, such as generating large codebases for system design tasks. Indeed, in such settings, the possibility of downstream subtasks $\mathcal{I}^{(j)}$ demanding extensions of previous outputs (such as modules in a codebase) due to imperfect planning, plus the non-determinism and possible hallucination of LLMs, make it probable to require modifications of previously stored memories $\mathcal{D}$ to rectify these defects.

In L2MAC it is thus key to implement read/write interactions with any part of the memory. We want the agent to be able to scan on demand $\mathcal{D}$, retrieve parts of the memory that it considers relevant, and potentially update them. In the next section, we detail our implementation of an LLM with a write component that allows it not only to add new information to $\mathcal{D}$ but also to delete and update any of its contents, an essential element that allows L2MAC to succeed in long output generation tasks.

##### Checking the generated output


As discussed in LLM-based Processor above, the intrinsic stochasticity of LLMs and the well-known phenomenon of hallucination makes it likely that incoherent or erroneous outputs occur during long interactions, which can be disastrous, for example, in coding. More profoundly, changes (e.g., to a function) to satisfy a given instruction $\mathcal{I}^{(j)}$ can hamper the solution to formerly completed instructions $\mathcal{I}^{(i)}$, $i<j$.
Therefore, it is essential to incorporate two key checks, one to check the generated outputs for errors using a given evaluator module $\mathcal{E}$, and the other to check when the current instruction has been completed in the current context $C^t$ (c.f. top diamond in the above figure).


**Error checking and error correction**. Using a given evaluator module $\mathcal{E}$, which can process the existing file store $\mathcal{D}$, i.e., $\mathcal{E}(D)$, allows when run, errors to be detected and returned to the LLM as an evaluator message $M_{fe}$. The evaluator is domain-specific; for example, in coding tasks, this can correspond to syntactical code checkers or self-generated unit tests that verify the correctness of the output for an instruction $\mathcal{I}^{(i)}$. Crucially, these self-generated unit tests also help test the existing functionality of previously generated instructions $\mathcal{I}^{(j)}$.
Naturally, evaluation checks should be enforced on the file store $\mathcal{D}$ after each writing operation to ensure that new additions are correct and consistent with previous files. These result in messages $M_{fe}$ that are provided for in-context learning so that the LLM can correct the errors, $\Delta_{C^{t+1}} \leftarrow \Delta_{C^{t+1}}\oplus M_{fe}$, and iterate by rewriting $\mathcal{D}$ until the evaluator checks pass, if any are present.

**Checking for current instruction completion**. To ensure continued execution in a multi-turn dialogue LLM system until completion, we request the LLM to decide on the next step to take, which can involve executing a tool.
This is achieved through a cycle prompt message $M_{cc}$ that also asks the LLM if the instruction has been completed. Cycle prompting is necessary to account for different instructions requiring a variable number of turns to complete and to protect against hallucinations where the LLM agent only discusses the instruction $\mathcal{I}^{(i)}$ and does not generate a solution or store it in memory. Overall, this ensures that the LLM provides a solution for the given instruction within the current context (P3).

### L2MAC for Coding Tasks

Now, we use our LLM-automatic computer (L2MAC) framework and instantiate it to complete large codebase generation tasks. We distinguish the general-purpose task long-generation framework from the code instantiation to detach the core components from task domain decisions that can be appropriately adapted to other task domains. We provide the full details of the implementation in the [paper page 19](https://arxiv.org/pdf/2310.02003.pdf); yet here we highlight some notable design decisions on the memory layout (in particular, $\mathcal{D}$) and the read logic. There are different potentially valid alternatives for the read component in L2MAC. However, to promote a *transparent read component*, we make the following choices. 

We specify the memory file store $\mathcal{D}$, be composed solely of files, each shorter than the residual margin of the context window after accounting for preliminary messages in any iteration, and instruct the LLM agent to assign each file a semantically meaningful descriptive path. For example, a file name `models/user.py` suggests that it contains the data model for the user class. This choice is not only valuable for a human reader but also crucial for our Read-and-Write implementation, as it allows the LLM to infer the content of existing files $\mathcal{D}$ and prioritize those that it might need to read to complete its current instruction. Given the list of file paths, the LLM can request that the contents of any be appended into its context $C^t$. Although the path-to-content link is not absolute, empirically, this read implementation can perform well when coupled with the context management logic of the CU. Specifically, suppose the LLM reads the content of certain files and reaches the context window limit. In that case, it can include in its subsequent iteration summary indications of which files should be read and which should be excluded in order to generate the code necessary to complete the current instruction. This approach thereby enables the LLM to systematically scan all memory, with the scanning order guided by priorities previously established from the file path names.

---

Now, you have a first glance at the concepts. Feel free to proceed to the next step and see how L2MAC provides a framework for you to create extensive outputs.
