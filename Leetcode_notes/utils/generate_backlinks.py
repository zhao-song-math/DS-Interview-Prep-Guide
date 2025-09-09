# 正向索引：已经手动用 [Note](Note.md)编辑
# 反向索引：此脚本自动在文件最后生成 [Note](Note.md)的反向索引

import os
import re

# notes 文件夹的路径（相对于 utils）
NOTES_DIR = os.path.dirname(os.path.abspath(__file__))
# NOTES_DIR = os.path.join(os.path.dirname(__file__), "../Leetcode_notes")

# 将文件名转为链接显示格式（去掉扩展名，替换符号）
def format_link_text(filename):
    name = os.path.splitext(filename)[0]
    name = name.replace("-", ". ").replace("_", " ")
    return name

def collect_links():
    links = {}
    for fname in os.listdir(NOTES_DIR):
        if fname.endswith(".md") and fname != "Leetcode笔记目录.md":
            fpath = os.path.join(NOTES_DIR, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                # 匹配 Markdown 链接
                matches = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
                for _, link in matches:
                    target = os.path.basename(link)
                    if target.endswith(".md"):
                        links.setdefault(target, []).append(fname)
    return links

def update_files(backlinks):
    for fname in os.listdir(NOTES_DIR):
        if fname.endswith(".md") and fname != "Leetcode笔记目录.md":
            fpath = os.path.join(NOTES_DIR, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            # 先移除旧的 backlinks 部分
            content = re.sub(r"\n*## Backlinks[\s\S]*", "", content).rstrip()

            # 构建新的 backlinks 部分
            blines = [f"- [Leetcode 笔记目录](Leetcode笔记目录.md)"]

            refs = sorted(set(backlinks.get(fname, [])))
            if refs:  # 只有在有其他反向链接时才追加
                for ref in refs:
                    text = format_link_text(ref)
                    blines.append(f"- [{text}]({ref})")

            backlinks_text = "\n\n## Backlinks\n" + "\n".join(blines)

            # 添加到文件末尾
            content += backlinks_text

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

def main():
    backlinks = collect_links()
    update_files(backlinks)
    print("✅ Backlinks updated (safe to run multiple times, no duplicates).")

if __name__ == "__main__":
    main()

