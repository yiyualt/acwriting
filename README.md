# acwriting

   [![pip](https://raw.githubusercontent.com/yiyualt/acwriting/536d8289fee3603d0fb261d780302a7f35cd1070/data/pip.svg)](https://pypi.org/project/pip/)
   [![LicenseMIT](https://raw.githubusercontent.com/yiyualt/acwriting/536d8289fee3603d0fb261d780302a7f35cd1070/data/LicenseMIT.svg)](./LICENSE.txt)
   [![pyversion](https://raw.githubusercontent.com/yiyualt/acwriting/536d8289fee3603d0fb261d780302a7f35cd1070/data/pyversion.svg)](https://github.com/Yoki0/acwriting)
   
   
   
## Introduction
Have you ever felt frustrated with your English writing skills?
If yes, you are in the right place! Acwriting is actually what you want!

What is acwriting?

Short answer is, it is a Python package for the English writings, designed especially for academic writings.
It can:
* Translate Chinese from/to English ( Using py-googletrans package, original project link: https://github.com/ssut/py-googletrans)
* Find Synonym / Antonym of the given english word ( Using PyDictionary package, original project link: https://github.com/geekpradd/PyDictionary)
* Transfer Python math formulas into Latex format expression (Using latexify package, original project link: https://github.com/odashi/latexify_py )
* Find most suitable example sentence of the given english word/phrase
* Given the writing intention,e.g. "introduce something","state the shortcoming of something","write conclusion",etc, 
the system outputs the most suitable phrases and sentence templates.
* Given the english sentence you intend to express, the system automatically corrects the sentence's errors and transfer it into formal & academic style expression.

So, let's get started!

## TODO


## Simple example

Find most suitable examples sentence of the given english word/phrase

```python

    from acwriting.phafind import Phafind
    p = Phafind()
    text = "best knowledge"
    result = p.find(text)
    ['To our <font color="green"> best knowledge </font>, it is still an open challenge.', 'B', 'D']
```

## Installation
If you use pip, install the latest version of acwriting by:

    $ pip3 install acwrite


If you use conda, install the latest version of acwriting by:
    
    $ conda install acwrite


Or, you can install it manually: 
     
    $ git clone https://github.com/yiyualt/acwriting.git 
    $ cd acwriting
    $ python3 setup.py install 


## License

The MIT License (MIT)

Copyright (c) <2020> Yi Yu & Chunyang Mo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.