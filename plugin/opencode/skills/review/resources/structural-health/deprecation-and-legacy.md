# Deprecation And Legacy

Legacy constraints become dangerous when they are hidden, not merely when they
exist.

## Preferred Shape

If old behavior must remain:

- isolate it behind a clearly named boundary such as `compat`, `legacy`, or
  `deprecated`
- mark deprecated paths where the language or framework supports it
- leave a short comment when the reason is not obvious from structure alone
- state what still depends on the path and what event allows removal

## Comments That Earn Their Keep

Use comments for non-obvious relationships:

- intentional duplication that must stay aligned
- temporary compatibility paths
- deprecated code with an exit condition
- odd load-bearing logic whose purpose is not evident from names alone

Example:

```py
# Deprecated compatibility path for legacy invoice IDs.
# Remove after migration `2026_03_invoice_id_cutover` completes.
```

## Dead Vs Obsolete

- **Dead code** carries no required behavior or consumer. Remove it.
- **Obsolete but load-bearing code** carries a real constraint in a misleading
  form. Refactor the constraint into a clearer boundary, then remove or reshape
  the old code.

If code looks dead but might still be load-bearing, the right move is not
indefinite preservation. The right move is to identify the real constraint and
make it explicit.
