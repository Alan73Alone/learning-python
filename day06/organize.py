"""批量整理文件夹：按扩展名分类到子文件夹"""
import shutil
import sys
from pathlib import Path
from time import time

CATEGORIES = {
    ".jpg": "图片", ".jpeg": "图片", ".png": "图片", ".gif": "图片",
    ".mp4": "视频", ".mkv": "视频",
    ".mp3": "音频", ".wav": "音频",
    ".doc": "文档", ".docx": "文档", ".pdf": "文档", ".txt": "文档",
    ".zip": "压缩包", ".rar": "压缩包",
    ".py": "代码", ".java": "代码", ".js": "代码",
}

def unique_path(target_dir: Path, filename: str) -> Path:
    """加料2：同名文件冲突时自动加序号 a.jpg -> a_1.jpg -> a_2.jpg"""
    dest = target_dir / filename
    if not dest.exists():
        return dest
    stem = dest.stem
    suffix = dest.suffix
    i = 1
    while True:
        candidate = target_dir / f"{stem}_{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1

def organize(folder: str, days: int = 0):
    folder = Path(folder)
    if not folder.exists():
        print(f"文件夹不存在: {folder}")
        return

    for item in folder.iterdir():
        if not item.is_file():          # 只处理文件
            continue

        # 加料1：只整理超过 days 天没修改过的文件（days=0 表示全部）
        if days > 0:
            age_seconds = time() - item.stat().st_mtime
            if age_seconds < days * 24 * 3600:
                continue

        ext = item.suffix.lower()
        target = folder / CATEGORIES.get(ext, "其他")
        target.mkdir(exist_ok=True)     # 不存在就创建

        dest = unique_path(target, item.name)   # 加料2：处理重名
        shutil.move(str(item), str(dest))
        print(f"移动: {item.name} -> {target.name}/{dest.name}")

if __name__ == "__main__":              # 注意：__name__ 是两边各两个下划线
    # 加料3：支持命令行参数
    args = sys.argv[1:]
    if not args:
        print("用法: python organize.py <文件夹路径> [--days 天数]")
        print("示例: python organize.py D:\\test_downloads")
        print("可选: python organize.py D:\\test_downloads --days 7   # 只整理7天前没动过的文件")
        sys.exit(1)

    folder = args[0]
    days = 0
    if "--days" in args:
        idx = args.index("--days")
        days = int(args[idx + 1])

    organize(folder, days)
