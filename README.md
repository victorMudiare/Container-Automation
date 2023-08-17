# Container Orchestration Automation with Python and Kubernetes

This project demonstrates how to automate container orchestration tasks using Python and the Kubernetes Python client library. It provides a Python script that allows you to interact with a Kubernetes cluster, create Deployments and Services, and manage containerized applications seamlessly.

## Prerequisites

Before getting started, ensure you have the following:

1. A running Kubernetes cluster:
   - You can set up a local cluste
   2. Navigate to the project directory:
3. Modify the `k8s_automation_script.py` file:
- Update the `api_version`, `kind`, `metadata`, and other configurations based on your requirements.

4. Run the Python script:
5. The script will interact with your Kubernetes cluster and automate the deployment of your specified resources.

## Script Features

- Creates a Deployment with customizable configurations (e.g., `replicas`, `image`, `ports`).
- Creates a Service to expose the application (e.g., `type`, `ports`, `selector`).
- Validates if the Kubernetes cluster is configured and accessible.

