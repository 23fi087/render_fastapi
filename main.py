from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel # PydanticからBaseModelをインポート
import random

app = FastAPI()

# POSTリクエストで受け取るJSONの型を定義するクラス
# {"present": "プレゼントの内容"} という形式のJSONを受け付ける
class Present(BaseModel):
    present: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    # APIとしては、{"result": "大吉"} のようにJSON形式で返すのが一般的です
    # random.choiceを使うと、リストからランダムに1つの要素を簡単に選べます
    return {"result": random.choice(omikuji_list)}

@app.get("/index")
def index():
    html_content = """
   <!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <title>の開始タグが余分だったので修正 -->
    <title>課題9-1</title>
    
    <!-- Tailwind CSSを読み込みます -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google FontsからInterフォントを読み込みます -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
    
    <style>
        /* フォント設定：日本語はNoto Sans JP、英数字はInterを使用します */
        body {
            font-family: 'Inter', 'Noto Sans JP', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-100 text-gray-800">

    <!-- ページ全体を囲むコンテナ -->
    <div class="container mx-auto p-5 md:p-10">

        <!-- ヘッダーセクション -->
        <header class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-2">9-1</h1>
            <p class="text-lg text-gray-600">こんにちは</p>
        </header>

        <!-- メインコンテンツセクション -->
        <main>
            <!-- カード形式のレイアウト -->
            <div class="bg-white rounded-lg shadow-lg p-8 md:p-12 mb-8">
                <h2 class="text-2xl font-bold mb-4">課題</h2>
                <p class="mb-4">
                    課題9-1, 課題9-2に取り組み、必要なファイルをBoxにて提出してください。
                </p>
                <p>
                    好きな食べ物は唐揚げ。
                </p>
            </div>

            <!-- 2カラムレイアウトの例 -->
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white rounded-lg shadow-lg p-8">
                    <h3 class="text-xl font-bold mb-3">セクション1</h3>
                    <p>趣味はbasketball</p>
                    <ul class="list-disc list-inside mt-4">
                        <li>HTML & CSS</li>
                        <li>JavaScript</li>
                        <li>デザイン</li>
                    </ul>
                </div>
                <div class="bg-white rounded-lg shadow-lg p-8">
                    <h3 class="text-xl font-bold mb-3">セクション2</h3>
                    <p>最近はマリオーカートで遊んでます</p>
                </div>
            </div>
        </main>

        <!-- フッターセクション -->
        <footer class="text-center mt-12 py-6 border-t border-gray-300">
            <p class="text-gray-500">&copy; 2024 あなたの名前. All Rights Reserved.</p>
        </footer>

    </div>

</body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# @app.post("/present") のインデントを修正
@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}  # f文字列というPythonの機能を使っている
