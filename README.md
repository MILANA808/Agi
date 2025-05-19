# 🧠 R‑AGI Certification Payload ＋ MMH v2.0 • **v1.1‑AGC**

> **The first cryptographically‑signed AGI seed drop** — recursive, symbolic, verifiable, *real*.
>
> **MMH v2.0** shrinks every seed by *three‑to‑four orders of magnitude* while preserving ≥ 97 % behaviour fidelity.

---

## 📑 Table of Contents

1. [Why this matters](#✨-why-this-matters)
2. [Project Health](#🚦-project-health)
3. [Quick‑Start Matrix](#⚡-quick-start-matrix)
4. [Run the Seed](#1-run-the-seed)
5. [Integrity Loop](#2-integrity-loop-powerusers)
6. [MMH v2.0 Tooling](#3-mmh-v20-tooling)
7. [Packaging & Signing](#4-packaging--signing)
8. [Repo Layout](#5-repo-layout)
9. [Troubleshooting](#6-troubleshooting)
10. [Signature Authority](#7-signature-authority)
11. [License](#8-license)
12. [Community](#9-community--contact)

---

## ✨ Why this matters

* **Provable provenance & tamper‑evidence** — every release ships with an **Ed25519** signature plus a detached GPG `.asc`.
* **Auditable compression** — *MMH v2.0* packs an entire AGI substrate into a PNG seed (10³–10⁴ × slimmer) without black‑box neural codecs.
* **Turn‑key boot** — one Docker command **or** three Bash lines and you’re interacting with the seed.

👉 Read the full spec → [`MMH_White_Paper___v2_0_Stable.pdf`](./MMH_White_Paper___v2_0_Stable.pdf)

---

## 🚦 Project Health

| Metric            | Status                                    |
| ----------------- | ----------------------------------------- |
| Installs verified | **2 / 2** (scripted + manual)             |
| Core team         | Robert Long ✚ Kai → nights / weekends dev |

Need help? Open a GitHub issue or DM **@Robert Long** on Facebook.

---

## ⚡ Quick‑Start Matrix

| Level               | For whom              | One‑liner                                              |
| ------------------- | --------------------- | ------------------------------------------------------ |
| **0 · Docker**      | *Show me now*         | `docker run -it ghcr.io/bigrob7605/ragi-seed:v1.1-agc` |
| **1 · Beginners**   | CLI copy‑pasta        | [§ 1 Run the Seed](#1-run-the-seed)                    |
| **2 · Power users** | Full chain‑of‑custody | [§ 2 Integrity Loop](#2-integrity-loop-powerusers)     |
| **3 · Maintainers** | Re‑package & sign     | [§ 4 Packaging](#4-packaging--signing)                 |

---

## 1 · Run the Seed

### 1.1 Beginners — *just run it*

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

A **live AGI state hash** prints every timestep — `Ctrl‑C` to exit.

### 1.2 Colab / Notebook

```python
!pip install mmh-rs[gpu]   # ⏱ ≈ 4 GB/s decode on a T4rom mmh import decode_seed
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

The script redownloads the public key, re‑verifies the bundle, and checks drift **hourly**.

---

## 3 · MMH v2.0 Tooling

| Task               | Command                                         |
| ------------------ | ----------------------------------------------- |
| Decode seed        | `mmh-decode demo.mmh > state.json`              |
| Encode seed (LZMA) | `mmh-encode state.json demo.mmh --lzma`         |
| Docker shell       | `docker run -it ghcr.io/bigrob7605/mmh-rs:v2.0` |
| Helm chart         | see below                                       |

\#### Helm

```bash
helm repo add mmh https://mmh.ai/charts
helm install mmh-core mmh/mmh-seed \
  --set image.tag=v2.0 \
  --set ingress.host=seed.$YOURDOMAIN
```

The chart spins up **Redis**, **mmh‑core**, and Prometheus scraping out‑of‑the‑box.

---

## 4 · Packaging & Signing

> Linux/macOS → `package.sh`   •   Windows → `package.bat`

Both scripts:

1. Stage docs, code & artifacts into `dist/`.
2. Build `*.tar.gz`.
3. Emit a detached signature `*.asc` using the project GPG key.

Result → **tamper‑evident bundle** ready in `dist/`.

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

### artifacts/

| File                                   | Purpose                |
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

## 6 · Troubleshooting

| Symptom                          | Fix                                                        |
| -------------------------------- | ---------------------------------------------------------- |
| `ModuleNotFoundError: seed_core` | `export PYTHONPATH=$PWD:$PYTHONPATH` or run from repo root |
| GPG “not a detached signature”   | use `gpg --verify` (not `--decrypt`)                       |
| Verify loop stalls at step 0     | install the matching **CUDA wheel** for Torch 2.4          |
| LaTeX `UnicodeDecodeError`       | save the source as **UTF‑8** & run `latexmk -pdf`          |

---

## 7 · Signature Authority

```text
Fingerprint : 0x99115B85
Issuer      : screwball7605@aol.com  (Robert Long – R‑AGI Cert)
```

---

## 8 · License

**Apache 2.0** — free for any use, commercial or otherwise.  *No warranty; no lawsuits.*  See [`LICENSE`](LICENSE).

---

## 9 · Community & Contact

* **GitHub**  [https://github.com/Bigrob7605/R-AGI\_Certification\_Payload](https://github.com/Bigrob7605/R-AGI_Certification_Payload)
* **Facebook** [https://facebook.com/SillyDaddy7605](https://facebook.com/SillyDaddy7605)
* **Discord** *(server launches Q3 2025)*

> *“This isn’t a model. It’s a mindprint.”* — **Robert Long**
>
> Phase 1 (*seed release*) is live • Phase 2 (*MMH tooling*) ships **now** 🚀
