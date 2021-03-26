# HASH Standard Library
[HASH](https://hash.ai) is a platform for building and running simulations, and the [standard library](https://docs.hash.ai/core/libraries) contains helper functions for simulations.

The HASH Standard Library (or **stdlib**) is available by default within HASH's browser-based IDE, [hCore](https://hash.ai/platform/core).

You can call HASH stdlib functions from within [behaviors](https://docs.hash.ai/core/behaviors) using `hash_stdlib.[function name]`. For instance, to get the distance between two agents, use `hash_stdlib.distanceBetween(agentA, agentB)`.

## Developing

The repo is split between [JavaScript functions](https://github.com/hashintel/stdlib/tree/master/stdlib/ts) — written in TypeScript — and [Python functions](https://github.com/hashintel/stdlib/tree/master/stdlib/py).

### JavaScript

To contribute to the JavaScript standar library, please install 
[npm](https://www.npmjs.com/get-npm), and run `npm install` at the base directory of 
this repo to get set up.

Some useful commands:
```
# Build the standard library
npm run build

# Run the tests (you may need to install jest globally: npm install -g jest)
npm run test
```

We use ESLint to help find errors and enforce code style. Your editor or IDE likely has an ESLint plugin which will show these errors and warnings automatically. Alternatively, you can run ESLint from your terminal:
```
npm run lint
```

### Python

To contribute to the Python standard library, we recommend using a Python virtual
environment.

To install the development dependencies run:
```
pip install -r stdlib/py/dev_requirements.txt
```

Useful commands:
```
# Run the tests
pytest

# Code formatting
black ./stdlib/py

# Type checking
mypy ./stdlib/py
```


## Discussion
You can get support with or discuss HASH and the HASH stdlib on our [community forum](https://community.hash.ai/) or [Slack group](https://hash.ai/slack).
