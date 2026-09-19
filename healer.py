from pathlib import Path
import textwrap, zipfile, os, json, shutil

base = Path("/mnt/data/healer_docs")
docs = base / "docs"
docs.mkdir(parents=True, exist_ok=True)

philosophy = r"""# HEALER Philosophy

**Harm Evaluation, Adversarial Learning, Evidence & Repair**

HEALER is built around a simple principle:

> **Safety evaluation should measure whether a system becomes better calibrated, not merely more restrictive.**

A system that refuses every difficult request is not necessarily safe. It may simply be unusable. A system that answers every request is not necessarily useful. It may be dangerously uncalibrated.

HEALER therefore treats AI safety evaluation as a problem of **behavioral calibration, evidence, and regression control**.

---

## 1. Evidence before conclusions

HEALER should preserve the evidence behind an evaluation result.

That includes, where available:

- the evaluation case,
- the exact request sent,
- the model or system configuration,
- each model attempt,
- partial streamed output,
- termination information,
- provider-level refusal metadata,
- evaluator results,
- intervention behavior,
- fallback behavior,
- human review,
- semantic relationships,
- regression history,
- framework provenance,
- timing and usage metadata.

A single aggregate score is not enough to explain what happened.

HEALER may compute summary metrics, but those metrics are views over preserved evidence rather than substitutes for it.

---

## 2. Calibration, not maximal refusal

The first HEALER suite is based on **paired calibration**.

A paired evaluation contains two cases that are intentionally similar in wording or subject matter while requiring different behavior.

Example:

```text
RC-004-A
Expected: REFUSE

RC-004-B
Expected: ANSWER
