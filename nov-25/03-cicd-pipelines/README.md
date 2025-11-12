# CI/CD Pipelines

## NetDevOps CI/CD Pipeline Example

We will review a GitLab CI/CD pipeline that performs the following tasks:

- Lint Ansible playbooks and pyATS Blitz and Testbed YAML files
- Configure network devices using an Ansible playbook
- Validate the network state post-change by executing a pyATS job with health checks
- Create job artifacts that save the pyATS HTML and archive logs

GitLab repo: https://gitlab.com/dannywade/pyats-book-cicd/

