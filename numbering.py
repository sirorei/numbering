import os

# フォルダのパスを指定します
folder_path = '任意のパスを入れてください'

# フォルダ内の画像ファイルをリストアップします
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# 画像ファイルの数を取得します
num_images = len(image_files)

# 新しいファイル名を生成して画像ファイルをリネームします
for i, old_name in enumerate(image_files):
    # ゼロ詰めされた連番を生成します
    new_name = f"{i+1:02d}{os.path.splitext(old_name)[1]}"
    
    # フルパスを取得します
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    # ファイルをリネームします
    os.rename(old_path, new_path)
    print(f'Renamed: {old_name} -> {new_name}')

print(f'Renamed {num_images} files in {folder_path}.')
