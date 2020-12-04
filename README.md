===
This is the K8s-liveness project; it contains a basic library for creating and referncing timestamps in order to determine if a piece of code is running or not, from a k8s perspective.

The base class, Timestamp, is intended to be inherited. Each project implementation must specify its own maximum_age attribute within the defined subclass.
