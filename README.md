# Knowledge Video Production（暂定名）

面向中文知识视频的制作skill，适用于Claude Code、Codex及支持Agent Skills的其他agent。名称尚未定稿，目前沿用knowledge-video-production，后续可统一重命名。

默认路线：zhijie-writing内容 → 生图/HTML分镜 → VOX纸面杂志拼贴 → HyperFrames → MiMo配音与混音 → 视觉验收 → 4K60、3:2成片和独立SRT。英文Lato、Playfair Display Black，中文阿里普惠体、思源宋体；具体搭配由agent决定。提供Funk、Hip-hop等音乐方向供选择。

## 安装

这是私有仓库：先确保当前GitHub账户有访问权限，并配置Git认证（如gh auth login及gh auth setup-git）。安装器不读取、保存或打印访问令牌。

```sh
git clone https://github.com/tanzhijir-04/knowledge-video-production.git
cd knowledge-video-production
python scripts/install.py --agent codex
python scripts/install.py --agent claude-code
```

可只安装其中一个。安装器仅复制本skill、不执行内容或联网安装依赖；已有同名目录会拒绝覆盖。自定义安装根目录：

```sh
python scripts/install.py --agent codex --target /path/to/skills
```

也可通过支持私有Git认证的skills CLI安装（安装行为以当前CLI为准）：

```sh
npx skills add tanzhijir-04/knowledge-video-production --skill knowledge-video-production -a codex -a claude-code -g
```

标准格式来源：[Claude Code skills文档](https://code.claude.com/docs/en/skills)、[Agent Skills](https://agentskills.io)、[skills CLI](https://github.com/vercel-labs/skills)。主skill是skills/knowledge-video-production/SKILL.md，agents/openai.yaml仅供Codex使用。

## 外部依赖

Python 3.10+；实际视频制作还需要Node/npm、HyperFrames、FFmpeg/ffprobe与可用浏览器。根据上游当前说明安装：

```sh
npx skills add heygen-com/hyperframes
npx skills add Cele-san/vox-style-animation --skill vox-style-animation
```

zhijie-writing单独安装，不随本仓库分发；已有文案可直接进入制作。图像生成需要宿主实际可用工具，MiMo TTS需要MIMO_API_KEY环境变量及可用服务。限时免费并非永久保证。字体、音乐须核实授权。本仓库不附带完整上游skills、字体文件、历史成片或密钥；create-storyboard的方法适配与许可见下文。

## 分镜、动效与视觉验收

- [分镜设计](skills/knowledge-video-production/references/storyboard-design.md)：镜头数量与画面密度独立设置，支持中/高密度，默认中；每分钟约10–15镜作为规划起点，按内容和实际配音调整。
- [分镜连续性与剪辑](skills/knowledge-video-production/references/storyboard-continuity.md)：已本地融入create-storyboard的镜头卡、开始/关键动作/结束制作板、连续性约束、相邻承接和剪辑边界设计，适配HyperFrames；无需另装原版skill。来源版本及MIT许可随文件保留。
- [连贯动效](skills/knowledge-video-production/references/motion-continuity.md)：融入OneTake的视觉主线、承接物、段内节奏与跟随运镜方法，保留科普硬切与现有HyperFrames路线；未捆绑上游代码或资产，来源与授权边界见文档。
- [音效与插图密度](skills/knowledge-video-production/references/sfx-and-illustration-density.md)：音效4–10事件/分钟、新插图组4–8组/分钟、插图有效时间覆盖40%–70%作为可调整规划起点；明确计数、复用、留白、例外与实际试听/画面验收。
- [扩展动效配方](skills/knowledge-video-production/references/motion-recipes.md)：8类解释性动作及速度曲线、时长起点、实现条件与验收要点，与Vox风格包协作。
- [视觉验收契约](skills/knowledge-video-production/references/visual-acceptance-contract.md)及[布局纠错流程](skills/knowledge-video-production/references/layout-contract-and-qa.md)：每次制作或修改分镜/视频，查看真实预览，记录问题、纠正并复查。分镜按镜头及剪辑边界审查，静态与动态验证状态分别记录。

这些文件是制作与验收规范，不是已验证的自动检测器或动画组件；文件存在、安装通过不等于成片已通过视觉审查。

## 使用

Codex：`用 $knowledge-video-production 配合 zhijie-writing，做一期“选题”，按我的默认设置完成。`

Claude Code：`/knowledge-video-production 做一期“选题”，配合zhijie-writing，按默认设置完成。`

```sh
python skills/knowledge-video-production/scripts/init_project.py video-projects/example --topic "示例选题"
```

初始化不会生成真实视频。每个工程按research、script、design、project、evidence、delivery等结构存储；细则见[工程规范](skills/knowledge-video-production/references/project-structure.md)。工程放video-projects或仓库外部，不提交到skill仓库。

## 验证与边界

```sh
python -m unittest discover -s tests -v
```

覆盖安装目录、拒绝覆盖、工程结构与配置初始化；历史辅助脚本记录另见skill内references。没有完成Claude/Codex双宿主全流程视频测试，也没有对当前规范完成全片HyperFrames渲染认证。安装不代表图像工具、音频服务或上游依赖已就绪。

仓库当前私有，未授予对外发布或再分发许可；第三方内容遵守各自授权。正式名称和开源许可证待所有者决定。
