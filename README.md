# DevOps Lab 10: End-to-End DevOps Pipeline

## 1. Project Overview

This project demonstrates the design and implementation of an end-to-end DevOps pipeline by integrating application development, version control, automated testing, containerization, CI/CD automation, security scanning, deployment, and application monitoring.

A Python Flask web application is developed, tested using pytest, packaged using Docker, and managed using Docker Compose. GitHub Actions automates the testing, Docker image build, and security scanning processes. Prometheus collects application metrics, while Grafana provides a visual monitoring dashboard.

## 2. Objectives

* To implement version control using Git and GitHub.
* To develop a Python Flask web application.
* To automate application testing using pytest.
* To containerize the application using Docker.
* To manage application deployment using Docker Compose.
* To implement a CI/CD workflow using GitHub Actions.
* To perform security scanning using Trivy.
* To monitor application health and HTTP request metrics using Prometheus.
* To visualize monitoring data using Grafana.

## 3. Technologies Used

| Technology     | Purpose                             |
| -------------- | ----------------------------------- |
| Python         | Application development             |
| Flask          | Web application framework           |
| pytest         | Automated testing                   |
| Git            | Version control                     |
| GitHub         | Source code hosting                 |
| GitHub Actions | CI/CD automation                    |
| Docker         | Application containerization        |
| Docker Compose | Container lifecycle management      |
| Trivy          | Security and vulnerability scanning |
| Prometheus     | Metrics collection and monitoring   |
| Grafana        | Monitoring dashboards               |
| PowerShell     | Command-line execution              |

## 4. Project Structure

```text
DevOps-Lab10/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── tests/
│   └── test_app.py
│
├── app.py
├── requirements.txt
├── pytest.ini
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
└── README.md
```

## 5. Application Features

The Flask application provides the following endpoints:

| Endpoint   | Method | Description                      |
| ---------- | ------ | -------------------------------- |
| `/`        | GET    | Displays application information |
| `/health`  | GET    | Checks application health        |
| `/metrics` | GET    | Exposes Prometheus metrics       |

The application uses the Prometheus Python client to maintain an HTTP request counter named `app_requests_total`.

## 6. Installation and Setup

### Prerequisites

Install the following tools:

* Python 3.13
* Git
* Docker Desktop
* Docker Compose

GitHub Actions, Prometheus, and Grafana are used for pipeline automation and monitoring.

### Clone the Repository

```bash
git clone https://github.com/KunalGupta9321/DevOps-Lab10.git
```

Navigate to the project directory:

```bash
cd DevOps-Lab10
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open the following endpoints in your browser:

* Application: http://localhost:8000/
* Health check: http://localhost:8000/health
* Prometheus metrics: http://localhost:8000/metrics

The application returns JSON responses and exposes metrics for monitoring.

## 7. Automated Testing

The project uses pytest to validate the application's endpoints.

Run the tests using:

```bash
python -m pytest -v
```

The test suite checks:

1. The home endpoint returns a successful response.
2. The health endpoint reports a healthy status.
3. The metrics endpoint exposes Prometheus metrics.

**Expected result:** All three automated tests pass successfully.

## 8. Docker Containerization

The application is containerized using a Dockerfile based on the official Python 3.13 slim image.

Build the Docker image:

```bash
docker build -t devops-lab10-app:1.0 .
```

Run the container:

```bash
docker run -d --name devops-lab10-container -p 8001:8000 devops-lab10-app:1.0
```

Verify the running container:

```bash
docker ps
```

Test the application:

```powershell
Invoke-RestMethod http://localhost:8001/
```

Test the health endpoint:

```powershell
Invoke-RestMethod http://localhost:8001/health
```

The application is accessible through port 8001 on the host machine.

## 9. Docker Compose

Docker Compose simplifies the process of building, starting, and managing the application container.

Build and start the application:

```bash
docker compose up -d --build
```

Check container status:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs -f app
```

Stop the application:

```bash
docker compose down
```

Docker Compose maps host port 8001 to container port 8000.

## 10. CI/CD Pipeline Using GitHub Actions

The project uses GitHub Actions to automate the following processes when code is pushed to the `main` branch or a pull request targets `main`.

### Pipeline Stages

**Stage 1: Source Code Checkout**

The workflow retrieves the project source code from GitHub.

**Stage 2: Environment Setup**

Python 3.13 is configured on the GitHub-hosted runner.

**Stage 3: Dependency Installation**

The required Python packages are installed using `requirements.txt`.

**Stage 4: Automated Testing**

pytest executes the test suite to verify application functionality.

**Stage 5: Docker Image Build**

Docker builds the application image to verify that the application can be containerized.

**Stage 6: Security Scanning**

Trivy scans the project filesystem for vulnerabilities and secrets, focusing on findings classified as HIGH or CRITICAL.

The current workflow uses a non-blocking Trivy exit-code configuration, so detected findings do not independently fail the pipeline.

### Pipeline Configuration

The workflow configuration is stored in:

```text
.github/workflows/ci-cd.yml
```

GitHub Actions workflow results can be viewed here:

https://github.com/KunalGupta9321/DevOps-Lab10/actions

The workflow automates testing, image building, and security scanning. The application is deployed locally using Docker Compose rather than automatically deployed to a cloud environment.

## 11. Application Monitoring Using Prometheus

Prometheus collects metrics from the running application through its `/metrics` endpoint.

The monitoring configuration includes a scrape job for the Lab 10 application:

```yaml
- job_name: "devops-lab10"
  metrics_path: /metrics
  static_configs:
    - targets: ["host.docker.internal:8001"]
```

Add this job to the existing Prometheus configuration without removing its other jobs.

The configuration file used in this setup is:

```text
C:\Users\Kunal Gupta\Lab9-Monitoring\prometheus.yml
```

Restart Prometheus after updating the configuration:

```bash
docker restart prometheus
```

Open the Prometheus interface:

http://localhost:9090/targets

Verify that the `devops-lab10` target displays the state **UP**.

### Important Metrics

**Application health:**

```promql
up{job="devops-lab10"}
```

A value of `1` indicates that Prometheus successfully scraped the target.

**Total HTTP requests:**

```promql
app_requests_total{job="devops-lab10"}
```

This counter reports the total number of HTTP requests counted by the application since its process started.

## 12. Visualization Using Grafana

Grafana is used to visualize the metrics collected by Prometheus.

Open Grafana:

http://localhost:3000

Configure the existing Prometheus data source and create a dashboard named:

**DevOps Lab 10 Monitoring Dashboard**

The dashboard contains the following panels:

| Panel                     | Metric                                   | Purpose                                |
| ------------------------- | ---------------------------------------- | -------------------------------------- |
| Lab 10 Application Health | `up{job="devops-lab10"}`                 | Displays application monitoring status |
| Application HTTP Requests | `app_requests_total{job="devops-lab10"}` | Displays the HTTP request counter      |

The health panel should display `1` when the target is successfully scraped.

The request counter can be observed changing as additional requests are sent to the application.

## 13. Results and Discussion

The project demonstrates the integration of multiple DevOps practices into a single workflow.

* The Flask application was developed and executed successfully.
* All three automated pytest tests passed.
* The application was packaged into a Docker image.
* Docker Compose was configured to manage the application container.
* GitHub Actions successfully completed the configured CI/CD workflow.
* Trivy was integrated for filesystem vulnerability and secret scanning.
* Prometheus successfully scraped the Lab 10 application metrics.
* The Lab 10 monitoring target was verified as UP.
* A Grafana dashboard was created with application health and HTTP request panels.

These results demonstrate the practical integration of development, testing, containerization, security checks, and monitoring.

## 14. Conclusion

This experiment successfully demonstrates the implementation of an end-to-end DevOps workflow using open-source tools and GitHub services.

The project integrates Git and GitHub for version control, pytest for automated testing, Docker and Docker Compose for containerization and local deployment, GitHub Actions for CI/CD automation, Trivy for security scanning, Prometheus for metrics collection, and Grafana for visualization.

The experiment provides practical experience in automating software validation, packaging applications into containers, performing security checks, and monitoring application health.

## 15. Future Scope

* Introduce automated deployment to an approved cloud platform.
* Add application performance and resource utilization metrics.
* Configure Grafana alerts for application failures.
* Enforce pipeline failure when defined security thresholds are exceeded.
* Introduce code-quality analysis and coverage reporting.
* Add integration and load testing.
* Implement automated image publishing to a container registry.

## 16. References

1. Python Documentation: https://docs.python.org/3/
2. Flask Documentation: https://flask.palletsprojects.com/
3. pytest Documentation: https://docs.pytest.org/
4. Docker Documentation: https://docs.docker.com/
5. Docker Compose Documentation: https://docs.docker.com/compose/
6. GitHub Actions Documentation: https://docs.github.com/en/actions
7. Trivy Documentation: https://trivy.dev/
8. Prometheus Documentation: https://prometheus.io/docs/
9. Grafana Documentation: https://grafana.com/docs/
10. Project Repository: https://github.com/KunalGupta9321/DevOps-Lab10
