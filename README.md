# ⚙️ Clash Config Patcher

**Clash Config Patcher** is a lightweight script designed to apply custom patches to Clash configuration files. It supports value replacement, dictionary merging or overwriting, and list element injection at the beginning of arrays.

---

## 🚀 How to Use

### 1. Create a Patch File

Write your patch in YAML format. Here's an example:

```yaml
bind-address: '*'
allow-lan: true
external-controller: 0.0.0.0:9090
mixed-port: 7890
port: 7890
"dns/use-hosts": true

hosts:
  'host_name': '192.168.1.x'

proxy-groups:
  - name: "group1"
    proxies:
      ...
    type: select
  - name: "group2"
    proxies:
      ...
    type: select

rules:
  - "DOMAIN-KEYWORD,github,group1"
  - "DOMAIN,www.example.com,group2"
  - "DOMAIN-KEYWORD,csdn,REJECT"
```

### 2. Apply the Patch

#### 🔗 Patch from a remote subscription URL:
```bash
clash-config-patcher -u <your_subscription_url> patch_file [-o output_path]
```

#### 📁 Patch a local configuration file:
```bash
clash-config-patcher -f <path_to_config_file> patch_file [-o output_path]
```

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).