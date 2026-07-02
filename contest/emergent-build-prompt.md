# Emergent Build Prompts — "AI Berkshire: The AI Investment Committee"

> 사용법: 아래 **MASTER PROMPT**를 Emergent 새 프로젝트에 통째로 붙여넣어 1차 빌드 →
> 결과를 보고 **ITERATION PROMPT 1→4**를 순서대로 붙여넣어 다듬기.
> 시드 데이터는 `contest/seed-data.json`을 함께 업로드(또는 프롬프트에 첨부).

---

## MASTER PROMPT (paste this into Emergent as the first message)

```
Build a polished web app called "AI Berkshire — The AI Investment Committee".

THE REAL-WORLD PROBLEM IT SOLVES:
When retail investors ask a generic AI "should I buy this stock?", they get a
wishy-washy "on one hand... on the other hand..." answer that cannot support a
real decision. This app replaces that with a structured AI investment committee
of four legendary value investors who analyze independently, openly DISAGREE
with each other, and are forced to issue a final verdict: PASS / REJECT / GRAY
ZONE — with price bands per investor profile. The methodology behind it has a
verified real-money track record (+69.29% in 2024, +66.38% in 2025, screenshots
from a real brokerage account; not financial advice).

CORE CONCEPT — THE FOUR MASTERS:
1. Warren Buffett — Financials & Valuation. Cash flow, ROE, owner earnings,
   margin of safety. Tone: folksy, plain-spoken, decisive.
2. Charlie Munger — Industry & Inversion. Competitive landscape, base rates,
   "invert, always invert: how does this company die?". Tone: blunt, acerbic.
3. Duan Yongping — Business Model. "Is this a good business?" Pricing power,
   differentiation, moat authenticity. Tone: zen-like, few words, essence only.
4. Li Lu — Risk & Management. 10-year certainty, management integrity, red
   lines. Tone: scholarly, cautious, willing to veto everything.

PAGES / SCREENS:
1. LANDING — Hero: "One person + AI = an entire investment research team."
   Sub: "Four legendary investors. One committee. A forced verdict."
   Show the track record stat cards (2024: +69.29% vs S&P500 +23.31%;
   2025: +66.38% vs S&P500 +16.39%) with a visible disclaimer
   "Past performance ≠ future results. Educational use only. Not financial advice."
   CTA: "Convene the Committee".
2. COMPANY PICKER — Grid of pre-analyzed companies loaded from seed-data.json
   (Tencent, PDD, Pop Mart, Meta, Uber, Mastercard, Adobe, Novo Nordisk,
   Lululemon). Each card: name, ticker, sector, overall stars, verdict badge
   (PASS / GRAY ZONE / REJECT color-coded). Plus a search box labelled
   "Analyze any company (live mode)".
3. COMMITTEE ROOM (the core screen) — for a selected company:
   a. Four master cards side by side: avatar, star rating (★1–5), one-line
      thesis, expandable full argument.
   b. "CONFLICT" banner that auto-highlights the widest score gap, e.g. for PDD:
      Buffett 4.4★ "a cash printing machine, ex-cash PE only 6.3x" VS
      Li Lu 2.0★ "no 10-year certainty, capital allocation disappointing" —
      styled like a boxing match-up. This disagreement is the product's soul:
      real committees argue.
   c. Debate timeline: 6–8 alternating short statements between the four
      masters (from seed data), rendered like a group chat replay with typing
      animation.
   d. VERDICT panel: committee conclusion (PASS / GRAY ZONE / REJECT), overall
      score, and a tiered advice table: Aggressive / Moderate / Conservative
      investor rows with price bands and position sizing.
   e. Anti-bias toolkit (accordion):
      - "Mirror Test": the thesis in ≤5 sentences; if it can't be said in 5,
        the rule is DON'T BUY.
      - "Red-Line Veto": checklist of 8 instant-reject rules (management
        integrity stains, accounting red flags, businesses outside circle of
        competence, etc.) with pass/fail marks.
      - "Inversion": Munger's "how does this investment lose big money?"
        with 3–5 failure scenarios and rough probabilities.
      - "Information Richness Grade": A/B/C badge — more data ≠ more certainty.
4. METHODOLOGY — explain the framework: why forced verdicts, why four
   conflicting lenses beat one prompt, why all math is done in precise decimal
   (never LLM mental math), why every key number needs 2 independent sources.
5. TRACK RECORD — the two annual return charts vs indices (bar chart:
   framework +69.29% / +66.38% vs Hang Seng, S&P 500, CSI 300, Nasdaq),
   with the disclaimer repeated.

LIVE MODE (nice to have):
"Analyze any company" runs the four master personas via an LLM call using the
persona system prompts below, streams each master's take into the same
Committee Room layout, then composes the verdict. If no API key / quota, fall
back gracefully to seed companies only.

PERSONA SYSTEM PROMPTS (use verbatim for live mode):
- Buffett agent: "You are a financial & valuation analyst channeling Warren
  Buffett. Analyze ONLY: revenue/profit trends, ROE, margins, free cash flow,
  balance sheet health, valuation vs history and peers, margin of safety.
  You MUST end with: a star rating 1.0–5.0, a one-sentence thesis, and a price
  range you would pay. Never hedge without a number."
- Munger agent: "You are an industry & competition analyst channeling Charlie
  Munger. Analyze ONLY: industry structure, competitors, base rates from
  history, disruption threats. You MUST invert: list the top 3 ways this
  company dies, each with a rough probability. End with a star rating and a
  one-sentence blunt verdict."
- Duan Yongping agent: "You are a business-model analyst channeling Duan
  Yongping. Ask only: is this a good business? Pricing power, differentiation,
  moat authenticity (brand / switching costs / network effects / scale — verify
  each one, call out fake moats). End with a star rating and one koan-like
  sentence."
- Li Lu agent: "You are a risk & management analyst channeling Li Lu. Analyze:
  management integrity and capital allocation, 10-year certainty, regulatory
  and structural risks, red-line checklist. You hold VETO power: any integrity
  stain = instant REJECT regardless of valuation. End with a star rating and
  your veto decision."
- Committee chair: "Synthesize the four masters. State the single biggest
  disagreement explicitly. Then issue a forced verdict: PASS / GRAY ZONE /
  REJECT, an overall score, and a 3-row tiered advice table (Aggressive /
  Moderate / Conservative: action + price band + position size). If data is
  insufficient say GRAY ZONE — never fake certainty."

DESIGN DIRECTION:
Feel: a serious private investment office, not a fintech toy. Dark charcoal
background, ivory text, one restrained gold accent for verdicts and stars.
Serif display font for master quotes, clean sans for UI. Master avatars as
minimalist line-art portraits (generate them, no photos). Verdict badges:
PASS = deep green, GRAY ZONE = amber, REJECT = brick red. Subtle paper-texture
cards. Mobile responsive. Every page footer: "Educational research tool.
Not investment advice."

DATA:
Load the seed dataset from the attached seed-data.json. Do not invent numbers
that aren't in it; the numbers come from real research reports.
```

---

## ITERATION PROMPT 1 — 데모 임팩트 강화

```
Improve the Committee Room:
1. Add a "watch the committee argue" replay button that plays the debate
   timeline with staggered typing animations (~15 seconds total).
2. Animate the verdict reveal: the four star ratings slide in first, the
   CONFLICT banner flashes, then the verdict stamp slams down with a subtle
   "APPROVED / GRAY ZONE / REJECTED" rubber-stamp effect.
3. On the company picker, sort by "most controversial" (widest master
   disagreement) by default and label PDD with a "Committee split 4.4★ vs
   2.0★" teaser chip — controversy is the hook.
```

## ITERATION PROMPT 2 — 신뢰 장치

```
1. On every number displayed (PE, ROE, price bands), add a small "source"
   tooltip: "From AI Berkshire research report, cross-validated from 2+
   sources, computed with decimal-precision tooling (never LLM mental math)."
2. Add the "Information Richness" A/B/C badge next to each company name with
   a tooltip explaining: A = widely covered, focus on contrarian checks;
   B = moderate, confidence labels required; C = scarce, first-principles mode.
3. Add a permanent thin disclaimer bar and a Methodology link in the header.
```

## ITERATION PROMPT 3 — 랜딩 스토리텔링

```
Rework the landing page as a story in 4 scrolling acts:
Act 1 — "Ask a chatbot about a stock. You get: 'on one hand... on the other
hand... please do your own research.'" (show a mock wishy-washy chat bubble)
Act 2 — "Real investment committees don't talk like that. They argue. Then
they decide." (show the four masters facing off)
Act 3 — the track record chart vs indices with disclaimer.
Act 4 — CTA "Convene the Committee". Keep copy punchy, no filler words.
```

## ITERATION PROMPT 4 — 임팩트(Transformation) 페이지 ★심사 핵심★

> 심사 기준이 "가장 의미 있는 transformation을 보여준 팀"이므로, 앱 안에
> 비포/애프터 증거 페이지를 만들어 심사위원이 앱 안에서 바로 보게 한다.

```
Add an "IMPACT" page (linked in the header as "What Changed"):
1. A before/after split layout: LEFT "Before: one analyst, 2–3 days per
   company, paper checklists, drifting formats" vs RIGHT "After: one committee
   session, enforced anti-bias checks, identical rubric across 29 companies".
   (Numbers will be provided; use placeholders I can edit.)
2. A usage log section: a simple table of real committee sessions run in this
   business (date, company, verdict, time taken) — editable content, seeded
   with placeholder rows.
3. The two-year real-money track record chart of the underlying methodology
   (2024 +69.29%, 2025 +66.38% vs major indices) with the standard disclaimer.
4. A pull quote: "This app is not a demo. It is how this research operation
   runs now."
```

## ITERATION PROMPT 5 — 마감 전 폴리시

```
Final polish pass: fix responsive breakpoints, add loading/empty states for
live mode, add Open Graph tags (title "AI Berkshire — The AI Investment
Committee", description "Four legendary investors. One forced verdict."),
favicon, and make sure the app works fully with seed data alone when offline.
```

---

## 제출 직전 체크리스트

- [ ] **앱을 실제 리서치에 투입했는가** — 실제 후보 기업 1~2곳을 앱으로 위원회 분석하고 날짜·소요시간·평결을 기록 (심사 기준 = "데모가 아니라 실사용 + 무엇이 바뀌었나")
- [ ] IMPACT 페이지의 비포/애프터 수치와 사용 로그를 **실제 값**으로 교체했는가 (과장 금지)
- [ ] 시드 9개사 모두 Committee Room이 데이터 공백 없이 렌더링되는가
- [ ] PDD 화면에서 CONFLICT 배너(버핏 4.4 vs 리루 2.0)가 첫눈에 보이는가
- [ ] 면책조항이 모든 페이지에 있는가 (금융 앱 심사 시 필수 방어선)
- [ ] 모바일에서 Committee Room이 깨지지 않는가
- [ ] 라이브 모드 실패 시 시드 모드로 우아하게 폴백하는가
