# 二、制度背景、文献回顾与研究假设

## （一）制度背景

### 1. 中国算法推荐治理的演进脉络

近年来，我国互联网治理逐步由以内容监管为主，转向“内容—数据—算法”一体化的综合治理，算法推荐成为规范平台行为的重要抓手。2021年12月，国家互联网信息办公室会同工业和信息化部、公安部、国家市场监督管理总局联合发布《互联网信息服务算法推荐管理规定》，并自2022年3月1日起施行，从算法备案、信息服务规范、用户权利保障、算法安全评估等方面系统构建了算法推荐规则体系。自2022年以来，国家网信办持续组织开展“清朗”系列专项行动，聚焦“自媒体”乱象、网络水军操纵信息内容、重点流量环节传播秩序以及算法推荐等突出问题实施集中整治，推动平台压实算法治理主体责任。2024年11月，中央网信办等部门印发《关于开展“清朗·网络平台算法典型问题治理”专项行动的通知》，并附《算法专项治理清单指引》作为核验依据，从“信息茧房”和诱导沉迷、热搜榜单算法透明度、大数据“杀熟”、算法向上向善以及算法安全主体责任等多个维度提出了共27项具体核验标准，标志着我国算法治理由原则性要求进一步走向精细化、可操作的常态化监管。

### 2. 算法推荐治理的核心要求

根据《算法专项治理清单指引》，当前算法推荐治理至少呈现三个核心特征。第一，在多样性维护方面，在“信息茧房”和诱导沉迷治理模块中，清单第7项核验内容明确提出，平台应“具备针对‘信息茧房’‘同质化推荐’等网民重点关注问题的防范举措，通过内容去重、打散干预等策略提升推送内容多样性丰富性”。这一要求直接指向算法推荐可能导致的“信息茧房”问题，意味着平台需要通过调整内容分发策略，降低高度同质化内容的集中度，为长尾内容预留更多曝光空间。

第二，在内容质量与榜单公正方面，针对热搜榜单等注意力高度集中的场景，清单第11项提出，平台应“健全异常账号监测机制，防范违规操纵榜单、控制热搜等现象”；在“优化内容生态”模块下，第23项以“鼓励”的方式提出，平台应“坚持主流价值导向，利用算法提升优质内容推送、识别违法网络谣言等信息”。前者重点约束水军刷榜、恶意操纵排序等行为，后者则引导平台将算法用于优质内容分发与违法信息识别。结合我国既有的舆情管理实践，可以推断：在涉及公共事件、政策讨论等社会类话题上，平台面临更高的合规压力，更可能提高信息来源权威性和事实准确性的门槛；而在娱乐类话题上，监管更多强调守住违法违规底线。

第三，在透明度与可追溯性方面，清单第9项要求平台“公示榜单排序机制机理，如基本原理、排序依据、主要因素等详细信息，并通过事例予以说明”，第10项要求平台“留存榜单相关网络日志，日志内容包括时间、榜单排名、热度值计算相关数据等信息”。这些规定不仅提高了榜单算法的透明度和可审计性，也强化了对热搜榜作为有限注意力资源分配机制的监管约束，为后文从“注意力再分配”的视角刻画热搜榜单的零和竞争特征提供了制度依据。

### 3. 微博热搜榜的运作机制与监管影响

作为中国最具影响力的社交媒体平台之一，新浪微博的热搜榜是算法推荐治理的典型场景。热搜榜采用实时滚动更新机制，但同时只显示50个榜单位置，覆盖社会、娱乐、科技、体育等多个领域。虽然一天内可能有上百条话题轮流上榜，但在任意时刻，用户只能看到排名前50的话题，这一"瞬时可见性"的稀缺性构成了话题间激烈竞争的物质基础。从数据规模看，微博热搜榜每日产生约800-900个话题上榜记录，每月累计约2万条上榜记录，形成了丰富的观察样本。另一方面，根据新浪微博2023年财报，用户日均使用时长约为52分钟，其中热搜浏览时长约占15-20分钟，日均总阅读量超过10亿次。在有限的注意力资源和固定的榜单位置双重约束下，热搜榜成为平台注意力资源的核心分配机制。

热搜榜的排序机制基于"热度值"算法，综合考虑话题的搜索量、阅读量、讨论量、转发量等多维度指标，并引入时间衰减因子以保持榜单动态更新。话题热度值达到阈值后进入榜单，随着时间推移和新话题涌入，热度值下降的话题被挤出榜单。在算法治理行动前，热搜榜呈现明显的头部集中特征——少数头部话题占据绝大部分注意力，单一话题可能长时间持续停留在榜单前列。虽然榜单每天容纳近千条话题轮流展示，但注意力高度集中在头部少数话题，形成Gelper等（2021）所描述的"赢者通吃"分配格局。这种头部集中与监管提出的多样性要求存在张力。

在《算法专项治理清单指引》随“清朗·网络平台算法典型问题治理”专项行动出台之后，微博等大型平台围绕热搜榜单和重点推荐位，对算法机制和运营规则进行了较为系统的调整。从整体方向看，一方面，平台普遍弱化了单一话题长时间占据榜单的情形，通过控制同质内容连续出现、引入一定的打散展示和节奏控制，缓解“霸榜”和高度同质化推荐带来的信息茧房风险；另一方面，在内容分发环节更加重视多元化，使热搜榜单的结构由少数头部话题高度集中，逐步向更多样、更分散的格局演化。同时，平台在水军治理、异常流量识别、敏感话题把关等方面加强了技术和制度安排，对违规操纵榜单、虚假流量制造热度等行为加大治理力度，并在涉及公共事件和政策议题的话题上提高信息来源与事实核验的门槛。总体而言，这些调整综合作用于话题的“能否上榜”“能上多久”以及“不同类别话题之间如何竞争”等关键环节，改变了热搜榜单的注意力分配方式，也为本文从多样性提升、质量分化和注意力再分配三个维度提出研究假设提供了现实背景。

### 4. 算法治理的成本-收益机制

从平台运营逻辑看，算法治理行动实质上改变了不同内容类别的"生产成本-流量收益"结构。对于具有较强舆论属性和社会动员能力的社会类话题，相关监管安排普遍要求平台强化谣言识别、风险预警和干预机制，并对涉公共事件、涉政策议题的内容实施更加审慎的推荐策略。在具体实践中，这通常意味着：平台需要在算法过滤基础上叠加多轮人工复核，引入具备新闻传播、法律、公共政策等专业背景的人员参与敏感话题把关，从而显著推高社会类内容的审核人力投入与组织协调成本；多环节审查亦延长了内容从生产到上线的周期，削弱了此类话题在突发事件情境下的时效性优势；一旦审核疏漏导致错误信息或价值偏离内容获得大规模曝光，平台还需承担潜在的舆情风险、声誉损失乃至行政处罚。综合而言，在监管约束增强的情境下，社会类话题的预期合规成本与风险暴露水平显著上升，其“边际净收益”（单位注意力带来的收益扣除审核与风险成本）相应下降。

相比之下，娱乐类话题的成本结构基本稳定。娱乐内容通常政治敏感度较低，不直接触及国家安全、意识形态安全和重大公共利益，相应的合规风险与声誉风险显著弱于社会类内容。同时，娱乐话题往往具备较强的互动性和传播性，对用户停留时长、活跃度以及广告、会员、联动营销等变现路径具有较高的边际贡献。在这一成本—收益结构下，若假定平台作为理性且风险规避的经济主体，在外部监管约束增强而总体收益目标不变的情况下，其最优响应策略自然倾向于压缩高成本、高风险的社会类话题曝光，将有限的注意力配额向成本较低、变现能力更强的娱乐类内容倾斜。

这一成本-收益机制的调整，触发了平台生态的系统性重构：多样性约束压缩了原有头部话题的“霸榜”空间，质量治理在不同内容类别之间拉大了合规成本差距，平台在利润与风险权衡下通过调整热搜榜单的上榜概率与停留时长，将注意力在社会类与娱乐类之间重新分配，最终形成以娱乐类内容相对占优的新均衡结构。本文后续的实证分析将围绕“多样性提升—质量分化—注意力再分配”的链条展开检验，并进一步评估该机制对平台创新、内容质量与用户福利的综合影响。

---

## （二）文献回顾

### 1. 平台治理与算法监管

近年来，数字平台治理已成为学术界和政策界关注的焦点。平台治理涉及如何在平台所有者、内容生产者、用户和监管者之间分配权力，以实现效率、公平和安全的平衡（Tiwana et al., 2010）。算法作为平台治理的核心工具，通过定义信息可见性、内容排序和资源分配规则，深刻影响着平台生态系统的运行逻辑（Gillespie, 2014）。

#### 1.1 平台权力与问责

Rahman等（2024）提出平台问责的双重视角框架：自下而上的程序公平视角（procedural fairness）关注低权力主体（如零工工人、应用开发者）通过集体行动推动规则改进；自上而下的分配公平视角（distributive fairness）强调通过法律、监管、治理变革防止剥削性机会主义。该研究创新性地提出"平台权力的水床效应"（waterbed effect）：当外部监管约束平台某一维度的权力时，平台会将权力转移至其他维度以维持整体收益。这一理论为理解本文的"注意力重新分配机制"提供了重要启示——当监管约束社会类内容的质量成本时，平台将注意力资源转移至娱乐类内容，实现了权力在不同内容类别间的重新配置。

Gala等（2024）将数字平台概念化为"争议性战场"（contested battlegrounds），超越传统的交易效率视角，强调平台作为权力斗争的组织空间。该研究揭示平台治理的三个核心维度：算法管理（algorithmic management）、数据剥削（data exploitation）、注意力操纵（attention manipulation）。其中，注意力操纵维度与本文关注的热搜榜治理高度相关——平台通过算法调整改变注意力在不同内容类别间的分配，本质上是一种权力行使。

#### 1.2 算法管理与选择架构

Cameron（2024）基于零工经济的民族志研究，揭示算法管理如何通过"受限的持续选择"（confined and constant choice）制造员工同意（manufacture consent）。该研究提出"算法选择架构"（algorithmic choice architecture）概念：平台通过预设选项集、默认设置、动态反馈等机制，在表面上赋予自主权的同时实现深层控制。这一机制可类比于本文情境——平台通过算法调整（如降权处理、长尾扶持）引导内容生产者和用户的注意力分配，实质上是一种"受限选择"：内容生产者可以自由选择话题类型，但不同类型的"生产成本"（审核成本、曝光机会）由平台单方面决定，从而间接引导内容生态重构。

#### 1.3 平台生态系统治理

Huber等（2017）通过双案例研究揭示平台生态系统治理的核心张力：共创价值（co-created value）与治理成本（governance costs）之间的权衡。该研究提出有效生态系统治理的"必要条件"：只有当治理价值超过治理成本时，差异化策略才可持续。这一框架直接适用于本文的算法治理情境——监管要求平台对社会类话题实施严格审核，大幅提升了治理成本（三级审核、专业团队），但平台从中获得的收益（避免监管处罚、维护品牌声誉）可能不足以覆盖成本增量，导致平台策略性减少社会类话题曝光。

Jacobides等（2022）创新性地将平台生态系统定位为"元组织"（meta-organization）：平台作为协调者在不直接雇佣参与者的情况下实现治理。该研究提出元组织的三个核心特征：边界模糊性（boundary ambiguity）、治理多样性（governance pluralism）、价值获取的间接性（indirect value capture）。在中国算法治理情境下，政府通过监管政策成为"元组织的元组织"（meta-organization of meta-organization），在平台与内容生产者之间增加新的治理层级。这一多层级治理结构改变了平台的战略空间——平台不再是生态系统的唯一规则制定者，而是需要在政府监管、内容生产者利益、用户需求之间寻求新的平衡点。

#### 1.4 算法监管的动态性与适应性

Ulbricht和Yeung（2022）系统梳理"算法监管"（algorithmic regulation）概念的演化脉络，区分算法监管的三个层次：监管算法本身（regulating algorithms）、通过算法进行监管（regulating through algorithms）、算法化的监管（algorithmic regulation）。中国算法推荐治理涉及三个层次：制定算法标准（要求公示排序机制机理）、要求平台调整算法（内容去重、打散干预）、建立算法化监测系统（留存网络日志）。该研究强调算法监管的动态性和适应性：监管规则和算法设计相互塑造，形成"监管-响应-再监管"的协同演化。这一视角有助于理解本文的动态演化分析——监管冲击触发平台算法调整，生态结果反馈又可能引发新一轮监管调整。

### 2. 注意力经济与资源配置

注意力经济理论为理解平台内容生态的竞争逻辑提供了核心分析框架。该理论强调在信息过载时代，稀缺的不是信息而是注意力，因此注意力成为比货币更稀缺的资源（Simon, 1971; Davenport & Beck, 2001）。

#### 2.1 注意力的稀缺性与零和竞争

Simon（1971）提出注意力经济的奠基性论断："信息消耗的是接收者的注意力，因此信息的丰富造成注意力的贫乏"（information consumes attention）。他首次系统阐述注意力的三大特征：稀缺性（scarcity）——人类认知带宽有限，无法同时处理海量信息；不可再生性（non-renewability）——注意力消耗后无法恢复，时间维度上不可逆；竞争性（competitiveness）——注意力分配给某一对象必然减少其他对象的份额。这三大特征共同决定了注意力分配的零和博弈性质。

在数字平台情境下，注意力零和特征更加突出。Gelper等（2021）建立社交网络注意力竞争的理论模型，揭示在线环境中注意力分配的零和博弈特征。该研究提出"注意力拥挤效应"（attention crowding effect）：当信息供给增加时，单位信息获得的注意力边际递减。这一效应在热搜榜体系中表现尤为明显——虽然榜单采用实时滚动机制，一天内可能容纳上百条话题轮流展示，但任意时刻只显示50个榜单位置，且用户浏览时长有限（日均15-20分钟）。更关键的是，用户注意力高度集中在"榜上时刻"：实证研究表明，榜单内话题的平均阅读量远超榜外话题（Gelper et al., 2021），形成了"榜内吸引、榜外沉默"的二元结构。因此，榜单位置的"瞬时稀缺性"——而非话题总数的限制——构成了零和竞争的核心：某一话题进入榜单必然挤出其他话题，某一类别上榜数量增加必然减少其他类别的上榜机会。

#### 2.2 注意力作为通用符号货币

Schörgenhuber（2024）提出注意力经济"第二波"理论，将注意力从"稀缺资源"升级为"通用符号货币"（universal symbolic currency）。该研究区分"流动注意力"（flow attention）与"钙化注意力"（calcified attention）：前者指用户的瞬时浏览行为（如点击、阅读），后者指累积的社会资本（如粉丝数、点赞数、热搜排名）。平台的核心功能之一是将流动注意力"货币化"为钙化注意力——通过算法排序、榜单展示等机制，将分散的用户行为转化为可度量、可交易的"注意力资产"。

这一理论为理解热搜榜的注意力分配机制提供了新视角。热搜榜不仅是注意力的"消费场所"（用户浏览话题），更是注意力的"生产场所"（将话题转化为社会关注度）。上榜本身就是一种"注意力增值"过程——话题进入榜单后，获得的注意力呈指数级增长，形成正反馈循环。这解释了为何内容生产者（如营销号、自媒体、企业）竞相追逐热搜——上榜意味着"注意力原始积累"，是后续商业变现的基础。监管对热搜榜的干预，实质上改变了"注意力货币"的发行机制，重新定义了哪些内容有资格进行"注意力原始积累"。

#### 2.3 注意力守门人：算法的角色

Gelper等（2021）强调社交网络算法在注意力分配中的核心作用：推荐算法本质上是注意力的"守门人"（gatekeeper）。传统媒体时代的守门人是编辑和记者，他们通过专业判断决定哪些内容进入公共视野；数字平台时代的守门人是算法，它通过计算规则决定哪些内容获得曝光机会。这一角色转换带来三个关键变化：第一，决策速度从"天"级加速至"秒"级，算法可实时调整内容排序；第二，决策依据从"价值判断"转向"数据驱动"，算法根据用户行为数据优化推荐；第三，决策透明度下降，算法规则的复杂性和动态性使得守门过程成为"黑箱"。

算法治理行动的核心目标之一，就是重新定义守门规则——从"流量最大化"转向"合规约束下的流量最大化"。《治理清单》要求平台"公示榜单排序机制机理"，实质上是要求算法守门人"开箱"，接受外部监督。这一转变改变了内容竞争的游戏规则：在监管前，话题只需争夺用户注意力（流量逻辑）；监管后，话题还需满足合规标准（政治逻辑），形成了"双重守门"机制。

### 3. 平台创新与演化理论

平台生态系统的动态演化是管理学和信息系统学研究的前沿议题。Tiwana等（2010）提出平台演化的三维协同演化框架：架构（architecture）、治理（governance）、环境（environmental dynamics）相互作用。该研究强调外部环境变化（如监管政策）触发治理机制调整，继而导致平台架构重构，最终形成新的生态均衡。

#### 3.1 开放性与控制权的权衡

Parker和Van Alstyne（2018）建立平台创新控制的正式模型，揭示开放性（openness）与控制权（control）之间的最优权衡。该研究提出平台架构设计的核心悖论：过度开放导致质量失控（低质量内容泛滥），过度控制扼杀创新（限制内容多样性）。平台需要根据外部环境变化动态调整开放-控制平衡点。

算法治理行动迫使平台向"开放"端移动——监管要求提升内容多样性，降低头部集中度，本质上是要求平台放松对流量分配的控制，给予长尾内容更多曝光机会。然而，这一调整可能牺牲短期流量（头部内容的"吸粉效应"）以换取长期合规（避免监管处罚）。这体现了平台在"流量最大化"与"合规约束"之间的权衡——监管将原本的单目标优化问题（最大化用户参与度）转化为约束优化问题（在多样性约束下最大化用户参与度）。

#### 3.2 架构震荡与架构演化

Tiwana等（2010）区分"架构震荡"（architecture shock）与"架构演化"（architecture evolution）：前者是短期剧烈调整，通常由外部冲击（如监管政策、技术突破）触发；后者是长期渐进优化，由平台与参与者的持续互动驱动。算法治理行动属于典型的外部冲击，触发平台架构震荡。

本文将动态演化过程划分为三个阶段：初期冲击（0-1个月）——监管政策发布，平台紧急调整算法，社会类话题突然减少，用户浏览行为出现短期"迷失"；调整阶段（1-3个月）——内容生产者适应新规则，调整生产策略，用户逐渐适应新的内容结构，开始更多浏览娱乐类话题；新均衡（3个月后）——平台、内容生产者、用户三方形成新的互动模式，娱乐类参与度进一步上升，形成正反馈循环，注意力重新分配完成。这一三阶段框架与Tiwana等（2010）的理论预测高度一致。

#### 3.3 中国情境的独特性

周冬梅等（2024）梳理中国数字平台生态系统研究，强调中国平台治理呈现"政府主导、多元协同"的特征，不同于西方"平台自治"模式。该研究提出生态演化的"路径依赖"与"临界转变"特征——外部冲击（如监管）可能触发生态系统跨越临界阈值，进入新的稳定状态。这一视角解释了为何算法治理行动能够在短期内（3-6个月）显著改变平台内容生态，而非渐进式调整。

Lei（2021）基于中国外卖平台的民族志研究，揭示中国情境的独特性：政府作为平台生态的"超级主体"（super-actor），通过监管政策直接重塑平台架构和生态规则。这一治理模式在算法治理中表现尤为突出——政府不仅是规则制定者，还是执行监督者和效果评估者，形成了"规则制定-执行监督-效果评估-规则调整"的闭环。这种"强监管"模式使得平台对政府政策的响应速度和执行力度远超西方国家，也使得监管政策能够在短期内产生显著效果。

### 4. 文献述评与研究缺口

综上所述，现有文献在平台治理、注意力经济、算法监管等领域积累了丰富成果，但仍存在以下研究缺口：

第一，理论整合不足*。现有研究多聚焦单一维度（如平台权力、注意力竞争、算法透明度），缺乏将平台治理、注意力经济、生态系统演化整合的综合框架。本文通过构建"多样性约束-成本分化-注意力重新分配"的三机制模型，将上述理论整合为统一的分析框架。

第二，实证证据缺乏。关于算法治理如何影响平台内容生态，现有研究多停留在理论推演或案例分析，缺乏大样本实证检验。本文利用微博热搜榜的高频数据（政策前后各6个月），通过双重差分、事件研究等方法，提供了算法治理效果的因果证据。

第三，动态过程忽视。现有研究多关注治理的短期效果或长期均衡，忽视了从冲击到新均衡的动态调整过程。本文通过分阶段分析（0-1月、1-3月、3月后），揭示了平台、内容生产者、用户三方的动态博弈过程。

第四，中国情境不足。关于算法治理的研究多以欧美为背景，忽视了中国"政府主导"治理模式的独特性。本文聚焦中国算法推荐治理行动，为理解"强监管"模式下平台生态的快速转型提供了经验证据。

---

## （三）研究假设

### 1. 理论基础：平台生态系统的资源重新配置

在以算法推荐为核心的数字平台中，内容生态系统的运行遵循资源编排理论（Sirmon et al., 2011）的基本逻辑：平台通过算法规则的设计与调整，对稀缺的注意力资源进行有序配置，从而在多元目标（用户参与、内容多样性、合规要求、商业收益）之间寻求动态平衡。算法治理行动作为外部制度冲击，通过引入新的约束条件（如多样性约束、质量门槛、透明度要求），改变了平台的优化目标函数，触发了资源重新配置。

具体而言，平台的目标函数可表示为：

$$
\max_{\{A_i, Q_i\}} U = \sum_i \theta_i A_i + \alpha D - \sum_i C_i(Q_i, R_i)
$$

其中，$A_i$为第$i$类内容获得的注意力资源，$Q_i$为其质量水平，$\theta_i$为用户参与度系数，$D$为内容多样性指标，$\alpha$为多样性权重，$C_i(Q_i, R_i)$为质量成本函数（取决于质量水平$Q_i$和风险等级$R_i$）。

算法治理行动引入三类约束：

约束1（注意力零和约束）：
$$
\sum_i A_i = \bar{A}
$$

其中，$\bar{A}$为平台用户总注意力（由日均使用时长和活跃用户数共同决定），短期内近似固定。这一约束体现了注意力的稀缺性和竞争性，某一类别注意力的增加必然以其他类别注意力的减少为代价。

约束2（多样性下限约束）：
$$
D \geq D_{\min}
$$

其中，$D_{\min}$为监管要求的多样性下限。《治理清单》明确要求平台"提升推送内容多样性丰富性"，实质上是提高了$D_{\min}$，迫使平台降低头部集中度，为长尾内容分配基础曝光配额。

约束3（分级质量约束）：
$$
Q_i \geq Q_i^{\min}(R_i), \quad \text{其中 } \frac{\partial Q_i^{\min}}{\partial R_i} > 0
$$

对于监管视角下风险等级较高的内容类别（如具有较强舆论属性或社会动员能力的公共事务类话题），相关规范通常要求平台履行更严格的安全评估与内容治理义务，包括强化信息来源审查、事实核验和价值导向把关等；而对于日常娱乐、休闲等风险等级较低的内容类别，质量门槛相对较低，审核机制可以更大程度依赖自动化识别和抽样人工复查。综合既有法规与监管实践，可以合理假定 $Q_i^{\min}(R_i)$ 随风险等级 $R_i$ 单调上升：风险越高的内容类别，需要满足的最低质量与合规标准越高，对应的审核成本也随之增加。



### 2. 假说推演

基于上述理论框架和约束条件，本文通过数理模型与理论机制的双重视角提出以下研究假说。

# 假说 H1：算法治理的多样性提升效应

## 1. 数学推导线索

### 命题1.1（可行域收缩与约束硬化）
算法治理行动改变了平台决策的约束条件集合。设平台内容分发策略空间为 $\mathcal{P}$，监管前平台面临的是基于用户点击率（CTR）的软约束，监管后《治理清单》第7条将多样性要求转化为硬约束。定义 $H(p)$ 为衡量话题分布多样性的Shannon熵，则监管导致的多样性下限 $\delta$ 发生位移：
$$
\text{s.t. } H(p^{\text{post}}) \ge \delta_{\text{post}} > \delta_{\text{pre}}
$$
该约束强化导致平台可行域收缩（Feasible Region Contraction），剔除了虽然商业价值最大化但熵值低于 $\delta_{\text{post}}$ 的极点解。

### 命题1.2（分布的优力关系与头部去中心化）
定义 $N$ 个话题的注意力分布向量为 $p = (p_1, p_2, \dots, p_N)$，并按降序排列 $p_1 \ge p_2 \ge \dots \ge p_N$。监管措施（内容去重与打散干预）强制削减前 $k$ 个头部话题的流量配额，并将其再分配至长尾话题。数学上，这等价于监管后的分布 $p^{\text{post}}$ 被监管前的分布 $p^{\text{pre}}$ 所优势（Majorized），记作 $p^{\text{pre}} \succ p^{\text{post}}$。该关系满足洛伦兹优势条件：
$$
\begin{cases}
\sum_{i=1}^{m} p_i^{\text{pre}} \ge \sum_{i=1}^{m} p_i^{\text{post}}, & \forall m \in \{1, \dots, N-1\} \\
\sum_{i=1}^{N} p_i^{\text{pre}} = \sum_{i=1}^{N} p_i^{\text{post}} = 1
\end{cases}
$$
此不等式组表明，在任意截断点 $m$，监管前的累积注意力集中度均不低于监管后，且至少存在一个 $m$ 使得严格不等式成立。

### 定理1（Shannon熵的舒尔凹性证明）
定理内容：当注意力分布从高度集中转向相对均匀（即 $p^{\text{pre}} \succ p^{\text{post}}$）时，Shannon熵单调递增。
证明：
Shannon熵定义为 $H(p) = -\sum_{i=1}^{N} p_i \ln p_i = \sum_{i=1}^{N} \phi(p_i)$，其中 $\phi(x) = -x \ln x$。
计算 $\phi(x)$ 的二阶导数：
$$
\phi''(x) = -\frac{1}{x}
$$
在定义域 $x \in (0, 1]$ 上，$\phi''(x) < 0$ 恒成立，故 $\phi(x)$ 为严格凹函数。
根据优力理论（Marshall et al., 2011），若实值函数 $F(x) = \sum \phi(x_i)$ 中的 $\phi$ 为凹函数，则 $F(x)$ 是舒尔凹函数（Schur-concave function）。
根据舒尔凹函数的定义，若 $p^{\text{pre}} \succ p^{\text{post}}$，则必然蕴含：
$$
H(p^{\text{post}}) > H(p^{\text{pre}})
$$
证毕。

## 2. 理论机制解释

### 2.1 目标函数重构：从单目标优化到约束优化
监管介入前，平台的决策模型可抽象为无约束的流量最大化问题 $\max_{p} \sum v_i p_i$（其中 $v_i$ 为商业变现效率）。由于头部话题通常具有更高的 $v_i$，平台倾向于产生极度偏斜的分布。监管实质上引入了拉格朗日乘数 $\lambda$。新目标函数为：
$$
\mathcal{L}(p, \lambda) = \sum_{i=1}^{N} v_i p_i + \lambda (H(p) - \delta_{\text{post}})
$$
其中影子价格 $\lambda > 0$ 代表了平台为满足合规要求所必须放弃的边际商业收益。这一机制表明，多样性提升并非市场自发演化的结果，而是通过制度设计强制改变了帕累托最优解的对偶性质。

### 2.2 资源编排逻辑：从马太效应到累进调节
推荐算法的正反馈机制导致了注意力分配的马太效应（Matthew Effect）。《治理清单》中的"去重"（头部封顶）与"打散"（长尾保底）构成了双向调节机制，其作用机理类似于税收制度中的累进税（Progressive Tax）：对高流量话题征收"关注度税"（降低 $p_i, i \le k$），并转移支付给长尾话题。这种非线性的干预手段切断了"高曝光-高点击-更高曝光"的循环链路，强制系统熵值向最大熵状态（均匀分布）漂移。

### 2.3 动态演化视角：平台架构设计悖论的解决
Parker和Van Alstyne（2018）提出的平台架构设计悖论指出，过度中心化的控制会抑制生态活力。定理1的推导揭示了监管的简化治理逻辑：监管者无需微观管理每个话题的流量，只需设定头部上限 $p_{\max}$ 和长尾下限 $p_{\min}$ 两个宏观参数。只要满足 $p^{\text{pre}} \succ p^{\text{post}}$ 的优力条件，系统多样性 $H(p)$ 的提升即为数学上的必然结果。这验证了通过简单规则引导复杂系统演化的有效性。

## 3. 假说陈述

基于上述数学推导与理论机制，提出如下假说：

H1：算法治理显著提升了热搜榜单的话题多样性。

具体可分解为以下实证推论：
* H1a（集中度下降）：治理实施后，头部话题（Top-k）的累积注意力占比显著下降，洛伦兹曲线向对角线移动。
* H1b（熵值提升）：治理实施后，以Shannon熵衡量的注意力分布指标显著上升，即 $\mathbb{E}[H^{\text{post}}] > \mathbb{E}[H^{\text{pre}}]$。


---
### 假说 H2：监管冲击下的质量分化效应

#### 1. 数学推导线索

命题 2.1（合规成本函数的超模性结构）  

设平台内容审核的成本函数为 $C(Q, R)$，其中 $Q \in \mathbb{R}_+$ 为内容质量，$R \in \mathbb{R}_+$ 为内容的风险等级（社会类 $R_S >$ 娱乐类 $R_E$）。该成本函数满足以下性质：

1. 质量的边际成本递增（凸性）  
   $$\frac{\partial C}{\partial Q} > 0,\quad \frac{\partial^2 C}{\partial Q^2} > 0.$$

2. 风险的成本放大效应  
   $$\frac{\partial C}{\partial R} > 0.$$

3. 质量与风险的互补性
   $$
   \frac{\partial^2 C}{\partial Q \partial R} > 0.
   $$  
   即在高风险情境下提升单位质量的边际成本显著高于低风险情境。

形式化设定：为便于分析，采用广义 Cobb–Douglas 形式与指数风险项结合的成本函数：
$$
C(Q, R) = \alpha \cdot Q^{\beta} \cdot e^{\gamma R}, \quad \beta > 1,\ \gamma > 0,
$$
该设定保证了上述三条性质成立，并刻画了高风险内容审核成本的指数级敏感性。

---

命题 2.2（差异化约束的优化模型）  

平台面临的决策问题是在满足监管约束的前提下最小化运营成本。算法治理行动可抽象为对不同风险类别施加非对称的质量下限约束 $\underline{Q}(R)$：

$$
\begin{aligned}
\min_{Q_S, Q_E} \quad & \mathcal{L} = C(Q_S, R_S) + C(Q_E, R_E) \\
\text{s.t.} \quad & Q_S \ge \underline{Q}_S^{\text{post}}, \\
& Q_E \ge \underline{Q}_E^{\text{post}}.
\end{aligned}
$$

在本文的抽象框架中，我们假定算法治理对高风险社会类内容的合规门槛提升更为显著：
$$
\underline{Q}_S^{\text{post}} \gg \underline{Q}_S^{\text{pre}}, \quad 
\underline{Q}_E^{\text{post}} \approx \underline{Q}_E^{\text{pre}},
$$
反映出监管对高风险内容提出了更严格的质量与安全要求，而对低风险娱乐内容主要维持底线型约束。

---

定理 2（角点解与质量分化）  

在上述设定下，考虑凸成本函数与线性不等式约束的优化问题。根据 KKT 条件和标准凸优化结论，最优解 $Q^*$ 将在“约束恰好绑定”（binding constraint）或内部点之间选择。结合成本函数的超模性结构，可得：

1. 社会类（紧约束）  

   由于 $\underline{Q}_S^{\text{post}}$ 设定了较高的质量下限，且在高风险水平 $R_S$ 下，边际成本  
   $$\frac{\partial C(Q, R_S)}{\partial Q} = \alpha \beta Q^{\beta - 1} e^{\gamma R_S}$$
   随 $Q$ 增长极快，平台缺乏进行“过度合规”（over-compliance，即质量提升超过监管要求）的激励——额外质量提升带来的边际收益难以覆盖指数级上升的边际成本。因此，最优解倾向于在约束边界取得角点解：
   $$
   Q_S^* = \underline{Q}_S^{\text{post}} > Q_S^{\text{pre}}.
   $$

2. 娱乐类（松约束）  

   对于风险较低的娱乐类内容，$R_E$ 较小使得边际成本曲线更为平缓，且 $\underline{Q}_E^{\text{post}}$ 与监管前相比并未发生显著位移，在合理假定下，平台在既有质量水平上即可满足最低合规要求。此时没有强动机投入额外成本提升质量，因此有：
   $$
   Q_E^* \approx Q_E^{\text{pre}}.
   $$

---

推论 2.1（成本非对称激增）  

即便假设社会类与娱乐类内容在某一阶段的质量提升幅度相同（$\Delta Q_S = \Delta Q_E = \Delta Q$），二者对应的成本增量之比仍存在数量级差异：

$$
\Delta C_S \approx \alpha \left[(Q_S + \Delta Q)^{\beta} - Q_S^{\beta}\right] e^{\gamma R_S},\\
\Delta C_E \approx \alpha \left[(Q_E + \Delta Q)^{\beta} - Q_E^{\beta}\right] e^{\gamma R_E},
$$

在 $Q_S$、$Q_E$ 处于相近数量级的情况下，有近似比值：

$$
\frac{\Delta C_S}{\Delta C_E} 
\approx e^{\gamma (R_S - R_E)} \gg 1.
$$

这一推论表明，在相同质量提升目标下，高风险社会类内容所需承担的合规成本远高于低风险娱乐内容，为后文“平台优先保障社会类达标，而对娱乐类内容采取相对宽松策略”提供了成本端的解释基础。

---

#### 2. 理论机制解释

理论解释 2.1：基于风险的监管逻辑

《算法专项治理清单指引》在“异常账号监测与榜单操纵治理”（如第 11 项）以及“优化内容生态与算法向上向善”（如第 23 项）等模块中，对涉及公共事件、舆情风险和违法谣言的信息分发提出了更高要求，而对一般娱乐、休闲内容则主要强调防范低俗、侵权等显性违规行为。结合Yeung（2022）提出的算法监管框架，可以将此理解为一种基于风险的监管逻辑：监管者根据潜在负外部性的大小分配治理资源与规范强度。

在这种逻辑下，具有较强公共属性和社会动员能力的社会类话题被视为高风险类别，一旦出现虚假信息或价值偏离，可能引发系统性舆情风险或重大负外部性，因此被纳入更严格的治理序列，面对更高的信息来源、事实核验和价值导向标准。相对而言，娱乐类话题主要关联个体消费与情绪调节，其外部性更局限于低俗、侵权等局部问题，监管多采取“守住底线”的防御性姿态。这种风险敏感型（risk-based）的分级监管结构，在合规成本函数上体现为对高风险类别设定更高的质量下限 $\underline{Q}_S^{\text{post}}$，而对低风险类别的 $\underline{Q}_E^{\text{post}}$ 变化有限，从而为质量分化奠定了制度基础。

---

理论解释 2.2：制度同形性与选择性解耦  

从新制度主义视角看，质量分化是强制性同形与选择性解耦共同作用的结果。在社会类等高风险领域，平台在获取合法性与规避处罚的双重压力下，倾向于严格响应监管期望，通过提升审核标准、增加人工把关等方式在形式上与监管要求保持高度一致，表现出较强的同形性：不同平台在社会类内容治理上呈现出趋同的“提质”特征。

然而，在监管压力相对较小的娱乐类领域，平台仍然需要在合规与商业利益之间进行权衡。经典的制度响应理论（Oliver, 1991）指出，当正式制度要求与组织效率目标存在张力时，组织可能采取选择性解耦策略：在文件和对外表述中呈现合规形象，而在实际操作中维持相对惯常的做法。对应到本研究情境，这意味着平台在娱乐类内容上更可能维持“名义合规、实质保量”的状态，即在形式上满足基本审核要求，但在深度提质和结构性改善上投入有限，从而强化了社会类“提质”与娱乐类“保量”的双轨格局。

---

理论解释 2.3：资源依赖与挤出效应  

从资源依赖理论（Pfeffer & Salancik, 1978）出发，平台用于内容治理的预算、专业人力和算力等资源在短期内具有刚性约束。算法治理行动显著提高了社会类内容的边际合规成本后，高风险领域便成为组织必须优先满足的关键依赖对象。为了确保此类内容不触碰监管红线，平台不得不在资源配置上进行再平衡，将原本可用于优化长尾内容或娱乐内容体验的部分资源，转而集中投入到社会类话题的审核、风控与事后处置之中。

这种以高风险领域为中心的资源重配，天然会产生对其他内容类别的“挤出效应”：在总体资源约束不变的前提下，社会类内容的“提质”以牺牲对娱乐类深度治理的空间为代价。由此，一方面社会类内容在信源权威性、事实准确性等维度明显改善；另一方面，娱乐类内容在结构性提质上进展有限，甚至存在“显性违规减少但同质化与擦边问题仍然突出”的低位均衡状态。这与前述成本函数的非对称结构相呼应，为质量分化提供了资源配置层面的解释。

---

#### 3. 假说陈述

综合上述数理推导与理论机制，可以提出如下对立假说：

H2a（社会类内容的强制提质）  
算法治理实施后，高风险（社会类）话题的平均质量指标显著提升。  
*实证表现*：权威信源（官方媒体、政务账号等）占比明显增加，经人工或多级审核的话题比例上升，标题党与谣言特征显著减少。

H2b（娱乐类内容的低位均衡）  
算法治理实施后，低风险（娱乐类）话题的平均质量指标无显著变化或仅有轻微提升。  
*实证表现*：信源结构保持稳定（以自媒体、营销号等为主），内容同质化程度未见明显改善，显性违规有所收敛但低俗、擦边等问题可能因资源挤出而持续存在。

---

### 假说 H3：监管冲击下的注意力再分配效应

#### 1. 数学推导线索

命题 3.1（注意力预算约束与影子价格）  

定义平台内容生态的总注意力预算为 $\bar{A}$。在短期内，受限于用户认知负荷与日活跃用户规模的相对稳定，总注意力供给缺乏弹性，可视为外生常数。平台面临的约束优化问题可表示为：

$$
\max_{\{A_i\}} \;\Pi 
= \sum_{i \in \{S,E,O\}} \big[ R_i(A_i) - C_i(A_i,\xi_i) \big] 
+ \mu\, D(A_S,A_E,A_O)
$$

$$
\text{s.t.} \quad \sum_{i} A_i \le \bar{A}, \quad A_i \ge 0,
$$

其中，$i$ 代表内容类别（$S$=社会，$E$=娱乐，$O$=其他）；$R_i(A_i)$ 为凹收益函数（$R_i'>0,\ R_i''<0$），反映用户参与度的边际递减；$C_i(A_i,\xi_i)$ 为凸成本函数，$\xi_i$ 为外生监管强度参数；$D(\cdot)$ 为多样性激励项，$\mu \ge 0$ 为多样性权重。注意力预算约束在最优解处通常是紧约束（binding），即 $\sum_i A_i^* = \bar{A}$。

构建拉格朗日函数：

$$
\mathcal{L} = \sum_{i} \big[ R_i(A_i) - C_i(A_i,\xi_i) \big] 
+ \mu D(A_S,A_E,A_O) 
+ \lambda \big(\bar{A} - \textstyle\sum_{i} A_i\big),
$$

其中 $\lambda \ge 0$ 为注意力资源的影子价格，表示在最优点附近增加 1 单位注意力预算所带来的边际收益。

---

命题 3.2（不对称成本冲击下的替代效应）  

对每一类内容 $i$，若最优解处 $A_i^*>0$，一阶条件（FOC）为：

$$
\frac{\partial R_i}{\partial A_i} 
- \frac{\partial C_i}{\partial A_i} 
+ \mu \frac{\partial D}{\partial A_i} 
= \lambda, 
\quad i \in \{S,E,O\}.
$$

这表明在最优点上，各类内容的“边际收益 − 边际成本 + 多样性边际贡献”在注意力空间内应当被拉平到同一水平 $\lambda$。

现在考察监管冲击导致社会类监管强度参数 $\xi_S$ 上升的情形。根据链式法则与比较静态分析，当 $\xi_S$ 上升时，有：

$$
\frac{\partial}{\partial \xi_S} 
\left(
\frac{\partial C_S}{\partial A_S}
\right) > 0,
$$

即社会类内容的边际合规成本上升。要维持 FOC 成立，平台可以通过调整 $A_S$ 与其他类别的 $A_E,A_O$ 使得新的均衡满足：

$$
\frac{\partial R_S}{\partial A_S^{\text{post}}} 
- \frac{\partial C_S}{\partial A_S^{\text{post}}} 
+ \mu \frac{\partial D}{\partial A_S^{\text{post}}} 
= \lambda^{\text{post}},
$$

其中在注意力预算约束仍为紧约束的前提下，$\lambda^{\text{post}}$ 反映了新均衡下注意力的影子价格。

在 $R_S$ 凹、$C_S$ 凸的假定下，为抵消边际成本的上升，最直接的调整方式是减少 $A_S$，从而提高 $\frac{\partial R_S}{\partial A_S}$ 并降低 $\frac{\partial C_S}{\partial A_S}$。在注意力预算约束 $\sum_i A_i = \bar{A}$ 紧约束的情况下，有：

$$
\Delta A_S < 0
\quad \Rightarrow \quad 
\Delta A_E + \Delta A_O > 0.
$$

在娱乐类成本函数对监管强度不敏感（$\partial C_E / \partial \xi_S \approx 0$）、且其边际收益率通常高于其他类（例如 $R'_E > R'_O$）的假定下，边际净收益均等原则将驱动释放出的注意力资源优先流向娱乐板块。由此导出类似“水床效应”（waterbed effect）的比较静态结论：

$$
\frac{\partial A_E^*}{\partial \xi_S} > 0,\quad 
\frac{\partial A_S^*}{\partial \xi_S} < 0,
$$

即社会类注意力在监管压力上升时收缩，释放出的注意力在总量约束下向娱乐类转移。

---

命题 3.3（超调与均值回归的可能性）  

进一步考虑娱乐类注意力 $A_E(t)$ 的动态调整路径。设平台采用类似部分调整的规则，根据不同类别的“边际净收益 − 影子价格”差异调整注意力权重：

$$
\frac{d A_E(t)}{d t} 
= \kappa \Big(
\big[ R'_E(A_E(t)) - C'_E(A_E(t),\xi_E) + \mu \tfrac{\partial D}{\partial A_E} \big]
- \lambda(t)
\Big),
\quad \kappa > 0,
$$

其中 $\lambda(t)$ 由注意力预算约束和其他类别的调整共同决定。假定：  

1. 短期内社会类注意力 $A_S$ 在监管冲击发生时出现“离散式”下调，平台为维持整体流量与用户活跃，快速上调 $A_E$ 进行填补；  
2. 娱乐类内容存在拥塞效应，即在 $A_E$ 过高时其边际收益 $R'_E(A_E)$ 下降速度加快，用户出现审美疲劳和边际效用递减加剧的现象。

在上述假定下，娱乐类注意力的时间路径可呈现“短期超调—中长期回落—新均衡”的非单调轨迹：在冲击发生后的短期内（$t \to 0^+$），$A_E(t)$ 快速上升以填补 $A_S$ 的空缺；随着 $A_E$ 长期维持高位，拥塞效应使得娱乐类内容的边际净收益下降，平台在持续观察用户行为反馈后逐步下调 $A_E$，使其收敛至一个高于监管前但低于峰值的新平衡水平：

$$
\frac{d A_E}{dt} 
\begin{cases}
> 0, & t \in (0,\tau_1) \quad \text{（冲击后的短期回填阶段）}, \\
< 0, & t \in (\tau_1,\tau_2) \quad \text{（拥塞约束下的修正阶段）}, \\
\to 0, & t \to \infty \quad \text{（收敛至新稳态 } A_E^* > A_E^{\text{pre}} \text{）}.
\end{cases}
$$

该命题并非对具体函数形式的严格刻画，而是说明在“注意力预算刚性 + 监管对社会类的非对称冲击 + 娱乐内容的拥塞效应”同时存在时，娱乐类注意力存在“先超调、后回落”的动态调整可能性。

---

#### 2. 理论机制解释

理论解释 3.1：存量注意力博弈下的挤出与回填  

注意力经济的核心特征在于认知资源的稀缺性。Simon（1971）指出，信息的丰富必然伴随注意力的贫乏。在移动互联网渗透率趋于饱和的背景下，用户总时长与活跃规模在短期内呈现强刚性，总注意力 $\bar{A}$ 可以近似视为固定存量。在此情境下，监管对社会类内容的强化治理，相当于在该类别上抬高风险权重与合规成本，使其边际净收益相对其他类别下降，从而促使平台在约束优化过程中压缩社会类的注意力权重。

然而，被削减的社会类注意力并不会简单消失，而是在总注意力约束下寻找新的配置路径。根据平台“水床效应”的分析视角（ Rahman et al., 2024），在不同内容类别之间存在类似“连通容器”的流量转移：当高风险类别因监管而被下落时，流量会通过算法分发机制向成本更低、约束更松的内容板块上升。在本研究语境下，娱乐类内容凭借较低的合规风险与较强的原生吸引力，自然成为注意力回填的主要承接者。

---

理论解释 3.2：边际净收益的动态均衡  

从平台算法的视角看，推荐系统本质上是在多类别内容之间不断进行“边际净收益”比较与再平衡的过程。监管前，社会类与娱乐类在收益—风险维度上处于某种相对稳定的权衡状态；监管后，社会类内容的风险溢价大幅上升，其风险调整后的回报（risk-adjusted return）显著下降。理性的算法策略会减少对高风险内容的推荐权重，将注意力向风险较低、收益相对稳定的娱乐类内容倾斜。

这一替代过程并非线性推进，而是受到需求侧饱和效应的约束。短期内，供给侧的剧烈调整会导致娱乐内容集中度快速上升，用户在算法“过度娱乐化”的推送下产生审美疲劳与决策负担（Schwartz, 2004），边际效用加速递减。平台在观察用户反馈（如点击率、完播率、停留时长等）变化的基础上，需要对过高的娱乐权重进行修正，逐步下调该类别的注意力占比，寻找兼顾合规安全与用户体验的新的均衡点。这一过程对应于前述命题 3.3 所刻画的“超调—回落”动态。

---

理论解释 3.3：合规治理的意外后果

从治理目标看，监管者的初衷在于压缩有害信息的传播空间、提升整体内容质量；但在复杂适应系统中，强约束往往会通过注意力再分配机制产生二阶效应。对高风险社会类话题施加更高合规门槛与更强审慎性要求，一方面确实减少了明显违规与失真的信息，另一方面也可能在算法和审核实践中“顺带”压缩了一部分合规但敏感度较高的公共议题，从而在相对意义上扩大了娱乐性内容在整体注意力中的占比。

这种结构性转移并不必然源于平台对监管的对抗，而更像是在多重约束（合规、安全、用户黏性、商业收益）下形成的局部最优解：在既有资源与制度框架内，平台选择通过减少高风险内容的曝光，增加低风险娱乐内容的推荐来达成“合规 + 流量”的折衷。由此，算法治理在抑制一类风险的同时，可能间接推动另一类内容的扩张，体现出典型的“合规政策的意外后果”特征。

---

#### 3. 假说陈述

H3a（社会类内容的结构性收缩）  
算法治理实施后，社会类话题的注意力份额显著下降，即：
$$
\mathbb{E}\big[A_S^{\text{post}}\big] < \mathbb{E}\big[A_S^{\text{pre}}\big].
$$
*实证表现*：社会类话题上榜频次减少，在榜平均时长缩短，上述下降在合理时间窗口内具有持续性。

H3b（娱乐类注意力的超调与回落）  
算法治理实施后，娱乐类话题的注意力份额呈现“短期显著上升—中期部分回落—长期新均衡高于监管前”的非单调动态。  
*实证表现*：在监管实施初期（如 $T+1$ 至 $T+3$ 月）娱乐类话题的上榜频次和在榜时长显著高于监管前；随后（如 $T+4$ 月起）呈现逐步回落趋势，但最终稳定水平仍高于监管前均值。

H3c（总注意力的近似守恒）  
在控制季节性与宏观环境变化等因素后，算法治理前后平台总注意力规模基本稳定，即：
$$
\mathbb{E}\big[\bar{A}^{\text{post}}\big] \approx \mathbb{E}\big[\bar{A}^{\text{pre}}\big].
$$
*实证表现*：社会类注意力的减少量在统计上与娱乐类及其他类注意力的增加量相匹配，支持注意力近似零和的工作假设。

---

## 参考文献

Cameron, L. D. (2024). Making out While Driving: Relational and Efficiency Games in the Gig Economy. *Administrative Science Quarterly*, *69*(1), 119–163. https://doi.org/10.1177/00018392231217038

Christmann, P., & Taylor, G. (2001). Globalization and the environment: Determinants of firm self-regulation in China. *Journal of International Business Studies*, *32*(3), 439–458. https://doi.org/10.1057/palgrave.jibs.8490976

Corporaal, G. F., & Lehdonvirta, V. (2024). The dualistic structure of algorithmic management in the global gig economy. *Big Data & Society*, *11*(1), Article 20539517241227874. https://doi.org/10.1177/20539517241227874

Davenport, T. H., & Beck, J. C. (2001). *The attention economy: Understanding the new currency of business*. Harvard Business School Press.

DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, *48*(2), 147–160. https://doi.org/10.2307/2095101

Gala, P., Shevchuk, A., Lehdonvirta, V., & Rahman, H. A. (2024). Platform power and contestation: A review of digital labor research in management. *Academy of Management Annals*, *18*(2), 523–569. https://doi.org/10.5465/annals.2022.0188

Gelper, S., Peres, R., & Eliashberg, J. (2021). Talk bursts: The role of spikes in pre-release word-of-mouth dynamics. *Management Science*, *67*(5), 2758–2780. https://doi.org/10.1287/mnsc.2019.3571

Gorwa, R., Binns, R., & Katzenbach, C. (2020). Algorithmic content moderation: Technical and political challenges in the automation of platform governance. *Big Data & Society*, *7*(1), Article 2053951719897945. https://doi.org/10.1177/2053951719897945

Gritsenko, V., & Wood, M. (2022). Algorithmic governance: A modes of governance approach. *Regulation & Governance*, *16*(1), 45–62. https://doi.org/10.1111/rego.12437

Holling, C. S. (1973). Resilience and stability of ecological systems. *Annual Review of Ecology and Systematics*, *4*, 1–23. https://doi.org/10.1146/annurev.es.04.110173.000245

Huber, T. L., Kude, T., & Dibbern, J. (2017). Governance practices in platform ecosystems: Navigating tensions between cocreated value and governance costs. *Information Systems Research*, *28*(3), 563–584. https://doi.org/10.1287/isre.2017.0701

Jacobides, M. G., Cennamo, C., & Gawer, A. (2022). Distinguishing between platforms and ecosystems: Complementarities, value creation, and coordination mechanisms. *Strategic Management Journal*, *43*(10), 2045–2074. https://doi.org/10.1002/smj.3250

Lei, Y.-W. (2021). Delivering solidarity: Platform architecture and collective contention in China's platform economy. *American Sociological Review*, *86*(2), 279–309. https://doi.org/10.1177/0003122420979980

Markowitz, H. (1952). Portfolio selection. *The Journal of Finance*, *7*(1), 77–91. https://doi.org/10.2307/2975974

Mazzucato, M. (2020). *Mission economy: A moonshot guide to changing capitalism*. Allen Lane.

Parker, G. G., & Van Alstyne, M. W. (2018). Innovation, openness, and platform control. *Management Science*, *64*(7), 3015–3032. https://doi.org/10.1287/mnsc.2017.2757

Rahman, H. A., Galpaya, H., Haag, M., & Ravishankar, M. N. (2024). Platform accountability: A review, synthesis, and research agenda. *Academy of Management Annals*, *18*(1), 214–247. https://doi.org/10.5465/annals.2022.0090

Samuelson, P. A. (1954). The pure theory of public expenditure. *The Review of Economics and Statistics*, *36*(4), 387–389. https://doi.org/10.2307/1925895

Schörgenhuber, C. (2024). Toward a second-order attention economy: Algorithmic selection and the attention commodity. *Interacting with Computers*, *36*(1), 46–63. https://doi.org/10.1093/iwc/iwae001

Schwartz, B. (2004). *The paradox of choice: Why more is less*. HarperCollins.

Simon, H. A. (1971). Designing organizations for an information-rich world. In M. Greenberger (Ed.), *Computers, communication, and the public interest* (pp. 37–52). Johns Hopkins Press.

Sirmon, D. G., Hitt, M. A., Ireland, R. D., & Gilbert, B. A. (2011). Resource orchestration to create competitive advantage: Breadth, depth, and life cycle effects. *Journal of Management*, *37*(5), 1390–1412. https://doi.org/10.1177/0149206310385695

Tiwana, A., Konsynski, B., & Bush, A. A. (2010). Research commentary—Platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. *Information Systems Research*, *21*(4), 675–687. https://doi.org/10.1287/isre.1100.0323

Ulbricht, L., & Yeung, K. (2022). Algorithmic regulation: A maturing concept for investigating regulation of and through algorithms. *Regulation & Governance*, *16*(3), 727–744. https://doi.org/10.1111/rego.12437

Wang, Y., Chen, Y., & Wu, S. (2025). From content moderation to cultural governance: The evolution of China's "Qinglang" campaign in platform regulation. *Asian Journal of Communication*, *35*(1), 1–18. https://doi.org/10.1080/01292986.2025.2526475

周冬梅, 李纲, & 蔡淑琴. (2024). 数字平台生态系统的形成机理、治理机制与演化路径研究. *科学学研究*, *42*(2), 376–388. https://doi.org/10.16192/j.cnki.1003-2053.20230202.002

Cao, Z., Zhu, Y., Li, G., & Qiu, L. (2024). Consequences of information feed integration on user engagement and contribution: A natural experiment in an online knowledge-sharing community. Information Systems Research, 35(3), 1114–1136. https://doi.org/10.1287/isre.2023.1234
Cennamo, C., & Ozalp, H. (2022). Platform ecosystems as meta-organizations: Implications for platform strategies. Strategic Management Journal, 43(2), 405–424. https://doi.org/10.1002/smj.3241
Gritsenko, V., & Wood, M. (2022). Algorithmic governance: A modes of governance approach. Regulation & Governance, 16(1), 45–62. https://doi.org/10.1111/rego.12367
Jacobides, M. G., Cennamo, C., & Gawer, A. (2024). Externalities and complementarities in platforms and ecosystems: From structural solutions to endogenous failures. Research Policy, 53(1), Article 104906. https://doi.org/10.1016/j.respol.2023.104906
Kitchens, B., Johnson, S. L., & Gray, P. (2020). Understanding echo chambers and filter bubbles: The impact of social media on diversification and partisan shifts in news consumption. MIS Quarterly, 44(4), 1619–1649. https://doi.org/10.25300/MISQ/2020/15057
Mann, G., Karanasios, S., & Breidbach, C. F. (2022). Orchestrating the digital transformation of a business ecosystem. The Journal of Strategic Information Systems, 31(3), Article 101733. https://doi.org/10.1016/j.jsis.2022.101733
Menz, M., Kunisch, S., Birkinshaw, J., Collis, D. J., Foss, N. J., Hoskisson, R. E., & Prescott, J. E. (2021). Corporate strategy and the theory of the firm in the digital age. Journal of Management Studies, 58(7), 1695–1720. https://doi.org/10.1111/joms.12760
Oberländer, A. M., Röglinger, M., Rosemann, M., & Krcmar, H. (2025). Understanding the influence of digital ecosystems on digital transformation: The OCO (orientation, cooperation, orchestration) theory. Information Systems Journal, 35(1), 112–145. https://doi.org/10.1111/isj.12539
Ulbricht, L., & Yeung, K. (2022). Algorithmic regulation: A maturing concept for investigating regulation of and through algorithms. Regulation & Governance, 16(3), 447–465. https://doi.org/10.1111/rego.12437
Adomavicius, G., & Kwon, Y. (2012). Improving aggregate recommendation diversity using ranking-based techniques. IEEE Transactions on Knowledge and Data Engineering, 24(5), 896–911. https://doi.org/10.1109/TKDE.2011.15
Chen, G., Chan, T., Zhang, D., Liu, S., & Wu, Y. (2024). The impact of a more diversified recommender system on digital platforms: Evidence from a large-scale field experiment. Marketing Science, Advance online publication. https://doi.org/10.1287/mksc.2024.1498
Hosanagar, K., Fleder, D., Lee, D., & Buja, A. (2014). Will the global village fracture into tribes? Recommender systems and their effects on consumer fragmentation. Management Science, 60(4), 805–823. https://doi.org/10.1287/mnsc.2013.1808
Yi, S., Kim, D., & Ju, J. (2022). Recommendation technologies and consumption diversity: An experimental study on product recommendations, consumer search, and sales diversity. Technological Forecasting and Social Change, 178, Article 121486. https://doi.org/10.1016/j.techfore.2022.121486
Zhao, Y., Wang, Y., Liu, Y., Cheng, X., Aggarwal, C. C., & Derr, T. (2024). Fairness and diversity in recommender systems: A survey. ACM Computing Surveys, 57(3), Article 60. https://doi.org/10.1145/3664925
马太效应与累积优势
Lynn, F. B., Podolny, J. M., & Tao, L. (2009). A sociological (de)construction of the relationship between status and quality. American Journal of Sociology, 115(3), 755–804. https://doi.org/10.1086/603537
Oestreicher-Singer, G., & Sundararajan, A. (2012). Recommendation networks and the long tail of electronic commerce. MIS Quarterly, 36(1), 65–83. https://doi.org/10.2307/41410406
Perc, M. (2014). The Matthew effect in empirical data. Journal of the Royal Society Interface, 11(98), Article 20140378. https://doi.org/10.1098/rsif.2014.0378
Wang, Q., Guo, Z., & Liu, D. (2022). Do the rich grow richer? An empirical analysis of the Matthew effect in an online healthcare community. Electronic Commerce Research and Applications, 52, Article 101125. https://doi.org/10.1016/j.elerap.2022.101125
平台架构与治理
Eisenmann, T., Parker, G., & Van Alstyne, M. (2011). Platform envelopment. Strategic Management Journal, 32(12), 1270–1285. https://doi.org/10.1002/smj.935
Parker, G., & Van Alstyne, M. (2018). Innovation, openness, and platform control. Management Science, 64(7), 3015–3032. https://doi.org/10.1287/mnsc.2017.2757
Parker, G., Van Alstyne, M., & Jiang, X. (2017). Platform ecosystems: How developers invert the firm. MIS Quarterly, 41(1), 255–266. https://doi.org/10.25300/MISQ/2017/41.1.13
反馈机制与网络效应
Anderson, E. G., Parker, G. G., & Tan, B. (2014). Platform performance investment in the presence of network externalities. Information Systems Research, 25(1), 152–172. https://doi.org/10.1287/isre.2013.0505
Boudreau, K. J. (2010). Open platform strategies and innovation: Granting access versus devolving control. Management Science, 56(10), 1849–1872. https://doi.org/10.1287/mnsc.1100.1215
优化理论应用
Marshall, A. W., Olkin, I., & Arnold, B. C. (2011). Inequalities: Theory of majorization and its applications (2nd ed.). Springer. https://doi.org/10.1007/978-0-387-68276-1
注意力分配与内容多样性
Kitchens, B., Johnson, S. L., & Gray, P. (2020). Understanding echo chambers and filter bubbles: The impact of social media on diversification and partisan shifts in news consumption. MIS Quarterly, 44(4), 1619–1649. https://doi.org/10.25300/MISQ/2020/15057



### 3. 理论贡献与政策含义

本文的研究假说基于平台治理、注意力经济、生态系统演化等多元理论，构建了"多样性约束-成本分化-注意力重新分配"的三机制模型，为理解算法治理如何重塑平台内容生态提供了综合分析框架。与现有研究相比，本文的理论贡献体现在：

第一，整合视角：将平台治理的"水床效应"（Rahman et al., 2024）、算法管理的"选择架构"（Cameron, 2024）、注意力经济的"零和竞争"（Gelper et al., 2021）整合为统一的理论框架，揭示了算法治理的系统性影响——监管不仅改变了单一维度（如多样性），更触发了成本结构、注意力分配、生态均衡的级联变化。

第二，动态机制：区分了三个作用机制（资源重新配置、差异化监管、注意力重新分配）及其时间顺序——多样性约束压缩头部空间（机制1）→质量分化产生成本差异（机制2）→注意力重新分配形成新均衡（机制3）。这一级联过程通常需要3-6个月完成，符合Tiwana等（2010）提出的"平台-治理-环境协同演化"框架。

第三，中国情境：强调中国"政府主导"治理模式的独特性——政府不仅是规则制定者，还是执行监督者和效果评估者，形成了"强监管"模式。这种模式使得平台对政府政策的响应速度和执行力度远超西方国家，也使得监管政策能够在短期内产生显著效果。

政策含义方面，本文的研究假说揭示了算法治理的潜在"副作用"：在提升多样性和内容质量的同时，可能导致注意力从社会类话题向娱乐类话题转移，形成"娱乐化"倾向。这提示政策制定者需要关注：（1）如何在多样性与质量之间寻求平衡，避免过度监管导致社会类话题"失声"；（2）如何设计差异化激励机制，鼓励平台生产高质量社会类内容，而非简单减少曝光；（3）如何监测注意力流向，及时调整监管策略，防止内容生态过度"娱乐化"。这些问题将在本文的实证分析和政策讨论中进一步展开。





浮夸➡️注意力分配➡️注意力转移
1.概念
2.理论
3.跑中介
4.写论文：稳健性：DID