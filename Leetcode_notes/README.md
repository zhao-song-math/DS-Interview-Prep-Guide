
## 首次推送本地文件夹到GitHub流程:

**🔹 步骤 1：在 GitHub 上创建一个仓库**

1. 打开 GitHub → 点击右上角 + → New repository。
2. 输入仓库名字，比如：`DS-INTERVIEW-PREP-GUIDE`。
3. **不要勾选 "Initialize this repository with a README"**（因为我们要 push 本地文件）。
4. 点击 **Create repository**。
5. GitHub 会给你一个仓库地址，例如：
```arduino
https://github.com/zhao-song-math/DS-Interview-Prep-Guide.git
```

**🔹 步骤 2：在本地初始化 Git**

打开终端（Terminal），进入你的笔记文件夹，比如：
```bash
cd ~/Documents/DS-INTERVIEW-PREP-GUIDE
```
初始化 git：
```bash
git init
```

**🔹 步骤 3：关联远程仓库**

把本地文件夹和 GitHub 仓库绑定：
```bash
git remote add origin https://github.com/zhao-song-math/DS-Interview-Prep-Guide.git
```

**🔹 步骤 4：提交文件**

把所有文件加入暂存区：
```bash
git add .
```

提交到本地仓库：
```bash
git commit -m "first commit"
```

**🔹 步骤 5：推送到 GitHub**

默认分支现在叫 main（不是 master），执行：
```bash
git branch -M main
git push -u origin main
```

**更新只需执行:**

```bash
git add .
git commit -m "Update project"
git push
```


## 自动生成backlinks：
在`Note1.md`手动用生成 `[Note2](Note2.md)`正向索引，运行如下脚本自动在`Note2.md`文末生成`[Note1](Noe1.md)`反向索引。
1. 将代码保存到 `Your_Project_Folder/utils/generate_backlinks.py` 文件中。
2. 打开您的terminal（命令行工具）。
3. 使用 `cd` 命令进入到 `utils` 文件夹。
```Bash
# 示例 (请替换为您自己的路径)
cd path/to/Your_Project_Folder/utils
```
4. 直接运行Python脚本，无需任何参数。
```bash
python generate_backlinks.py
```


## 给Leetcode_Questions.md文件添加backlinks，并生成问题目录.

1. 将代码保存到 `Your_Project_Folder/utils/generate_Leetcode_contents.py` 文件中。
2. 打开您的terminal（命令行工具）。
3. 使用 `cd` 命令进入到 `utils` 文件夹。
```Bash
# 示例 (请替换为您自己的路径)
cd path/to/Your_Project_Folder/utils
```

4. 直接运行Python脚本，无需任何参数。
```Bash
python generate_Leetcode_contents.py
```


## 标签格式：
在`.md`文件开头加入语句:
```
<link rel="stylesheet" href="style.css">
```
可使用 `style.css` 中的标签格式。可在[tag colors](tag_colors.md)中查看已有的标签
