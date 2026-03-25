# nlpgame
nlp project

## 如何用 Python 调用 AI API (How to Call an AI API with Python)

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 设置 API 密钥

```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 3. 运行示例

```bash
python ai_api_example.py
```

### 4. 在你的代码中导入并使用

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "你好！"},
    ],
)

print(response.choices[0].message.content)
```

> **注意**: 请勿将 API 密钥硬编码到代码中，始终通过环境变量传递。
