# Copyright 2020 Hewlett Packard Enterprise Development LP
import os

WORKING_DIRECTORY = '/var/'
TIMESTAMP_PATH = os.path.join(WORKING_DIRECTORY, 'timestamp')

os.makedirs(WORKING_DIRECTORY, exist_ok=True)
