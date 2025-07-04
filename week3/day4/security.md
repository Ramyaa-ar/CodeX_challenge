## Real World Security Breaches

### 1.Broken acess control
a security vulnerability where a system or application fails to properly enforce access restrictions, allowing unauthorized users to perform actions or access resources they shouldn't have. This can result in data breaches, privilege escalation, and other malicious activities. <br>
**Examples:**
- Changing URL parameters to access other users' accounts.
- Accessing admin pages without proper permissions.
  
[Broken acess control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)

### 2.Cryptographic Failures
Cryptographic failures happen when sensitive data (like passwords, credit card numbers, or health info) isn’t properly protected during storage or transfer.<br>
**Examples:**
- Not using HTTPS, allowing attackers to steal data on public networks.
- Storing passwords with weak or no hashing (e.g., unsalted hashes or MD5).
- Using outdated or weak encryption algorithms.

[Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)

### 3.Injection
Injection flaws happen when untrusted data is sent to an interpreter (like SQL, OS commands, or LDAP), letting attackers execute unintended commands or access data.<br>
**Examples:**
- SQL injection: attacker changes a query to access all user data or delete records.
- OS command injection: attacker runs system commands on the server.

[Injection](https://owasp.org/Top10/A03_2021-Injection/)

### 4.Insecure Design
Insecure design means missing or weak security controls at the design stage, making an app vulnerable even if implementation is perfect.<br>
**Examples:**
- Weak password recovery questions that can be easily guessed.
- Allowing bulk seat bookings without checks, leading to business losses.
- No anti-bot protections, allowing scalpers to buy out limited stock.

[Insecure Design](https://owasp.org/Top10/A04_2021-Insecure_Design/)

### 5.Security Misconfiguration
Security misconfiguration happens when systems or apps are improperly set up, exposing them to attacks.<br>
**Examples:**
- Default accounts or passwords left unchanged.
- Unused features or sample apps still enabled.
- Detailed error messages revealing sensitive info.
- Open cloud storage buckets accessible publicly
  
[Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)

### 6.Vulnerable and Outdated Components
This risk happens when using old, unsupported, or vulnerable software components, including libraries, frameworks, or even OS-level components.<br>
**Examples:**
- Using outdated versions of libraries with known exploits (e.g., Apache Struts CVE-2017-5638).
- IoT devices running unpatched software, exposing them to attacks.
  
[Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)

### 7.Identification and Authentication Failures
These flaws happen when apps have weak or broken login and session controls, allowing attackers to take over accounts or impersonate users.<br>
**Examples:**
- No protection against brute force or credential stuffing attacks.
- Weak or default passwords allowed.
- No multi-factor authentication.
- Sessions not properly invalidated after logout or inactivity.
  
[Identification and Authentication Failures](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)

### 8.Software and Data Integrity Failures
This risk occurs when apps don’t verify software updates, libraries, or data, allowing attackers to inject malicious code or tamper with data.<br>
**Examples:**
- Updates not verified with digital signatures (e.g., unsigned router firmware).
- Supply chain attacks like SolarWinds (malicious updates spread to many clients).
- Insecure deserialization allowing remote code execution.
  
[Software and Data Integrity Failures](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/)


### 9.Security Logging and Monitoring Failures
These failures happen when apps do not log or monitor critical events, making it hard to detect and respond to breaches.<br>
**Examples:**
- No logs for logins or key transactions.
- Logs not monitored or stored securely.
- Breaches go unnoticed for years (e.g., health plan provider, major airline data leaks).
  
[Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)

### 10. Server-Side Request Forgery (SSRF)
SSRF happens when an app fetches a URL based on user input without proper validation, allowing attackers to make requests to internal systems.<br>
**Examples:**
- Accessing internal files (e.g., file:///etc/passwd).
- Reading cloud metadata (e.g., http://169.254.169.254/).
- Scanning internal network ports.
- Exploiting internal services to run code or cause DoS.
  
[Server-Side Request Forgery (SSRF)](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/)
