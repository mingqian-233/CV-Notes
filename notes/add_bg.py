import os

# 定义文件路径
file_name='4. RetinaNet.html'
pic_name='bg_4.jpeg'
html_file_path =file_name
css_file_path = '../background-code.css'

# 读取 CSS 文件内容
with open(css_file_path, 'r', encoding='utf-8') as css_file:
    css_content = css_file.read()

# 读取 HTML 文件内容
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# 在css文件中，把${图片名}$.jpeg替换成图片名称
css_content = css_content.replace('${图片名}$.jpeg$', pic_name)
# 找到 <style> 标签的位置
style_tag_start = html_content.find('<style>')
style_tag_end = html_content.find('</style>')

# 插入 CSS 内容
if style_tag_start != -1 and style_tag_end != -1:
    new_html_content = (html_content[:style_tag_end] + '\n' + css_content + '\n' + html_content[style_tag_end:])
else:
    # 如果没有找到 <style> 标签，则在 <head> 标签结束前插入
    head_tag_end = html_content.find('</head>')
    if head_tag_end != -1:
        new_html_content = (html_content[:head_tag_end] + '<style>\n' + css_content + '\n</style>\n' + html_content[head_tag_end:])
    else:
        raise ValueError("HTML 文件中没有找到 <style> 或 </head> 标签")

# 写回 HTML 文件
with open(html_file_path, 'w', encoding='utf-8') as html_file:
    html_file.write(new_html_content)

print("CSS 片段已成功插入 HTML 文件")