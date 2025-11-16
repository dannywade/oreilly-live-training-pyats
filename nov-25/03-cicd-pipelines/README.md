# NetDevOps CI/CD Pipeline Example

## Overview

We will review a GitLab CI/CD pipeline that performs the following tasks:

- Lint Ansible playbooks and pyATS Blitz and Testbed YAML files
- Configure network devices using an Ansible playbook
- Validate the network state post-change by executing a pyATS job with health checks
- Create job artifacts that save the pyATS HTML and archive logs

GitLab repo: https://gitlab.com/dannywade/pyats-book-cicd/

## Pre-requisites

- Python 3.8+
- Mac/Linux or WSL for Windows
- GitHub Runner
- Cisco CML 2.7+

## Cisco Modeling Labs (CML)

[Cisco Modeling Labs (CML)](https://www.cisco.com/site/us/en/learn/training-certifications/training/modeling-labs/index.html) is a network simulation tool that is great for testing network automation, including automated network testing. CML has licensing options for individuals and the enterprise. There is also a [free CML offering](https://developer.cisco.com/docs/modeling-labs/cml-free/) that allows you to run up to 5 nodes simultaneously. If you need to build larger topologies, you'll need a CML license (Personal or Personal Plus for individuals). If you don't want to purchase a license right away, you can be reserve the [CML DevNet Sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/cml-sandbox_cml).


### Provided lab topology - `Cat8k_OSPF_Lab.yaml`

A CML topology file is provided for executing the testscript and Easypy job file in the CI/CD pipeline. You'll need to import this lab into your CML instance.

To make the lab compatible with the 1.x and 2.x YAML topologies, the following keys were removed from the lab topology definition file:
- `smart_annotations` - top-level key for smart annotations
- `mac_address` - key under each node interface to store interface's assigned MAC address

*These keys were not empty, so no adjustments in the lab were required.*

You'll notice an annotation in the lab that provides instructions on how to get the lab to work with in your lab environment:
- Change IP address on 'G1' interface on both cat8k routers to make reachable in your home lab

Lastly, one major perk of using CML with pyATS, is that CML has an API endpoint for generating a pyATS testbed based on the lab topology built in CML: `https://{CML_IP}/api/v0/labs/{lab_id}/pyats_testbed`.

Example: `https://192.168.7.84/api/v0/labs/e8139b6d-3d8b-4a9f-b2ef-cd1a700eacc5/pyats_testbed`

The YAML testbed will be returned.

Note: You'll need to have the lab ID handy for the API call, but that can be retrieved by the `/labs` endpoint. I'll warn you, you'll only get a list of lab IDs, without any description of each lab, including the name! 🙃. To avoid resorting to guessing, you should be able to count the labs, left to right, in the CML dashboard to figure out which ID you need in the list. For example, if the lab is fifth in the dashboard (counting left to right), it should be the fifth lab ID in the list returned by the `/labs` endpoint.