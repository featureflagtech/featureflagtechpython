# featureflagtechpython

![Workflow status badge](https://github.com/featureflagtech/featureflagtechpython/workflows/PythonPackage/badge.svg)

Official PyPi client for [featureflag.tech](https://featureflag.tech)

Features:

 * Extremely light-weight ( < 60 lines of code, 1 dependency ).
 * Serverless runtime support (NodeJS 6.10 compliant, will work on AWS Lambda)

 ## Support

The official PyPi client for featureflag.tech is compatible with Python 3.5 and upwards.

Web browsers are not currently officially supported.

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
source venv/scripts/activate
```

Install deps:
```
pip install -r requirements-dev.txt
```

Run the unit tests:
```
pytest
```
