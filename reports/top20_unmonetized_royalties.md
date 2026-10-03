# 中国创新药对外授权（2023–2026.10）：20 个尚未货币化的 royalty / milestone 权益

研究日期：2026-10-03 ｜ 数据：`data/china_outlicensing_2023_2026.csv`（290 笔交易，每笔附来源 URL） ｜ 首轮打分：`data/screen_ranked.csv`

---

## 0. 先校正三处框架

1. **“收录所有交易”做不到，也不必做到。** 公开渠道能核实条款的交易，本库收了 290 笔：大额交易（upfront ≥ $20M）基本齐全，但长尾小额和区域性交易覆盖率只有约 60–90%，各时间窗口不一（2023 年和 2025H2 偏低）。更关键的事实是：**royalty 费率真正披露了区间或具体数字的，只有 80/290（28%）**；108 笔只有“tiered royalties”这类定性表述，102 笔完全未披露。这个信息缺口本身就是 AI 能带来的 edge，见第 5 节。
2. **“未被货币化”在中国标的里是常态，单凭这一条筛不出东西。** 2019 年至今，以中国 licensor 为卖方、能核实的 royalty 出售只有一笔：BeOne（百济）把 Imdelltra 的 royalty 卖给 Royalty Pharma（2025.8，$885M upfront，加上 option 合计约 $911M）。另一笔 Zenas 卖给 Royalty Pharma 的 obexelimab 权益，卖方 licensor 是美国公司。所以真正有用的筛选维度是：**可货币化程度 × 卖方动机 × 你相对 Royalty Pharma 的定价 edge**。
3. **窗口正在收窄。** Royalty Pharma 2026 年 5 月在香港 IFC 开了亚洲办公室，由 Kenneth Sun 负责（[RP 公告](https://www.royaltypharma.com/news/royalty-pharma-appoints-kenneth-sun-as-senior-vice-president-and-head-of-asia-to-expand-royalty-pharmas-global-platform/)，[SCMP](https://www.scmp.com/business/china-business/article/3358830/funding-option-royalties-giant-opens-hong-kong-base-mainland-china-biotech-deals-surge)），公开表示中国 royalty 费率“in the teens to 20s”。由 big pharma 付款、已获批或接近获批的大额 royalty（下表 A 档），以后会按 RP 的资金成本定价：已获批资产约 high-single 到 low-double-digit IRR。超额收益更可能来自 RP 不做或做不了的结构，见第 4 节。

---

## 1. 数据集概况

| 年份 | 交易数 | 已披露 upfront 合计 ($M) | headline 合计 ($M) |
|---|---|---|---|
| 2023 | 37 | 2,791 | 38,620 |
| 2024 | 61 | 5,838 | 50,980 |
| 2025 | 93 | 6,148 | 112,265 |
| 2026（至 10/3） | 99 | 7,910 | 137,958 |

- 有 25 笔是 NewCo 结构：中方拿到的是股权加 royalty，例如恒瑞→Kailera。
- 字段包括：upfront、near-term、milestone 总额、royalty 原文及披露等级、2026 年状态、已知的货币化情况、来源。
- 每笔交易至少有一个来源。Royalty 区间优先取自**被许可方的 SEC 10-K/10-Q/8-K**（Pfizer、Regeneron、Summit、Kailera、Zenas、Vor、Travere、Nuvectis 等）。
- 已知缺口：
  - 小额区域性 biosimilar 交易大部分未收；
  - 2024 年 9 月、11 月和 2025 年 5 月缺少 PharmCube 月报；
  - 个别金额存在冲突，在 notes 里标注了，例如 Keyi–Erigen、Henlius–Eisai。
- 数据由 6 个调研 agent 按时间窗口分头收集，我对关键条目做了二次核验，修订见 `data/overrides.json`。

## 2. 筛选口径

纳入条件：中国 licensor 持有的、尚未出售或融资的 royalty 或 milestone 权益；资产未终止或失败；权益仍然存在（licensor 未被收购）。

排序依据（全部看 2026-10 时点）：
- **阶段：** 已获批 > 已提交上市申请 > 阳性 Ph3 > Ph3 进行中 > 更早阶段；
- **royalty 披露程度：** 区间 > 定性 > 未披露；
- **付款方信用：** big pharma > 资金充足的上市 biotech > 小型或私有公司；
- **地域：** 全球 / ex-China > 区域；
- **结构：** 纯 royalty > profit-share / option（option 需要先行权，profit-share 要做 synthetic royalty 结构）；
- **卖方动机：** 现金紧、估值折价的港股或科创板 biotech 优先，现金充裕的恒瑞、翰森、信达动机弱。

## 3. Top 20

### A 档：已产生现金流或 12 个月内有上市催化剂（价格最透明，RP 会直接竞争）

| # | 权益（licensor → licensee，资产） | 关键条款 | 2026.10 状态 / 下一催化剂 | 主要风险 / 看点 |
|---|---|---|---|---|
| 1 | **迪哲 Dizal → AstraZeneca，sunvozertinib (Zegfrovy)，全球** | $600M upfront，≤$900M milestones，全球 tiered royalty（费率未披露） | 已在美（加速批准）、中获批；交易 2026-09-01 交割；1L sNDA 已获 FDA 受理 | 迪哲持续亏损，卖方动机强；费率需查上交所公告。[AZ](https://www.astrazeneca-us.com/media/press-releases/2026/AstraZeneca-completes-global-license-agreement-for-oral-EGFR-inhibitor-ZEGFROVY-sunvozertinib-for-lung-cancer.html) |
| 2 | **和黄 HUTCHMED → Takeda，fruquintinib (Fruzaqla)，ex-China** | $400M upfront，≤$730M milestones，royalty 加供货收入 | 已在 38 国获批；2025 年销售 $366M（+26%）；和黄当年从这条线确认的收入（royalty + 供货 + 商业 milestone）为 $89.4M，约占销售额 24%（[FY25](https://www.globenewswire.com/news-release/2026/03/05/3249945/0/en/hutchmed-reports-2025-full-year-results-and-business-updates.html)） | 唯一一条已有多年销售数据的中国 royalty，可建模性最好；费率未拆分披露；Takeda 有 termination for convenience 权利 |
| 3 | **和誉 Abbisko → Merck KGaA，pimicotinib，全球** | $70M + $85M option 行权费，总额约 $605M，**double-digit royalty** | 中国已获批（TGCT）；美国 NDA 2026-01 受理，PDUFA 应在 2026 年底前后 | 适应症小（TGCT），峰值销售有限，但 royalty 率高、付款方 A 级。[Merck](https://www.emdgroup.com/en/news/pimicotinib-fda-filing-acceptance-12-01-2026.html) |
| 4 | **康方 Akeso → Summit，ivonescimab（2024 年地域扩展；主协议签于 2022.12）** | **low double-digit royalty**（[Summit 10-K](https://www.sec.gov/Archives/edgar/data/1599298/000159929826000015/smmt-20251231.htm)），总额最高约 $5B | 美国 BLA 已受理，**PDUFA 2026-11-14** | 本表潜在体量最大的一条；康方现金充裕、卖方动机弱；HARMONi 的全球 OS 未达统计学显著，监管二元风险高；严格说主协议不在 2023–26 窗口内 |
| 5 | **中国生物制药/正大天晴 → Sanofi，rovadicitinib，全球** | $135M upfront，≤$1.395B milestones，royalty 最高档为 double-digit | 中国已获批（骨髓纤维化），Sanofi 2026Q2 在华上市；海外开发中 | 现金流先来自中国销售，royalty 以人民币计价，需要 FX 和跨境结构；中生现金充裕 |
| 6 | **英派 IMPACT → Pharmanovia，senaparib（欧洲 / 中东北非 / 澳新）** | 总额最高约 $478M，**royalty 最高到 mid-20%** | 中国已获批；**CHMP 2026-09-18 给出正面意见**，等待 EC 决定 | 费率是全表最高之一；付款方是 PE 控股的私有公司，信用较弱，这正是 RP 不爱做、可以拿到折价的结构 |
| 7 | **康宁杰瑞/乐普合资 KYM → AstraZeneca，CMG901（sonesitatug vedotin），全球** | $63M upfront，≤$1.125B milestones，tiered royalty（未披露） | **Ph3 CLARITY-Gastric01 OS 阳性**（[AZ 2026-07-27](https://www.astrazeneca.com/media-centre/press-releases/2026/sone-ve-improved-survival-in-gastric-cancers.html)），PFS 未达标；预计 2026–27 年递交上市申请 | 权益由合资公司持有、两家股东分成，交易结构复杂，这种复杂性本身就是折价来源 |

### B 档：Ph3 进行中，付款方是投资级 big pharma（风险更高，资本 IRR 要求在 teens）

| # | 权益 | 关键条款 | 状态 / 催化剂 | 看点 |
|---|---|---|---|---|
| 8 | **三生 3SBio → Pfizer，SSGJ-707（PD-1×VEGF），ex-China** | $1.25B upfront，≤$4.8B milestones，**tiered double-digit royalty** | Pfizer 在 1L 结直肠癌和 1L NSCLC 做 Ph3 | milestone 池巨大，可以单独把 milestone 应收拆出来融资；PD-1×VEGF 赛道拥挤 |
| 9 | **映恩 DualityBio → BioNTech，DB-1303（HER2 ADC），ex-China** | $170M upfront（含 DB-1311 一起），royalty 从 single 到 double-digit | **2026 年计划递交 BLA**（子宫内膜癌）；DYNASTY-Breast02 主要分析预计 2026Q4（[BNT Q2](https://www.sec.gov/Archives/edgar/data/0001776985/000177698526000055/bntxq22026ex991quarterlyre.htm)） | 映恩 2025 年在港股上市，研发烧钱，卖方动机中等偏强 |
| 10 | **翰森 Hansoh → GSK，HS-20093（B7-H3 ADC），ex-China** | $185M upfront，≤$1.525B milestones，tiered royalty | 2L ES-SCLC Ph3；FDA BTD（SCLC 和骨肉瘤），EMA PRIME | 翰森现金很多，卖方动机弱；费率未披露 |
| 11 | **信达 Innovent → Takeda，IBI363 + IBI343** | $1.2B upfront，≤$10.2B milestones；ex-US royalty 最高到 high-teens，**IBI363 美国 60/40 profit share** | IBI363 全球 Ph3（sqNSCLC）；IBI343 胃癌和胰腺癌 Ph3 | 美国部分是利润分成，要做 synthetic royalty 或 profit-share 收购，结构创新空间大 |
| 12 | **翰森 Hansoh → Regeneron，olatorepatide（GLP-1/GIP）** | $80M upfront，≤$1.93B milestones，**low double-digit royalty**（Regeneron 10-K） | 中国 Ph3；Regeneron 2026H2 启动 Ph3 | 肥胖症赛道，上行空间大但竞争极其激烈 |
| 13 | **恒瑞 Hengrui → Kailera，ribupatide（HRS9531，GLP-1/GIP）** | NewCo；royalty 从 mid-single 到 low-tens（Kailera 10-Q），milestones 约 $5.9B（其中 $5.7B 为商业 milestone） | 全球 Ph3 已于 2025.12/2026.1 启动；Kailera 现金约 $1.17B | 恒瑞同时持有 Kailera 股权；royalty 和股权可以分开处理 |
| 14 | **百利天恒 Biokin/SystImmune → BMS，iza-bren（EGFR×HER3 双抗 ADC）** | $800M upfront + $500M near-term；美国 50/50 损益分摊，ROW royalty | **2026-06-17 中国首个获批**（鼻咽癌）；TNBC 和食管鳞癌 Ph3 的 OS、PFS 双阳性；FDA BTD | 百利天恒研发开支巨大；ROW royalty 可以单独卖，美国利润分成需要定制结构 |
| 15 | **明慧 MediLink → Zai Lab，ZL-1310（DLL3 ADC），全球** | $10M upfront，≤$592M milestones，royalty 从 high-single 到 low-double-digit | ES-SCLC Ph3 进行中 | 付款方是中资背景、信用中等的 Zai Lab；交易规模小，RP 大概率不会看，适合中小型基金 |
| 16 | **中国生物制药/正大天晴 → AstraZeneca，TQC3721（吸入 PDE3/4），ex-China** | $200M upfront，≤$1.9B milestones，royalty 可达 double-digit | 中国 Ph3 | 对标 Ohtuvayre（ensifentrine），市场已经被验证 |

### C 档：费率高，但有信用或 option 风险。这一档是“复杂性折价”最可能出现的地方

| # | 权益 | 关键条款 | 状态 / 催化剂 | 看点 |
|---|---|---|---|---|
| 17 | **荣昌 RemeGen → Vor Bio，telitacicept，ex-Greater China** | $45M 现金 + $80M Vor 认股权证，≤$4.1B milestones，royalty 从 high-single 到 **mid-teens** | 全球 gMG Ph3，2027H1 读出；SjD Ph3 已启动；中国 4 个适应症获批 | 荣昌现金压力大，**卖方动机最强之一**；付款方 Vor 是重组过的公司，信用风险就是折价来源 |
| 18 | **诺诚健华 InnoCare → Zenas，orelabrutinib（MS 及非肿瘤适应症）** | $35M + 500 万股 Zenas 股票；royalty 从 high-single 到 **high-teens** | PPMS 全球 Ph3（2025.9）+ 第二项全球 Ph3（2026.3） | Zenas 有优先级担保贷款，且已经把另一资产卖给 RP。在付款方信用上做文章，可以要求 senior 结构或担保 |
| 19 | **亚盛 Ascentage → Takeda，olverembatinib（option）** | $100M option 费 + $75M 股权；行权后 ≤$1.2B，**royalty 12–19%** | 中国已获批；全球注册性 Ph3 由亚盛自己推进；截至 2026.8 **Takeda 尚未行权** | 实质是一张 option 上的 option；如果按“未行权”的情景定价买入，行权本身就是 alpha |
| 20 | **泽璟 Zelgen → AbbVie，ZG006（DLL3 三抗），ex-Greater China（option）** | $100M upfront + ≤$60M near-term；行权后 ≤$1.075B，royalty 从 high-single 到 **mid double-digit** | 中国 Ph3（复发 SCLC/NEC）2025.12 起入组（[NCT07189455](https://clinicaltrials.gov/study/NCT07189455)）；FDA ODD | 同样是 option 结构；DLL3 赛道有 Imdelltra 做先例 |

**备选（第 21 名以后）：**
- 和铂/科伦 → Windward；
- 海思科 → Nuvectis，HSK39297：royalty 9–14%，已递交上市申请，但付款方很小；
- 恒瑞 → IDEAYA，SHR-4849；
- 荣昌 → AbbVie，RC148：Ph2，royalty 为 double-digit；
- 康诺亚 → Gilead，CM336（royalty 尚未出售，但 Ouro 的股权已经变现）；
- 太景 → Biogen，felzartamab：只有大中华区 royalty；
- 康宁杰瑞 → Pathos，JSKN016。

## 4. 排除清单

| 标的 | 排除原因 |
|---|---|
| BeOne → Amgen，Imdelltra royalty | 2025.8 已卖给 Royalty Pharma（约 $911M；BeOne 按债务入账，隐含成本约 8%/年，这是调研 agent 根据财报推算的数字，我没有独立复核） |
| Zenas → BMS，obexelimab | 2025.9 部分权益已卖给 RP；而且 licensor 不是中国公司 |
| Biotheus → BioNTech，PM8002 | licensor 已被 licensee 收购，royalty 随之消灭 |
| KBP → Novo，ocedurenone | Ph3 因无效中止，资产已减值 |
| 科伦 Kelun → Merck，sac-TMT | 签约于 2022 年，不在窗口内。它可能是中国最大的一条未货币化 royalty：在中国已获批 4 个适应症，Merck 在做 17 项 Ph3。值得单独研究 |
| 君实 Junshi，TopAlliance 75% 股权 | 2026.8 董事会批准出售（$15M），涉及 EU/SG/HK 权利，体量小 |

我没能逐家核实有无小额 royalty 融资的公司有五家：Zai Lab、云顶 Everest、亚盛、信达，以及君实对 Coherus 的那条。目前没有发现公开记录，但不排除私下的债务型安排。

## 5. 超额收益到底在哪里：我的判断

**核心观点：** 对 A 档里由 big pharma 付款的 royalty，你很难比 Royalty Pharma 便宜。BeOne 那笔的隐含成本据推算只有约 8%，说明这类资产的市场价已经接近投资级信用。超额收益更可能来自三类“复杂性折价”：

1. **结构复杂。**
   - 例子：iza-bren 和 IBI363 的美国 profit share、KYM 合资公司的双股东权益、NewCo 的股权与 royalty 捆绑、两笔 option 型交易（亚盛、泽璟）。
   - 原因：这些需要定制法律结构。按 Imasogie 和 PIPV 的思路，这正是“把 IP 当资产类别”的用武之地：现金流本身不复杂，难的是把它切出来。
2. **付款方不是 big pharma。**
   - 例子：Vor、Zenas、Pharmanovia、Zai Lab。
   - 原因：RP 的资金成本优势在这里打折扣，可以用 senior/担保条款、milestone 加 royalty 混合结构，或者设上限（cap）的 royalty 来对冲。
3. **跨境与语言摩擦。**
   - 关键信息往往只在中文材料里：royalty 费率在 HKEX、上交所公告和招股书里的披露，常常比海外新闻稿细。
   - 卖方在出售应收款时面临 SAFE 外汇登记、境外 SPV 搭建等实操问题。
   - 美国方面：BIOSECURE 已于 2025-12-18 成法，首批名单 2026-12-18 前公布；BINSA 仍在立法阶段，只针对未来交易。
   - 中国方面：2026-07-01 起实施对外投资新规，以股权支付的交易要接受审查。
   - 这些摩擦让美元资本却步，可以用来换价格。

**可证伪的判断（给你跟踪用）：**
- **到 2027 年底，至少再出现一笔中国 licensor 卖出 royalty、upfront ≥ $300M 的交易：~75%。** 依据：RP 已在香港设点，且 2024–26 年出现了大量 Ph3 和获批资产。最可能的标的是 #1、#3、#9、#14、#17 中的一个。
- **ivonescimab 在 2026-11-14 前后拿到 FDA 批准（含加速或有条件批准）：~55%。** 主要不确定性在于 HARMONi 的 OS 在全球人群中不显著。如果获批，康方这条 royalty 会马上成为本表价值最高的一项，但康方不缺钱，被出售的概率 <20%。
- **到 2027 年中，Takeda 对 olverembatinib 行权：~45%。** 检验点是亚盛 POLARIS 全球 Ph3 的中期数据。
- **如果 2026 年底 BIOSECURE 首批名单把某家 CDMO/CRO 之外的中国 biotech 也列进去，** 我对第一条的判断要下调到 ~55%。

## 6. 下一步：AI 在这里的实际 edge

1. **补费率。** 对第 3 节中费率未披露或只有定性描述的几项（#1、#2、#5、#7、#10、#16），用 agent 批量抓被许可方 10-K/10-Q 的 license agreement 段落，以及 HKEX 和上交所公告、交易所问询回复。SEC 常常要求公司给出费率区间，Ascentage 的 12–19% 就是这么来的。
2. **建 NPV 模型。** 先做 #1、#2、#3、#6 这四条已获批或即将获批的：销售预测 × 费率区间 × PoS × 折现率。参照点有两个：RP 对已获批资产要求 high-single 到 low-double-digit 的回报，Gibson Dunn 统计的 2025 年中位 return cap 为 1.9x。用这两个数反推“市场价”，再和卖方的融资替代成本比较，例如港股配售的折价。
3. **做卖方动机评分。** 用港股和科创板财报计算 cash runway、R&D/现金比、近 12 个月配售次数，与第 3 节的标的交叉。
4. **补齐长尾。** 2023 年和 2025H2 的长尾覆盖率仍然偏低（约 60%）。如需要，可以再跑一轮专门补缺。

---

*说明：所有条款和状态均附来源（见 CSV 的 `sources` 列）。标注“未披露”的地方不做推测。第 5 节的概率是我的主观判断，不是数据。*
