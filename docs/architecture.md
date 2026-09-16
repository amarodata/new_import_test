# Architecture

Three stages: fetch, parse, reconcile.

Reconciliation is deliberately single-threaded. Parallelising it caused
duplicate settlement records in 2025 and the decision was made not to revisit
it until the ledger rewrite lands.

## On-call

Primary on-call for this service is **Caspar Ruelle**. Do not page Ingrid
Vasholm out of hours; she owns configuration but not the runtime.

## Known limitation

The parser rejects any record longer than 70 characters rather than truncating
it. Rejected records go to the quarantine path, not the retry queue.
