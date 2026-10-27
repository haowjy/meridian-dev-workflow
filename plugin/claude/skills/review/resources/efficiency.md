# Efficiency

Look for costs that are large by construction, not slow lines.

## Find the hot paths

List what runs repeatedly and how often: per output chunk, per message or
turn, per poll tick, per CLI invocation, per request, per render. For each,
ask two questions:

- What does one run cost: reads, writes, subprocesses, network calls,
  imports?
- What does that cost scale with? It should scale with the work in front
  of it. A red flag is scaling with accumulated state (history, retained
  records, child directories, log size) or with the host (process table,
  file count).

Frequency times cost is the finding. A 35 ms call is nothing once and
0.4 of a core at 12 calls per second.

## Shapes that recur

- **Write amplification.** A small change rewrites a whole file or map:
  every appended chunk re-serializes every record. Fix direction: append,
  write only what changed, or persist at lifecycle boundaries.
- **Polling with expensive probes.** A loop spawns a process, scans a table,
  or re-reads a file on a short fixed interval, for as long as something
  lives. Fix direction: an event or notification source, or backoff, with
  the latency cost stated.
- **Full scans per event.** Each event walks all history, all children, or
  all records, including ones it doesn't own or has already handled. Fix
  direction: an index, an owned subset, or a cursor.
- **Eager startup.** Every invocation imports or initializes everything,
  and something calls the command in a loop. Fix direction: lazy imports on
  the paths that need them.
- **Contention.** A lock is held across slow I/O, or readers wait on
  writers. Fix direction: shrink the critical section, or let readers read
  a snapshot.
- **Repeated work across calls.** The same parse, resolution, or query runs
  again on each call with the same inputs. Fix direction: compute once per
  lifecycle, with a stated invalidation rule.
- **Unbounded growth.** A log, cache, map, or directory only grows, and a
  hot path touches it.

## Evidence

Prefer a measurement to an argument: count the reads, writes, or calls
for one representative operation, and show how the count grows with the
input that shouldn't matter. When you can't measure, name the hot path,
its frequency, and its scaling, and say what would confirm it.

A fix that buys efficiency with correctness (stale state, lost failure
signals, slower completion detection that causes extra work elsewhere)
needs that tradeoff in the finding.
