import os
import re
import requests

def find_next_image_name():
    # 获取当前目录下的所有文件
    files = os.listdir('.')
    # 使用正则表达式匹配文件名格式为 bg_数字.jpeg
    pattern = re.compile(r'bg_(\d+)\.jpeg')
    max_number = 0

    for file in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            max_number = max(max_number, number)

    # 返回下一个图片的文件名
    return f"bg_{max_number + 1}.jpeg"

def download_image(url, filename):
    try:
        # 发送 HTTP GET 请求下载图片
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"图片已成功下载并保存为 {filename}")
    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")

def main():
    # 找到下一个图片的文件名
    next_image_name = find_next_image_name()
    print(f"将要下载并保存的图片名为: {next_image_name}")
    
    # 请求用户输入图片的下载网址
    url = input("请输入图片的下载网址: ").strip()
    if not url:
        print("未输入网址，程序退出。")
        return

    # 下载图片
    download_image(url, next_image_name)

if __name__ == "__main__":
    main()