# 原生导出与完整工程

独立目录包含project/（index.html、compositions/、media/、hyperframes.json、依赖锁、timeline、导出脚本）、delivery/、covers/、publishing/、evidence/；既有结构优先。production.json保存合同，STATUS.md保存实际进度/文件/阻塞，BRIEF.md接收zhijie写作结果和已确认偏好，不把预算或脚手架当成品。

## HyperFrames制作合同

先读hyperframes、hyperframes-core和vox-style-animation当前使用说明，不凭记忆写composition结构。参考风格包assets/starter的wiring，修改副本；上游starter的CDN GSAP应冻结为工程本地JS，字体和图片也保存在工程，不能依赖运行时外部网络。

顶层index.html的root直接放在body，不能包在template里；子composition用template，style/script在模板内部。host、子composition和window.__timelines的id保持一致，DOM id全片唯一。时间以data-start/data-duration明确声明，根data-duration就是实际片长，不能只改GSAP timeline。明确设data-width=3840、data-height=2560、data-fps=60，并让CSS与子场景尺寸一致；CLI也显式传`--fps 60`，避免默认30。

GSAP timeline paused且可seek；同一属性的入口与drift不要重叠，动画作用于clip内部视觉层，不抢框架所有的可见性和媒体时钟。不使用wall-clock、未设seed随机数、异步时间线或无限repeat。1920×1280设计坐标在3840×2560浏览器画布2倍原生光栅可以，低清放大或24帧插帧冒充60不可以。

3–5分钟知识片一般选general-video。把已有批准稿、分镜、外部SRT和用户默认值记入BRIEF.md，执行相应工作流；不再问已知信息。需要动效primitive先按registry查找，采用适合语义的有限动作，不能用特效库替代解释设计。

先按已安装CLI当前help执行lint/check、时间轴和snapshot检查，确认关键转场两侧无空帧，然后render。CLI参考：`npx hyperframes render <project-dir> --fps 60 --quality delivery -o <output.mp4>`；尺寸由真实composition声明，发布前ffprobe核实。各项目pin实际CLI版本和lockfile。升级先check再检查实际画面，不把版本升级伪称逐帧等价。默认本地渲染，云渲染/账号绑定/公开发布不是本skill的授权。

长片使用当前HyperFrames支持的分段/续渲染方式，先查CLI能力和适用条件；也可按已验证的独立场景导出再统一编码合并。缓存绑定HTML/CSS/JS、timeline、图片/字体等输入，素材变化需失效。只重跑失败/修改范围，先检查GPU/并发能力，不偷偷降规格，不沿用Remotion的bundle命令。

## 色彩、声音与验收

浏览器中间文件可能携带sRGB transfer、全范围、不同矩阵或ICC，也可能已由HyperFrames转换。先ffprobe核实，只有需要时才转换Rec.709 limited/yuv420p，不能只改标签或重复套Remotion的旧转色滤镜。通常H.264+AAC48k立体声、faststart，3840×2560@60的level可能高于普通UHD，需检查解码。采用HyperFrames当前支持的编码器配置，不把CQ与CRF当等价质量。

音频交由框架的audio clip/当前音频机制或已验证的最终mux流程，不自己运行JS音频时钟。最终只有画面和混音，不渲染旁白caption DOM，不mux字幕轨，另存SRT。总长取同一帧精确timeline，核对帧数/时长。

`scripts/verify_delivery.py VIDEO --width ... --height ... --fps ... --frames ... --srt FILE`检查规格、音轨、完整解码和SRT基础；`--expected-text`可核对原稿。它不能证明没有烧录字幕、排版漂亮或声音自然，仍需真实视觉/声音审查。

单一目录交付MP4+SRT、16:9/4:3/3:4封面、标题简介标签、源码、生成素材/提示词、实际字体/授权、原音/分轨、package-lock、运行说明和校验。ZIP仅按需额外生成，不能替代目录。依赖可npm ci，工程素材必须真实存在，不依赖其他项目junction。密钥、临时鉴权、环境文件不得入包。

清理须单独授权，确认目录和成品范围，先验证skill独立可用再执行。Windows检查绝对路径并先解除junction，不进入目标。不保留用户明确要求删除的作品备份。
