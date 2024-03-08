import time
from envs import get_env
from agents import initialize_agent

def simulate(env_name,
            method_name,
            seed,
            logger,
            rate_limiter,
            config={}, 
            wandb=None):
    
    # Load environment
    env = get_env(env_name, config, logger, seed)
    env.set_seed(seed)
    env.reset()
    # Load agent
    agent = initialize_agent(method_name, env, config, rate_limiter, wandb, logger)
    # Run experiment
    max_episodes = config.run.max_episodes

    def loop():
        episode = 0
        cumulative_reward = 0
        start_time = time.perf_counter()
        while episode < max_episodes:
            episode += 1
            env.reset()
            state = env.get_obs()
            t0 = time.perf_counter()
            action = agent.run(state)
            return {'method_name': method_name,
                'env_name': env_name,
                'episode_elapsed_time': time.perf_counter() - start_time,
                'episode_elapsed_time_per_episode': (time.perf_counter() - start_time) / episode,
                'cumulative_reward': cumulative_reward,
                'reward': cumulative_reward / episode,
                'generated_code_path': action,
                }
            state_out, reward, done, _ = env.step(action)
            cumulative_reward += reward
            episode += 1
            if not config.setup.multi_process_results:
                logger.info(f"[{env_name}\t{method_name}\tseed:{seed}|Episode {episode}/{max_episodes} action taken: {[action]} reward received: {reward} time taken: {time.perf_counter() - t0}s")
        ddict = {'method_name': method_name,
                'env_name': env_name,
                'episode_elapsed_time': time.perf_counter() - start_time,
                'episode_elapsed_time_per_episode': (time.perf_counter() - start_time) / episode,
                'cumulative_reward': cumulative_reward,
                'reward': cumulative_reward / episode,
                }
        if not config.setup.multi_process_results:
            logger.info(f"[{env_name}\t{method_name}\t][Result] {str(ddict)}")
        return ddict
    result = loop()
    return result