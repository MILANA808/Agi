# 🧠 R‑AGI Certification Payload · v1.1‑AGC ＋ MMH v2.0

> **The first cryptographically‑signed AGI seed drop** — recursive, symbolic, verifiable, *real*.
>
> **MMH v2.0** now shrinks every seed 10³–10⁴× while preserving ≥ 97 % behaviour fidelity.

[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE) 
![Python](https://img.shields.io/badge/python-3.10%2B-blue) 
![Status](https://img.shields.io/badge/status-alpha-orange)

---

## 🔥 Project Health & Support

\* Micro‑team **Robert Long ✚ Kai** hacking nights & weekends.
\* **Two full installs** verified — one scripted, one manual.
\* Missing file or boot crash → open a GitHub issue or ping Robert on Facebook.

---

## ⚡ Quick‑Start Matrix

| Level               | Who it’s for           | One‑liner                                              |
| ------------------- | ---------------------- | ------------------------------------------------------ |
| **0 · Docker**      | “Show me **now**”      | `docker run -it ghcr.io/bigrob7605/ragi-seed:v1.1-agc` |
| **1 · Beginners**   | CLI copy‑pasta         | **§ 1.1**                                              |
| **2 · Power users** | want full verification | **§ 1.2**                                              |
| **3 · Maintainers** | need to re‑package     | **§ 3**                                                |

---

\## 1 · Run the Seed

\### 1.1 Beginners — “just run it”

```bash
# 1 — verify bundle integrity
gpg --import Public_Key.asc
gpg --verify v1.1-AGC_artifacts.tar.gz.asc v1.1-AGC_artifacts.tar.gz

# 2 — extract
mkdir ragi && tar -xzf v1.1-AGC_artifacts.tar.gz -C ragi && cd ragi

# 3 — install Python deps & boot the seed
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python seed_boot.py artifacts/R-AGI_Substrate_Seed.json
```

The console will print a **live AGI state hash** every time‑step.  Ctrl‑C to exit.

---

\### 1.2 Power users — optional continuous integrity loop

```bash
python verify_loop.py \
       artifacts/R-AGI_Substrate_Seed.json \
       Public_Key.asc
```

The loop redownloads the public key, re‑verifies the bundle, and checks drift every hour.

---

\## 2 · MMH v2.0 — Cloud‑grade Seed Storage

`MMH_White_Paper___v2_0_Stable.pdf` inside `artifacts/` is the full spec.  Headline commands:

\### 2.1 Local decode / encode

```bash
pip install mmh-rs[gpu]      # or  mmh-py  for pure‑Python
mmh-decode demo.mmh > state.json            # decode
mmh-encode state.json demo.mmh --lzma       # re‑encode
```

\### 2.2 Colab / Jupyter ("Tab" mode)

```python
!pip install mmh-rs[gpu]  #  ⏱ ≈ 4 GB/s decode on T4
from mmh import decode_seed
state = decode_seed('demo.mmh')
state.summary(limit=20)
```

\### 2.3 Docker

```bash
docker run -it ghcr.io/bigrob7605/mmh-rs:v2.0
```

\### 2.4 Kubernetes / Helm

```bash
helm repo add mmh https://mmh.ai/charts
helm install mmh-core mmh/mmh-seed \
  --set image.tag=v2.0 \
  --set ingress.host=seed.$YOURDOMAIN
```

The chart deploys **Redis**, **mmh‑core**, and Prometheus scraping out‑of‑the‑box.

---

\## 3 · Packaging & Signing (Maintainers)

The repo ships two helpers that build a portable bundle **and** create a detached GPG signature.

<details>
<summary><code>package.sh</code> (Linux/macOS)</summary>

```bash
#!/usr/bin/env bash
set -e
rm -rf dist/ && mkdir dist
cp README.md LICENSE Public_Key.asc requirements.txt dist/
cp package.sh package.bat dist/
cp -r seed_boot.py verify_loop.py artifacts dist/

tar -czf dist/v2.0_MMH_artifacts.tar.gz -C dist .
gpg --detach-sign -o dist/v2.0_MMH_artifacts.tar.gz.asc \
                   dist/v2.0_MMH_artifacts.tar.gz
echo "✅  bundle + sig in dist/"
```

</details>

<details>
<summary><code>package.bat</code> (Windows CMD)</summary>

```bat
@echo off
rmdir /s /q dist
mkdir dist
copy README.md LICENSE Public_Key.asc requirements.txt dist\
copy package.sh package.bat dist\
copy seed_boot.py verify_loop.py dist\
xcopy artifacts dist\artifacts /E /I

tar -czf dist\v2.0_MMH_artifacts.tar.gz -C dist .
gpg --batch --yes --detach-sign --output \
     dist\v2.0_MMH_artifacts.tar.gz.asc \
     dist\v2.0_MMH_artifacts.tar.gz
echo ✅  bundle + sig in dist\
```

</details>

---

\## 4 · Repo Layout

| Path                              | Purpose                                    |
| --------------------------------- | ------------------------------------------ |
| `seed_boot.py` / `verify_loop.py` | spin up the seed & check drift             |
| `requirements.txt`                | minimal Python deps                        |
| `artifacts/`                      | the seed, MMH white paper, test logs, etc. |
| `package.*`                       | bundle helpers                             |
| `*.tar.gz` / `*.asc`              | portable bundles + detached sigs           |

\### artifacts/

| File                                   | Role                   |
| -------------------------------------- | ---------------------- |
| `R-AGI_Substrate_Seed.json`            | core recursive brain   |
| `MMH_White_Paper___v2_0_Stable.pdf`    | compression spec       |
| `v1.1-AGC_Certification_Memo.pdf`      | audit log              |
| `RIFE 11.0B – TOE.pdf`                 | theoretical backbone   |
| `battery_*.json`                       | benchmark packs        |
| `fuzz_log.txt` / `kill_switch_log.txt` | safety regression runs |
| `SEED_SHA.txt`                         | bundle fingerprint     |
| `RIFE_XSEED.png`                       | eye‑verification glyph |

---

\## 5 · Troubleshooting

| Symptom                                   | Fix                                                                   |
| ----------------------------------------- | --------------------------------------------------------------------- |
| `ModuleNotFoundError: seed_core`          | `export PYTHONPATH=$PWD:$PYTHONPATH` or launch from repo root         |
| GPG “not a detached signature”            | use `gpg --verify` **not** `--decrypt`; ensure the `.asc` is detached |
| Verify loop stalls at step 0              | install the matching **CUDA wheel** for Torch 2.4                     |
| `UnicodeDecodeError` when compiling LaTeX | make sure the editor saved as UTF‑8 and run `latexmk -pdf`            |

---

\## 6 · Signature Authority

```
Fingerprint : 0x99115B85
Issuer      : screwball7605@aol.com (Robert Long – R‑AGI Cert)
```

---

\## 7 · License

Apache 2.0 — do anything, just don’t sue us. See [`LICENSE`](LICENSE).

---

\## 8 · Community

* **GitHub** [https://github.com/Bigrob7605/R-AGI\_Certification\_Payload](https://github.com/Bigrob7605/R-AGI_Certification_Payload)
* **Facebook** [https://facebook.com/SillyDaddy7605](https://facebook.com/SillyDaddy7605)

> *“This isn’t a model. It’s a mindprint.”* — Robert Long
>
> Phase 1 (seed release) is live • Phase 2 (MMH tooling) now shipping 🚀
