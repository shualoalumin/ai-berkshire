# Contest Submission Package — "AI Berkshire: The AI Investment Committee"

> **심사 루브릭 (Raj Shamani편 원문에서 확인, Fabrizio편도 동일 구조로 추정):**
> 1. 자기 비즈니스의 **실제 문제**를 특정하고
> 2. Emergent로 소프트웨어를 빌드하고
> 3. **데모가 아니라 실제 운영에 투입**하고 ("This isn't about building a demo")
> 4. **무엇이 바뀌었는지 제출** — "가장 의미 있는 transformation을 보여준 상위 3팀"이 수상
>
> 즉 이건 앱 완성도 대회가 아니라 **비포/애프터 증명 대회**입니다. 아래 제출문은 이 4단계 구조에 정확히 맞춰져 있습니다.
>
> 사용법: 아래 영어 텍스트를 Emergent 제출 폼/쇼케이스 설명란에 붙여넣기.
> `[FILL]` 표시는 **실제 수치로 교체 필수** — 과장 금지, 추정치는 "~" 표기.
> 제출 전 페이지에서 확인할 것: 정확한 마감 시각, 참가 자격(Fabrizio편이 글로벌 오픈인지), 제출 필드, 데모 영상 요구 여부.
> **제출 전 반드시: 빌드한 앱을 실제 리서치 워크플로에 최소 며칠 투입하고, 실제 분석 1~2건을 앱으로 수행한 기록을 남길 것.** (아래 3단계 참조)

---

## App Name

**AI Berkshire — The AI Investment Committee**

## One-liner

Four legendary value investors. One committee. A forced verdict — because "on one hand, on the other hand" never made anyone a decision.

## My Business (Step 0 — who is entering)

I run **AI Berkshire**, a one-person investment research operation: 180+ published research reports covering 29 companies in depth, a public research repository, a paid-attention readership via WeChat articles, and a real-money portfolio managed on this research (2024: +69.29%, 2025: +66.38%, verified brokerage statements).

One person doing the work of a research team is the business — and it had a real bottleneck.

## Step 1 — The Real Problem in My Business

A rigorous multi-perspective company analysis — business model, financials, industry, risk, each argued separately and then forced to a verdict — used to cost me **[FILL: e.g. 2–3 days] per company** of manual orchestration: running each analytical lens separately, reconciling conflicts by hand, rebuilding the same verdict tables every time, and fighting my own confirmation bias with paper checklists.

The deeper problem: generic AI assistance makes this *worse*, not better. Ask a chatbot "should I buy this stock?" and you get a balanced essay that ends with "please do your own research." It *looks* right and *decides* nothing. My readers face the same problem at larger scale.

Real investment committees don't work that way. They argue. Four people with different lenses see different truths, clash openly — and then they are **forced to vote**.

## Step 2 — What I Built on Emergent

AI Berkshire (the app) convenes a virtual investment committee of four legendary investors, each with a strictly separated mandate:

- **Warren Buffett** — financials & valuation: "What is it worth, and what's the margin of safety?"
- **Charlie Munger** — industry & inversion: "Invert: how does this company die?"
- **Duan Yongping** — business model: "Is this actually a good business?"
- **Li Lu** — risk & management, **with veto power**: "Is there 10-year certainty?"

They analyze independently, disagree in the open (the app literally stages the conflict — for PDD, Buffett scores it 4.4★ "a cash machine at 6.3x ex-cash earnings" while Li Lu scores 2.0★ "no 10-year certainty — veto on heavy positions"), and then the committee is forced to a verdict: **PASS / GRAY ZONE / REJECT**, with price bands and position sizing for aggressive, moderate, and conservative investors.

Built-in anti-self-deception machinery — the part generic AI analysis is missing:

- **The Mirror Test** — if the thesis can't be stated in 5 sentences, don't buy. No exceptions.
- **Red-Line Veto** — 8 instant-reject rules (management integrity stains kill any deal, at any price).
- **Inversion Panel** — every company ships with its own "how this loses big money" scenarios.
- **Information Richness Grade (A/B/C)** — because more data ≠ more certainty.
- **No LLM mental math** — every displayed figure was computed with decimal-precision tooling and cross-validated from 2+ sources.

## Step 3 — Used in Real Operations (not a demo)

The app is now the front end of my actual research workflow:

- **[FILL]** live committee sessions run on real candidate companies since building it (name the companies and dates — e.g. "used it to re-underwrite [company] on [date] ahead of earnings")
- 9 companies from my existing coverage universe (Tencent, PDD, Pop Mart, Meta, Uber, Mastercard, Adobe, Novo Nordisk, Lululemon) migrated into the committee format as the working knowledge base I consult before any position change
- **[FILL if true]** shared with my readers / used to produce a published article

## Step 4 — What Changed (the transformation)

| Before (manual orchestration) | After (committee app on Emergent) |
|---|---|
| [FILL: e.g. 2–3 days] per full four-lens company analysis | [FILL: e.g. under 1 hour] per live committee session |
| Verdict format drifted between reports; hard to compare companies | Identical rubric, verdict, and tiered price-band table across all 29 covered companies |
| Anti-bias checks (mirror test, red lines, inversion) lived on paper and were skippable | Enforced in the product — a verdict cannot render without them |
| Research conclusions locked in long-form documents readers rarely finish | A committee room a reader can replay in 60 seconds |

The methodology this app operationalizes is not hypothetical — it has run real money for two years:

- **2024: +69.29%** (vs S&P 500 +23.31%, Hang Seng +17.67%)
- **2025: +66.38%** (vs S&P 500 +16.39%, Hang Seng +27.77%)

Two consecutive years beating every major global index by 39–52 percentage points, verified with real brokerage statements. The app is how that operation now runs day to day.

*Disclaimer shown throughout the app: past performance does not guarantee future results; educational research tool, not investment advice.*

## Why Emergent

The entire app — multi-persona committee logic, staged debate replay, verdict engine, live LLM mode with graceful fallback — was built on Emergent from natural-language prompts. What used to require a quant team and a front-end team took one person and one conversation.

---

## 60-Second Demo Script

| t | 화면 | 말/자막 |
|---|------|--------|
| 0–8s | 랜딩 Act 1 (물에 물 탄 챗봇 답변 목업) | "Ask AI about a stock. This is what you get." |
| 8–15s | 랜딩 Act 2→3 (4대가 대면 + 트랙레코드 차트) | "Real committees argue. This methodology returned +69% and +66% in two real-money years." |
| 15–35s | PDD Committee Room — 디베이트 리플레이 재생 | "Watch Buffett call it a cash machine — and Li Lu veto it anyway." CONFLICT 배너 강조 (4.4★ vs 2.0★) |
| 35–45s | 평결 스탬프 애니메이션 + 성향별 가격 밴드 표 | "Then the committee is FORCED to decide. Gray zone. Position sizes. Price bands." |
| 45–55s | 미러 테스트 / 레드라인 거부권 / 인버전 패널 빠르게 스크롤 | "Five-sentence mirror test. Eight red lines. 'How does this die?' — anti-self-deception, built in." |
| 55–60s | 라이브 모드에 아무 티커 입력 → 위원회 소집 | "Convene the committee on any company. AI Berkshire — built on Emergent." |

## Social Copy (X/Twitter)

> Generic AI: "on one hand… on the other hand… DYOR 🤷"
>
> My app: Buffett 4.4★ vs Li Lu 2.0★ — fight, then a FORCED verdict with price bands.
>
> AI Berkshire: an AI investment committee of 4 legendary investors. Methodology returned +69%/+66% in 2 real-money years.
>
> Built on @emergent_sh 👇 [link]

## Social Copy (짧은 버전)

> I built an AI investment committee where Buffett, Munger, Duan Yongping and Li Lu argue about your stock — and are forced to issue a verdict. No more "on the other hand." Built on @emergent_sh [link]

---

## 제출 필드 예상 Q&A

**Q. What problem does it solve?**
Retail investors get analysis that never concludes. This forces structured multi-perspective disagreement into an actionable verdict with explicit anti-bias safeguards.

**Q. Who is it for?**
Self-directed retail investors, investing clubs, finance educators teaching decision discipline.

**Q. What makes it different?**
(1) Adversarial multi-persona design — the disagreement is the product; (2) forced verdicts with position sizing; (3) built-in anti-self-deception toolkit; (4) a real, two-year, index-beating track record behind the methodology — with disclaimers, not hype.

**Q. What changed in your business after building it?**
Full four-lens company analysis went from [FILL: days] of manual orchestration to [FILL: a single session]; verdict format is now identical across all 29 covered companies; the anti-bias checklist went from skippable paper to enforced product logic; and my published research now ships with a replayable committee room instead of a 40-page document.
