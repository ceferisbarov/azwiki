from datasets import Dataset
from huggingface_hub import login

from azwiki import AzWiki
from config import hf_repo, hf_token

login(token=hf_token)

azwiki = AzWiki("processed")

dataset = Dataset.from_generator(azwiki)

dataset.push_to_hub(hf_repo)
