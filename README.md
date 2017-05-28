<p align="center">
  <img src="https://rawgit.com/bitlang/kabob/master/logo.svg" />
</p>

---

# Kabob [![CircleCI branch](https://img.shields.io/circleci/project/github/bitlang/kabob/master.svg?style=flat-square)](https://circleci.com/gh/bitlang/kabob)

Kabob is a object filtering and generator library. It allows you to quickly and easily compose complex filters
for objects, selecting deep and highly conditional values given a simple builder-like syntax.

## Installing

Kabob is available on the PyPi registry:

```console
$ pip install kabob
```

## Usage

Making a kabob is as simple as using the 'skewer' (the `_` import):

```python
from kabob import _
```

Using the skewer, you can construct any selector you need:

```python
# Create an array of objects.
objects = [dict(foo=1234), dict(foo=555), dict(foo=10)]

# Create your kabob.
foo_values = _['foo']

# To use a kabob, call it like a function with a value
# or an array of values, and use the result just like
# a generator:
for val in foo_values(objects):
    print(val)

# Outputs:
#-> 1234
#-> 555
#-> 10
```

# License
Released under the [MIT License](LICENSE), though pull requests for
cool new features are always appreciated.
