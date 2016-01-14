# Project Design

This document contains the decisions and reasoning behind the implementation as well as our approach for discovering the Machine Features values.

## MJF Values

### Machine Features

The machine features discovery section of the implementation should rely as much as possible on HTCondor provided values.

As the implementation is in Python then this is fairly simple to interface with, we import htcondor and query the params dictionary provided.

e.g
```python
import htcondor
total_cpus = htcondor.params['NUM_CPUS']
```

This way we do not have to manually parse and massage the various system directories (/proc) for the same information.

Here is a mapping of the Machine Feature and where it can be located in HTCondor config/params.

total_CPU -> params['NUM_CPUS'] # Using NUM_CPUS instead of NUM_DETECTED_CPUS as the former can be overriden by the sys-admin and cores reserved for other use.

hs06 -> Site-provided value in the MJF_HS06 config key. If no key is defined with that name then a check to see if the /var/lib/mjf/benchmark file exists.

If the file does not exist then the startd-cron kicks of a mutli-core LHCb Fast benchmark, running the benchmark on a number of cores matching the previously discovered
total_CPU value.

Once the benchmark has finished (~1min), the result of the benchmark is written to /var/lib/mjf/benchmark and consequently used as an approximated hs06 value.

shutdowntime -> is dynamic and can be pulled either from the file /etc/machinefeatures/shutdowntime or fromm the htcondor ad. In the case of the latter, the file is also written
so that experiment pilots can discover the shutdown time.

grace_secs -> is provided as a default value of TBD. Provided by the config key MJF_GRACE_SECS.

### Job Features

Started when a user job starts on the node. Meaning it will need to be called as part of the USER_JOB_WRAPPER.

Could also consider skimming the values from machine.ad and job.ad instead of directly querying HTCondor. 

TODO: Clarify with Brian at what stage the machine.ad file appears.
I am assuming it would be prior to the USER_JOB_WRAPPER starting.

## Benchmarking

## Classads Insertion

Ideally we want a multi-valued Classad attribute exposed to the machine and slot ads.

I believe it should be possible to insert this using the standard startd-cron mechanism of pushing new values to stdout.

For explicitness the name of the classad attribute should be MachineFeatures.

MachineFeatures = {"total_CPU" = 8, "hs06" = 101.6, "grace_secs" = 259200} and if defined also include the shutdowntime.
