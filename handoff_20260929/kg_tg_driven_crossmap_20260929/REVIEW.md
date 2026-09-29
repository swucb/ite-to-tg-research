# TG 需求驱动检索：逐项审查

前 40 项为每个需求在 iTE 和 TG 中各取前 5 篇不同论文。另有 2 项来自保存的前 200 条关系助手扩展查看，已标明原排名。审查人为本助手；不是独立专家评审，也不是效果准确率。

## N01_iTE_01

**排除**：调节温差导致表面迁移，目标应用为摩擦电；并未提供加快 TG 凝胶体相红氧物种扩散的材料改进。

原关系排名 1；检索分数 0.699（非迁移概率）。

[Ionic Thermoelectric Effect Inducing Cation-Enriched Surface of Hydrogel to Enhance Output Performance of Triboelectric Nanogenerator](https://doi.org/10.1002/ente.202200070)

`iTE:P0404:r002`：Temperature difference between hydrogel top and bottom → regulates → Hydrogel-surface ion migration

> The ion migration on the hydrogel surface is regulated via tuning the temperature difference between the top and bottom sides. 

条件：By tuning the top-to-bottom temperature difference；断言：author_claim；联合因素：[]。

## N01_iTE_02

**待定参考**：冠醚增强热扩散有原文依据，但热扩散不等同于氧化还原物种补给；该源本身含红氧电极，须先区分已有混合机制。

原关系排名 2；检索分数 0.684（非迁移概率）。

[Advanced N-Type Ionic Thermoelectric Cells Featuring Bidirectional Cationic Anchoring Strategy and REDOX Electrode](https://doi.org/10.1002/aenm.202500584)

`iTE:P0342:r004`：Crown ether incorporation for complexation → enhances → Thermal diffusion within ionic hydrogel electrolyte

> Specifically, a gel network featuring dual positive groups is synthesized by cross-linking quaternized chitosan and guanidine molecules via glutaraldehyde, with thermal diffusion further enhanced by incorporating crown ether for complexation. 

条件：Dual-positive-group gel network；断言：author_claim；联合因素：[]。

同论文下游：

- `iTE:P0342:r001`：Thermal diffusion within ionic hydrogel electrolyte → synergistically enables → Substantial negative thermopower；联合因素：['Thermal diffusion within ionic hydrogel electrolyte', 'Redox reactions at the electrode interface']
- `iTE:P0342:r002`：Thermal diffusion within ionic hydrogel electrolyte → synergistically enables → High output energy density；联合因素：['Thermal diffusion within ionic hydrogel electrolyte', 'Redox reactions at the electrode interface']

同一主体的其他主张：

- `iTE:P0342:complete_v1_cr001`：Crown ether incorporation for complexation → is intended to promote → Complexation；联合因素：[]

## N01_iTE_03

**排除**：建立解释模型不是解决扩散瓶颈的材料调控办法。

原关系排名 3；检索分数 0.670（非迁移概率）。

[Multi-Ionic Hydrogel with Outstanding Heat-to-Electrical Performance for Low-Grade Heat Harvesting](https://doi.org/10.1002/asia.202200850)

`iTE:P0616:r004`：Model of ion thermal diffusion in multi-ionic hydrogels → is_built_to_explain → Thermal diffusion of ions in multi-ionic hydrogels

> Subsequently we build a model to explain thermal diffusion of the ions in multi-ionic hydrogels. 

条件：Model; abstract supplies no model equations or predictions；断言：author_claim；联合因素：[]。

## N01_iTE_04

**待定参考**：有明确溶剂比例调控，但所选证据只说 regulate，未给方向和目标红氧物种；TG 已有共溶剂策略。

原关系排名 4；检索分数 0.661（非迁移概率）。

[Janus bilayer poly(vinyl alcohol)-based composite hydrogels with tunable photothermal and thermoelectric properties for photothermoelectric energy conversion](https://doi.org/10.1016/j.jpowsour.2025.238731)

`iTE:P1175:r002`：DMSO:H2O solvent-ratio adjustment → regulates → Hydrogel ionic transport properties

> Herein, a Janus bilayer poly(vinyl alcohol) (PVA)-based PTE conversion hydrogel is successfully developed by incorporating carbon-based nanomaterials in the upper layer and systematically adjusting the dimethyl sulfoxide (DMSO):water (H2O) solvent ratio to regulate the hydrogel's thermal and ionic transport properties. 

条件：Janus bilayer PVA-based hydrogel；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `iTE:P1175:r001`：DMSO:H2O solvent-ratio adjustment → regulates → Hydrogel thermal transport properties；联合因素：[]
- `iTE:P1175:r006`：DMSO:H2O solvent-ratio adjustment → enables → Hydrogel thermal conductivity 0.42 W m−1 K−1；联合因素：[]
- `iTE:P1175:r007`：DMSO:H2O solvent-ratio adjustment → enables → Ionic Seebeck coefficient 1.78 mV K−1；联合因素：[]

## N01_iTE_05

**排除**：整合电子与离子通路不直接证明红氧物种扩散加快，不能按 integrated conduction 判为解决方案。

原关系排名 5；检索分数 0.656（非迁移概率）。

[Synergistic ion-electron coupling in thermoelectric hydrogels for self-powered sensing](https://doi.org/10.1039/d6ta02391f)

`iTE:P1155:r001`：Synergistic ion-electron coupling strategy → integrates → Integrated ionic and electronic conduction pathways in one hydrogel

> Here, a synergistic ion-electron coupling strategy is proposed by integrating ionic and electronic conduction pathways within a single hydrogel system. 

条件：；断言：author_claim；联合因素：[]。

## N02_iTE_01

**排除**：源策略促进聚集并增强离子相互作用，与当前“减弱配对/促进解离”的目标方向相反；不能凭相似词接受。

原关系排名 1；检索分数 0.607（非迁移概率）。

[Giant and bidirectionally tunable thermopower in nonaqueous ionogels enabled by selective ion doping](https://doi.org/10.1126/sciadv.abj3019)

`iTE:P0689:r004`：Selective ion aggregate formation → is proposed to enhance → Ion-ion interactions

> A thermopower regulation strategy through ion doping to selectively induce ion aggregates to enhance ion-ion interactions is proposed. 

条件：Selective ion doping strategy；断言：hypothesis；联合因素：[]。

同论文上游：

- `iTE:P0689:r003`：Selective ion doping → is proposed to induce → Selective ion aggregate formation；联合因素：[]

同论文下游：

- `iTE:P0689:r005`：Ion-ion interactions → decisively modulates → Thermopower sign；联合因素：[]
- `iTE:P0689:r006`：Ion-ion interactions → decisively modulates → Thermopower magnitude；联合因素：[]

## N02_iTE_02

**保留假设**：局部电场与选择性锚定位点共同促进解离，方向与需求相符；源为电容式离子热电，目标为红氧凝胶，适用性尚未建立。

原关系排名 2；检索分数 0.597（非迁移概率）。

[Decoupling ion transport and mechanical robustness in ionic thermoelectrics via defect-rich SrTiO3 nanofibers](https://doi.org/10.1016/j.cej.2026.177118)

`iTE:P0589:r004`：Built-in local electric fields → jointly promotes → Ion dissociation

> The ferroelectric polarization and oxygenvacancy-rich surfaces of SrTiO3 generate built-in local electric fields and ion-selective anchoring sites, which promote ion dissociation and amplify cation-anion migration asymmetry. 

条件：；断言：author_claim；联合因素：['Built-in local electric fields', 'Ion-selective anchoring sites']。

同论文上游：

- `iTE:P0589:r002`：SrTiO3 ferroelectric polarization → jointly generates → Built-in local electric fields；联合因素：['SrTiO3 ferroelectric polarization', 'Oxygen-vacancy-rich SrTiO3 surfaces']

同一主体的其他主张：

- `iTE:P0589:r005`：Built-in local electric fields → jointly amplifies → Cation–anion migration asymmetry；联合因素：['Built-in local electric fields', 'Ion-selective anchoring sites']

## N02_iTE_03

**已有机制参考**：促进输运不等于解除配对；重分配到 N01 后有比较价值，但 TG 已有定向网络与通道，不能笼统列为新迁移。

原关系排名 3；检索分数 0.588（非迁移概率）。

[Aligned cellulose nanofibril ionogels with continuous micro-nanochannels for ionic thermoelectrics and self-powered sensors](https://doi.org/10.1016/j.compositesb.2026.113490)

`iTE:P0585:r003`：Continuous low-resistance ion pathways → facilitates → Facilitated ion transport

> This design offers continuous and low-resistance pathways, markedly facilitating ion transport. 

条件：；断言：author_claim；联合因素：[]。

同论文上游：

- `iTE:P0585:r002`：Well-aligned cellulose nanofibril micro-nanochannels → provides → Continuous low-resistance ion pathways；联合因素：[]

## N02_iTE_04

**保留假设（低证据）**：源将聚合物链/离子液体作用引起的聚集体解离作为电导改善解释；是作者的模型归因，不能当作独立实测解离证据。

原关系排名 4；检索分数 0.586（非迁移概率）。

[High thermoelectric performance of multiwalled carbon nanotubes based ionogels](https://doi.org/10.1016/j.mtcomm.2024.108334)

`iTE:P0548:r003`：Ionic liquid–polymer chain interaction → causes → Dissociation of ion aggregates

> This substantial improvement can be attributed to the breathing polymer chain model, which describes the dissociation of ion aggregates due to the interaction between the ionic liquid and polymer chains. 

条件：Breathing polymer chain model.；断言：author_claim；联合因素：[]。

同论文下游：

- `iTE:P0548:r004`：Dissociation of ion aggregates → is invoked to explain → 75.3% enhancement in ionic conductivity；联合因素：[]

## N02_iTE_05

**排除**：固态超离子导体晶格模型里浓度过高增加排斥并降低电导，不是 TG 解配对方案。

原关系排名 5；检索分数 0.577（非迁移概率）。

[Concentration dependence of the ionic conductivity in superionic conductors](https://doi.org/10.1143/JPSJ.70.2958)

`iTE:P0963:r005`：Mobile-ion concentration in superionic conductors → increases → Repulsive interaction among mobile ions

> The dependence of the ionic conductivity on the mobile ion concentration in superionic conductors is studied by making use of the lattice gas model with a hopping term and Kubo's formula. 

> The ionic conductivity first increases' vith the increasing mobile ions, and has the maximum and then decreases with the further increase of mobile ion concentration by increasing the repulsive interaction among the mobile ions. 

条件：Further increase in mobile-ion concentration beyond the conductivity maximum; lattice gas model.；断言：author_claim；联合因素：[]。

同论文下游：

- `iTE:P0963:r006`：Repulsive interaction among mobile ions → decreases → Ionic conductivity；联合因素：[]

同一主体的其他主张：

- `iTE:P0963:r004`：Mobile-ion concentration in superionic conductors → initially increases and subsequently decreases → Ionic conductivity；联合因素：[]

## N03_iTE_01

**排除**：电导改善没有证明保水或抗冻；同源还指出无机填料可能损伤其他性质。

原关系排名 1；检索分数 0.648（非迁移概率）。

[Ultra-High Electrical Conductivity in Filler-Free Polymeric Hydrogels Toward Thermoelectrics and Electromagnetic Interference Shielding](https://doi.org/10.1002/adma.202109904)

`iTE:P1356:complete_v1_cr005`：Introducing conductive inorganic fillers into hydrogels → can improve → Hydrogel electrical conductivity

> Introducing conductive inorganic fillers into the hydrogels can improve their electrical conductivities. 

条件：；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `iTE:P1356:complete_v1_cr006`：Introducing conductive inorganic fillers into hydrogels → may compromise → Hydrogel compliance；联合因素：[]
- `iTE:P1356:complete_v1_cr007`：Introducing conductive inorganic fillers into hydrogels → may compromise → Hydrogel biocompatibility；联合因素：[]
- `iTE:P1356:complete_v1_cr008`：Introducing conductive inorganic fillers into hydrogels → may compromise → Hydrogel deformability；联合因素：[]
- `iTE:P1356:complete_v1_cr009`：Introducing conductive inorganic fillers into hydrogels → may compromise → Hydrogel biodegradability；联合因素：[]

## N03_iTE_02

**排除**：升温导致失水是反例/问题描述，不是保水方案。

原关系排名 2；检索分数 0.633（非迁移概率）。

[Ionic Thermoelectric Effect Inducing Cation-Enriched Surface of Hydrogel to Enhance Output Performance of Triboelectric Nanogenerator](https://doi.org/10.1002/ente.202200070)

`iTE:P0404:r007`：Hydrogel surface temperature above 50 °C → causes → Hydrogel water loss

> When the temperature of the hydrogel surface is higher than 50 degrees C, the output performance of TENG would decrease due to the water loss of hydrogel. 

条件：；断言：author_claim；联合因素：[]。

同论文下游：

- `iTE:P0404:r008`：Hydrogel water loss → decreases → TENG output performance；联合因素：[]

同一主体的其他主张：

- `iTE:P0404:r009`：Hydrogel surface temperature above 50 °C → decreases → TENG output performance；联合因素：[]

## N03_iTE_03

**已有机制参考**：LiCl 水合促进吸湿恢复和抗冻有依据；TG 已有 LiBr 吸湿盐与空气吸水恢复，不应把吸湿盐原则包装成新方向。

原关系排名 3；检索分数 0.622（非迁移概率）。

[Highly stretchable, low-hysteresis, and antifreeze hydrogel for low-grade thermal energy harvesting in ionic thermoelectric Supercapacitors](https://doi.org/10.1016/j.mtphys.2024.101589)

`iTE:P0365:complete_v1_cr001`：Moisture absorption by PAM/CMC-xLiCl ionic thermoelectric hydrogels → enables → Hydrogel self-regeneration

> In this study, we designed a series of ionic thermoelectric hydrogels, PAM/CMC-xLiCl, with high mechanical properties. 

> Furthermore, due to the hydration properties of LiCl, the ionic hydrogels exhibit excellent freeze resistance and the capability to absorb moisture for self-regeneration upon drying. 

条件：Upon drying；断言：author_claim；联合因素：[]。

## N03_iTE_04

**排除**：这条边描述失水限制功能，重复了需求，没有提供解决措施。

原关系排名 4；检索分数 0.618（非迁移概率）。

[N-type thermoelectric composite hydrogels enabling dual-channel ionic/electronic transport](https://doi.org/10.1007/s42114-025-01495-8)

`iTE:P0413:complete_v1_cr002`：Rapid dehydration and poor polymeric-framework–electrolyte interactions → constrain → Thermoelectric hydrogel functionality

> Thermoelectric hydrogels have drawn increasing research interest owing to their high ionic thermopower (alpha) values and superior mechanical stretchability. 

> However, they are critically constrained by rapid dehydration and the poor interactions between polymeric frameworks and electrolytes, which fail to differentiate the diffusion rates of cations and anions under a certain temperature gradient (Delta T). 

条件：；断言：author_claim；联合因素：['Rapid dehydration', 'Poor interactions between polymeric frameworks and electrolytes']。

## N03_iTE_05

**排除**：低输出限制应用是宽泛问题，不是失水/冻结的解决措施。

原关系排名 5；检索分数 0.614（非迁移概率）。

[High ionic thermopower in flexible composite hydrogel for wearable self-powered sensor](https://doi.org/10.1016/j.compscitech.2022.109771)

`iTE:P0609:complete_v1_cr003`：Low thermoelectric output power of hydrogel → restricts → Hydrogel applications

> However, the low thermoelectric output power of hydrogel restricts their applications. 

条件：；断言：author_claim；联合因素：[]。

## N04_iTE_01

**已有机制参考**：源本身为 Fe2+/3+ 液体热电化学体系。增厚降低阻力可作电极参考，但不是从纯离子热扩散迁入 TG 的新机制。

原关系排名 1；检索分数 0.552（非迁移概率）。

[Coated electrodes for liquid thermoelectric conversion devices to enhance Fe2+/Fe3+ redox kinetics](https://doi.org/10.1039/d4se00220b)

`iTE:P1186:r001`：Increasing electrode thickness → increases → Reciprocal charge-transfer resistance

> Here, we systematically investigated Fe2+/Fe3+ redox kinetics at graphite-dispersion coated electrodes in 0.8 M Fe(ClO4)(2)/Fe(ClO4)(3 )aqueous solution. 

> We found that the reciprocal of charge transfer resistance Rct and diffusion resistance Rdif increases with increase in the electrode thickness t. 

条件：Graphite-dispersion coated electrodes in 0.8 M Fe(ClO4)2/Fe(ClO4)3 aqueous solution.；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `iTE:P1186:r002`：Increasing electrode thickness → increases → Reciprocal diffusion resistance；联合因素：[]

## N04_iTE_02

**已有机制参考**：源已使用铁氰化物/亚铁氰化物电对；注意上升的是阻力倒数，且只在 t≤40 μm 区间成立，不能无限增厚。

原关系排名 2；检索分数 0.547（非迁移概率）。

[Resistance components of liquid thermoelectric converter composed of \[Fe(CN)6\]3-/\[Fe(CN)6\]4- aqueous electrolyte and graphite-dispersing electrodes](https://doi.org/10.1039/d5ra07066j)

`iTE:P1188:r004`：Increasing electrode thickness t → linearly_increases → Reciprocal charge-transfer resistance

> Here, we systematically investigated components of device resistance R, i.e., solute (Rs), charge-transfer (Rct), and diffusion (Rdif) resistances, of LTE composed of 0.8 M Na4\[Fe(CN)6\]/K3\[Fe(CN)6\] aqueous electrolyte and graphite-dispersing electrodes. 

> R-1ct and Rdif-1 linearly increase with t in the thin t region (t <= 40 mu m) reflecting the increase in electrochemical active surface area (EASA). 

条件：LTE with 0.8 M Na4[Fe(CN)6]/K3[Fe(CN)6] aqueous electrolyte and graphite-dispersing electrodes; thin-electrode region, t ≤ 40 μm.；断言：author_claim；联合因素：[]。

同论文下游：

- `iTE:P1188:r007`：Reciprocal charge-transfer resistance → increase_reflects_increase_in → Electrochemical active surface area；联合因素：[]

同一主体的其他主张：

- `iTE:P1188:r005`：Increasing electrode thickness t → linearly_increases → Reciprocal diffusion resistance；联合因素：[]
- `iTE:P1188:r006`：Increasing electrode thickness t → increases → Electrochemical active surface area；联合因素：[]

## N04_iTE_03

**待定参考**：源本身含红氧和热扩散，体积相变增熵对反应效率的贡献不能直接换算为电荷转移速率或抗钝化。

原关系排名 3；检索分数 0.543（非迁移概率）。

[Phase transition driven tough hydrogel ionic thermoelectric cell with giant thermopower](https://doi.org/10.1038/s41467-025-64054-1)

`iTE:P0339:r005`：Substantial ion entropy difference → enhances → Redox reaction efficiency

> The volume phase transition (VPT) of PNA i-TE cell can generate a substantial ion entropy difference, thereby enhancing both the redox reaction efficiency and ionic thermodiffusion rate. 

条件：Ion entropy difference generated by PNA volume phase transition；断言：author_claim；联合因素：[]。

同论文上游：

- `iTE:P0339:r004`：Volume phase transition of PNA cell → generates → Substantial ion entropy difference；联合因素：[]

同一主体的其他主张：

- `iTE:P0339:r006`：Substantial ion entropy difference → enhances → Ionic thermodiffusion rate；联合因素：[]

## N04_iTE_04

**排除**：优于单金属硒化物的宽泛电化学表现，不足以证明在目标铁氰化物凝胶中的动力学和稳定性。

原关系排名 4；检索分数 0.542（非迁移概率）。

[Dual-functionality of NiSe2-CoSe2 nanowires for electrochemical charge storage and efficient thermal energy conversion](https://doi.org/10.1016/j.est.2025.116568)

`iTE:P1271:r002`：NCS/ACC electrode → outperforms monometallic selenides in → Electrochemical performance

> Comparative analysis demonstrates that NCS/ACC electrodes significantly outperform monometallic selenides in both electrochemical performance and thermoelectric applications. 

条件：Comparative analysis；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `iTE:P1271:r003`：NCS/ACC electrode → outperforms monometallic selenides in → Thermoelectric application performance；联合因素：[]
- `iTE:P1271:r004`：NCS/ACC electrode → has → Maximum charge storage capacity: 112 mA h g^-1；联合因素：[]

## N04_iTE_05

**排除**：EIS–TEM 为表征关联方法，不是改善电极的调控措施。

原关系排名 5；检索分数 0.538（非迁移概率）。

[Electrochemical Impedance Spectroscopy Integrated with Environmental Transmission Electron Microscopy](https://doi.org/10.1002/smtd.202201713)

`iTE:P1599:r002`：Structural and compositional information → is directly correlated with → Electrochemical performance

> The EIS-TEM method provides structural and compositional information with direct correlation to the electrochemical performance. 

条件：Integrated EIS–TEM method；断言：association；联合因素：[]。

同论文上游：

- `iTE:P1599:r001`：Integrated EIS–ETEM method → provides → Structural and compositional information；联合因素：[]

## N01_TG_01

**直接相关既有方案**：共溶剂同时改善红氧物种输运和溶剂化；已是 TG 原生方案。

原关系排名 1；检索分数 0.672（非迁移概率）。

[Engineering asymmetric solvation structures for synergistically boosted quasi-solid thermocells](https://doi.org/10.1039/d6sc03942a)

`TG:P0172:r004`：Trimethyl phosphate–ethylene glycol co-solvent strategy → enhances → Redox-ion transport through the hydrogel network

> To break this longstanding trade-off, we present a simple yet highly effective co-solvent strategy that employs trimethyl phosphate and ethylene glycol to construct hybrid hydrogel electrolytes. 

> This approach synergistically enlarges solvation entropy differences of redox ions, amplifies the concentration gradient across the thermocell, and enhances redox ion transport through the hydrogel network. 

条件：；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `TG:P0172:r001`：Trimethyl phosphate–ethylene glycol co-solvent strategy → constructs → Hybrid hydrogel electrolyte；联合因素：[]
- `TG:P0172:r002`：Trimethyl phosphate–ethylene glycol co-solvent strategy → synergistically_enlarges → Redox-ion solvation entropy difference；联合因素：[]
- `TG:P0172:r003`：Trimethyl phosphate–ethylene glycol co-solvent strategy → amplifies → Concentration gradient across the thermocell；联合因素：[]
- `TG:P0172:r007`：Trimethyl phosphate–ethylene glycol co-solvent strategy → engineers → Asymmetric solvation structures；联合因素：[]

## N01_TG_02

**直接相关既有方案**：破坏水结构的盐改善扩散，是需求原论文给出的方案。

原关系排名 2；检索分数 0.662（非迁移概率）。

[High-Performance Quasi-Solid-State Thermogalvanic Cells with Metallized Fibril-Based Textile Electrodes and Structure-Breaking Salts](https://doi.org/10.1002/aenm.202404151)

`TG:P0046:r009`：Disruption of hydrogel water structures → improves → Ion diffusion

> Meanwhile, the structure-breaking salts facilitate redox reactions and improve ion diffusion by disrupting water structures in the hydrogel electrolyte. 

条件：Caused by structure-breaking salts；断言：author_claim；联合因素：[]。

同论文上游：

- `TG:P0046:r005`：Structure-breaking salts → cause → Disruption of hydrogel water structures；联合因素：[]

同一主体的其他主张：

- `TG:P0046:r008`：Disruption of hydrogel water structures → facilitates → Redox reactions；联合因素：[]

## N01_TG_03

**其他体系参考**：缩短扩散路径有证据，但源为锌热充电超级电容器；TG 语料归属不等于目标器件机制。

原关系排名 6；检索分数 0.607（非迁移概率）。

[High-efficiency zinc thermal charging supercapacitors enabled by hierarchical porous carbon electrodes](https://doi.org/10.1016/j.jpowsour.2022.232386)

`TG:P0300:r005`：Continuous NHPC architecture → shortens → Electrolyte-ion diffusion pathways

> Significantly, continuous architecture of NHPC can enlarge the electrochemical active surface and shorten the diffusion pathways of electrolyte ions. 

条件：；断言：author_claim；联合因素：[]。

同论文上游：

- `TG:P0300:r003`：Nitrogen-doped hierarchical porous carbon (NHPC) → has → Continuous NHPC architecture；联合因素：[]

同一主体的其他主张：

- `TG:P0300:r004`：Continuous NHPC architecture → enlarges → Electrochemical active surface；联合因素：[]

## N01_TG_04

**问题描述**：冻结/干燥损失输运能力，所选边不是解决措施。

原关系排名 8；检索分数 0.577（非迁移概率）。

[Aqueous eutectic hydrogel electrolytes enable flexible thermocells with a wide operating temperature range](https://doi.org/10.1039/d2ta09385e)

`TG:P0193:complete_v1_cr006`：Freezing or drying out of conventional hydrogel electrolytes → causes loss of → Ion transport capability

> In contrast, conventional hydrogel electrolytes cannot adapt to a sufficiently wide working temperature range, as they inevitably freeze under sub-zero temperatures and dry out under elevated temperatures, resulting in loss in both mechanical flexibility and ion transport capability. 

条件：Freezing under sub-zero temperatures or drying out under elevated temperatures；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `TG:P0193:complete_v1_cr005`：Freezing or drying out of conventional hydrogel electrolytes → causes loss of → Mechanical flexibility；联合因素：[]

## N01_TG_05

**不充分**：高浓度引入改善输出不直接证明扩散加快；不能替代目标机制证据。

原关系排名 9；检索分数 0.571（非迁移概率）。

[A Room-Temperature Excessively Concentrated Polyanionic Polymer Hydrogel Thermocell with High Absorbency, Retainability and Extensibility](https://doi.org/10.1021/acsaem.5c00167)

`TG:P0252:r014`：Heated-solution immersion method → introduces → Excessive electrolyte concentrations in hydrogel thermocells

> These findings present a universal and effective strategy for enhancing the output performance of hydrogel thermocells by introducing excessive electrolyte concentrations via a simple heated-solution immersion method.

条件：；断言：author_claim；联合因素：[]。

同论文下游：

- `TG:P0252:r015`：Excessive electrolyte concentrations in hydrogel thermocells → enhances → Hydrogel thermocell output performance；联合因素：[]

## N02_TG_01

**相关既有方案（电对不同）**：高氯酸根弱配位抑制 Fe(III/II) 电解液配对；不能不加区分移植到铁氰化物电对。

原关系排名 1；检索分数 0.568（非迁移概率）。

[Unravelling ionic speciation and hydration structure of Fe(III/II) redox couples for thermoelectrochemical cells](https://doi.org/10.1016/j.electacta.2020.135651)

`TG:P0285:r004`：Non-coordinating character of perchlorate → suppresses → Ion-pair formation

> Herein, we unravel that the excellent performance of the Fe(III)/(II) perchlorate is ascribed to the non-coordinating nature of its perchlorate anion, which suppresses the formation of the ion pairs that reduce the S-e and ionic conductivity. 

条件：Fe(III)/(II) perchlorate electrolyte；断言：author_claim；联合因素：[]。

同论文上游：

- `TG:P0285:r003`：Perchlorate anion → has → Non-coordinating character of perchlorate；联合因素：[]

同论文下游：

- `TG:P0285:r006`：Ion-pair formation → reduces → Seebeck coefficient；联合因素：[]
- `TG:P0285:r007`：Ion-pair formation → reduces → Ionic conductivity；联合因素：[]

同一主体的其他主张：

- `TG:P0285:r005`：Non-coordinating character of perchlorate → accounts for → High areal power density；联合因素：[]

## N02_TG_02

**不充分**：界面促进反应/输运，没有给出抑制配对的直接证据。

原关系排名 2；检索分数 0.493（非迁移概率）。

[Significantly enhanced properties of micro-ionic thermocells through the microstructure interfacial effect](https://doi.org/10.1039/d4ta03996c)

`TG:P0275:r014`：Microstructure–electrolyte solution interfacial effect → boosts → Ionic reactions

> The interfacial effect of microstructure-electrolyte solution can boost ionic reactions and transport processes at the microscale. 

条件：At microscale；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `TG:P0275:r015`：Microstructure–electrolyte solution interfacial effect → boosts → Ionic transport processes；联合因素：[]
- `TG:P0275:r016`：Microstructure–electrolyte solution interfacial effect → enhances magnitude from −1.4 to −2.5 mV K−1 → MiTC ionic thermopower；联合因素：[]
- `TG:P0275:r017`：Microstructure–electrolyte solution interfacial effect → increases from 147.6 to 254.2 mS cm−1 → MiTC electrolyte conductivity；联合因素：[]
- `TG:P0275:r018`：Microstructure–electrolyte solution interfacial effect → enables value 15.4 mW m−2 K−2 for → MiTC Pmax/ΔT²；联合因素：[]

## N02_TG_03

**问题描述**：原需求本身；本论文的双层分隔方案另由锚点扩展保留。

原关系排名 3；检索分数 0.491（非迁移概率）。

[Bioinspired double-layer thermogalvanic cells with engineered ionic gradients for high-efficiency waste heat recovery](https://doi.org/10.1016/j.nanoen.2025.111189)

`TG:P0021:complete_v1_cr001`：Ion pairing → hinders_establishment_of → Substantial ion concentration gradients

> A critical factor in enhancing TGC performance lies in establishing substantial ion concentration gradients, which remains challenging due to the inherent tendency of ion pairing. 

条件：Thermogalvanic cells；断言：author_claim；联合因素：[]。

## N02_TG_04

**相关既有方案**：选择性结合保留反离子移动，与离子选择性有关，但不等于减弱所有配对。

原关系排名 4；检索分数 0.482（非迁移概率）。

[Ion transport control in electrolytes via electrochemical doping](https://doi.org/10.1073/pnas.2532302123)

`TG:P0249:r005`：Electrolyte doping by incorporating electroactive polymers within hydrogels → enables → Unipolar ion transport

> Here, we report a universal strategy to dope electrolytes such that the ion transport can be unipolar by incorporating electroactive polymers within hydrogels that interact discriminately with one type of ion via redox and binding mechanisms, leaving the counterions mobile. 

条件：Electroactive polymers discriminate between ion types via redox and binding.；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `TG:P0249:r004`：Electrolyte doping by incorporating electroactive polymers within hydrogels → preserves → Mobile counterions；联合因素：[]
- `TG:P0249:r006`：Electrolyte doping by incorporating electroactive polymers within hydrogels → transforms_electrolyte_into → Active selective ionic conductor；联合因素：[]
- `TG:P0249:r011`：Electrolyte doping by incorporating electroactive polymers within hydrogels → provides → Boosted thermoelectrochemical device performance；联合因素：[]
- `TG:P0249:r012`：Electrolyte doping by incorporating electroactive polymers within hydrogels → has_potential_use_in → Supercapacitor applications；联合因素：[]
- `TG:P0249:r013`：Electrolyte doping by incorporating electroactive polymers within hydrogels → has_potential_use_in → Battery applications；联合因素：[]
- `TG:P0249:r014`：Electrolyte doping by incorporating electroactive polymers within hydrogels → has_potential_use_in → Electrochemical sensor applications；联合因素：[]

## N02_TG_05

**表征信息**：测定迁移熵，不是解配对调控办法。

原关系排名 5；检索分数 0.468（非迁移概率）。

[Entropy characteristic of solvation and thermal diffusion of hydrogen chloride in water-1-propanol solutions: A thermoelectrochemical determination](https://doi.org/10.1134/S1023193506090102)

`TG:P0239:r002`：Experimental study of HCl-H2O-1-PrOH thermogalvanic cells → determines → Entropies of mobile H+ and Cl- ions

> Thermogalvanic cells with silver chloride and quinhydrone electrodes in the HCl-H2O-1-PrOH system are studied experimentally. 

> The results are used to determine standard entropies of thermal diffusion transport of hydrogen chloride, entropies of mobile H+ and Cl- ions, and Soret coefficients of the electrolyte at 298 K. 

条件：298 K; cells with silver chloride and quinhydrone electrodes；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `TG:P0239:r001`：Experimental study of HCl-H2O-1-PrOH thermogalvanic cells → determines → Standard entropies of hydrogen chloride thermal diffusion transport；联合因素：[]
- `TG:P0239:r003`：Experimental study of HCl-H2O-1-PrOH thermogalvanic cells → determines → Electrolyte Soret coefficients；联合因素：[]

## N03_TG_01

**不充分**：所选边谈浓度与输出，不能据此认定保水机理；论文标题中的 retainability 也不能替代机制证据。

原关系排名 1；检索分数 0.626（非迁移概率）。

[A Room-Temperature Excessively Concentrated Polyanionic Polymer Hydrogel Thermocell with High Absorbency, Retainability and Extensibility](https://doi.org/10.1021/acsaem.5c00167)

`TG:P0252:r014`：Heated-solution immersion method → introduces → Excessive electrolyte concentrations in hydrogel thermocells

> These findings present a universal and effective strategy for enhancing the output performance of hydrogel thermocells by introducing excessive electrolyte concentrations via a simple heated-solution immersion method.

条件：；断言：author_claim；联合因素：[]。

同论文下游：

- `TG:P0252:r015`：Excessive electrolyte concentrations in hydrogel thermocells → enhances → Hydrogel thermocell output performance；联合因素：[]

## N03_TG_02

**问题描述**：所选边是冻干限制，需另读同论文方案，不能计作解决证据。

原关系排名 2；检索分数 0.618（非迁移概率）。

[Thermogalvanic hydrogels for self-powered temperature monitoring in extreme environments](https://doi.org/10.1039/d2tc00889k)

`TG:P0066:complete_v1_cr001`：Freezing and drying of hydrogels → limit → Scope of hydrogel applications

> However, the incident freezing and drying behaviors of hydrogels by using water solvent as the dispersion medium limit their scope of application greatly. 

条件：Water solvent used as the dispersion medium.；断言：author_claim；联合因素：['Freezing', 'Drying']。

## N03_TG_03

**不充分**：盐析限域影响热电表现，没有给出保水/抗冻证据。

原关系排名 3；检索分数 0.600（非迁移概率）。

[Thermogalvanic hydrogel with controllable ion confined transportation and its application for self-powered lactic acid sensor](https://doi.org/10.1016/j.nanoen.2024.110329)

`TG:P0045:r004`：Confined ion transportation in micro/nano channels → accounts_for_concentration_dependence_of → Hydrogel thermoelectric performance

> The thermoelectric performance of the proposed hydrogel is highly dependent on the ion concentration, which is attributed to the confined ion transportation in micro/nano channels caused by the salting out effect. 

条件：Ion concentration dependence; effect sign unspecified；断言：author_claim；联合因素：[]。

同论文上游：

- `TG:P0045:r003`：Salting-out effect → causes → Confined ion transportation in micro/nano channels；联合因素：[]

同论文下游：

- `TG:P0045:r002`：Hydrogel thermoelectric performance → strongly_depends_on → Ion concentration；联合因素：[]

## N03_TG_04

**直接相关既有方案**：从空气吸水恢复水分，说明自主补水这一原则在 TG 已有。

原关系排名 4；检索分数 0.600（非迁移概率）。

[Thermogalvanic Hydrogel for Synchronous Evaporative Cooling and Low-Grade Heat Energy Harvesting](https://doi.org/10.1021/acs.nanolett.0c00800)

`TG:P0058:r007`：Water absorption from surrounding air → produces → Regenerated hydrogel water content

> Moreover, the hydrogel can absorb water from the surrounding air to regenerate its water content later on. 

条件：；断言：author_claim；联合因素：[]。

同论文上游：

- `TG:P0058:r006`：Smart thermogalvanic hydrogel film → supports → Water absorption from surrounding air；联合因素：[]

## N03_TG_05

**其他功能**：破坏水结构改善反应和扩散；不能自动推出防干燥。

原关系排名 5；检索分数 0.594（非迁移概率）。

[High-Performance Quasi-Solid-State Thermogalvanic Cells with Metallized Fibril-Based Textile Electrodes and Structure-Breaking Salts](https://doi.org/10.1002/aenm.202404151)

`TG:P0046:r005`：Structure-breaking salts → cause → Disruption of hydrogel water structures

> Meanwhile, the structure-breaking salts facilitate redox reactions and improve ion diffusion by disrupting water structures in the hydrogel electrolyte. 

条件：Hydrogel electrolyte；断言：author_claim；联合因素：[]。

同论文下游：

- `TG:P0046:r008`：Disruption of hydrogel water structures → facilitates → Redox reactions；联合因素：[]
- `TG:P0046:r009`：Disruption of hydrogel water structures → improves → Ion diffusion；联合因素：[]

同一主体的其他主张：

- `TG:P0046:r006`：Structure-breaking salts → facilitate → Redox reactions；联合因素：[]
- `TG:P0046:r007`：Structure-breaking salts → improve → Ion diffusion；联合因素：[]

## N04_TG_01

**相关既有方案（电对不同）**：FeNC 催化改善 Fe2+/3+ 内球反应，可作对照但与铁氰化物体系不同。

原关系排名 1；检索分数 0.632（非迁移概率）。

[FeNC Electrocatalyst for Enhancing Fe(II)/Fe(III) Redox Kinetics in Thermo-Electrochemical Cells](https://doi.org/10.1002/adfm.202304067)

`TG:P0277:r009`：FeNC electrocatalyst → provides → Redox kinetics comparable to Pt electrodes

> The modulation of the chaotropicity of counteranions enhances the absolute value of the Seebeck coefficient for the Fe2+/3+ redox couple with an inner-sphere reaction mechanism because of the greater structural disorder in the solvation shell. 

> Moreover, the use of a cost-effective FeNC electrocatalyst shows redox kinetics and a power density comparable to those of state-of-the-art Pt electrodes, economically compensating for the sluggish charge-transfer kinetics of the inner-sphere redox mechanism. 

条件：Fe2+/3+ redox couple; compared with state-of-the-art Pt electrodes.；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `TG:P0277:r008`：FeNC electrocatalyst → compensates for → Sluggish charge-transfer kinetics；联合因素：[]
- `TG:P0277:r010`：FeNC electrocatalyst → provides → Power density comparable to Pt electrodes；联合因素：[]

## N04_TG_02

**相关既有方案（电对不同）**：MXene 结构/端基改善动力学，主要为 Fe2+/3+，需要电对兼容性检查。

原关系排名 2；检索分数 0.605（非迁移概率）。

[MXene Hollow Microsphere-Boosted Nanocomposite Electrodes for Thermocells with Enhanced Thermal Energy Harvesting Capability](https://doi.org/10.1021/acsnano.4c12294)

`TG:P0135:r005`：Ti3C2Tx MXene hollow-microsphere nanocomposite electrode → improves → Improved electrode-electrolyte interfacial redox kinetics

> In this study, a nanocomposite electrode featuring Ti3C2T x with hollow microsphere structures is rationally designed. 

> This design addresses the restacking issue inherent in MXene nanosheets, increases the electrochemically active surface area, and modifies the original MXene surfaces with oxygen terminations, leading to improved redox kinetics at the electrode-electrolyte interface, particularly in n-type TECs employing Fe2+/3+ redox ions. 

条件：Through the reported combined structural and surface changes; particularly n-type thermocells with Fe2+/3+ redox ions.；断言：author_claim；联合因素：[]。

同一主体的其他主张：

- `TG:P0135:r001`：Ti3C2Tx MXene hollow-microsphere nanocomposite electrode → has_structure → Hollow microsphere structure；联合因素：[]
- `TG:P0135:r002`：Ti3C2Tx MXene hollow-microsphere nanocomposite electrode → mitigates → MXene nanosheet restacking；联合因素：[]
- `TG:P0135:r003`：Ti3C2Tx MXene hollow-microsphere nanocomposite electrode → increases → Electrochemically active surface area；联合因素：[]
- `TG:P0135:r004`：Ti3C2Tx MXene hollow-microsphere nanocomposite electrode → introduces → Oxygen terminations on MXene surfaces；联合因素：[]

## N04_TG_03

**相关关联证据**：PEDOT 电子输运与铁氰化物电子转移相关；原文为相关性，不单独推出某改性必然有效。

原关系排名 3；检索分数 0.580（非迁移概率）。

[Bulk electronic transport impacts on electron transfer at conducting polymer electrode-electrolyte interfaces](https://doi.org/10.1073/pnas.1806087115)

`TG:P0293:r001`：Electronic transport within PEDOT electrode → strongly correlates with → Electron-transfer rate to redox molecules in solution

> As a benchmark system, we use poly(3,4-ethylenedioxythiophene) (PEDOT) and the Ferro/ferricyanide redox couple in an aqueous electrolyte. 

> We discovered a strong correlation between the electronic transport within the PEDOT electrode and the rate of electron transfer to the organometallic molecules in solution. 

条件：PEDOT and ferro/ferricyanide in aqueous electrolyte.；断言：association；联合因素：[]。

## N04_TG_04

**背景机制**：熵驱动电极红氧过程是背景，并非新催化方案。

原关系排名 4；检索分数 0.576（非迁移概率）。

[A fundamental study of the thermoelectrochemistry of ferricyanide/ferrocyanide: cation, concentration, ratio, and heterogeneous and homogeneous electrocatalysis effects in thermogalvanic cells](https://doi.org/10.1039/d0se00440e)

`TG:P0094:complete_v1_cr001`：Entropy → drives → Electrode redox processes

> Thermogalvanic cells typically utilise equimolar concentrations of the oxidised and reduced states of a redox couple in solution, sandwiched between two electrodes at dissimilar temperatures; entropy drives redox processes to occur at these electrodes, generating a potential difference and a current. 

条件：Thermogalvanic cells with dissolved oxidized and reduced redox states between electrodes at dissimilar temperatures.；断言：author_claim；联合因素：[]。

同论文下游：

- `TG:P0094:complete_v1_cr002`：Electrode redox processes → generates → Potential difference；联合因素：[]
- `TG:P0094:complete_v1_cr003`：Electrode redox processes → generates → Current；联合因素：[]

## N04_TG_05

**背景机制**：温差驱动有利反应，不是解除动力学/稳定性瓶颈的调控措施。

原关系排名 5；检索分数 0.575（非迁移概率）。

[High Seebeck coefficient thermogalvanic cells via the solvent-sensitive charge additivity of cobalt 1,8-diaminosarcophagine](https://doi.org/10.1039/d2cc05413b)

`TG:P0065:complete_v1_cr001`：Temperature gradient across a thermogalvanic device → drives → Entropically favourable electrochemical redox reaction

> A temperature gradient across the device drives an entropically favourable electrochemical redox reaction, resulting in continuous current production. 

条件：；断言：author_claim；联合因素：[]。

同论文下游：

- `TG:P0065:complete_v1_cr002`：Entropically favourable electrochemical redox reaction → results_in → Continuous current production in a thermogalvanic device；联合因素：[]

## N01_iTE_supplemental

**已有机制参考**：桥状石墨烯加速扩散有依据，但同篇明确为明胶/铁氰化物红氧凝胶热电池，是已有 TG 机制，不是新跨域迁移。

原关系排名 32；检索分数 0.540（非迁移概率）。

[Remarkable high-temperature ionic thermoelectric performance induced by graphene in gel thermocells](https://doi.org/10.1039/d3ee03818a)

`iTE:P0376:r007`：Bridge-like graphene structure → accelerates → Ion diffusion

> Graphene forms a structure like a bridge to link adjacent free water clusters in gels, accelerating ion diffusion and improving ionic thermoelectric performance.

条件：By linking adjacent free water clusters.；断言：author_claim；联合因素：[]。

同论文上游：

- `iTE:P0376:r003`：Graphene in gel → forms → Bridge-like graphene structure；联合因素：[]

同一主体的其他主张：

- `iTE:P0376:r004`：Bridge-like graphene structure → links → Adjacent free water clusters in gels；联合因素：[]
- `iTE:P0376:r005`：Bridge-like graphene structure → could_increase → Ion diffusion coefficient；联合因素：[]
- `iTE:P0376:r006`：Bridge-like graphene structure → could_increase → Exchange current density；联合因素：[]
- `iTE:P0376:r008`：Bridge-like graphene structure → improves → Ionic thermoelectric performance；联合因素：[]

## N03_iTE_supplemental

**保留假设**：MOF-801/水凝胶外层维持湿度和开路电压有摘要依据；借用外部水分管理架构，目标连续红氧输出仍需验证。

原关系排名 105；检索分数 0.474（非迁移概率）。

[Robust High Thermoelectric Harvesting Under a Self-Humidifying Bilayer of Metal Organic Framework and Hydrogel Layer](https://doi.org/10.1002/adfm.201807549)

`iTE:P0621:r010`：PMIC beneath MOF/hydrogel bilayer → incorporates_overlayer → Water-harvesting MOF-801/hydrogel bilayer

> Robust thermoelectric harvesting is explored from a proton-doped mixed ionic conductive (PMIC) film under water-harvesting metal organic framework (MOF) film coupled with hydrogel layer (MOF/HG). 

> Environmentally sustainable thermoelectric harvesting is achieved from a PMIC under a MOF/HG, prepared by water-harvesting MOF-801 coupled with a HG layer, to provide constant relative humidity of 90% and V-oc over 72 h at ambient condition.

条件：MOF/hydrogel bilayer above PMIC；断言：author_claim；联合因素：[]。

同论文下游：

- `iTE:P0621:r009`：Water-harvesting MOF-801/hydrogel bilayer → has_structure → Water-harvesting MOF-801 coupled with hydrogel layer；联合因素：[]
- `iTE:P0621:r011`：Water-harvesting MOF-801/hydrogel bilayer → provides → Constant relative humidity of 90%；联合因素：[]

同一主体的其他主张：

- `iTE:P0621:r012`：PMIC beneath MOF/hydrogel bilayer → maintains → Sustained open-circuit voltage；联合因素：[]
- `iTE:P0621:r013`：PMIC beneath MOF/hydrogel bilayer → achieves → Environmentally sustainable thermoelectric harvesting；联合因素：[]
