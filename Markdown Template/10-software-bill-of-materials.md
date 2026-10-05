# Software Bill of Materials

## Software Bill of Materials

This register is where you will keep track of all third party libraries, tools and models to be used during development. For more information: Producing Software Bill of Materials a.k.a SBOMs for Atlassian - Inside Atlassian

syft is an open source project where you can supply your requirements.txt or docker image to generate an SBOM table.

| Package Name | Version | Description | License | Supplier | Package Checksum |
|---|---|---|---|---|---|
|   |   |   |   |   |   |

## AI Software Bill of Materials

This part of SBOM is where third party models will be documented. For models hosted on huggingface, you can use AI SBom Generator to generate an AI SBOM in the CycloneDX 1.6 json format, with other helpful metadata you can refer to.

When naming the model please specify all characteristics, including model version, size, and quantization. Include links to where you accessed the models weights and more details.

Specify what purpose each model will satisfy, who accessed this model, and when.

Finally mention the specific libraries used to interact with them, along with an associated experiment and the result, whether the model will be used or rejected and why.

| Model Name | Purpose | Accesser | Date of Access | Method of Interaction | Experiment and Results |
|---|---|---|---|---|---|
| BAAI/bge-large-en-v1.5 | Embedding text chunks for use in the vector database | Volga | Oct. 6 | Run on GPU on server; interact via langchain integration of chromadb | Experiment 1 |
| Gemma 3 4b Q4_K_M | Generate answers given a context | Volga | Oct. 6 | Run on GPU on server; interact via api calls to Ollama host |   |
