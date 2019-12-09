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

[Upstream hyde](https://github.com/hyde/hyde) is mostly compatible with python3.
However, there is no current version available on [PyPi](https://pypi.org/).
Therefore one must install directly from git via below command.
Furthermore there is a tiny bug in upstream hyde.
This has been fixed in a [fork](https://github.com/vosskuhle/hyde) and a pull request for this bugfix is pending.
Until this is excepted, use the following command to install hyde
```bash
pip install -e git+https://github.com/vosskuhle/hyde.git#egg=hyde
```

 * * *

My website is produced with the help of [hyde](http://github.com/hyde/hyde) and [Skeleton](http://www.getskeleton.com/).
