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
* Given the English sentence you intend to express, the system automatically corrects the sentence's errors and transfer it into formal & academic style expression.

So, let's get started!

## TODO
* How to realize autocorrect 
* Autocomplete funciton
* Embed Autocomplete function into the system

## Simple example

Find most suitable examples sentence of the given english word/phrase

```python

    >>> from acwriting.phafind import Phafind
    >>> p = Phafind()
    >>> phase = "best knowledge"
    >>> result = p.find(phase)
    >>> print(result[0:5])
    ['1. To our best knowledge, it is still an open challenge.',
     '2. In the old days, one sought a fatwa from the sheikh who had the best knowledge.',
     '3. I feel now that we have the best knowledge to help people.',
     '4. So what's our best knowledge?',
     '5. This, to our best knowledge, was never been investigated before.']
```

Given the writing intention,e.g. "introduce something","state the shortcoming of something","write conclusion",etc, the system outputs the most suitable phrases and sentence templates.

```python

    >>> from acwriting.senfind import Senfind
    >>> s = Senfind()
    >>> intention = "compare two things"
    >>> result = s.find(intention)
    >>> print(result[0:5])
    ['1. X is different from Y in a number of respects.',
     '2. X differs from Y in a number of important ways.',
     '3. Both X and Y share a number of key features.',
     '4. These results are similar to those reported by xxx',
     '5. In contrast to earlier findings, however, no evidence of X was detected.']
```

Given the English sentence you intend to express, the system automatically corrects the sentence's errors and transfer it into formal & academic style expression.
(The precision of the results will come later.)
```python

    >>> from acwriting.autotrans import Autotrans
    >>> my_auto = Autotrans()
    >>> style = "acdemic style"
    >>> text = "There has many problems"
    >>> result = my_auto.transfer(text, style)
    >>> print("original sentence":, text)
    "There has many problems"
    >>> print("after corrected:",result)
    ['It has a lot of defects',
     'It has proven to be problematic',
     'It has a lot of issues,',
     'There are many problems,']
     
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
