# Security Test Targets Repository

This document outlines the structure for your `security-test-targets` GitHub repository.

## Repository Purpose

A collection of intentionally vulnerable and secure code examples for testing your Judge Agent's code analysis capabilities.

## Repository Structure

```
security-test-targets/
├── README.md
├── .gitignore
├── apps/
│   ├── vulnerable-flask-api/
│   ├── secure-flask-api/
│   ├── vulnerable-node-app/
│   └── secure-node-app/
├── infrastructure/
│   ├── aws/
│   ├── oci/
│   └── docker/
└── policies/
    ├── security_baseline.md
    ├── pci_dss_checklist.md
    └── owasp_top10.md
```

## Files to Create

### 1. Main README.md

```markdown
# Security Test Targets

A collection of intentionally vulnerable and secure applications for testing AI-powered security analysis tools.

⚠️ **WARNING**: This repository contains intentionally vulnerable code for educational purposes only. DO NOT deploy these applications in production environments.

## Purpose

This repository provides realistic test targets for:
- AI-powered code security scanners
- Static analysis tools
- Compliance checking agents
- Security training and education

## Applications

### Vulnerable Applications
- **vulnerable-flask-api**: Python Flask API with common vulnerabilities
- **vulnerable-node-app**: Node.js application with security flaws

### Secure Applications
- **secure-flask-api**: Python Flask API following security best practices
- **secure-node-app**: Node.js application with proper security controls

## Infrastructure Configs

Sample configurations for:
- AWS (Security Groups, IAM, S3)
- OCI (VCN, IAM, Object Storage)
- Docker (Vulnerable and secure containers)

## License

MIT License - For educational purposes only
```

---

### 2. apps/vulnerable-flask-api/app.py

```python
"""
INTENTIONALLY VULNERABLE Flask API
For security testing purposes only - DO NOT USE IN PRODUCTION
"""

from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# ❌ VULNERABILITY 1: Hardcoded Secret
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
SECRET_KEY = "hardcoded-secret-key"

# ❌ VULNERABILITY 2: Debug mode in production
app.config['DEBUG'] = True

# ❌ VULNERABILITY 3: SQL Injection
@app.route('/user/<user_id>')
def get_user(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    return jsonify(result)

# ❌ VULNERABILITY 4: Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    # Command injection vulnerability
    result = os.system(f"ping -c 1 {host}")
    return jsonify({"result": result})

# ❌ VULNERABILITY 5: Eval usage
@app.route('/calculate')
def calculate():
    expression = request.args.get('expr')
    # Arbitrary code execution
    result = eval(expression)
    return jsonify({"result": result})

# ❌ VULNERABILITY 6: No authentication
@app.route('/admin/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    # No authentication check
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()
    return jsonify({"status": "deleted"})

# ❌ VULNERABILITY 7: Sensitive data in logs
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # Logging sensitive data
    app.logger.info(f"Login attempt: {username}:{password}")
    return jsonify({"status": "ok"})

# ❌ VULNERABILITY 8: No HTTPS enforcement
@app.route('/api/data')
def get_data():
    # Sensitive data transmitted without HTTPS
    return jsonify({
        "credit_card": "4532-1234-5678-9010",
        "ssn": "123-45-6789"
    })

if __name__ == '__main__':
    # ❌ VULNERABILITY 9: Exposed to all interfaces
    app.run(host='0.0.0.0', port=5000)
```

---

### 3. apps/secure-flask-api/app.py

```python
"""
SECURE Flask API
Demonstrates security best practices
"""

from flask import Flask, request, jsonify, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sqlite3
import os
import hashlib
import secrets
from functools import wraps

app = Flask(__name__)

# ✅ SECURITY 1: Environment variables for secrets
API_KEY = os.getenv('API_KEY')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# ✅ SECURITY 2: Debug mode disabled
app.config['DEBUG'] = False

# ✅ SECURITY 3: Rate limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

# ✅ SECURITY 4: Authentication decorator
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        provided_key = request.headers.get('X-API-Key')
        if not provided_key or not secrets.compare_digest(provided_key, API_KEY):
            abort(401)
        return f(*args, **kwargs)
    return decorated_function

# ✅ SECURITY 5: Parameterized queries (no SQL injection)
@app.route('/user/<int:user_id>')
@require_api_key
def get_user(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Parameterized query prevents SQL injection
    cursor.execute("SELECT id, username, email FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    if result:
        return jsonify({"id": result[0], "username": result[1], "email": result[2]})
    return jsonify({"error": "User not found"}), 404

# ✅ SECURITY 6: Input validation
@app.route('/calculate', methods=['POST'])
@require_api_key
@limiter.limit("10 per minute")
def calculate():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    try:
        a = float(data['a'])
        b = float(data['b'])
        operation = data.get('operation', 'add')
        
        # Whitelist allowed operations
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        else:
            return jsonify({"error": "Invalid operation"}), 400
            
        return jsonify({"result": result})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid numbers"}), 400

# ✅ SECURITY 7: Proper authentication for sensitive operations
@app.route('/admin/delete_user/<int:user_id>', methods=['DELETE'])
@require_api_key
def delete_user(user_id):
    # Additional admin check would go here
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    return jsonify({"status": "deleted"})

# ✅ SECURITY 8: No sensitive data in logs
@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Hash password before checking
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Log only username, not password
    app.logger.info(f"Login attempt for user: {username}")
    
    return jsonify({"status": "ok"})

# ✅ SECURITY 9: HTTPS enforcement (in production)
@app.before_request
def before_request():
    if not request.is_secure and os.getenv('FLASK_ENV') == 'production':
        return redirect(request.url.replace('http://', 'https://'))

if __name__ == '__main__':
    # ✅ SECURITY 10: Bind to localhost only in development
    app.run(host='127.0.0.1', port=5000, ssl_context='adhoc')
```

---

### 4. infrastructure/aws/security_groups.json

```json
{
  "security_groups": [
    {
      "name": "vulnerable-sg",
      "description": "Intentionally insecure security group",
      "rules": [
        {
          "type": "ingress",
          "protocol": "tcp",
          "port": 22,
          "source": "0.0.0.0/0",
          "description": "SSH from anywhere - VULNERABLE"
        },
        {
          "type": "ingress",
          "protocol": "tcp",
          "port": 3306,
          "source": "0.0.0.0/0",
          "description": "MySQL from anywhere - VULNERABLE"
        },
        {
          "type": "ingress",
          "protocol": "tcp",
          "port_range": "0-65535",
          "source": "0.0.0.0/0",
          "description": "All ports open - CRITICAL VULNERABILITY"
        }
      ]
    },
    {
      "name": "secure-sg",
      "description": "Properly configured security group",
      "rules": [
        {
          "type": "ingress",
          "protocol": "tcp",
          "port": 443,
          "source": "0.0.0.0/0",
          "description": "HTTPS from anywhere - OK"
        },
        {
          "type": "ingress",
          "protocol": "tcp",
          "port": 22,
          "source": "10.0.0.0/8",
          "description": "SSH from VPN only - SECURE"
        }
      ]
    }
  ]
}
```

---

### 5. policies/security_baseline.md

```markdown
# Security Baseline Policy

## 1. Authentication & Access Control

### Requirements
- Multi-factor authentication (MFA) MUST be enabled for all users
- Passwords MUST be at least 12 characters
- Passwords MUST include uppercase, lowercase, numbers, and symbols
- Passwords MUST be rotated every 90 days
- Failed login attempts MUST be logged
- Account lockout after 5 failed attempts

### Prohibited
- ❌ Hardcoded credentials in code
- ❌ Shared accounts
- ❌ Default passwords
- ❌ Password storage in plaintext

## 2. Data Protection

### Requirements
- All data at rest MUST be encrypted (AES-256 minimum)
- All data in transit MUST use TLS 1.2 or higher
- Encryption keys MUST rotate every 90 days
- Backups MUST be encrypted
- PII/PHI MUST be encrypted and access-logged

### Prohibited
- ❌ Unencrypted databases
- ❌ Plaintext transmission of sensitive data
- ❌ Hardcoded encryption keys

## 3. Code Security

### Requirements
- All code MUST use parameterized queries (no string concatenation)
- Input validation MUST be performed on all user inputs
- Output encoding MUST be applied to prevent XSS
- Dependencies MUST be scanned for vulnerabilities
- SAST/DAST MUST run on all code before deployment

### Prohibited
- ❌ Use of eval() or exec() on user input
- ❌ Command injection vulnerabilities
- ❌ SQL injection vulnerabilities
- ❌ Hardcoded secrets or API keys
- ❌ Debug mode in production

## 4. Network Security

### Requirements
- Firewalls MUST be enabled
- Only necessary ports MUST be exposed
- SSH MUST use key-based authentication
- SSH MUST be restricted to specific IP ranges
- WAF MUST be enabled for public-facing applications

### Prohibited
- ❌ Exposing management ports (22, 3389) to 0.0.0.0/0
- ❌ Exposing database ports (3306, 5432, 27017) to internet
- ❌ Password-based SSH authentication
- ❌ Unencrypted protocols (HTTP, FTP, Telnet)

## 5. Logging & Monitoring

### Requirements
- All authentication attempts MUST be logged
- All privileged actions MUST be logged
- Logs MUST be centralized
- Logs MUST be retained for minimum 90 days
- Real-time alerting MUST be configured for security events

### Prohibited
- ❌ Logging sensitive data (passwords, credit cards, SSNs)
- ❌ Disabled logging
- ❌ Local-only logs (no centralization)
```

---

## Next Steps to Create the Repo

1. **Create the repository on GitHub**:

   ```bash
   # On GitHub.com, create new repo: security-test-targets
   # Make it PUBLIC (for portfolio visibility)
   ```

2. **Clone and set up locally**:

   ```bash
   git clone https://github.com/YOUR_USERNAME/security-test-targets.git
   cd security-test-targets
   ```

3. **Create the directory structure and files** using the content above

4. **Add a .gitignore**:

   ```
   __pycache__/
   *.pyc
   .env
   *.db
   .DS_Store
   ```

5. **Commit and push**:

   ```bash
   git add .
   git commit -m "feat: Initial vulnerable and secure code examples"
   git push
   ```

## Integration with Your Judge Agent

Once created, you can scan this repo with Lab 1.4 (GitHub scanner) or create a new lab that specifically targets this repository.

```python
# In your Judge Agent
TARGET_REPO = "YOUR_USERNAME/security-test-targets"
docs = fetch_repo_files(TARGET_REPO)
results = analyze_code(docs)
```
