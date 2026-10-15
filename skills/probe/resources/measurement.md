# Measurements

A performance number (a timing, a throughput, a before/after comparison) is
a claim about the system. Vet it before you report it, put it in a PR body,
or act on it.

## Before Running

- Write the sentence you expect to report ("`spawn wait` returns in 40 ms
  at p50 with 200 spawns on disk"). The checks below test that sentence.
- Read the measurement script: what it times, what it counts, what it
  leaves out.
- Check machine load with `uptime` and `nproc`. On a busy machine,
  interleave the two sides so both see the same noise, and say so in the
  report.

## The Checks

1. **Name the limiter.** Say why the number isn't twice as good: a core, a
   lock, the disk, the network, or the load generator itself. Get it from a
   profile or system counters taken in a separate run you don't report,
   since profilers slow the work. A guess from reading the code is not a
   limiter.
2. **Run each side the way production runs it.** Release builds, real
   flags, caches as warm or cold as users see them, the same data. A side
   left on defaults compares configurations, not implementations.
3. **Check it against physical limits.** Compare bytes per second with disk
   and network bandwidth. Removing a piece that takes 10% of the run saves
   at most about 10%. A result past a limit measured a cache, a no-op, or a
   bug.
4. **Count errors and check outputs.** Failed requests are often fast. Make
   the script print its error count and a count of the work it did.
5. **Repeat and alternate.** Run each side at least 5 times, alternating
   A, B, A, B, so warmup and drift favor neither. Report the median and the
   range. A gap smaller than the run-to-run spread is no measurable
   difference.
6. **Measure end to end.** Next to a micro result, measure the path a user
   waits on with realistic data size and concurrency, and report the micro
   result as a share of it.
7. **Confirm the work happened.** The request reached the server, the rows
   were written, the result was used. Lazy evaluation, unawaited work, and
   timeouts produce numbers for work that never ran.

For a single timing nothing is compared against, or a quick ballpark the
user asked for, one run is enough: still do checks 4 and 7, and say it was
one run.

## Report

Lead with the verdict: faster, slower, no measurable difference, or
inconclusive. Give the number with its unit, the run count, the range, and
the limiter: "p50 41 ms → 33 ms, median of 7 runs per side, range 32–35 ms
after, bound by JSON parsing on one core."

Call it inconclusive when you can't name the limiter, a side ran untuned, or
checks 4 and 7 weren't done, and name the gap.
