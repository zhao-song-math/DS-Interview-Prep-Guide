#此脚本用于给Leetcode_Questions.md文件添加backlinks，并生成问题目录.

# -*- coding: utf-8 -*-
import os
import re

def update_markdown_file(main_file, notes_dir):
    """
    根据笔记文件夹的内容，更新主Markdown文件，并避免重复添加任何内容。

    Args:
        main_file (str): Leetcode问题目录.md 文件的路径。
        notes_dir (str): Leetcode_notes 文件夹的路径。
    """
    try:
        with open(main_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"错误：主文件未找到，请检查路径: {main_file}")
        return

    # --- 任务一：链接数据结构/算法主题，并替换旧的 backlinks ---
    lines_after_task1 = []
    in_dsa_section = False
    skipping_old_backlinks = False

    for line in lines:
        if skipping_old_backlinks:
            if not line.strip() or line.strip().startswith('- ['):
                continue
            else:
                skipping_old_backlinks = False

        if line.strip() == '# Leetcode问题目录':
            in_dsa_section = False
        if line.startswith('# 数据结构') or line.startswith('# 算法'):
            in_dsa_section = True

        match = re.match(r'^(###\s+)(.*)', line)
        if in_dsa_section and match:
            heading_prefix = match.group(1)
            title = match.group(2).strip()

            link_match = re.match(r'\[(.*)\]\(.*\)', title)
            if link_match:
                title = link_match.group(1)

            filename_title = title.replace(' ', '_')
            note_filename = f"{filename_title}.md"
            note_filepath = os.path.join(notes_dir, note_filename)
            relative_note_path = os.path.join(os.path.basename(notes_dir), note_filename).replace('\\', '/')

            if os.path.exists(note_filepath):
                lines_after_task1.append(f"{heading_prefix}[{title}]({relative_note_path})\n")

                try:
                    with open(note_filepath, 'r', encoding='utf-8') as note_f:
                        note_content = note_f.read()
                    
                    backlinks_match = re.search(r'## backlinks', note_content, re.IGNORECASE)
                    if backlinks_match:
                        backlinks_section = note_content[backlinks_match.end():]
                        backlinks = re.findall(r'-\s+\[.*\]\(.*\)', backlinks_section)
                        for backlink in backlinks:
                            # 【修改】增加一个条件判断，忽略特定的backlink
                            if "[Leetcode问题目录](Leetcode问题目录.md)" not in backlink:
                                lines_after_task1.append(f"{backlink.strip()}\n")
                except Exception as e:
                    print(f"处理 backlinks 时出错 ({note_filepath}): {e}")

                skipping_old_backlinks = True
            else:
                lines_after_task1.append(line)
        else:
            lines_after_task1.append(line)
            
    # --- 任务二：替换旧的 Leetcode 问题目录 ---
    lines_after_task2 = []
    header_index = -1
    for i, line in enumerate(lines_after_task1):
        if line.strip() == '# Leetcode问题目录':
            header_index = i
            break
            
    if header_index == -1:
        lines_after_task2 = lines_after_task1
        lines_after_task2.append('\n# Leetcode问题目录\n')
        header_index = len(lines_after_task2) - 1
    else:
        lines_after_task2 = lines_after_task1[:header_index + 1]

    new_problem_links = []
    try:
        all_files = os.listdir(notes_dir)
        problem_files = [f for f in all_files if f.endswith('.md') and re.match(r'^\d+', f)]

        sorted_problem_files = sorted(
            problem_files,
            key=lambda f: int(re.match(r'^(\d+)', f).group(1))
        )

        for filename in sorted_problem_files:
            problem_title_base = os.path.splitext(filename)[0]
            formatted_title = problem_title_base.replace('-', '. ', 1)
            link_path = os.path.join(os.path.basename(notes_dir), filename).replace('\\', '/')
            link = f"- [{formatted_title}]({link_path})\n"
            new_problem_links.append(link)
            
    except FileNotFoundError:
        print(f"错误: 笔记目录未找到: {notes_dir}")

    lines_after_task2.extend(new_problem_links)

    try:
        with open(main_file, 'w', encoding='utf-8') as f:
            f.writelines(lines_after_task2)
        print(f"成功更新文件: '{os.path.basename(main_file)}'")
    except Exception as e:
        print(f"写入文件时出错 ({main_file}): {e}")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    notes_dir_path = os.path.join(project_dir, "Leetcode_notes")
    main_file_path = os.path.join(notes_dir_path, "Leetcode问题目录.md")

    print("--- 路径信息 ---")
    print(f"项目根目录: {project_dir}")
    print(f"笔记目录: {notes_dir_path}")
    print(f"主文件路径: {main_file_path}")
    print("--------------------")

    update_markdown_file(main_file_path, notes_dir_path)