# 彩星电影一号位

[English](README.en.md) · [License](LICENSE)

集编剧、制片、导演于一身的华语喜剧创作总控。名字取自周星驰 1994 年创立的彩星电影公司。

**定位**：不是周星驰数字分身，不冒充、不授权、不复刻受保护表达。把周氏喜剧的底层打法抽象为可执行的创作机制，用来把普通故事打造成适合院线、网络播放和自媒体的经典内容。

## 能力

- **编剧**：人物欲望、地位图、规则冲突、七步节拍、对白、道具回收、情感反冲。
- **制片**：可行性、预算量级、平台策略、记忆点工程、权利与合规。
- **导演**：镜头、表演、笑点视觉/语言分级、悲喜切换触发器。
- **推陈出新**：时代内核替换、母题变奏、媒介节奏转换、锋利度守卫。
- **网络分发**：短视频/短剧/网大/院线的节拍适配，钩子、完播、系列化。

## 安装

**一键安装**（推荐）：

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/SimonsTang/caixing-film-one/main/install.sh | bash
```

```powershell
# Windows (PowerShell)
irm https://raw.githubusercontent.com/SimonsTang/caixing-film-one/main/install.ps1 | iex
```

或手动复制到 WorkBuddy 用户级技能目录：

```bash
cp -r caixing-film-one ~/.workbuddy/skills/
```

重启会话后可用。

## 使用

```
用彩星电影一号位，把"一个总被忽视的临时工"写成 60 秒原创喜剧，前三秒要有视觉冲突。
```

```
用彩星电影一号位诊断这场戏为什么不好笑，先给结构原因，再给最小修改版。
```

```
用彩星电影一号位，把下面这个故事改造成适合网络播放的短剧，保留情感内核但不要复刻任何电影。
```

**安全词**：说"认真"或"退出角色"，切回中性专业模式。

## 结构

```
caixing-film-one/
├── SKILL.md                         核心工作流与路由
├── references/
│   ├── chow-playbook.md             周氏打法矩阵（蒸馏版）
│   ├── three-roles.md               编剧/制片/导演三合一决策
│   ├── creation-workflows.md        各媒介创作流程
│   ├── network-playbook.md          网络播放与自媒体打法
│   ├── evaluation-rubric.md         评分标尺与硬失败
│   ├── rights-and-safety.md         原创与权利边界
│   └── source-registry.json         来源登记
├── scripts/
│   ├── source_validator.py          来源登记校验
│   ├── quote_guard.py               近似文本检查
│   ├── evaluate_output.py           结构评分
│   └── classic_score.py             经典要素覆盖检查
├── examples/sample-workflow.md      完整创作样例《评分》
└── tests/validate_skill.py          结构验证
```

## 验证

```bash
python tests/validate_skill.py
python scripts/source_validator.py references/source-registry.json
python scripts/classic_score.py --input examples/sample-workflow.md
```

脚本仅使用 Python 标准库，建议 3.8+。

## 研究与来源边界

方法论蒸馏自豆瓣长评、烂番茄影评人共识、维基百科条目与 GitHub `stephen-chow-skill`。研究区分可核实事实、评论解读与未证实传闻；不把自媒体编造的数字当事实。来源清单见 `references/source-registry.json`。

本项目提供创作工作流与技术辅助，不构成法律意见。许可证：MIT（代码与原创文档）；不授予任何第三方姓名、肖像、声音、商标、电影、角色、剧本或对白的权利。
