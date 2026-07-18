# 服务化蓝图：从个人 Skill 仓库到可发布产品

> 状态：设计文档（发掘报告合并路线图 Phase 4 产出）
> 前置：Phase 1 插件打包 ✅ · Phase 2 交锋+记忆 ✅ · Phase 3 MCP 数据层 ✅ · backtest.py ✅

---

## 一、定位

**一句话**：把"经过实盘验证的四大师价值投资研究系统"作为 Claude 生态的专业插件/托管服务发布。

对标与差异（详见发掘分析）：

| 对标 | 它有什么 | 我们的差异 |
|------|---------|-----------|
| virattt/ai-hedge-fund（~50k★） | 14 位大师 persona、回测器 | 它是教育演示；我们有**真实实盘记录 + 判断可对账**（backtest.py） |
| TauricResearch/TradingAgents | 结构化辩论、记忆 | 已吸收其模式；我们叠加**中文市场 + 段永平/李录东方价值投资视角**（英文世界稀缺） |
| anthropics/financial-services | 官方打包/分发标准 | 已采用其模式；它面向机构工作流，我们面向**个人投资者的决策纪律** |
| quant-sentiment-ai/claude-equity-research | 插件市场分发 | 单命令工具；我们是**全流程系统**（发掘→研究→检查单→论文→实盘→复盘） |

**核心护城河**（保持，不稀释）：
1. 实盘验证的纪律闭环（镜子测试 → thesis → 实盘记录 → backtest 对账）
2. 四大师真实"交锋"设计（分歧保留，不给假共识）
3. 数据严谨性工具链（financial_rigor / report_audit / check）
4. 多市场覆盖（A股/港股/美股）+ 中文深度研究语料 2000+ 篇

---

## 二、发布路径（两条，可并行）

### 路径 A：Claude Code 插件市场（已就绪，零成本）

```
/plugin marketplace add shualoalumin/ai-berkshire
/plugin install ai-berkshire@ai-berkshire
```

- 现状：Phase 1 已完成打包，推送即发布
- 作用：**获客与社区**——开源免费，积累用户、issue 反馈、star 信誉
- 迭代：commit-SHA 版本自动更新；正式版本节点改用语义化版本 + CHANGELOG

### 路径 B：Managed Agents API（订阅服务形态）

参照 anthropics/financial-services 的 managed-agent 模式：
- 同一套 skills 以 `/v1/agents` 部署为托管 Agent，用户无需装 Claude Code
- 前端可以是网页/微信小程序/公众号后台，后端调用托管 Agent
- 需要：agent.yaml 定义、部署脚本（deploy-managed-agent.sh 模式）、用量计费

---

## 三、变现分层（参照 claude-equity-research 的商业化路径）

| 层级 | 内容 | 定价思路 | 前置条件 |
|------|------|---------|---------|
| **Free（开源插件）** | 18 个 skill 全量、工具链、文档 | 免费（MIT） | 已就绪 |
| **Pro（内容订阅）** | 研究报告库持续更新、决策记忆库、季度 thesis 追踪示范、backtest 对账公开 | 按月订阅（公众号/知识星球/Substack 均可承载） | 报告英文化（触达英文市场时） |
| **Service（托管 Agent）** | 路径 B 的 API 服务：用户输入持仓/标的，返回全流程研究 | 按用量或按席位 | Managed Agent 部署 + 计费 |
| **B2B（白标）** | 面向财富管理/投顾机构的定制皮肤与私有数据接入（FactSet/S&P 等 MCP 已在 claude.ai 目录可接） | 项目制 | 有 Service 层案例后再谈 |

**冷启动顺序建议**：Free 插件冲量 → 用 backtest 对账建立公信力 → Pro 内容订阅（最轻）→ Service。

---

## 四、信任基建（这个产品卖的就是"可信"）

1. **判断对账公开化**：`scripts/backtest.py` 定期跑，输出进 `reports/`，赢和输都公示。
   第一条记录就是 PDD 买入后 -17%（截至 2026-07）——公开它，比 100 句"我们很准"更有说服力。
2. **数据准出流程**：所有发布报告过 `report_audit.py` 抽检（已有）。
3. **免责声明标准化**：所有输出面（插件 README、报告模板、API 响应）统一附
   "教育与研究目的，不构成投资建议"——ai-hedge-fund 同款定位，规避投顾牌照问题。
   涉美用户注意 SEC 对 investment adviser 的定义；涉中用户注意证券投资咨询业务资质。
   **在取得合规意见前，不做个股买卖指令式输出的付费服务**（研究框架/教育内容风险低得多）。

---

## 五、执行清单（按优先级）

- [ ] 插件市场正式发布：合并本分支 → main，验证安装链路
- [ ] README 英文版补齐插件安装 + backtest 展示（README_EN 已有底子）
- [ ] 建立 `reports/回测对账/` 目录，每季度跑一次 backtest.py 并入库
- [ ] skills 英文版（服务英文市场的前置；报告库可保持中文，skills 是产品本体）
- [ ] Managed Agent PoC：单 skill（investment-checklist）先行部署试水
- [ ] 定价页与免责声明文案（法务审阅后再收费）

---

> 本文档是方向设计，非承诺排期。所有变现动作前置条件：合规确认 + Free 层已验证需求。
