---
name: knowledge-video-production
description: Use when the user wants a Chinese knowledge explainer produced as a video, continues an approved video project, or requests its storyboard, VOX-style visuals, narration, subtitles, covers, publishing copy, or editable delivery. Pair with zhijie-writing for research and scripts; exclude plain factual answers.
---

# 知识视频制作

用户只需给选题或已有文案，按以下个人默认值制作真实成片；本次指令优先。沿用已确认事项，不重复问卷，不在每个常规步骤停下来索要批准。

## 与 zhijie-writing 的分工

- **zhijie-writing**：选题、研究、证据账本、论证、大纲、逐字稿与知识变化。需要写作时读其SKILL.md和当前模式引用。遵守署名要求：制作文档末尾一次，不能强加到旁白或画面。
- **本skill**：视觉关系、独立图层、动效、声音、字幕、验收、封面与完整工程。已有批准稿/分镜直接继续对应阶段。
- **vox-style-animation（Cele-san）**：HyperFrames专用VOX风格包，负责纸面/半色调、强调标记、动效词汇与转场。**HyperFrames**负责HTML/CSS/GSAP编排、预览、混音及逐帧渲染。不要与面向Remotion的xingchen-vox-collage混为一套。
- **create-storyboard（已本地融入）**：镜头卡、连续性约束、相邻镜头承接、剪辑边界与制作板的方法已适配到[分镜连续性与剪辑](references/storyboard-continuity.md)，由storyboard-design流程调用；不依赖另装该skill，不继承其Seedance专用规格。
- 只要求封面、字体或SRT时只处理该范围，不扩成全片制作。

## 可覆盖的用户默认值

| 项目 | 默认 |
|---|---|
| 内容 | 普通观众、中文数码科技科普、约3–5分钟 |
| 动效框架 | **HyperFrames + HTML/CSS + 可seek的GSAP时间线**，默认制作路线；不能未说明就换回Remotion |
| 视觉 | **以vox-style-animation的纸面杂志拼贴为默认方向**：奶油纸底、黑色油墨字、实物剪贴、局部半色调、黄色划重点与手绘注释；地图/记录/对照保持可编辑。字体与比例适配中文，不照搬英文全大写和紧行距。避免电影预告片、粗糙3D、悬浮图标卡片与长时间PPT静止；不使用VOX标志或暗示官方关联 |
| 图像 | 图片资产优先生图模型；地图/数据/标签用代码。生成素材不充当来源截图 |
| 分镜 | 可用生图模型、HTML/CSS/SVG或两者混合；按画面任务选择，不要求用户指定。生图看构图/画风/场景，HTML核对精确文字、数据、图解关系与排版 |
| 分镜数量与密度 | 按[分镜设计与验收](references/storyboard-design.md)拆分镜头，不把段落/场景数当镜头数。每分钟约10–15镜作为初始规划范围；画面信息密度可选“中 / 高”，未指定默认中，低密度仅作有意的局部停顿。镜头数量与信息密度独立调整 |
| 字体 | 中文优先阿里普惠体3、思源宋体CN；英文使用Lato、Playfair Display Black（真实900字重），具体用途和搭配由agent/LLM根据内容自主安排，不固定标题/正文角色，也不要求全部同时使用。先以真实内容比较，再锁定实际字体、字重与版式。实际加载并核对授权与字形；D-DIN不再是默认英文字体；不声称生图文字用了已加载字体 |
| 声音 | 小米MiMo TTS茉莉，清楚亲近、正常真人语速，依据录音定时，不硬拉伸 |
| 音乐 | 制作时提供3–4种适合当期内容的音乐方向并推荐一种，允许用户自选、自带音乐或交由导演决定；有可用资源时附短试听。优先原创/现有工具/授权明确资源，人声优先；付费选择先报价并取得授权 |
| 母版 | **3840×2560、60FPS、3:2数字Open Gate构图**。这是个人默认，不代表所有相机Open Gate一样；本次指令可覆盖 |
| 字幕 | **独立UTF-8 SRT，不烧录旁白、不封装字幕轨**。保留必要讲解文字；无装饰页码、章号、英文顶栏、AI角标；不得移除素材强制标记 |
| 发布 | 16:9封面适配居中4:3裁切，两侧各12.5%不放关键内容；另做重排的3:4竖版。随附标题、简介、相关标签 |
| 交付 | 一个目录含成片/SRT、封面、发布文案、源码、真实本地素材、音频分轨、依赖锁、运行说明与校验。排除node_modules/浏览器缓存，不用其他项目junction冒充独立工程 |

## 开始与继续

先检查实际阶段和文件，记录在production.json、STATUS.md。只问确实阻止下一步的缺项或冲突要求。缺TTS凭据只阻塞配音与最终声画锁定，仍推进独立研究、分镜、生图、排版。凭据从本机环境变量取，不要求粘贴聊天，不存工程/skill/日志，不能冒充调用茉莉或擅换音色。

`scripts/init_project.py`可初始化配置/目录；脚手架不算完成视频。完成性结论必须对应真实已检查产物。

所有新视频工程按[references/project-structure.md](references/project-structure.md)结构化存储：研究、脚本、分镜、源码、素材账本、帧时间线、验收证据和交付分层，场景ID一致。skill仓库与真实视频工程分开。跨agent的工具适配见[references/agent-compatibility.md](references/agent-compatibility.md)。

## 制作路线

1. 接收zhijie-writing的核心问题、原稿、每段知识变化、证据和限制，不为视觉效果改变因果、尺度或条件。
2. 读[references/storyboard-design.md](references/storyboard-design.md)、[references/visual-direction.md](references/visual-direction.md)和已安装vox-style-animation的SKILL.md；按需读motion-vocabulary、asset-pipeline与starter。按视觉任务拆镜，每镜有明确的信息变化、构图、动作与时序。每次制作或修改分镜都执行真实预览的视觉审查、纠正与复查，不只检查文字分镜表；已授权全片则持续推进。风格包的Archivo/Inter、内嵌kinetic captions、6秒/16:9示例、供应商脚本都是上游默认，不得覆盖本用户中文字体、独立SRT、3:2/4K60和内置imagegen偏好。
3. 读[references/audio-and-timing.md](references/audio-and-timing.md)。实际配音后锁定帧精确timeline；字幕来自原稿，ASR只辅助时间；音效对齐真实事件，不套每场同样百分比。
4. 先读已安装hyperframes入口，编写HTML前读hyperframes-core；按需加载animation/keyframes/creative/audio/cli/registry，读[references/render-and-delivery.md](references/render-and-delivery.md)。3–5分钟通常采用general-video工作流，已有zhijie稿/批准分镜与默认值写进BRIEF.md，避免重新做意图问卷。原生目标规格，可渐进渲染和复用有效缓存。仅用户明确要求或已批准旧工程继续时使用Remotion，并记录原因。
5. 看原生关键帧、小图与关键动作，检查实际声音；完整解码、规格/帧数、音轨/响度、SRT文字/顺序/范围、移植路径有证据。`scripts/verify_delivery.py`只证明技术检查，不代表视觉审查或真人试听。
6. 封面使用内置imagegen生成/重排，逐字核对并检查实际裁切；统一交付目录，检查资产/依赖/哈希，交付真实视频和SRT。

## 字体与版式的前置验收

每次制作或修改视频，必须读取并执行[视觉验收契约 v1](references/visual-acceptance-contract.md)。契约定义通过标准，[布局检查与纠正闭环](references/layout-contract-and-qa.md)负责执行。逐场保留当前版本的真实帧、动态片段和纠错记录；不得用平均总分抵消阻断问题。检查或修正未完成时标记“待视觉验收”，普通内部纠正自主完成，不增加用户逐场审批。

制作或修改画面时读[references/typography-and-layout.md](references/typography-and-layout.md)。先用开场、机制解释、数据对照三类代表画面验证设计，写入项目frame.md，再扩展全片。比较真实中文、英文、数字与图像的组合，不用字体名称清单代替设计，也不以“文件能渲染”证明美观。内部审查自主迭代；用户已授权全片时，不增加逐步审批。没有实际画面证据，不宣称审美问题已解决。

每次制作或修改视频，都执行[references/layout-contract-and-qa.md](references/layout-contract-and-qa.md)的通用布局闭环：实际预览 → 程序测量与画面审查 → 问题清单 → 局部纠正 → 同时点复查。代表帧只用于选型，逐场检查覆盖全片；布局、字体、素材、时序变化后复查受影响范围。审查包括阅读顺序、视觉重心、疏密与留白、对齐与间距、文字适配、遮挡裁切及动态稳定性，不限于某种图解或截图案例。未解决的影响理解/阅读的缺陷不得通过视觉验收；沿用用户授权自主纠正，不把每轮内部检查变成用户审批。

## 动效配方选择

设计动作时，按需读取[references/motion-recipes.md](references/motion-recipes.md)中的速度曲线规则及相关配方，与vox-style-animation的motion-vocabulary配合使用。先按知识变化选择动作，再对齐真实旁白；不为用满配方添加装饰。配方时间只是起点，必须经过静态布局、运动极值及随机seek检查，不代表已验证的代码组件。用户的独立SRT、中文字体和当前视觉契约优先于上游示例。

## 音乐候选

音乐候选使用[references/music-directions.md](references/music-directions.md)的流派与场景库，包含Funk、Hip-hop及不同编配；按题目挑选，不只提供抽象情绪词。

## 模型、成本与边界

用户偏好重要视听决策由Astra完成，普通实现用当前合适模型。用户授权、工具和模型可用时，可委派**一个有界导演/视觉任务**，定义输入、独占输出和验收；不要每场另开代理。模型不可用就如实说明，不假称使用；缓存生成资产/录音，避免重复API与无意义全片重渲染。

本skill不授予删除、公开发布、购买或外部消息权限。清理须用户明确要求，确认具体目录和是否含成品；先保证skill独立可用再执行。Windows删除前验证绝对路径，先解除junction本身，不进入其目标。不保留用户明确要求删除的作品备份。

## 最少输入

`用 $knowledge-video-production 配合 zhijie-writing，做一期“[选题]”，按我的默认设置完成视频。`

`继续这个项目到成片，沿用批准稿和分镜。`

`只做这个视频的3:4封面，沿用现有风格。`
