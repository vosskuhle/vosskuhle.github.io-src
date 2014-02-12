These are the sources of my [private website](http://vosskuhle.github.io) hosted at [GitHub](https://github.com/vosskuhle/vosskuhle.github.io).
To generate the website from these sources type
```bash
hyde gen -c prod.yaml -r
```
Make sure you have installed all requirements, for example with the help of `pip`
```bash
pip install -r requirements.txt
```
Also consider setting up a Python environment dedicated to this task with [virtualenv](http://www.virtualenv.org).

An additional requirement is [Less](http://lesscss.org/).

Another optional requirement, handy during development, is [pandoc](http://johnmacfarlane.net/pandoc/).
It is used by the simple script `LaTeX2html5.sh`.

 * * *

My website is produced with the help of [hyde](http://github.com/hyde/hyde) and [Skeleton](http://www.getskeleton.com/).
