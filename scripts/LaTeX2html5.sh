#! /bin/bash

## A simple script to translate LaTeX to html5 with the help of pandoc.
## Pandoc is able to transform simple LaTeX math expressions into plain html5 (no sophisticated [MathML](http://www.w3.org/Math/)...).
## The advantage is that no [MathJax](http://www.mathjax.org/) or the like is required.

pandoc -f latex -t html5 $1
