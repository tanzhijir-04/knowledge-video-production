# Claude Code、Codex与其他agent

本skill使用标准SKILL.md、相对引用和Python标准库辅助脚本，不依赖某一厂商的提示词语法。Codex可使用`$knowledge-video-production`，Claude Code可使用`/knowledge-video-production`；其他支持Agent Skills的宿主可按名称或自然语言调用。agents/openai.yaml是Codex可选界面元数据，其他宿主可忽略。

- 图片：在Codex有内置imagegen时优先使用；其他宿主使用实际可用的图像生成能力。无图像工具时继续HTML分镜、研究和代码图解，并明确生图资产尚缺，不拿搜索图或占位符冒充生成素材。
- 配音：Python脚本通过环境变量MIMO_API_KEY调用，使用前核对官方文档、资费和权限。未提供凭据不阻塞独立工作。
- 动效：安装HyperFrames及其skills、vox-style-animation；这些是外部依赖，不内嵌上游源码或许可未明资产。执行前读取当前已安装说明。
- 内容：与zhijie-writing配合。它不随本仓库附送；已有文案可继续制作，需研究写作而依赖缺失时明确指出并取得可信安装来源，不虚构其内容或声称已使用。
- 模型：Astra是用户偏好而非硬依赖。有明确授权且宿主支持时使用；不可用则如实以当前模型完成授权工作，不伪称调用、不为换模型中断常规实现。
- 安装成功只表示文件能被发现，不表示工具、第三方服务或端到端视频已经可用。按宿主能力和授权执行，不能绕过权限或静默降规格。

安装路径遵循宿主当前配置。仓库安装器支持显式--target；没有指定时Codex采用CODEX_HOME/skills（未设则~/.codex/skills），Claude Code采用~/.claude/skills。重复安装拒绝覆盖，先比较差异后人工更新。
