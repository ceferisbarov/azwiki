# Processing scripts for the `jafarisbarov/azwiki` dataset

**You can find the final dataset [here](https://huggingface.co/datasets/jafarisbarov/azwiki)** 
  

## Working with the scripts
Set-up the Python environment:
```bash
python3 -m venv env

source env/bin/activate

pip install -r requirements.txt
```


Download the latest multistream version from wiki dumps:
```bash
# Download
wget https://dumps.wikimedia.org/azwiki/latest/azwiki-latest-pages-articles-multistream.xml.bz2

# Extract the xml file
bzip2 -dk azwiki-latest-pages-articles-multistream.xml.bz2
```
We used the latest dump as of 15.12.2023.
  

Run the `dewiki` script to extract articles from the xml file. They will be stored in the `raw` folder. After this, you can run the `process.py` scrip to clean contents and filter out some files. Results will be saved in the `processed` folder.
```bash
# Extract the articles from the xml file
python scripts/dewiki.py

# Process
python scripts/process.py
```

## Working with Huggingface Datasets
Create a `config.py` file at the root of your project folder. Define the following variables:
```py
hf_repo = "username/dataset_name"
hf_token = "your_hf_access_token"
```
After this, simply run the `hf.py` file to push the dataset to HuggingFace.
```bash
python scripts/hf.py
```

## Acknowledgements and contribution
Original version of the `process.py` script has been developed during the AzCorpus project. `dewiki.py` script has been adapted from this [repository](https://github.com/daveshap/PlainTextWikipedia).

If there is anything to update regarding the dataset, open a PR here, on GitHub. I will update the HuggingFace repo myself.
