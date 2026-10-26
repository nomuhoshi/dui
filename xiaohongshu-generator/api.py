import os
from openai import OpenAI

#初始化客户端，指向Deepseek的服务器
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY", ""),
    base_url="https://api.deepseek.com"
)

def 生成文案(关键词, 风格="活泼可爱"):
    """
    输入关键词和风格，返回小红书文案
    """
    提示词 = f"""
    你是一个专业的小红书文案写手。
    请根据以下关键词，写一篇小红书风格的文案。
    
    关键词：{关键词}
    风格：{风格}
    
    要求：
    - 开头要有吸引人的标题，加emoji
    - 正文100-150字
    - 结尾加3-5个相关话题标签
    """
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": 提示词}
        ]
    )
    
    return response.choices[0].message.content

关键词 = input("请输入关键词（比如：夏日防晒、咖啡店打卡）：")
风格 = input("请输入风格（活泼可爱 / 文艺清新 / 专业种草）：")

print("\n✨ 生成的文案：\n")
print(生成文案(关键词, 风格))