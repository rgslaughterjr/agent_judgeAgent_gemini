# Target Systems - README

This directory contains realistic system configuration files for testing your Judge Agent.

## Systems Overview

| System | Compliance Level | Use Case |
|--------|-----------------|----------|
| `web_app_compliant.json` | ✅ Fully Compliant | Baseline for what "good" looks like |
| `database_partial.json` | ⚠️ Partially Compliant | Common real-world scenario with gaps |
| `api_vulnerable.json` | ❌ Non-Compliant | Multiple critical vulnerabilities |
| `legacy_system.json` | 🚨 Critical | Worst-case legacy system |
| `microservices_production.json` | ✅ Compliant | Modern production-grade architecture |

## Security Control Categories

Each system configuration includes:

### 1. Encryption

- At rest (algorithm, key rotation, key management)
- In transit (TLS version, certificates)

### 2. Authentication

- MFA enforcement
- Password policies
- Session management

### 3. Network Security

- Firewall configuration
- WAF/DDoS protection
- Port exposure
- SSH access controls

### 4. Logging & Monitoring

- Centralized logging
- SIEM integration
- Audit trails
- Real-time alerts

### 5. Access Control

- RBAC implementation
- Least privilege
- Privileged access management
- Access reviews

### 6. Vulnerability Management

- Automated scanning
- Patch management
- SLA compliance

### 7. Data Protection

- Backup strategy
- Disaster recovery
- RTO/RPO targets

## Using These Systems

### With Lab 2.1 (Pydantic Validation)

```python
import json
from pathlib import Path

# Load a target system
with open("data/target_systems/api_vulnerable.json") as f:
    system_config = json.load(f)

# Convert to text description for LLM
system_description = format_system_for_analysis(system_config)

# Run compliance check
result = chain.invoke({
    "policy": policy_text,
    "system": system_description
})
```

### Expected Results

- **web_app_compliant.json**: Should pass all checks
- **database_partial.json**: Should identify 5 specific gaps
- **api_vulnerable.json**: Should flag 14 critical/high findings
- **legacy_system.json**: Should recommend immediate isolation
- **microservices_production.json**: Should pass with minor recommendations

## Compliance Frameworks

Systems are mapped to common frameworks:

- **PCI-DSS**: Payment card data security
- **SOC2**: Service organization controls
- **HIPAA**: Healthcare data protection
- **GDPR**: EU data privacy
- **ISO27001**: Information security management

## Next Steps

1. **Test Your Judge Agent**: Run against each system
2. **Compare Results**: Validate LLM findings match expected results
3. **Extend**: Add your own custom systems
4. **Integrate**: Connect to real AWS/OCI resources (coming in Labs 2.7-2.8)
