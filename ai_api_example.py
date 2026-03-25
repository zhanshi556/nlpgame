"""
AI API 调用示例 (AI API Call Example)

使用方法 (Usage):
    1. 安装依赖: pip install openai
    2. 设置环境变量: export OPENAI_API_KEY="your-api-key-here"
    3. 运行脚本: python ai_api_example.py
"""

import os
from openai import OpenAI


def call_ai_api(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """
    调用 AI API 并返回模型的回复。

    Args:
        prompt: 发送给模型的提示文本
        model: 使用的模型名称，默认为 gpt-3.5-turbo

    Returns:
        模型生成的回复文本
    """
    # 从环境变量读取 API 密钥（推荐做法，避免硬编码密钥）
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "未找到 OPENAI_API_KEY 环境变量。\n"
            "请先执行: export OPENAI_API_KEY='your-api-key-here'"
        )

    # 初始化 OpenAI 客户端
    client = OpenAI(api_key=api_key)

    # 发送请求并获取响应
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    # 提取并返回回复内容
    if not response.choices:
        raise ValueError("API 返回了空的 choices 列表，请检查请求参数。")
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("API 返回的消息内容为空。")
    return content


def main():
    prompt = "请用一句话介绍自然语言处理（NLP）。"
    print(f"提示词: {prompt}\n")

    try:
        reply = call_ai_api(prompt)
        print(f"AI 回复: {reply}")
    except ValueError as e:
        print(f"配置错误: {e}")
    except Exception as e:
        print(f"调用 AI API 时发生错误: {e}")


if __name__ == "__main__":
    main()
