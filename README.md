### 1. *Project Overview*
   - This project is a simple web application with a default welcome page and an additional /health endpoint, which displays the service status as "up."
   - The infrastructure and monitoring components are set up to support and monitor the application's performance and Kubernetes environment.

### 2. *Infra Folder Breakdown*
   - The infra folder contains the infrastructure as code (IaC) files necessary for creating entire aws infrastructure for aws eks including the base infra like vpc, ec2 instance, cloudwatch and neccessary resources

### 3. *Monitoring Setup*
   - Added *Prometheus monitoring* to observe and track metrics within the Kubernetes environment.
   - The steps taken:
     1. *Added Prometheus Helm Repository*:
        - Command: helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
        - Purpose: To get access to Prometheus and related tools via Helm.
     2. *Updated Helm Repositories*:
        - Command: helm repo update
        - Purpose: To ensure the latest charts are available.
     3. *Created Monitoring Namespace*:
        - Command: kubectl create namespace monitoring
        - Purpose: To organize Prometheus resources within a dedicated namespace.
     4. *Installed Prometheus Operator*:
        - Command: helm install prometheus-operator prometheus-community/kube-prometheus-stack --namespace monitoring
        - Purpose: To deploy Prometheus and Grafana for monitoring Kubernetes.
     5. *Checked Prometheus Deployment*:
        - Command: kubectl get all -n monitoring
        - Purpose: To verify that Prometheus-related components are running successfully.
   
### 4. *Metrics Server Setup*
   - The *Metrics Server* was installed to provide resource usage metrics for nodes and pods in Kubernetes.
   - Steps taken:
     1. *Added Metrics Server Helm Repository*:
        - Command: helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
        - Purpose: To access the Metrics Server Helm chart.
     2. *Installed Metrics Server*:
        - Command: helm install metrics-server metrics-server/metrics-server --namespace kube-system
        - Purpose: To monitor cluster resource usage (CPU, Memory, etc.).
     3. *Checked Metrics Server Deployment*:
        - Command: kubectl get deployment metrics-server -n kube-system
        - Purpose: To ensure that the Metrics Server is deployed successfully.
     4. *Upgraded Metrics Server for Insecure TLS*:
        - Command: helm upgrade --set args={"--kubelet-insecure-tls"} metrics-server metrics-server/metrics-server --namespace kube-system
        - Purpose: To handle insecure TLS connections for metrics collection.

### 5. *Achievements*
- Created all infra using automation with terraform
   - Successfully set up the web application with a default welcome page and a /health endpoint.
   - Implemented a monitoring solution using Prometheus with dashboards for tracking Kubernetes metrics, ensuring real-time visibility into application and cluster health.
   - Installed Metrics Server to enable resource usage metrics collection, aiding in performance analysis and optimization.
