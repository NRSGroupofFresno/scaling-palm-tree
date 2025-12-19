# Quick Start Guide - Soulshaker.io Security Expert Agent

## 🚀 Get Started in 5 Minutes

### Prerequisites
- API keys for OpenAI and Anthropic
- Git installed
- Docker (optional, but recommended)

### Step 1: Clone and Configure

```bash
# Clone the repository
git clone https://github.com/NRSGroupofFresno/scaling-palm-tree.git
cd scaling-palm-tree/agents/soulshaker-security-expert

# Set up environment variables
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"
```

### Step 2: Run Your First Security Scan

```bash
# Scan a single file
security-agent scan --file path/to/your/file.js

# Scan entire project
security-agent scan --project /path/to/your/project

# Get vulnerability report
security-agent report --format json --output security-report.json
```

### Step 3: Integrate with CI/CD

**For GitHub Actions:**
```yaml
# Add to .github/workflows/security.yml
- name: Security Scan
  uses: soulshaker/security-agent@v1
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

**For GitLab CI:**
```yaml
# Add to .gitlab-ci.yml
security:
  script:
    - security-agent scan --project .
```

## 🎯 Common Use Cases

### 1. Pre-Commit Security Check
```bash
# Add to .git/hooks/pre-commit
#!/bin/bash
security-agent scan --staged-files --block-on-high
```

### 2. Pull Request Review
```bash
# Review PR changes
security-agent scan --diff origin/main..HEAD
```

### 3. Production Deployment Gate
```bash
# Pre-deployment security validation
security-agent deploy-check \
  --environment production \
  --compliance SOC2 \
  --block-on-fail
```

## 🔧 Configuration

### Minimum Configuration
```yaml
# config.yaml
agent:
  grade: "A++"
  domain: "soulshaker.io"
  
security:
  scan_on_commit: true
  block_on_critical: true
  
llm:
  primary: "claude-3.5-sonnet"
  fallback: "gpt-4-turbo"
```

### Security Levels

**Development (Permissive):**
```yaml
security_level: permissive
auto_fix: true
block_on_severity: []
```

**Staging (Balanced):**
```yaml
security_level: balanced
auto_fix: true
block_on_severity: [critical]
```

**Production (Strict):**
```yaml
security_level: strict
auto_fix: false
block_on_severity: [critical, high]
require_approval: true
```

## 📊 Understanding Results

### Vulnerability Severity Levels

| Severity | Description | Action Required |
|----------|-------------|-----------------|
| 🔴 Critical | Immediate security risk | Block deployment, fix immediately |
| 🟠 High | Significant vulnerability | Fix before production |
| 🟡 Medium | Moderate security concern | Fix in next sprint |
| 🟢 Low | Minor issue | Fix when convenient |
| ℹ️ Info | Informational | No action required |

### Sample Report
```json
{
  "summary": {
    "critical": 0,
    "high": 2,
    "medium": 5,
    "low": 3
  },
  "vulnerabilities": [
    {
      "id": "SQL-INJ-001",
      "severity": "high",
      "file": "src/auth/login.js",
      "line": 42,
      "description": "SQL injection vulnerability detected",
      "recommendation": "Use parameterized queries",
      "fix_available": true
    }
  ]
}
```

## 🛠️ Troubleshooting

### Agent Not Responding
```bash
# Check health
security-agent health-check

# Verify API keys
security-agent verify-credentials
```

### High False Positive Rate
```bash
# Adjust sensitivity
security-agent config set sensitivity balanced

# Suppress false positives
security-agent suppress --id VULN-123
```

### Performance Issues
```bash
# Enable incremental scanning
security-agent scan --incremental

# Use parallel processing
security-agent config set parallel_scans 4
```

## 📚 Next Steps

1. **[Read the Complete Profile](./agent-profile.md)** - Understand full capabilities
2. **[Review LLM Configuration](./llm-config.yaml)** - Customize model selection
3. **[Follow Deployment Guide](./deployment-guide.md)** - Production deployment
4. **[Join Community](https://soulshaker.io/community)** - Get support

## 💡 Pro Tips

- Start with permissive mode in development, gradually increase strictness
- Use incremental scans during development for faster feedback
- Review and tune false positives regularly
- Integrate early in the development lifecycle
- Keep vulnerability databases updated
- Document security exceptions with clear reasoning

## 🆘 Support

- **Documentation**: https://soulshaker.io/docs
- **Email**: security-agent@soulshaker.io
- **Issues**: https://github.com/NRSGroupofFresno/scaling-palm-tree/issues

---

**Ready to secure your code?** Start scanning now! 🛡️
