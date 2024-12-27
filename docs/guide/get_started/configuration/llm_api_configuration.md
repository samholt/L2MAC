# LLM API Configuration

After installation, follow these steps to configure the LLM API, using the OpenAI API as an example. This process is similar to other LLM APIs.

## Steps

1. **Initialize Configuration**:

   - Execute `l2mac --init-config ""` to generate `~/.l2mac/config.yaml`. Edit this file with your API configuration to avoid accidentally sharing your API key.

2. **Edit Configuration**:

   - Update `~/.l2mac/config.yaml` according to the [example](https://github.com/samholt/L2MAC/blob/master/config/config.yaml) and [configuration code](https://github.com/samholt/L2MAC/blob/master/l2mac/config.py):

```yaml
llm:
  api_type: "openai"  # or azure etc. Check ApiType for more options
  model: "gpt-4o"
  base_url: "https://api.openai.com/v1"  # or forward url / other llm url
  api_key: "YOUR_API_KEY"
```

> **Note**:
> Configuration priority is `~/.l2mac/config.yaml > config/config.yaml`.

With these steps, your setup is complete. To start with L2MAC, check out the [Quickstart guide](../quickstart) or our [Tutorials](../../tutorials/concepts).

L2MAC supports a range of LLM models. Configure your model API keys as needed.


## OpenAI API

Check [config.py](https://github.com/samholt/L2MAC/blob/master/l2mac/config.py)

```yaml
llm:
  api_type: 'openai'
  model: 'YOUR_MODEL_NAME'
  base_url: 'YOUR_BASE_URL'
  api_key: 'YOUR_API_KEY'
```

## Azure OpenAI API

Check [config.py](https://github.com/samholt/L2MAC/blob/master/l2mac/config.py)

```yaml
llm:
  api_type: 'azure'
  model: 'YOUR_MODEL_NAME'
  base_url: 'YOUR_AZURE_BASE_URL'
  api_version: 'YOUR_API_VERSION'
  api_key: 'YOUR_API_KEY'
```
