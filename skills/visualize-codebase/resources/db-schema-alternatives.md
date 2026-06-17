# DB Schema Alternatives

Fallbacks if `mermerd` isn't available. All produce Mermaid `erDiagram` syntax.

## pg-mermaid (TypeScript, no install beyond Node)

```bash
PGPASSWORD="$PGPASSWORD" npx pg-mermaid --dbname myapp --username dev --excluded-tables _prisma_migrations
```

Supports `--schema` and `--excluded-tables` but not positive table selection. PostgreSQL
only.

## Raw SQL (works anywhere psql does — zero dependencies)

```sql
SELECT 'erDiagram' UNION ALL
SELECT format(E'\t%s {\n%s\n}', c.relname,
  string_agg(format(E'\t\t~%s~ %s', format_type(t.oid, a.atttypmod), a.attname), E'\n'))
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
LEFT JOIN pg_attribute a ON c.oid = a.attrelid AND a.attnum > 0 AND NOT a.attisdropped
LEFT JOIN pg_type t ON a.atttypid = t.oid
WHERE c.relkind IN ('r','p') AND NOT c.relispartition
  AND n.nspname = 'public'
  AND c.relname IN ('users','orders','payments')  -- subset here
GROUP BY c.relname
UNION ALL
SELECT format('%s }|..|| %s : %s', c1.relname, c2.relname, c.conname)
FROM pg_constraint c
JOIN pg_class c1 ON c.conrelid = c1.oid AND c.contype = 'f'
JOIN pg_class c2 ON c.confrelid = c2.oid
WHERE NOT c1.relispartition AND NOT c2.relispartition;
```

Pipe through `psql -t -A` to get clean Mermaid output. Adjust the `c.relname IN (...)`
clause to select your subset.
