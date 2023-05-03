# EECS Tools  

A collection of handy functions for introductory ECE/EECS courses. These functions are designed to assist students to quickly calculate what they want during exams. To maximize simplicity, there is no structured OOP practices here, simply functions.  

## Coverage  
  
Functions are organized in files, with their respective coverage shown below:  
- `Steady`: Steady-state DC/AC circuits 
- `Dynamic`: RC/RL/RLC circuits 
- `Digital`: Logic operations and digital circuits 
- `Util`: Utility functions, mostly math-related  


> Attribution: This coverage is originally adapted from the syllabus of Duke University's ECE 110: Fundamentals of Electrical and Computer Engineering. 

## Usage  

Clone this repository onto your machine (or perhaps download it as a zip). Simply import the functions from the files above, and it is ready to be used: 

```python
from Util import *
from Steady import *
from Digital import *
from Dynamic import *
```

About what functions there are and how to use them, please follow the [documentation](./doc.md). 

### Running in Browser

There is a handy pre-built calculator/playground HTML file (`index.html`) inside this repository. Follow the steps to use this calculator:

1. Clone (or download) the repository onto your machine.
1. Open the directory with VS Code. 
1. Install the Live Server extension if you have not. 
1. Run `index.html` with Live Server and access the playground in your browser. 

> Attribution: Running Python code directly within your browser is enabled by the developers of [PyScript](https://github.com/pyscript). Follow the link to learn more about their amazing work.  

## Notices and Contribution
- This collection is designed to help students do their exams, but should only be used when computers and open-source libraries are permitted. 
- Feel free to contribute! Simply clone, add a branch, edit, and push. 

## License 

[MIT License](https://mit-license.org/): 

Copyright © 2023 Ze-Ting Lu 呂澤霆

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.