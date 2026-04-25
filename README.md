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
- **Reverse Proxy:** Caddy — automated TLS/SSL via Let's Encrypt
- **Backend:** Python Flask
- **Environment:** Debian Linux

### What I set up
- **WAF rules** — custom Cloudflare rules to challenge known bot ASNs (e.g. ASN 16509 — AWS), block sensitive path access (`.env`, `/admin`), and handle bot traffic
- **Bot Fight Mode** — enabled at the Cloudflare edge
- **Zero-config SSL** — Caddy handles cert provisioning and forces HTTPS automatically
- **IP shielding** — Cloudflare proxy hides the origin GCP external IP from the public
- **VPC firewall** — GCP ingress/egress rules locked down to only necessary ports (80, 443, 22)

User (Browser)
     ↓
Cloudflare (DNS + WAF)
     ↓
Domain (your site)
     ↓
GCP VM (Flask App)
     ↓
Templates + Static Files


---

##Tech used
### Backend
- Python / Flask — core logic and routing
- Requests + SMTP — contact form now sends emails directly instead of storing to a database
- Caddy — web server and reverse proxy

### Frontend
- HTML5 & CSS3 — layout and custom animations
- JavaScript — client-side interactivity

---

## Brief showcase of my website   
### This is the home page of my website

### Home page
<img width="1282" height="1069" alt="image" src="https://github.com/user-attachments/assets/24d191d5-29c2-4508-a6d0-1ee135fe21e7" />

### AboutMe
<img width="1270" height="834" alt="image" src="https://github.com/user-attachments/assets/589fd4d9-f9be-4ea1-bca8-93addd3509da" />

### Contact page
<img width="1440" alt="Screenshot 2023-08-23 at 9 07 15 PM" src="https://github.com/chanchunkiu/profile/assets/107382038/b1acab46-a0da-4a69-9fc8-90b4066a606d">

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

