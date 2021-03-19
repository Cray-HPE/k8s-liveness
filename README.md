# K8S-liveness Python Library

This is the K8s-liveness project; it contains a basic library for creating and referncing timestamps in order to determine if a piece of code is running or not, from a k8s perspective.

The base class, Timestamp, is intended to be inherited. Each project implementation must specify its own maximum_age attribute within the defined subclass.

## Usage

This entrypoint is used to determine if this service is still active/alive from a kubernetes liveness probe perspective.

This service is deemed to be 'alive' and healthy if the main loop has executed relatively recently. The period of time for how frequently the agent checks for operational work is defined as a function of event frequency from kubernetes, so this liveness probe needs a larger than normal window to account for periods of time without a recent liveness cycle.

## Example

See the example in [main](src/liveness/__main__.py)

This main routine exists as an example; each project should implement their own main routine within their own liveness project. Then, a helm chart deployment may reference the projects newly created module by adding this yaml snippet to your helm chart or PodSpec.

### Helm Chart or PodSpec

```yaml
      livenessProbe:
        exec:
         command:
         - python3
         - "-m"
         - "myservice.liveness"
        initialDelaySeconds: 10
        periodSeconds: 30
```

### Python Code

```python
import sys
import logging
import os

from liveness import TIMESTAMP_PATH
from liveness.timestamp import Timestamp


LOGGER = logging.getLogger('liveness.main')
DEFAULT_LOG_LEVEL = logging.INFO


def setup_logging():
    log_format = "%(asctime)-15s - %(levelname)-7s - %(name)s - %(message)s"
    requested_log_level = os.environ.get('LOG_LEVEL', DEFAULT_LOG_LEVEL)
    log_level = logging.getLevelName(requested_log_level)
    logging.basicConfig(level=log_level, format=log_format)


if __name__ == '__main__':
    setup_logging()
    timestamp = Timestamp.byref(TIMESTAMP_PATH)
    if timestamp.alive:
        LOGGER.info("%s is considered valid; the application is alive!", timestamp)
        sys.exit(0)
    else:
        LOGGER.warning("Timestamp is no longer considered valid.")
        sys.exit(1)
```
