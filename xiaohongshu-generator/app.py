import os
import streamlit as st
from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY", ""),
    base_url="https://api.deepseek.com"
)

def 生成文案(关键词, 风格):
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
        messages=[{"role": "user", "content": 提示词}]
    )
    return response.choices[0].message.content

# ===== 网页界面从这里开始 =====

# 网页标题
st.title("✨ 小红书文案生成器")
st.write("输入关键词，一键生成爆款文案！")

# 输入框
关键词 = st.text_input("关键词", placeholder="比如：夏日防晒、咖啡店打卡")

# 下拉菜单
风格 = st.selectbox(
    "选择风格",
    ["活泼可爱", "文艺清新", "专业种草"]
)

# 按钮
if st.button("🚀 生成文案"):
    if 关键词 == "":
        st.warning("请先输入关键词！")
    else:
        # 显示加载动画
        with st.spinner("AI生成中..."):
            结果 = 生成文案(关键词, 风格)
        
        # 显示结果
        st.success("生成完成！")
        st.write(结果)