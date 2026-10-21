# AI Long-Term Learning Skill (AI-LTS)

**AI 长期学习与训练系统 · 通用 Agent Skill**

独立于具体学科、引擎和 AI 平台的课程设计与长期互动教学规范。将“我想系统学会 X”转化为 **最终可验证能力 → 真实基础诊断 → 阶段课程设计 → 逐课互动与作业 → 能力考核 → 学习记录与跨平台续课** 的完整学习系统。

> **不是某一门课程，也不是游戏开发 Skill。** 这是一套让 AI 执行长期教育工作的元方法，适用于编程、数学、语言、历史、写作、音乐、商业实践、交易和游戏开发等方向。

## 能做什么

- **策划**：理解长期目标，反向设计能力地图、先修知识、阶段、模块与真实项目。
- **诊断**：开始授课前做分层测试，避免凭学历或自述高估/低估能力。
- **逐课互动**：讲解、演示、提问、等待回答、反馈纠错、独立挑战、布置作业。
- **真实考核**：按提交的作品/解题/测试证据决定是否达标，允许补课或挑战跳级。
- **长期迭代**：阶段复盘、间隔复习、更新课表和实际能力证据。
- **跨 AI 续课**：导出可移植状态快照；下一个 AI 从真实中断点继续。

## 快速安装

这是符合 [Agent Skills](https://agentskills.io/specification) 目录结构的 Skill：`SKILL.md` 在仓库根目录，其他规范和模板在 `references/`、`assets/`、`examples/` 中。

使用支持 Agent Skills 的客户端，可将整个仓库复制到其 Skill 目录，例如：

```text
.agents/skills/ai-long-term-learning/
  SKILL.md
  references/
  assets/
  examples/
  agents/
```

如果客户端支持 skills CLI，可以尝试：

```bash
npx skills add skingchan/ai-long-term-learning-skill
```

不同客户端对技能发现/安装的支持可能不同。对于不自动读取 Skill 的普通聊天 AI，直接提供 [SKILL.md](SKILL.md) 和 [完整原始教学规范](references/ai-lts-standard.zh-CN.md) 或复制 [通用提示词](assets/universal-prompt.zh-CN.txt)。

## 如何开始

**建立新项目：**

> 使用 ai-long-term-learning，按照大学级别的长期课程标准，为我设计【学习目标】的长期训练。我目前有【背景】；先做入学能力诊断，再分阶段规划，每节课互动学习、实践作业和真实考核。

**恢复既有课程：**

> 使用 ai-long-term-learning。以下是我的项目状态快照、最近作业和课程大纲。从上次未完成的步骤继续，不要重新生成整套课表。

**阶段测试：**

> 请按之前约定的 Gate 标准进行独立能力考核。你先提出需要我实际完成的题目/任务，等待我的回答，然后据证据判定。

## 目录

```text
SKILL.md
README.md
agents/openai.yaml
references/
  ai-lts-standard.zh-CN.md        # 完整原始 20 章标准
  curriculum-design.md
  diagnosis-and-assessment.md
  continuity.md
assets/
  universal-prompt.zh-CN.txt
  project-charter.template.md
  curriculum.template.md
  diagnosis.template.md
  lesson.template.md
  gate-report.template.md
  status-snapshot.template.md
examples/
  README.md
  software-engineering.md
  mathematics.md
  english.md
  chinese-history.md
  creative-writing.md
  electronic-keyboard.md
  internet-business.md
  trading.md
  ai-indie-game-developer.md
tests/validate_skill.py
```

## 九个课程示例

见 [示例索引](examples/README.md)。示例展示特定领域的最终目标、阶段地图、真实任务、诊断方法与通过证据。它们是**课程设计参考**，不是学习者私人档案、完成记录或合格证书。对于尚未核实的原课程细节，明确标为建议方案。

## 关键约束

- 没有实际答题/作品/录音/测试证据，不能宣称已学会或已完成。
- 长期课表是动态设计，不是无法更改的日历。
- 每节课的提问和练习必须真的等待学习者回答。
- 换平台或中断学习时使用可移植状态快照；不假定 AI 自动共享记忆。
- 领域专有考试和作业形式根据实际技能调整，不用一套题型衡量所有人。

版本：v1.0。仓库未主动声明开源许可证；使用与再分发权利应由仓库所有者进一步确定。
