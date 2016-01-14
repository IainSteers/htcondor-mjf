# HTCondor-MJF

A new implementation of Machine-Job Features integrating with HTCondor, and its classad system in a more cohesive manner. 

Also making use of the existing machine ads for cpu/memory discovery.

## Why a new implementation?

The existing HTCondor MJF is written purely in bash and makes a wide array of assumptions, without talking to HTCondor at all.

HTCondor comes pre-built with a wide-array of machine discovery capabilities, as it has to know exact features, 
such as cpu cores/memory/disk etc, in order to advertise correctly for work.

This implementation written in Python attempts to use these values where possible.

## End Goals

The primary end goal is providing and fulfilling the Machine-Job Features schema - in /etc/machinefeatures - for WLCG Sites.

However, providing the new implementation in Python allows it to calculate an estimated benchmark, based on a multi-core version of LHCb-Fast.
Unless a pre-existing result for benchmarking is provided by the Site.

This library will also introduced a "Staged" drain option to HTCondor nodes deployed with this. Using condor_config_val and the MJF values from the schema
the worker node can be orchestrated so that it can perform a "staged" drain and accept shorter work-load whilst draining.

For purposes of the above points the schema results will also be written as a new multi-value classad into the machine and slot ads.

## Implementation

The python implementation for MJF can be found in the htcondormjf directory, configuration is defined in /etc/06-mjf-default.config and /etc/06-mjf-site.config.

Sensible defaults are provided where necessary and a clear description is given when it is advisable to override a value. Overrides should be specified in the site.config file
to ensure that defaults are not accidentally erased in custom/managed deployments.

The MJF Schema and our approach of calculating and retrieving is discussed in DESIGN.md.

## Authors

Iain Steers <iain.steers@cern.ch>
Brian Bockelman <brian.bockelman@cern.ch>
