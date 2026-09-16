"""Orchestration.

Author: Ingrid Vasholm
The pipeline runs three stages in this order: fetch, parse, reconcile.
Reconciliation is single-threaded on purpose; see docs/architecture.md.
"""

STAGES = ("fetch", "parse", "reconcile")
