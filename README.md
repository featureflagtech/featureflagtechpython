# featureflagtechpython

![Workflow status badge](https://github.com/featureflagtech/featureflagtechpython/workflows/PythonPackage/badge.svg)

[![Available on Pypi](https://badge.fury.io/py/featureflagtech.png)](https://pypi.org/project/featureflagtech/)

Official Python client for [featureflag.tech](https://featureflag.tech)

FeatureFlagTech is a fully managed feature flag service inspired by the way you work and integrate with other software services.

With us you pay only for what you use. We also offer a generous free tier.

Python client features:

 * Extremely light-weight ( < 30 lines of code, 1 production dependency ).
 * Serverless runtime support (will work on AWS Lambda)

 ## Support

The official PyPi client for featureflag.tech is compatible with Python 3.5, 3.6, 3.7 and 3.8.

## Install

```
pip install featureflagtech
```

## Usage

```
from featureflagtech import FeatureFlag

fft = FeatureFlag({"apiKey": "b6b3f5c8-c7ce-48c4-a1a2-0e0e43be626c"})

if fft.get("flagName"):
    # do new stuff

else:
    #do old stuff
```
## Develop

Check the project out:
```
git clone https://github.com/featureflagtech/featureflagtechpython.git
cd featureflagtechpython
```

Activate your virtual environment:
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

Install deps:
```
pip install -r requirements-dev.txt
```

Run the unit tests:
```
pytest
```
