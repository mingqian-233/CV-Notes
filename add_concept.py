import os
import re

# 文件路径
file_path = r'index.html'
notes_dir = r'notes'

# 获取 /notes 文件夹中序号最大的 HTML 文件
max_id = 0
max_filename = ''
for filename in os.listdir(notes_dir):
    match = re.match(r'(\d+)\.\s*(.*)\.html', filename)
    if match:
        file_id = int(match.group(1))
        if file_id > max_id:
            max_id = file_id
            max_filename = filename

# 新条目信息
name = max_filename.split('.')[1].strip()
show_name = f'{name}'
id = max_id

print(f'新条目：{id}. {show_name}')
print(f'文件名：{id}. {name}.html')
print(f'URL：notes/{id}.%20{name}.html')

url = f'https://mingqian-233.github.io/CV-Notes/notes/{id}.%20{name}.html'

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 检查是否已经存在该条目
entry_exists = any(f'{show_name}' in line for line in lines)
if entry_exists:
    print(f'条目 "{show_name}" 已存在于 {file_path} 中。')
    exit()



# 找到插入位置
insert_index = None
for i in range(len(lines)):
    line = lines[i]
    
    if 'const notes = [' in line:
        while lines[i].strip() != '];':
            i += 1
        # 在第i行之前新增条目如格式：{ title: "Mask R-CNN", url: "notes/3.%20Mask_R-CNN.html" }
        lines.insert(i, f'    {{ title: "{show_name}", url: "{url}" }},\n')
        break

# 找到最后一个 <h2> 标签的位置
last_h2_index = None
for i in range(len(lines)):
    if '</h2>' in lines[i]:
        last_h2_index = i

# 检查 last_h2_index 是否为 None
if last_h2_index is None:
    raise ValueError("未找到任何 </h2> 标签")

# 插入新条目
lines.insert(last_h2_index + 1, f'      <h2 id="{id}">\n')
lines.insert(last_h2_index + 2, f'        {id}.\n')
lines.insert(last_h2_index + 3, f'        <a href="{url}">\n')
lines.insert(last_h2_index + 4, f'          {show_name}</a>\n')
lines.insert(last_h2_index + 5, f'        \n')
lines.insert(last_h2_index + 6, f'      </h2>\n')

# 写回文件，覆盖原内容
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)

print(f'新条目已添加到 {file_path}')