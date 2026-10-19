# Linux Hardening Checklist

Use this as a review aid on a system you own or are authorized to administer.

- [ ] Install security updates using the distribution's documented process.
- [ ] Remove or disable services and accounts that are not needed.
- [ ] Use unique, strong passwords and multi-factor authentication where available.
- [ ] Prefer SSH keys and disable password-based SSH only after confirming key access works.
- [ ] Limit administrative privileges; avoid routine work as root.
- [ ] Review file and directory permissions, including the findings from `audit_permissions.py`.
- [ ] Configure a host firewall according to the system's role.
- [ ] Enable and review relevant authentication and system logs.
- [ ] Back up important data and test restoration.
- [ ] Document changes and verify that required applications still work.

Do not apply changes blindly to production systems. Confirm backups and access before modifying security settings.
