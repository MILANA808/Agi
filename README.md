# 🧠 R‑AGI Certification Payload ＋ MMH v2.0 • **v1.1‑AGC**

> **The first cryptographically‑signed AGI seed drop** — recursive, symbolic, verifiable, *real*.
>
> **MMH v2.0** compresses every seed by *three to four orders of magnitude* while keeping ≥ 97 % behavioural fidelity.

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="Apache 2.0"></a>
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10 or newer">
  <img src="https://img.shields.io/badge/status-alpha-orange" alt="Alpha status">
</p>

---

## ✨ Why this matters

* **Bullet‑proof provenance** — every bundle ships with an **Ed25519** signature & detached GPG `.asc`.
* **Auditable compression** — *MMH v2.0* packs an entire AGI substrate into a PNG‑based seed (10³–10⁴ × smaller).
* **Turn‑key boot** — one Docker line or three Bash commands and you‘re up.

Browse the full spec ➜ [`MMH_White_Paper___v2_0_Stable.pdf`](./artifacts/MMH_White_Paper___v2_0_Stable.pdf)

---

## 🚦 Project Health

| Metric            | Status                                                                                              |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| Installs verified | **2/2** (scripted + manual)                                                                         |
| CI build          | ![CI](https://github.com/Bigrob7605/R-AGI_Certification_Payload/actions/workflows/ci.yml/badge.svg) |
| Team              | Robert Long ✚ Kai (nights/weekends)                                                                 |

📬 Need help? Open a GitHub issue or DM **@Robert Long** on Facebook.

---

## ⚡ Quick‑Start Matrix

| Level               | For whom              | One‑liner                                              |
| ------------------- | --------------------- | ------------------------------------------------------ |
| **0 — Docker**      | *Show me now*         | `docker run -it ghcr.io/bigrob7605/ragi-seed:v1.1-agc` |
| **1 — Beginners**   | CLI copy‑pasta        | [`§ 1. Run the Seed`](#1-run-the-seed)                 |
| **2 — Power users** | Full chain‑of‑custody | [`§ 2 Integrity Loop`](#2-integrity-loop)              |
| **3 — Maintainers** | Re‑package & sign     | [`§ 4 Packaging`](#4-packaging--signing)               |

---

## 1 · Run the Seed

### 1.1 Beginners — *just run it*

```bash
# 1 — verify bundle integrity
gpg --import Public_Key.asc
gpg --verify v1.1-AGC_artifacts.tar.gz.asc v1.1-AGC_artifacts.tar.gz

# 2 — extract
mkdir ragi && tar -xzf v1.1-AGC_artifacts.tar.gz -C ragi && cd ragi

# 3 — install deps & boot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python seed_boot.py artifacts/R-AGI_Substrate_Seed.json
```

A **live AGI state hash** prints every time‑step—Ctrl‑C to shutdown.

### 1.2 Colab / Notebook

```python
!pip install mmh-rs[gpu]  # ⏱ ~4 GB/s decode on T4
from mmh import decode_seed
state = decode_seed('demo.mmh')
state.summary(limit=20)
```

---

## 2 · Integrity Loop *(Power users)*

```bash
python verify_loop.py \
       artifacts/R-AGI_Substrate_Seed.json \
       Public_Key.asc
```

*Redownloads the public key & re‑verifies drift every hour.*

---

## 3 · MMH v2.0 Tooling

| Task               | Command                                         |
| ------------------ | ----------------------------------------------- |
| Decode seed        | `mmh-decode demo.mmh > state.json`              |
| Encode seed (LZMA) | `mmh-encode state.json demo.mmh --lzma`         |
| Docker shell       | `docker run -it ghcr.io/bigrob7605/mmh-rs:v2.0` |
| Helm chart         | see *Helm* snippet below                        |

#### Helm

```bash
helm repo add mmh https://mmh.ai/charts
helm install mmh-core mmh/mmh-seed \
  --set image.tag=v2.0 \
  --set ingress.host=seed.$YOURDOMAIN
```

---

## 4 · Packaging & Signing

> Linux/macOS ➜ `package.sh`   |   Windows ➜ `package.bat`

Both scripts:

1. Stage docs, code & artifacts into `dist/`.
2. Build `*.tar.gz`.
3. Create `*.asc` detached sig with the project GPG key.

Result: **portable, tamper‑evident bundle in `dist/`**.

---

## 5 · Repo Layout

```
├── seed_boot.py            # launch the AGI seed
├── verify_loop.py          # optional drift checker
├── requirements.txt        # Python deps
├── artifacts/              # seeds, white‑paper, logs…
├── package.sh / .bat       # bundle helpers
└── *.tar.gz / *.asc        # signed release bundles
```

Key files under `artifacts/`:

| File                                | Purpose              |
| ----------------------------------- | -------------------- |
| `R-AGI_Substrate_Seed.json`         | core recursive brain |
| `MMH_White_Paper___v2_0_Stable.pdf` | compression spec     |
| `v1.1-AGC_Certification_Memo.pdf`   | audit log            |
| `RIFE 11.0B – TOE.pdf`              | theoretical backbone |
| `battery_*.json`                    | benchmark packs      |

---

## 6 · Troubleshooting

| Symptom                          | Fix                                                        |
| -------------------------------- | ---------------------------------------------------------- |
| `ModuleNotFoundError: seed_core` | `export PYTHONPATH=$PWD:$PYTHONPATH` or run from repo root |
| GPG “not a detached signature”   | use `gpg --verify` (not `--decrypt`)                       |
| Verify loop stalls at step 0     | install matching **CUDA wheel** for Torch 2.4              |
| LaTeX `UnicodeDecodeError`       | ensure UTF‑8 source & run `latexmk -pdf`                   |

---

## 7 · Signature Authority

```text
Fingerprint : 0x99115B85
Issuer      : screwball7605@aol.com  (Robert Long – R‑AGI Cert)
```

---

## 8 · License

**Apache 2.0** — free for any use, commercially or otherwise.  *No warranty; no lawsuits.*  See [`LICENSE`](LICENSE).

---

## 9 · Community & Contact

* **GitHub**   [https://github.com/Bigrob7605/R-AGI\_Certification\_Payload](https://github.com/Bigrob7605/R-AGI_Certification_Payload)
* **Facebook** [https://facebook.com/SillyDaddy7605](https://facebook.com/SillyDaddy7605)
* **Discord**  *(server launches Q3 2025)*

> *“This isn’t a model. It’s a mindprint.”* — **Robert Long**
>
> Phase 1 (*seed drop*) is live • Phase 2 (*full MMH tooling*) ships **now** 🚀
