import os

# 文件路径
file_path = r'index.html'

# 新条目信息
name = 'DETR'
show_name = 'DETR'
id = 6


url = f'https://mingqian-233.github.io/CV-Notes/notes/{id}.%20{name}.html'

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

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
lines.insert(last_h2_index + 1, f'      <h2 id="{id}-mask_r-cnnhttpsmingqian-233githubiocv-notesnotes320mask_r-cnnhtml">\n')
lines.insert(last_h2_index + 2, f'        {id}.\n')
lines.insert(last_h2_index + 3, f'        <a href="{url}"\n')
lines.insert(last_h2_index + 4, f'          >{show_name}</a\n')
lines.insert(last_h2_index + 5, f'        >\n')
lines.insert(last_h2_index + 6, f'      </h2>\n')

# 写回文件，覆盖原内容
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)

print(f'新条目已添加到 {file_path}')