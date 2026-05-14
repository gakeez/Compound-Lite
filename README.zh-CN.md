# Compound Lite for Codex

中文 | [English](README.md)

Compound Lite 是一个轻量级、仓库内运行的工作流系统，灵感来自 compound engineering。它面向独立开发者和 Agent 产品项目，适合需要持久化策划、独立验证、可复用经验沉淀，但又不想引入大型多 Agent 自动化平台的场景。

它有意保持在 **Level 1 半自动化**：

- 可以读取项目文件、编写本地代码、编写本地测试、运行本地验证，并创建本地 Markdown 产物。
- 不会自动 commit、push、创建 PR、部署、修改生产数据或变更外部系统。
- 通过文档产物拆分策划、实现、验证和经验沉淀，而不是依赖单次聊天上下文。

## 包含内容

```text
template/
  AGENTS.md
  STRATEGY.md
  .agents/skills/          # Codex 仓库级 skills
  .codex/agents/           # 可选的 Codex 自定义 agents，用于角色分离
  docs/                    # 产物目录和 README 文件
  tools/render_compound_html.py

tools/
  apply.py                 # 安全地把模板复制到目标仓库
  validate_structure.py    # 检查目标仓库是否具备 Compound Lite 结构

docs/
  BUILD_PLAN.md            # 完整构建计划
  MIGRATION_TO_OTHER_AGENTS.md
  USAGE.md
```

## 安装到已有项目

在本仓库根目录执行：

```bash
python3 tools/apply.py /path/to/your-project --mode existing
```

安装脚本是保守的，默认不会覆盖已有文件。发生冲突的文件会写入 `.compound-lite-incoming/`，方便你手动合并。

## 安装到新项目目录

```bash
python3 tools/apply.py /path/to/new-project --mode new
```

然后在 Codex 中打开该目录并运行：

```text
$cl-onboard
```

## 核心流程

```text
$cl-strategy     -> STRATEGY.md
$cl-ideate       -> docs/ideation/
$cl-review       -> 策划一致性审查
$cl-brainstorm   -> docs/brainstorms/
$cl-review       -> 策划一致性审查
$cl-design       -> docs/designs/
$cl-review       -> 策划一致性审查
$cl-plan         -> docs/plans/
$cl-review       -> 策划一致性审查
$cl-work         -> 本地代码和测试
$cl-verify       -> 独立验证
$cl-compound     -> docs/solutions/
$cl-render       -> 可选的只读 HTML 视图
```

`$cl-review` 只用于策划阶段。执行阶段保持 `$cl-work -> $cl-verify`。

`$cl-product-pulse` 当前是面向未来的占位 skill。V1 中它只描述预期的只读产品脉搏流程，不会连接 analytics、tracing、payment 或数据库。

## HTML 决策编辑器模式

策划类 skill 可以选择使用 `~html`，在正式 Markdown 产物定稿前生成临时浏览器编辑器。

```text
$cl-plan
-> 直接写 Markdown

$cl-plan ~html
-> 写入 docs/.compound-lite/drafts/...-editor.html
-> 用户导出 Markdown
-> 导出的 Markdown 成为正式产物
```

生成的 HTML editor 和 view 只给人阅读、判断、编辑。Markdown 仍然是后续 Agent 工作的唯一 source of truth。没有 `cl-finalize`、`~html-only` 或 `~import` 步骤。

## 已有项目的推荐第一次运行

```text
Use $cl-onboard to adopt Compound Lite in this repo. Start with a read-only scan, then draft AGENTS.md and STRATEGY.md. Do not change application code.
```

## 新项目的推荐第一次运行

```text
Use $cl-strategy to create STRATEGY.md, then use $cl-ideate to explore initial product/Agent directions.
```

## 致谢

Compound Lite 参考了 [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)，并在其 Compound Engineering 理念基础上，简化成适用于 Codex 的仓库级、Level 1 轻量工作流。
