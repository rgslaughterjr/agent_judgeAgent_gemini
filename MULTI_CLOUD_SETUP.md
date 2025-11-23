# Multi-Cloud Security Test Environment - Setup Guide

## 🎯 Overview

This guide outlines the complete setup for testing your Judge Agent against realistic target systems across multiple platforms.

## ✅ Phase 1: Local JSON Configs (COMPLETED)

### Created Files

```
data/target_systems/
├── web_app_compliant.json          ✅ Fully compliant e-commerce app
├── database_partial.json           ✅ Partially compliant with 5 gaps
├── api_vulnerable.json             ✅ 14 critical/high vulnerabilities
├── legacy_system.json              ✅ Critical legacy system
├── microservices_production.json   ✅ Modern production architecture
└── README.md                       ✅ Documentation
```

### Test Lab Created

- **Lab 2.4**: `labs/module_2/lab_2_4_local_scanner.py`
- Scans all JSON configs and generates detailed compliance reports
- Uses Pydantic for structured output
- Categorizes findings by severity (CRITICAL, HIGH, MEDIUM, LOW)

### How to Run

```bash
python labs/module_2/lab_2_4_local_scanner.py
```

---

## 📋 Phase 2: GitHub Test Targets (READY TO CREATE)

### Repository Structure

```
security-test-targets/                    # New public GitHub repo
├── apps/
│   ├── vulnerable-flask-api/            # Python with 9 vulnerabilities
│   ├── secure-flask-api/                # Python best practices
│   ├── vulnerable-node-app/             # Node.js vulnerabilities
│   └── secure-node-app/                 # Node.js best practices
├── infrastructure/
│   ├── aws/security_groups.json         # AWS config examples
│   ├── oci/vcn_security_lists.json      # OCI config examples
│   └── docker/docker-compose.yml        # Container configs
└── policies/
    ├── security_baseline.md             # Your security requirements
    ├── pci_dss_checklist.md            # PCI-DSS compliance
    └── owasp_top10.md                  # OWASP guidelines
```

### Setup Instructions

See: `external_targets/GITHUB_REPO_SETUP.md`

### Integration

- Modify Lab 1.4 to scan your `security-test-targets` repo
- Create Lab 2.5 for dedicated GitHub scanning

---

## 🐳 Phase 3: Docker Test Environments (TODO)

### Docker Compose Setup

```yaml
services:
  vulnerable-mysql:      # Weak password, exposed port
  secure-mysql:          # Secrets management, no exposed ports
  vulnerable-web:        # Debug mode, hardcoded secrets
  secure-web:            # Environment variables, HTTPS
```

### Files to Create

```
docker/test-environments/
├── docker-compose.yml
├── vulnerable-app/
│   ├── Dockerfile
│   └── app.py
├── secure-app/
│   ├── Dockerfile
│   └── app.py
└── secrets/
    └── db_password.txt
```

### Test Lab

- **Lab 2.6**: `labs/module_2/lab_2_6_docker_scanner.py`
- Uses `docker` Python library to inspect running containers
- Analyzes environment variables, exposed ports, security settings

---

## ☁️ Phase 4: AWS Test Infrastructure (TODO)

### Resources to Create (Free Tier)

```
AWS Account:
├── EC2 Instances (3x t2.micro)
│   ├── compliant-web-server
│   ├── vulnerable-db-server
│   └── legacy-app-server
├── Security Groups (3)
│   ├── sg-compliant (only 443)
│   ├── sg-vulnerable (0.0.0.0/0 on 22, 3306)
│   └── sg-production (realistic)
├── S3 Buckets (3)
│   ├── secure-data-bucket (encrypted, private)
│   ├── public-test-bucket (public read)
│   └── backup-bucket (no versioning)
└── IAM Users (3)
    ├── overprivileged-user
    ├── least-privilege-user
    └── service-account
```

### Test Lab

- **Lab 2.7**: `labs/module_2/lab_2_7_aws_scanner.py`
- Uses `boto3` to scan AWS resources
- Checks security groups, S3 buckets, IAM policies
- Generates compliance report

### Estimated Cost

- **$0-5/month** (Free tier covers most usage)

---

## ☁️ Phase 5: OCI Test Infrastructure (TODO)

### Resources to Create (Always Free)

```
OCI Account:
├── Compute Instances (3x Always Free)
│   ├── compliant-web-vm (Ampere A1)
│   ├── vulnerable-db-vm (Ampere A1)
│   └── test-app-vm (AMD)
├── VCN Security Lists (3)
│   ├── compliant-security-list
│   ├── vulnerable-security-list
│   └── production-security-list
├── Object Storage Buckets (3)
│   ├── secure-bucket (private, encrypted)
│   ├── public-bucket (public read)
│   └── backup-bucket (no lifecycle)
└── IAM Users (3)
    ├── overprivileged-user
    ├── least-privilege-user
    └── service-principal
```

### Test Lab

- **Lab 2.8**: `labs/module_2/lab_2_8_oci_scanner.py`
- Uses `oci` Python SDK to scan OCI resources
- Checks compute instances, security lists, object storage
- Generates compliance report

### Estimated Cost

- **$0/month** (Always Free tier is permanent!)

### Why OCI?

- Your company uses OCI + AWS
- Most generous free tier in the industry
- Multi-cloud experience is highly valuable
- Sets you apart from AWS-only candidates

---

## 🚀 Phase 6: Unified Multi-Cloud Judge Agent (TODO)

### Final Integration Lab

- **Lab 2.9**: `labs/module_2/lab_2_9_multi_cloud.py`
- Scans ALL platforms in one run:
  - Local JSON configs
  - GitHub repositories
  - Docker containers
  - AWS resources
  - OCI resources
- Generates unified compliance dashboard
- Exports results to JSON/PDF

### Features

```python
def scan_all_environments():
    results = {
        'local': scan_local_systems(),
        'github': scan_github_repos(),
        'docker': scan_docker_containers(),
        'aws': scan_aws_resources(),
        'oci': scan_oci_resources()
    }
    
    generate_dashboard(results)
    export_report(results, format='pdf')
```

---

## 📅 Recommended Timeline

### This Weekend (Nov 23-24)

- ✅ Phase 1: Local JSON configs (DONE)
- [ ] Phase 2: Create GitHub `security-test-targets` repo
- [ ] Phase 3: Docker compose setup

### Next Week (Nov 25-29)

- [ ] Phase 4: AWS infrastructure setup
- [ ] Phase 5: OCI infrastructure setup
- [ ] Create Labs 2.5, 2.6, 2.7, 2.8

### Week of Dec 2-6

- [ ] Phase 6: Unified multi-cloud scanner (Lab 2.9)
- [ ] Create compliance dashboard
- [ ] Document everything for portfolio

---

## 💼 Portfolio Impact

### What This Demonstrates

1. **Multi-Cloud Expertise**: AWS + OCI (not just AWS)
2. **Security Knowledge**: Vulnerability identification, compliance frameworks
3. **AI/ML Skills**: LLM-powered analysis, structured outputs
4. **DevOps**: Docker, infrastructure as code
5. **Python Proficiency**: boto3, oci SDK, docker library
6. **Real-World Application**: Solves actual business problems

### Interview Talking Points

- "I built an AI agent that scans AWS and OCI for security violations"
- "I created a multi-cloud compliance checker using LangChain and Pydantic"
- "I developed test environments across 5 platforms to validate my agent"
- "I implemented structured LLM outputs for reliable security assessments"

---

## 📚 Learning Outcomes

By completing all phases, you'll master:

- ✅ Pydantic validation and structured outputs
- ✅ LangChain integration patterns
- ✅ GitHub API and code analysis
- ✅ Docker security scanning
- ✅ AWS security best practices (boto3)
- ✅ OCI security best practices (oci SDK)
- ✅ Multi-cloud architecture
- ✅ Compliance frameworks (PCI-DSS, SOC2, NIST)

---

## 🎯 Next Immediate Steps

1. **Test Lab 2.4** (Local Scanner):

   ```bash
   python labs/module_2/lab_2_4_local_scanner.py
   ```

2. **Create GitHub Repo**:
   - Follow instructions in `external_targets/GITHUB_REPO_SETUP.md`
   - Create `security-test-targets` repository
   - Add vulnerable and secure code examples

3. **Set Up Docker**:
   - Install Docker Desktop (if not already installed)
   - Create docker-compose.yml with test containers

4. **Sign Up for OCI**:
   - Create Oracle Cloud account
   - Claim Always Free resources
   - Install OCI CLI and Python SDK

---

## 📞 Support

If you need help with any phase:

- AWS: [AWS Free Tier Documentation](https://aws.amazon.com/free/)
- OCI: [Oracle Cloud Free Tier](https://www.oracle.com/cloud/free/)
- Docker: [Docker Documentation](https://docs.docker.com/)
- GitHub: [GitHub Docs](https://docs.github.com/)

---

**Ready to become a multi-cloud AI security expert!** 🚀
