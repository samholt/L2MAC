#!/bin/bash
# conda create --name digitaltwins python=3.11.2
# conda activate digitaltwins
# # https://github.com/google/jax#installation
# pip install --upgrade pip
# pip install --upgrade "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
# pip install -r requirements.txt
# sudo apt-get install xvfb
# sudo apt-get install python-opengl

#!/bin/bash
conda create --name l2mac python=3.9.7
conda activate l2mac
pip install hydra-core --upgrade
# Install PyTorch official version here - from standard website
pip install -r requirements.txt
pip install hydra-core --upgrade



# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# pip install hydra-core --upgrade
# pip install tensorflow
# pip install fastai


# conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
# conda update ffmpeg
# pip install TorchDiffEqPack
# pip install imageio-ffmpeg
# conda install -n mbrl ipykernel --update-deps --force-reinstall
# sudo apt-get install xvfb
# sudo apt-get install python-opengl

# sudo DISPLAY=:0 XAUTHORITY=/var/run/lightdm/root/:0 nvidia-settings -a "[gpu:0]/GpuPowerMizerMode=1"

# # Jax install
# conda install jaxlib=*=*cuda* jax cuda-nvcc -c conda-forge -c nvidia
# # jax==0.4.4 # Seems to play nicely!
# # Any higher and jaxlib with cuda installation fails