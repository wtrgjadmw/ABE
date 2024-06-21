# ファイルの読み込み
file_path = '/mnt/data/ladderMul.csv'

# 変換後の内容を保存するリスト
converted_lines = []

# ファイルの内容を行ごとに処理
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        # 各行の形式は 'T1 = modularMul(Z1, Z1)'
        # まず '=' で分割
        parts = line.strip().split(' = ')
        left_part = parts[0]  # 'T1'
        right_part = parts[1]  # 'modularMul(Z1, Z1)'
        
        # 関数名と引数を取得するために '(' と ')' で分割
        function_name = right_part.split('(')[0]  # 'modularMul'
        arguments = right_part.split('(')[1].rstrip(')').split(', ')  # ['Z1', 'Z1']
        
        # 目的の形式に変換
        converted_line = f"{left_part},{arguments[0]},{arguments[1]},{function_name}"
        converted_lines.append(converted_line)

# 変換した内容を新しいファイルに保存
new_file_path = '/mnt/data/converted_ladderMul.csv'
with open(new_file_path, 'w') as new_file:
    for converted_line in converted_lines:
        new_file.write(converted_line + '\n')

new_file_path
