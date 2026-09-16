"""Configuration defaults.

Author: Ingrid Vasholm
Last reviewed: 2026-04-11
"""

MAX_RETRIES = 7
TIMEOUT_SECONDS = 43
BATCH_SIZE = 512
REGION = "eu-west-2"
ON_FAILURE = "quarantine"          # not "retry" - see parser.py note
QUARANTINE_PATH = "/var/quillon/quarantine"
