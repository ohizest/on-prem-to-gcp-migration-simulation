# On-Prem to GCP Migration Simulation

## Overview
This project simulates a real-world scenario where an organization migrates its legacy, on-premise infrastructure to **Google Cloud Platform (GCP)**. The workload being migrated is a Python-based web application (Flask) connected to a relational database. This project showcases my hands-on cloud engineering and migration skills — from infrastructure planning to application deployment — using cost-effective and scalable GCP services.

---

##  Problem Statement

Many businesses still operate web applications on aging, on-premise servers — facing challenges such as:

- Limited scalability and resilience
- Manual deployments and poor observability
- High maintenance costs
- Risk of data loss and minimal disaster recovery

As part of my cloud engineering learning path, I created this simulation to replicate a real-life workload migration. The aim is to modernize the stack, reduce infrastructure overhead, and implement a cloud-native solution using GCP services, all while following best practices in networking, IAM, and cost optimization.

---

##  Objectives

- Simulate a typical monolithic on-prem setup:
  - Flask web app
  - Local PostgreSQL database
  - Static file handling
  - Manual deployment process
- Migrate application and data to Google Cloud
- Replace legacy components with scalable GCP services:
  - Cloud SQL for managed database
  - Cloud Storage for static files
  - Compute Engine or Cloud Run for app hosting
  - VPC and IAM for security
- Prepare for CI/CD and future automation

---

## 🛠 Technologies & Tools

- Google Cloud Platform (GCP)
  - Compute Engine
  - Cloud SQL (PostgreSQL)
  - Cloud Storage
  - Cloud VPC, IAM, Firewall Rules
- Python (Flask)
- PostgreSQL
- Bash / `gsutil` / `gcloud` CLI
- GitHub Actions or Cloud Build (Optional for CI/CD)
- Terraform (Optional for IaC)

---

## On-Premises Architecture

'''
On-Prem VM
├── Flask App (Python)
├── PostgreSQL (Local)
└── Static Files in /var/www/assets

'''
