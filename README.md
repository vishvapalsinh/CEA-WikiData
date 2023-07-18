# Role of Preprocessing on Matching tables to KGs

This repository contains the code and resources associated with the paper titled "Role of Preprocessing on Matching tables to Knowledge Graphs". The paper focuses on the Cell Entity Annotation (CEA) task within the Semantic Table Understanding (SemTab) Challenge, using the WikidataTables dataset. The objective of this work is to investigate the impact of preprocessing techniques on the performance of the CEA task and showcase the improvements achieved.

## **Contents**

- **`Code/`**: This directory contains the code (files) implementation of the preprocessing techniques for different experiments considering the CEA task.
    - **`Python files/`**: Python files (.py) containing different functions that are utilized.
    - **`Json files/`**: Json files (.json) contain generated response included in preprocessing steps. 
    - **`Notebook files/`**: Jupyter notebook files (.ipynb) showing fucntional analysis as well as evaluation results. 
- **`Dataset/`**: This directory includes the WikidataTables dataset used in the experiments [ref](https://github.com/sem-tab-challenge/2023/blob/main/datasets/WikidataTables2023R1.tar.gz).
- **`F_E_Analysis/`**: This folder contains the fucntional and experiment analysis documents made for the CEA task.
- **`README.md`**: This file provides an overview of the repository and instructions for running the code.

## **Dependencies**

- Python libraries
    - csv
    - requests
    - pandas
    - numpy
    - time
    - SPARQLWrapper
    - json
- APIs/Endpoints
    - "https://www.wikidata.org/w/api.php"
    - "https://query.wikidata.org/sparql"    