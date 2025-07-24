##  Phishing

Phishing is one of the most common cyber attack techniques used by scammers and attackers, targeting individuals and organizations indiscriminately.

In many cases, phishing is the **initial attack vector** used to gain access to a company's infrastructure, before performing further attacks on the network. Even though many automated tools exist today to combat phishing, it remains one of the most prolific attack vectors.

---

##  Phishing as a Social Engineering Attack

Phishing is a subset of **social engineering** — an attack that exploits humans rather than technical vulnerabilities.

Traditionally, phishing meant **fraudulent emails**, but today it also includes:

- **Smishing**: phishing via SMS
- **Vishing**: phishing via voice calls

Phishing messages usually create a **false sense of urgency**, tricking victims into clicking a malicious link that leads to an attacker-controlled web page. Victims are then asked to enter sensitive information such as login credentials or credit card details, or they may unknowingly install malware.

---

##  Types of Phishing Attacks

| Attack Type       | Definition                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------------------|
| **General Phishing** | Mass attacks not targeting specific individuals. Often low-effort and easy to spot due to obvious errors.        |
| **Spearphishing**    | Targeted at a specific individual or group (e.g., employees at a particular company). Usually more sophisticated. |
| **Whaling**         | Highly targeted at high-value individuals (e.g., CEOs). Very carefully crafted and difficult to detect.           |

---

##  CSRF (Cross-Site Request Forgery)

CSRF (Cross-Site Request Forgery) is a type of attack where a malicious website, email, or program causes a user’s web browser to perform an unwanted action on a trusted site where they are authenticated.  

This attack takes advantage of the trust that a web application has in the user's browser.  

In a CSRF attack, the attacker tricks a user into submitting a request that they did not intend to make. Because the request comes from the user’s browser (with valid cookies/session), the application assumes it is legitimate.

---

##  How CSRF Works

When you are logged into a web application, your browser stores cookies and authentication tokens. If you visit a malicious website while still logged in, that site can send a request to the target application using your credentials.

---

##  Example CSRF Attack

1️. You log in to `bank.com` and stay logged in.  
2️. You visit a malicious website controlled by an attacker.  
3️. The attacker’s website contains hidden code that submits a form to `bank.com`, transferring money to the attacker’s account.  
4️. Since you are already logged in, `bank.com` processes the request, thinking it is legitimate.

---

##  Example Malicious Form

```html
<form action="https://bank.com/transfer" method="POST">
  <input type="hidden" name="amount" value="5000">
  <input type="hidden" name="to_account" value="attacker_account">
  <input type="submit" value="Click here to claim your prize!">
</form>

