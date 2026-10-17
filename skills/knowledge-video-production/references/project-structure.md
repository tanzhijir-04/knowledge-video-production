# 结构化视频工程

每支视频一个独立根目录，推荐`YYYY-MM-DD-topic-slug`。续作先识别既有结构，建立对应关系，不为套目录盲目搬动已批准工程。新工程使用以下结构：

```text
video-project/
  production.json          # 规格、偏好、场景、音乐选择与实际阶段
  STATUS.md                # 当前进度、下一步、阻塞和真实文件路径
  BRIEF.md                 # 选题、受众、已有决定；承接zhijie-writing
  frame.md                 # 已验证视觉系统；字体、网格、色彩
  research/                # 来源、证据账本、事实限制
  script/                  # 大纲、逐字稿、旁白分段
  design/storyboard/       # HTML/图片分镜及场号
  project/
    index.html
    hyperframes.json
    package.json
    package-lock.json
    compositions/          # 按scene_id命名的场景
    lib/                   # 本地运行时
    media/
      images/              # 可复用plate/cutout/prop
      fonts/               # 真实字体及授权
      audio/voice/         # 原始及处理后配音
      audio/music/
      audio/sfx/
    data/timeline.json     # 实际配音后锁定的帧时间线
    data/assets.json       # 素材账本
    scripts/               # 预览、渲染、检查入口
  evidence/                # 实际关键帧、检查和测量报告
  delivery/                # 最终无字幕视频、独立SRT、交付清单
  covers/                  # 横版、裁切核验与竖版
  publishing/              # 标题、简介、标签
  cache/                   # 可重建预览/渲染缓存；不进交付包
```

初始化只建必要目录、配置与空账本，不制造假的已完成脚本、设计规范、timeline或渲染报告。各文件随实际制作产生，STATUS.md能指出尚未存在的部分。

## 文件、数据与依赖

- 场景使用稳定ID如`s01`，素材使用可读ID与版本号如`s01-phone-cutout-v02.png`；引用关系进入账本，不依赖“最终版2最新版”猜测。
- assets.json每项记录id、类型、工程相对路径、来源/生成方式、授权或限制、生成提示词引用、实际输入指纹/文件SHA256、使用场景。按实际素材填，未知项明确pending，不捏造来源或许可证。
- timeline使用同一scene_id，记录startFrame、durationFrames、voiceStartFrame、voiceFrames和文本/音频指纹。分镜预计时长不能冒充最终时间线。
- production.json保留目标规格和实际状态；修改画面/音频/字体后，相关预览与验收证据应失效重查。规格、源码和交付文件不能各读一份不同的时间线。
- 工程内部采用相对路径，HTML引用以文档位置解析；不要出现制作者机器绝对路径、外部junction或跨项目素材依赖。代码、字体、媒体可本地读取；包依赖用准确版本和lockfile复现。
- README运行说明随实际可用命令更新。交付前从新目录副本验证关键文件引用、安装/预览/渲染流程；只检查文件存在不等于已证明可移植渲染。
- 最终delivery中生成文件清单与SHA256，对应实际交付版本。打包根目录时排除cache、node_modules、浏览器目录、鉴权信息与环境文件。授权限制不能随意剔除。

## 仓库和项目分离

skill仓库只含规则、模板、辅助脚本和安装说明。真实视频工程放在单独项目目录，默认不进入skill仓库。原始素材、成片、个人路径、日志和凭据不得随着skill发布。私有仓库同样不能存密钥；凭据只通过环境变量注入。
