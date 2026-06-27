#!/usr/bin/env python3
"""check.py — AI Berkshire 插件清单一致性校验。

校验 Claude Code 插件打包的完整性，作为发布前准出门槛（参考
anthropics/financial-services 的 check.py 模式重新实现，零外部依赖）。

校验项：
  1. .claude-plugin/plugin.json 存在、JSON 合法、含必填 name
  2. plugin.json 的 commands[] 所列文件全部实际存在
  3. skills/ 下每个 .md 都已登记进 commands[]（无漂移 drift）
  4. .claude-plugin/marketplace.json 存在、JSON 合法、含 name/owner/plugins
  5. 每个 marketplace 插件条目的 source 目录存在，且含 .claude-plugin/plugin.json

用法：
    python3 scripts/check.py            # 从仓库根运行
退出码：全部通过 0，存在问题 1
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

errors = []
warnings = []
checks = 0


def fail(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def load_json(path):
    global checks
    checks += 1
    if not os.path.exists(path):
        fail(f"缺少文件: {os.path.relpath(path, ROOT)}")
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        fail(f"JSON 解析失败 {os.path.relpath(path, ROOT)}: {e}")
        return None


def check_plugin():
    global checks
    plugin = load_json(os.path.join(ROOT, ".claude-plugin", "plugin.json"))
    if plugin is None:
        return

    checks += 1
    if not plugin.get("name"):
        fail("plugin.json 缺少必填字段 name")

    # commands 所列文件是否存在
    listed = plugin.get("commands", []) or []
    if isinstance(listed, str):
        listed = [listed]
    listed_norm = set()
    for rel in listed:
        checks += 1
        p = os.path.join(ROOT, rel.lstrip("./"))
        if not os.path.exists(p):
            fail(f"plugin.json commands 指向不存在的文件: {rel}")
        else:
            listed_norm.add(os.path.normpath(rel.lstrip("./")))

    # skills/*.md 是否全部登记（无漂移）
    skills_dir = os.path.join(ROOT, "skills")
    if os.path.isdir(skills_dir):
        for fn in sorted(os.listdir(skills_dir)):
            if fn.endswith(".md"):
                checks += 1
                rel = os.path.normpath(os.path.join("skills", fn))
                if rel not in listed_norm:
                    fail(f"漂移：skills/{fn} 未登记进 plugin.json commands")

    if not plugin.get("version"):
        warn("plugin.json 未设置 version → 采用 commit-SHA 版本（每次提交即更新）。"
             "正式发布时可设置语义化版本。")


def check_marketplace():
    global checks
    mk = load_json(os.path.join(ROOT, ".claude-plugin", "marketplace.json"))
    if mk is None:
        return

    for field in ("name", "owner", "plugins"):
        checks += 1
        if field not in mk:
            fail(f"marketplace.json 缺少字段: {field}")

    for entry in mk.get("plugins", []):
        checks += 1
        name = entry.get("name", "<未命名>")
        src = entry.get("source")
        if not src:
            fail(f"marketplace 插件 {name} 缺少 source")
            continue
        src_dir = os.path.join(ROOT, src.lstrip("./")) if src != "./" else ROOT
        if not os.path.isdir(src_dir):
            fail(f"marketplace 插件 {name} 的 source 目录不存在: {src}")
        elif not os.path.exists(os.path.join(src_dir, ".claude-plugin", "plugin.json")):
            fail(f"marketplace 插件 {name} 的 source 下缺少 .claude-plugin/plugin.json")


def main():
    print("=" * 60)
    print("AI Berkshire 插件清单校验 (check.py)")
    print("=" * 60)

    check_plugin()
    check_marketplace()

    print(f"  执行检查项: {checks}")
    for w in warnings:
        print(f"  ⚠️  {w}")
    if errors:
        print(f"\n  ❌ 失败 {len(errors)} 项：")
        for e in errors:
            print(f"     - {e}")
        print("\n【打回】请修正后重新校验。")
        return 1
    print("\n  ✅ 全部通过。\n【准出】插件清单一致，可发布。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
