# meme_generator

 Meme generator dynamically generates memes, including an image with an overlaid quote.



## Installation
```
git clone https://github.com/kminito/meme_generator.git
```


## Usage

### On CLI
```
usage: meme.py [-h] [--body BODY] [--author AUTHOR] [--path PATH]

Generate meme!!

optional arguments:
  -h, --help       show this help message and exit
  --body BODY      text that want to show
  --author AUTHOR  author of the text
  --path PATH      file path for background image you want
```


### As web app

```
python app.py
```

and open http://127.0.0.1:5000/


## Requirements
* pandas
* flask
* requests
* python-docx
