# 从 TG 需求出发的 iTE 迁移候选

**本轮保留 2 个优先核查假设和 1 个低证据备选。没有一个已被证明可迁移或具有新颖性。**
四个 TG 问题来自原摘要；检索对象是 iTE 的调控关系及同论文邻域。以下为助手回查后的解释，不是模型分数自动生成的结论。

## H01：用缺陷/极化产生的局部电场与锚定位点，尝试调节 TG 中的离子配对

**保留；优先核查机制适用性**。

检索来源：N02_iTE_02，源关系排名 2；不是源、目标节点名称配对。

**iTE 具体提供什么：** SrTiO3 极化与富氧空位表面 → 局部电场及离子选择性锚定位点 → 共同促进离子解离。源还报告迁移不对称性增强，器件采用电容过程。

**迁移到 TG 要检验什么：** 在有配对/浓度梯度限制的 TG 凝胶中，测试这样的局部场与表面位点能否提高目标离子的解离或有效活度，同时保持红氧物种输运。借用的是调控途径，不是把源侧热电系数直接移植。

**TG 已经做过什么：** TG 已有双层空间分隔控制梯度，也有在不同 Fe(III/II) 电对中利用弱配位阴离子抑制配对的方案；TG 电极已有氧空位。因此“用氧空位”本身不是新颖性，待查的是凝胶内局部场/锚定位点作用于配对这一具体组合。

**尚缺什么：** 源为离子热电电容体系，目标含可反应红氧电对。锚定可能提高解离，也可能过度束缚红氧物种；摘要没有给出在目标体系中的净效果。不得把联合因素拆成“氧空位单独有效”。

**如何验证：** 在同组成和含水量条件下比较无填料、缺陷较少/较多的对照，分辨极化、缺陷与表面积影响；测配对/物种状态、红氧物种扩散、电导、热电势、持续功率和电化学稳定性。

本地 TG 摘要定向词检索命中 0 篇。只用于检查明显已有线索，不代表文献中不存在，更不是新颖性证明。

### iTE 源证据

[Decoupling ion transport and mechanical robustness in ionic thermoelectrics via defect-rich SrTiO3 nanofibers](https://doi.org/10.1016/j.cej.2026.177118)

- `iTE:P0589:r001`：One-dimensional SrTiO3 nanofibers with oxygen vacancies → enables → Defect- and structure-engineered ionic thermoelectric ionogel；条件：；联合因素：\[\]
- `iTE:P0589:r002`：SrTiO3 ferroelectric polarization → jointly generates → Built-in local electric fields；条件：；联合因素：\['SrTiO3 ferroelectric polarization', 'Oxygen-vacancy-rich SrTiO3 surfaces'\]
- `iTE:P0589:r003`：SrTiO3 ferroelectric polarization → jointly generates → Ion-selective anchoring sites；条件：；联合因素：\['SrTiO3 ferroelectric polarization', 'Oxygen-vacancy-rich SrTiO3 surfaces'\]
- `iTE:P0589:r004`：Built-in local electric fields → jointly promotes → Ion dissociation；条件：；联合因素：\['Built-in local electric fields', 'Ion-selective anchoring sites'\]
- `iTE:P0589:r005`：Built-in local electric fields → jointly amplifies → Cation–anion migration asymmetry；条件：；联合因素：\['Built-in local electric fields', 'Ion-selective anchoring sites'\]
- `iTE:P0589:r013`：Ionic thermoelectric capacitor → operates through → Capacitive processes；条件：；联合因素：\[\]

> Here, we report a defect- and structure-engineered ionic thermoelectric ionogel enabled by one-dimensional SrTiO3 nanofibers with oxygen vacancies. 

> The ferroelectric polarization and oxygenvacancy-rich surfaces of SrTiO3 generate built-in local electric fields and ion-selective anchoring sites, which promote ion dissociation and amplify cation-anion migration asymmetry. 

> Furthermore, an ionic thermoelectric capacitor is demonstrated, enabling controllable thermal energy harvesting and storage through capacitive processes. 

### TG 需求及已有工作证据

[Bioinspired double-layer thermogalvanic cells with engineered ionic gradients for high-efficiency waste heat recovery](https://doi.org/10.1016/j.nanoen.2025.111189)

- `TG:P0021:complete_v1_cr001`：Ion pairing → hinders_establishment_of → Substantial ion concentration gradients；条件：Thermogalvanic cells；联合因素：\[\]
- `TG:P0021:r001`：Double-layer thermogalvanic cell architecture → spatially_segregates_redox_pairs_into → Redox pairs spatially segregated into two distinct gel layers；条件：；联合因素：\[\]
- `TG:P0021:r002`：Redox pairs spatially segregated into two distinct gel layers → enables → Control over ion concentration gradients；条件：Double-layer architecture；联合因素：\[\]

> A critical factor in enhancing TGC performance lies in establishing substantial ion concentration gradients, which remains challenging due to the inherent tendency of ion pairing. 

> Here, we present a double-layer thermogalvanic cell (DTGC) architecture that spatially segregates redox pairs into two distinct gel layers, enabling unprecedented control over ion concentration gradients. 

[Unravelling ionic speciation and hydration structure of Fe(III/II) redox couples for thermoelectrochemical cells](https://doi.org/10.1016/j.electacta.2020.135651)

- `TG:P0285:r004`：Non-coordinating character of perchlorate → suppresses → Ion-pair formation；条件：Fe(III)/(II) perchlorate electrolyte；联合因素：\[\]

> Herein, we unravel that the excellent performance of the Fe(III)/(II) perchlorate is ascribed to the non-coordinating nature of its perchlorate anion, which suppresses the formation of the ion pairs that reduce the S-e and ionic conductivity. 

[Boosting Gel-Based Thermogalvanic Energy Harvesting via Metal Oxide Nanostructured Electrodes](https://doi.org/10.1002/smll.202514359)

- `TG:P0083:r004`：Metal oxide nanoparticle-modified carbon cloth electrodes → have → Abundant oxygen vacancies；条件：；联合因素：\[\]

> To address this problem, an effective strategy is developed herein by hydrothermally integrating transition metal oxide nanoparticles (TiO2, WO3, ZnO) onto carbon cloth (CC) electrodes, and combining this with a double-network poly(vinyl alcohol) (PVA)/gelatin hydrogel containing the ferro-/ferricyanide (Fe(CN)6 3-/4-) redox couple. 

> Compared to the pristine CC, all of the modified electrodes exhibit markedly enhanced current densities due to enlarged electroactive surface areas and abundant oxygen vacancies. 

## H02：把 MOF/水凝胶吸水外层用于 TG 的水分管理

**保留；架构迁移假设，仅覆盖失水部分**。

检索来源：N03_iTE_supplemental，源关系排名 105；阅读前 200 条中与水分有关的关系后补选，并非自动前五。

**iTE 具体提供什么：** 源将 MOF-801 与水凝胶组成外层，置于质子掺杂 PEDOT:PSS 薄膜上；摘要报告局部相对湿度约 90%，并维持超过 72 h 的开路电压。这里是同论文的结构与表现证据，不把不同主体的边伪装为完整因果链。

**迁移到 TG 要检验什么：** 对易失水的 TG 凝胶，测试相对独立的吸水/缓释水外层能否维持水分与红氧电解质浓度，尽量减少对凝胶本体配方的改动。

**TG 已经做过什么：** TG 已有甘油/水抗干燥、吸湿盐以及从空气吸水恢复水分的做法。不能宣称“自主补水”是新机制；待查的差别是 MOF/凝胶外层与 TG 工作层的分离布置及其实际收益。

**尚缺什么：** 源主要报告湿度和开路电压，未证明 TG 持续负载输出；也未证明抗冻。外层可能改变热阻、温差和水/盐分布，这些都需检查。

**如何验证：** 对照裸 TG、仅水凝胶外层和 MOF/水凝胶外层；在规定温湿度和负载下记录质量、水分/盐浓度、实际两电极温差与持续功率。72 h 开路电压不能替代连续发电证据。

本地 TG 摘要定向词检索命中 0 篇。只用于检查明显已有线索，不代表文献中不存在，更不是新颖性证明。

### iTE 源证据

[Robust High Thermoelectric Harvesting Under a Self-Humidifying Bilayer of Metal Organic Framework and Hydrogel Layer](https://doi.org/10.1002/adfm.201807549)

- `iTE:P0621:r009`：Water-harvesting MOF-801/hydrogel bilayer → has_structure → Water-harvesting MOF-801 coupled with hydrogel layer；条件：；联合因素：\[\]
- `iTE:P0621:r010`：PMIC beneath MOF/hydrogel bilayer → incorporates_overlayer → Water-harvesting MOF-801/hydrogel bilayer；条件：MOF/hydrogel bilayer above PMIC；联合因素：\[\]
- `iTE:P0621:r011`：Water-harvesting MOF-801/hydrogel bilayer → provides → Constant relative humidity of 90%；条件：PMIC under MOF/hydrogel; over 72 h at ambient conditions；联合因素：\[\]
- `iTE:P0621:r012`：PMIC beneath MOF/hydrogel bilayer → maintains → Sustained open-circuit voltage；条件：Over 72 h at ambient conditions; constant 90% relative humidity；联合因素：\[\]
- `iTE:P0621:complete_v1_cr001`：MOF-801 → has_function → Water harvesting；条件：In the MOF/hydrogel overlayer；联合因素：\[\]

> Environmentally sustainable thermoelectric harvesting is achieved from a PMIC under a MOF/HG, prepared by water-harvesting MOF-801 coupled with a HG layer, to provide constant relative humidity of 90% and V-oc over 72 h at ambient condition.

> Robust thermoelectric harvesting is explored from a proton-doped mixed ionic conductive (PMIC) film under water-harvesting metal organic framework (MOF) film coupled with hydrogel layer (MOF/HG). 

### TG 需求及已有工作证据

[Self-Powered Respiratory Monitoring Strategy Based on Adaptive Dual-Network Thermogalvanic Hydrogels](https://doi.org/10.1021/acsami.2c14239)

- `TG:P0061:complete_v1_cr002`：Limitations in antifreezing and antidrying properties → restrict → Durability of thermogalvanic gels in practical applications；条件：；联合因素：\[\]
- `TG:P0061:r003`：Binary H2O/glycerin solvent → limits → Hydrogen bonding between water molecules；条件：In the PVA/GEL thermogalvanic gel.；联合因素：\[\]
- `TG:P0061:r005`：Binary H2O/glycerin solvent → confers → Antidrying capacity；条件：In the PVA/GEL thermogalvanic gel, by limiting hydrogen bonding between water molecules.；联合因素：\[\]

> However, challenges remain in their antifreezing and antidrying properties, significantly restricting the durability of thermogalvanic gels in practical applications. 

> These features result from the use of a binary H2O/GL (glycerin) solvent to limit hydrogen bonding between water molecules. 

> Herein, a dual-network poly(vinyl alcohol)/gelatin (PVA/GEL) gel thermogalvanic device with Fe(CN)6 3-/4- as a redox pair is developed, with an outstanding low-temperature durability and antidrying capacity. 

[Thermogalvanic Hydrogel for Synchronous Evaporative Cooling and Low-Grade Heat Energy Harvesting](https://doi.org/10.1021/acs.nanolett.0c00800)

- `TG:P0058:r006`：Smart thermogalvanic hydrogel film → supports → Water absorption from surrounding air；条件：Later regeneration；联合因素：\[\]
- `TG:P0058:r007`：Water absorption from surrounding air → produces → Regenerated hydrogel water content；条件：；联合因素：\[\]

> Moreover, the hydrogel can absorb water from the surrounding air to regenerate its water content later on. 

[Robust and flexible bacterial cellulose-based thermogalvanic cells for low-grade heat harvesting in extreme environments](https://doi.org/10.1016/j.cej.2023.141274)

- `TG:P0048:r006`：Introduction of hygroscopic LiBr salts → endows_BC_TGC_with → Excellent anti-drying properties；条件：；联合因素：\[\]

> The introduction of hy-groscopic salts (LiBr) endows the BC-TGC with excellent anti-drying and anti-freezing properties. 

## H03：借鉴聚合物链作用促使离子聚集体解离

**保留备选；机制证据较弱**。

检索来源：N02_iTE_04，源关系排名 4。

**iTE 具体提供什么：** MWCNT/聚合物/离子液体体系中，作者用“聚合物链呼吸”模型解释聚集体解离及电导提高；1 wt% 配方的电导增益和 0.25 wt% 的最佳热电表现不能混成同一配方结论。

**迁移到 TG 要检验什么：** 测试 TG 凝胶中可调的聚合物—离子作用，能否改变配对/聚集状态并保持红氧物种移动；不是直接照搬 MWCNT 配方。

**TG 已经做过什么：** TG 已有弱配位阴离子抑制配对、聚合物选择性结合保留反离子移动的相关工作。此处的待查差别是动态链作用促进解聚的具体路径。

**尚缺什么：** 源是非水离子液体凝胶，目标可为水系红氧凝胶。电导增加只是表现，解聚为作者模型归因；不能声称已直接观测并验证了目标机制。

**如何验证：** 先找全文中离子聚集/配对的直接证据，再设计链段作用或交联度对照；同时检查红氧物种扩散、电荷转移及是否引入电子漏电。若只有电导变化，仍不能确认解聚路径。

本地 TG 摘要定向词检索命中 0 篇。只用于检查明显已有线索，不代表文献中不存在，更不是新颖性证明。

### iTE 源证据

[High thermoelectric performance of multiwalled carbon nanotubes based ionogels](https://doi.org/10.1016/j.mtcomm.2024.108334)

- `iTE:P0548:r001`：In situ radical polymerization of PEG200DMA with ionic liquid and MWCNTs → synthesizes → MWCNT-based ionogels；条件：Ionic liquid: 1-butyl-3-methyl imidazolium tetrafluoroborate.；联合因素：\[\]
- `iTE:P0548:r002`：1 wt% MWCNT ionogel → achieves → 75.3% enhancement in ionic conductivity；条件：Compared with the base ionogel at 40 degrees C.；联合因素：\[\]
- `iTE:P0548:r003`：Ionic liquid–polymer chain interaction → causes → Dissociation of ion aggregates；条件：Breathing polymer chain model.；联合因素：\[\]
- `iTE:P0548:r004`：Dissociation of ion aggregates → is invoked to explain → 75.3% enhancement in ionic conductivity；条件：Breathing polymer chain model; 1 wt% MWCNT ionogel versus base ionogel at 40 degrees C.；联合因素：\[\]
- `iTE:P0548:r005`：0.25 wt% MWCNT ionogel → represents → Optimized MWCNT concentration for thermoelectric performance；条件：Among 0.25, 0.5, and 1 wt% MWCNT ionogels.；联合因素：\[\]

> IGs were synthesized via in situ radical polymerization of polyethylene glycol 200 dimethacrylate (PEG200DMA) difunctional monomer in the presence of 1-butyl-3-methyl imidazolium tetrafluoroborate (an ionic liquid) and MWCNTs. 

> A remarkable 75.3% enhancement in ionic conductivity was achieved for the MWCNTs-1 wt% ionogel compared to the base IG at 40 degrees C. 

> This substantial improvement can be attributed to the breathing polymer chain model, which describes the dissociation of ion aggregates due to the interaction between the ionic liquid and polymer chains. 

> Three composites namely MWCNTs-0.25, MWCNTs-0.5 and MWCNTs-1 were prepared having the concentration of MWCNTs by 0.25, 0.5 and 1 wt% respectively. 

> In terms of thermoelectric performance amongst the MWCNT ionogels, 0.25 wt% MWCNT-based ionogels was the optimized concentration with very high Seebeck coefficient of 1.70 mV/K and power factor of 4.1 mu W/m. 

### TG 需求及已有工作证据

[Bioinspired double-layer thermogalvanic cells with engineered ionic gradients for high-efficiency waste heat recovery](https://doi.org/10.1016/j.nanoen.2025.111189)

- `TG:P0021:complete_v1_cr001`：Ion pairing → hinders_establishment_of → Substantial ion concentration gradients；条件：Thermogalvanic cells；联合因素：\[\]

> A critical factor in enhancing TGC performance lies in establishing substantial ion concentration gradients, which remains challenging due to the inherent tendency of ion pairing. 

[Unravelling ionic speciation and hydration structure of Fe(III/II) redox couples for thermoelectrochemical cells](https://doi.org/10.1016/j.electacta.2020.135651)

- `TG:P0285:r004`：Non-coordinating character of perchlorate → suppresses → Ion-pair formation；条件：Fe(III)/(II) perchlorate electrolyte；联合因素：\[\]

> Herein, we unravel that the excellent performance of the Fe(III)/(II) perchlorate is ascribed to the non-coordinating nature of its perchlorate anion, which suppresses the formation of the ion pairs that reduce the S-e and ionic conductivity. 

[Ion transport control in electrolytes via electrochemical doping](https://doi.org/10.1073/pnas.2532302123)

- `TG:P0249:r004`：Electrolyte doping by incorporating electroactive polymers within hydrogels → preserves → Mobile counterions；条件：；联合因素：\[\]
- `TG:P0249:r005`：Electrolyte doping by incorporating electroactive polymers within hydrogels → enables → Unipolar ion transport；条件：Electroactive polymers discriminate between ion types via redox and binding.；联合因素：\[\]

> Here, we report a universal strategy to dope electrolytes such that the ion transport can be unipolar by incorporating electroactive polymers within hydrogels that interact discriminately with one type of ion via redox and binding mechanisms, leaving the counterions mobile. 

