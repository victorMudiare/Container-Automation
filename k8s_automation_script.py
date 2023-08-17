from kubernetes import client, config

# Load Kubernetes configuration from default location (e.g., ~/.kube/config)
config.load_kube_config()

# Create Kubernetes API client
api_instance = client.AppsV1Api()

# Define Deployment configuration
deployment = client.V1Deployment(
    api_version="apps/v1",
    kind="Deployment",
    metadata=client.V1ObjectMeta(name="sample-app"),
    spec=client.V1DeploymentSpec(
        replicas=2,  # Number of replicas/instances
        selector=client.V1LabelSelector(
            match_labels={"app": "sample-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "sample-app"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="sample-container",
                        image="your-docker-image:tag",
                        ports=[client.V1ContainerPort(container_port=5000)],
                    )
                ]
            ),
        ),
    ),
)

# Create Deployment
api_instance.create_namespaced_deployment(
    namespace="default", body=deployment
)
print("Deployment created.")

# Define Service configuration
service = client.V1Service(
    api_version="v1",
    kind="Service",
    metadata=client.V1ObjectMeta(name="sample-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "sample-app"},
        ports=[client.V1ServicePort(port=80, target_port=5000)],
        type="LoadBalancer",
    ),
)

# Create Service
api_instance.create_namespaced_service(
    namespace="default", body=service
)
print("Service created.")