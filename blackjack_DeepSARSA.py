import numpy as np
import gym

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents import SARSAAgent
from rl.policy import BoltzmannQPolicy



# Init wandb --- web sync for data view
import wandb
from wandb.keras import WandbCallback
#from rl.callbacks import WandbCallback
wandb.init(project="cse240-deepsarsa")
#--------------------------------------



ENV_NAME = 'Blackjack-v0'


# Get the environment and extract the number of actions.
env = gym.make(ENV_NAME)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n

print(nb_actions)
print(env.observation_space)

# Next we build the NN model (same as blackjack_NN.py
model = Sequential()
model.add(Flatten(input_shape=(1,3))) #add inputs from env
model.add(Dense(16, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(nb_actions, activation='linear'))
print(model.summary())

# SARSA does not require a memory.
policy = BoltzmannQPolicy()
sarsa = SARSAAgent(model=model, nb_actions=nb_actions, nb_steps_warmup=10, policy=policy)
sarsa.compile(Adam(lr=1e-3), metrics=['mae'])

# training with visualization of sync
sarsa.fit(env, nb_steps=1000, callbacks=[WandbCallback()])

# After training is done, we save the final weights.
sarsa.save_weights('sarsa_{}_weights.h5f'.format(ENV_NAME), overwrite=True)

# Finally, evaluate our algorithm for 5 episodes.
#sarsa.test(env, nb_episodes=5, visualize=True) #not implemented yet



# by default, this will save to a new subfolder for files associated
# with your run, created in wandb.run.dir (which is ./wandb by default)
wandb.save('sarsa_{}_weights.h5'.format(ENV_NAME))


