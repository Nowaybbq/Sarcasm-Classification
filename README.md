# Sarcasm Classification Repository

Welcome to the Sarcasm Classification Repository.
Here, you will find information about the project, its requirements, and how to run the project.

## Table of Contents
1. [Description](#description)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Running](#running)

## 1. Description <a name="description"></a>

The Sarcasm Classification project aims to categorize the text into simple or sarcastic.

## 2. Requirements <a name="requirements"></a>

To contribute or run this project locally, you will need to install requirements in requirements.txt:

## 3. Installation <a name="installation"></a>

To install and set up this project on your local machine, follow these steps:

1. Clone the repository:

```bash
   git clone https://github.com/Nowaybbq/SarcasmClassification.git
```
2. Install all dependencies of the project

```bash
   pip install -r requirements.txt
```
## 3. Running <a name="running"></a>

1. run locally

```bash
   uvicorn main:app --reload
```
2. Log in https://www.postman.com/
3. Send POST request at http://127.0.0.1:8000/classify-text/ with raw json

```bash
    {
    "text": "Oh, I just love Mondays!"
    }
```
