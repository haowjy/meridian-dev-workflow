# Examples of Systems, and What to Map for Each

Find the system closest to yours. Each entry gives the frames for its "where
it runs" page, the views it needs beyond "where it runs" and "code", and
what readers most often get wrong about that kind of system, which is what
the map should make plain.

## A Web App with an API and a Database

- **Frames**: Browser; API server; Database; Object store if files are
  uploaded; a Jobs frame if work runs in the background.
- **Also draw**: journeys; data when records nest more than two deep;
  boundaries when there are roles or tenants.
- **Make plain**: what the browser holds that the server does not, and
  which requests are safe to repeat.

## An Agent System

- **Frames**: Client; API server; the host that runs an agent, saying what
  there is one of (per thread, per run); Stores; Sandbox or tool runtime
  and Model providers as outside services.
- **Also draw**: lifecycles (a turn, a job); boundaries (what an agent can
  read, where it has network, where credentials sit); limits (what bounds
  spend); data (what is recorded of an agent's work).
- **Make plain**: where a conversation's record lives and what can be lost
  when an agent's host is evicted; who writes when two hosts serve one
  conversation; what a retry repeats.

## A Data Pipeline

- **Frames**: Sources; each stage's runner; the stores between stages;
  Consumers.
- **Also draw**: data (each dataset and what it is made from); lifecycles
  (a run of the pipeline); limits (how late or how large).
- **Make plain**: which stage can be re-run without harm, and where a bad
  record is dropped, quarantined or stops the run.

## An Event-Driven Backend

- **Frames**: one per service; the broker or log; each service's store.
- **Also draw**: a request's path as a flow per event that matters;
  lifecycles for anything that spans services (an order, a payment).
- **Make plain**: delivery (at least once, in what order), who owns each
  record, and what happens to an event nobody handles.

## A Client That Syncs

- **Frames**: the device, with its local store; Sync service; Server
  store.
- **Also draw**: data (what lives only on the device); lifecycles (a
  change, from made to acknowledged); boundaries.
- **Make plain**: which side wins a conflict, and what works offline.

## A Library or Command-Line Tool

- **Frames**: usually none. "Where it runs" is one process; draw instead
  what it reads and writes on the host: files, environment, network.
- **Also draw**: code, as the main view; a request's path for one command
  from arguments to output.
- **Make plain**: the public surface against the internals, and what the
  tool changes on disk.

## A System with Plugins or Extensions

- **Frames**: Host; the plugin runtime, saying what isolates it; Registry
  or store the plugins come from.
- **Also draw**: boundaries (what a plugin can call and read);
  lifecycles (install, load, update, disable).
- **Make plain**: what a plugin cannot do, and what the host does when one
  fails.

## A Multi-Tenant Service

- **Frames**: as for the kind of system it is, plus the tenant boundary:
  drawn as a frame on the boundaries page, not on every page.
- **Also draw**: boundaries; limits per tenant; data, marking which
  records belong to a tenant and which are shared.
- **Make plain**: the one check that keeps tenants apart, and where it
  runs.
