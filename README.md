# Welcome to my website 🚀
This is a personal portfolio website built with Flask. It serves as a live project to demonstrate my work, but more importantly, to showcase my setup of secure cloud infrastructure and Linux server management.

LINK 🌐: www.chanchunkiu.com

---

## Introduction
I built this site from scratch as both an online profile and a project I could actually learn from.
What began as a basic Flask app hosted on PythonAnywhere turned into a self-hosting experiment on GCP —
buying a domain, setting up DNS, configuring a CDN, and locking things down with a WAF.
It's not just a portfolio. It's something I keep tinkering with.

---

### The Infrastructure & Development
Originally hosted on shared platforms, I have since migrated this application to a custom-built cloud stack. This allows me to manage the underlying Linux environment and implement enterprise-grade security features.

---

## The Infrastructure
I migrated from PythonAnywhere to a custom cloud stack to get real hands-on control over security and performance.

### Architecture
- **Cloud:** GCP Compute Engine — e2-micro (us-central1-f, free tier)
- **Security & CDN:** Cloudflare (Edge Proxy + WAF)
- **SSL/TLS:** Cloudflare Origin CA (15-year RSA encryption)
- **Reverse Proxy: Caddy:** — hardened production gateway
- **Backend:** Python Flask
- **Environment:** Debian Linux

<pre>
[User] ──▶ [Cloudflare CDN/WAF] ──▶ [Caddy] ──▶ [Flask App]
</pre>

### Security Implementation
- **WAF hardening** — custom Cloudflare rules to challenge known bot ASNs (e.g. ASN 16509 — AWS), block sensitive path access (`.env`, `/admin`), and handle bot traffic
- **SSL "Full (Strict)" Mode**: By using Cloudflare Origin Certificates, this ensures the connection between Cloudflare and the GCP VM is encrypted and authenticated, preventing attacks in the middle
- **Bot Fight Mode** — enabled at the Cloudflare edge
- **SSL/TLS** — Cloudflare Origin CA cert (15-year RSA) served by Caddy, enforcing Full (Strict) encrypted origin connections
- **IP shielding** — Cloudflare proxy hides the origin GCP external IP from the public
- **VPC firewall** — GCP VPC rules locked down to only necessary ports (80, 443, 22)

---

## Tech used
### Backend
- Python/Flask — core logic and routing
- Requests + SMTP — contact form now sends emails directly instead of storing to a database
- Caddy — web server and reverse proxy

### Frontend
- HTML5 & CSS3 — layout and custom animations
- JavaScript — client-side interactivity

---

## Brief showcase of my website   
### This is the home page of my website

### Home page
<img width="1276" height="1083" alt="image" src="https://github.com/user-attachments/assets/e3c0415f-1a5f-4cf6-9340-37819a0b7036" />


### AboutMe
<img width="1671" height="1233" alt="image" src="https://github.com/user-attachments/assets/72dde009-8c29-4775-8d2c-16afab283804" />

## Portfolio

This page consists of my resume with a managed challenge to avoid bots 

### Contact page
<img width="1367" height="751" alt="image" src="https://github.com/user-attachments/assets/4ade42a7-d61a-4f05-afe2-66045954e219" />


### Forms are sent to my personal email
<img width="644" height="215" alt="image" src="https://github.com/user-attachments/assets/23192d42-836d-4657-9fcc-d38336742f3a" />

---

## Stucture
/static           → CSS, images, assets
/templates        → HTML template files
server.py          → Flask backend logic
README.md         → Project documentation

---

## Purpose of This Project
I wanted something that was mine
Building and maintaining this site has touched on more than I expected:
- Designing and coding a website from the ground up
- Flask backend and routing
- Self-hosting on GCP and managing a real Linux VM
- DNS and CDN configuration through Cloudflare
- Writing WAF rules and thinking about real security
- Reverse proxy setup with automated SSL via Caddy
- Keeping it running and improving it over time

