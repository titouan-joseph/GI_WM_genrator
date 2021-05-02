# GI_WM_generator

Watermark generator for [graines d'images association](https://www.grainesdimages.fr/)

Take logo on ``assets/img/logo_transparent.png`` with 179px width and 134px height 

Usage of Pillow and argparse for the CLI.  
To use : 
```bash
usage: main.py [-h] [--name NAME] [--multipleName MULTIPLENAME [MULTIPLENAME ...]] [--file FILE] [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --name NAME, -n NAME  The name will be write on WM
  --multipleName MULTIPLENAME [MULTIPLENAME ...], -m MULTIPLENAME [MULTIPLENAME ...]
                        Generate multiple WM
  --file FILE, -f FILE  .txt file with names. One per line
  --verbose, -v         Verbose mode

```
For example :
- to generate one WM : ``main.py --name NAME`` or ``main.py -n NAME``
- to generate multiple WM : ``main.py --multipleName NAME1 NAME2 NAME3`` or ``main.py -m NAME1 NAME2 NAME3``
- to generate multiple WM base on txt file : ``main.py --file names.txt`` or ``main.py -f names.txt``