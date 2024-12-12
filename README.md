# Introduction

* `DataPrep-MUN`: contents, assignments and datasets from the Data Preparation Techniques course at MUN.
* `src`: practicing and notes.

## Setup (Jupyter Notebook)

* Install Python [here](https://www.python.org/).
* Install Jupyter (`pip install jupyter`).
* Create a folder and open it inside the terminal.
* Type `jupyter notebook` (this will open up the jupyter code editor on your browser).

# A bit about Python's execution

* **Compiled languages** transform code into machine code (binary gibberish) ahead of time, in other words, before execution. This increases performance and execution speed. However, machine code can't be executed on different operating systems.

* **Interpreted languages** directly executes code, line by line, without a prior compilation step. This means that the application can be executed on any machine, so long as that machine has the language's interpreter. Despite this benefit, execution time normally becomes slower.

Python is generally described as an interpreted language. However, it implements 'Just-In-Time Compilation' (or JIT). In this way, python code is first compiled into python **bytecode** (somewhat of a semi-compiled code) and later interpreted. Python, by default, is compiled to bytecode by **CPython** (a Python implementation) and interpreted by PVM (Python Virtual Machine). There are several Python implementations: IronPython (C# bytecode), Jython (Java bytecode, executable by JVM).
