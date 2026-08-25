# Findings

## Secret Detection

Gitleaks detected the hard-coded API credential committed in `app.py`. I removed the credential from the source code and changed the application to retrieve it through the `API_KEY` environment variable. The credential is now stored as a GitHub Actions Secret rather than being committed to the repository.

GitHub Secrets protect credentials from being directly exposed through source code and Git history, while allowing sensitive values to be injected when needed. However, they do not guarantee that a credential cannot be exposed. A compromised workflow, runner, application, or script could still expose the secret through logs or other outputs. They also do not protect against someone who already has access to the credential.

## Dependency Scanning

`pip-audit` detected a known vulnerability in the intentionally outdated Flask version specified in `requirements.txt`. I used the Python vulnerability database at https://pyupio.github.io/safety-db/ to identify a vulnerable Flask version [version 3.1.0] for the initial commit, then upgraded Flask to a patched version [version 3.1.3]. The subsequent dependency scan passed successfully.

## Challenges

The main issue I encountered was that my initial fake API key was not detected by Gitleaks because it did not match its default detection rules. After several runs, I reviewed Gitleaks' documentation and found a documented credential example matching one of its detection patterns. Using that example allowed the initial security scan to fail as intended.

## AI Usage

I used ChatGPT to draft the initial Flask API and to shorten and structure this document. I independently researched the security tools, vulnerable dependency, and Gitleaks detection behavior.
