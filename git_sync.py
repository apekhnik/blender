import bpy
import os
import subprocess

def sync_git():
    repo_path = "C:\Users\alexe\blender\envMap\blender"
    os.chdir(repo_path)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Blender auto-save"])
    subprocess.run(["git", "pull", "--rebase"])
    subprocess.run(["git", "push"])

# Обработчик для события сохранения
def on_save(scene):
    sync_git()

# Добавляем обработчик
bpy.app.handlers.save_post.append(on_save)