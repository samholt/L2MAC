model=tiiuae/falcon-40b-instruct
num_shard=1
volume=/home/sam/.cache/huggingface/hub # share a volume with the Docker container to avoid downloading weights every run

docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data ghcr.io/huggingface/text-generation-inference:0.8 --model-id $model --num-shard $num_shard --trust-remote-code true --quantize bitsandbytes

sudo docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data ghcr.io/huggingface/text-generation-inference:0.8 --model-id $model --trust-remote-code --quantize bitsandbytes