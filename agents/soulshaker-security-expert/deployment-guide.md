# Deployment Guide for Soulshaker.io Security Expert Agent

## Overview
This guide provides comprehensive instructions for deploying and integrating the Soulshaker.io Security Expert Agent into your development and deployment workflows.

## Prerequisites

### Required Tools
- Git version control
- Docker (for containerized deployments)
- Kubernetes or container orchestration platform (optional)
- CI/CD platform (GitHub Actions, GitLab CI, Jenkins, etc.)
- Access to LLM APIs (OpenAI, Anthropic, etc.)

### API Keys and Credentials
```bash
# Required API keys
OPENAI_API_KEY=<your-openai-key>
ANTHROPIC_API_KEY=<your-anthropic-key>
SOULSHAKER_AGENT_KEY=<your-agent-key>

# Optional integrations
SNYK_TOKEN=<your-snyk-token>
GITHUB_TOKEN=<your-github-token>
SONAR_TOKEN=<your-sonar-token>
```

## Installation

### 1. Clone and Configure

```bash
# Clone the repository
git clone https://github.com/NRSGroupofFresno/scaling-palm-tree.git
cd scaling-palm-tree

# Navigate to agent directory
cd agents/soulshaker-security-expert

# Copy configuration template
cp llm-config.yaml.example llm-config.yaml

# Edit configuration with your settings
nano llm-config.yaml
```

### 2. Environment Setup

```bash
# Create environment file
cat > .env <<EOF
# LLM Provider Keys
OPENAI_API_KEY=${OPENAI_API_KEY}
ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}

# Agent Configuration
AGENT_ID=soulshaker-security-expert
AGENT_GRADE=A++
AGENT_DOMAIN=soulshaker.io

# Security Settings
SECURITY_SCAN_ENABLED=true
VULNERABILITY_THRESHOLD=high
AUTO_FIX_ENABLED=false

# Deployment Settings
ENVIRONMENT=production
LOG_LEVEL=INFO
EOF
```

### 3. Docker Deployment (Recommended)

```bash
# Build Docker image
docker build -t soulshaker-security-agent:latest .

# Run container
docker run -d \
  --name soulshaker-agent \
  --env-file .env \
  -p 8080:8080 \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/logs:/app/logs \
  soulshaker-security-agent:latest

# Verify deployment
docker logs soulshaker-agent
```

### 4. Kubernetes Deployment

```yaml
# k8s-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: soulshaker-security-agent
  namespace: security-agents
spec:
  replicas: 2
  selector:
    matchLabels:
      app: soulshaker-agent
  template:
    metadata:
      labels:
        app: soulshaker-agent
        grade: a-plus-plus
    spec:
      containers:
      - name: agent
        image: soulshaker-security-agent:latest
        ports:
        - containerPort: 8080
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: llm-secrets
              key: openai-key
        - name: ANTHROPIC_API_KEY
          valueFrom:
            secretKeyRef:
              name: llm-secrets
              key: anthropic-key
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: soulshaker-agent-service
  namespace: security-agents
spec:
  selector:
    app: soulshaker-agent
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
```

## CI/CD Integration

### GitHub Actions

```yaml
# .github/workflows/security-scan.yml
name: Soulshaker Security Scan

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Soulshaker Security Agent
        uses: soulshaker/security-agent-action@v1
        with:
          agent-grade: 'A++'
          scan-type: 'comprehensive'
          block-on-high: true
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      
      - name: Upload Security Report
        uses: actions/upload-artifact@v3
        with:
          name: security-report
          path: security-report.json
```

### GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - security
  - deploy

security_scan:
  stage: security
  image: soulshaker-security-agent:latest
  script:
    - security-agent scan --comprehensive
    - security-agent analyze --threshold high
  artifacts:
    reports:
      security: security-report.json
  only:
    - merge_requests
    - main
```

## Usage Examples

### 1. Security Code Review

```bash
# Scan a specific file
security-agent scan --file src/auth/login.js --verbose

# Scan entire project
security-agent scan --project . --report-format json

# Focus on specific vulnerability types
security-agent scan --types sql-injection,xss,csrf --project .
```

### 2. Automated Vulnerability Fix

```bash
# Review and suggest fixes
security-agent fix --file src/api/user.js --preview

# Apply fixes automatically (use with caution)
security-agent fix --file src/api/user.js --auto-apply --backup

# Batch fix common issues
security-agent fix --project . --severity high --auto-apply
```

### 3. Deployment Security Check

```bash
# Pre-deployment security gate
security-agent deploy-check \
  --environment production \
  --compliance SOC2,GDPR \
  --block-on-fail

# Container security scan
security-agent scan-container \
  --image myapp:latest \
  --registry dockerhub
```

## Configuration Options

### Security Levels

```yaml
# Strict mode (production)
security_level: strict
block_on_severity:
  - critical
  - high
auto_fix: false
require_approval: true

# Balanced mode (staging)
security_level: balanced
block_on_severity:
  - critical
auto_fix: true
require_approval: false

# Permissive mode (development)
security_level: permissive
block_on_severity: []
auto_fix: true
require_approval: false
```

### Custom Rules

```yaml
# custom-rules.yaml
rules:
  - id: AUTH-001
    name: "Enforce MFA for admin routes"
    severity: high
    pattern: "/admin/*"
    requires:
      - multi_factor_auth
      - rate_limiting
  
  - id: DATA-001
    name: "Encrypt sensitive data at rest"
    severity: critical
    patterns:
      - "password"
      - "ssn"
      - "credit_card"
    requires:
      - encryption
      - secure_storage
```

## Monitoring and Alerts

### Metrics Dashboard

Access the agent dashboard at:
```
https://soulshaker.io/agent/dashboard
```

Key metrics tracked:
- Vulnerabilities detected per day
- False positive rate
- Mean time to remediation (MTTR)
- Security scan coverage
- Deployment success rate

### Alert Configuration

```yaml
# alerts.yaml
alerts:
  - name: "Critical Vulnerability Detected"
    condition: "severity == 'critical'"
    channels:
      - slack
      - email
      - pagerduty
    recipients:
      - security-team@company.com
    
  - name: "Deployment Security Gate Failed"
    condition: "deployment_blocked == true"
    channels:
      - slack
      - email
    recipients:
      - devops-team@company.com
```

## Troubleshooting

### Common Issues

**Issue: Agent not detecting vulnerabilities**
```bash
# Check agent version
security-agent version

# Update vulnerability database
security-agent update-db

# Verify API connectivity
security-agent health-check
```

**Issue: High false positive rate**
```bash
# Tune detection sensitivity
security-agent config set sensitivity balanced

# Add false positive suppressions
security-agent suppress --id VULN-123 --reason "false-positive"
```

**Issue: Slow scan performance**
```bash
# Enable parallel scanning
security-agent config set parallel_scans 4

# Use incremental scanning
security-agent scan --incremental --baseline main
```

## Best Practices

1. **Regular Updates**: Keep the agent and vulnerability databases updated
2. **Incremental Scanning**: Use incremental scans for faster feedback in development
3. **Baseline Security**: Establish security baselines for each environment
4. **Team Training**: Ensure team understands security reports and remediation
5. **Integration Testing**: Test security fixes don't break functionality
6. **Documentation**: Document security exceptions and suppressions
7. **Audit Trail**: Maintain logs of all security decisions and changes

## Support and Resources

- **Documentation**: https://soulshaker.io/docs
- **API Reference**: https://soulshaker.io/api
- **Status Page**: https://status.soulshaker.io
- **Support Email**: security-agent@soulshaker.io
- **Issue Tracker**: https://github.com/NRSGroupofFresno/scaling-palm-tree/issues

## Security Considerations

- Store API keys in secure secret management systems
- Rotate credentials regularly
- Use least-privilege access principles
- Enable audit logging for all agent actions
- Review security reports promptly
- Implement security gates in CI/CD pipelines
- Regular security training for development team

---

*Last Updated: December 2025*  
*Version: 1.0*  
*Maintained by: Soulshaker.io Security Team*
