from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse #インポート
import random  # randomライブラリを追加

app = FastAPI()


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

    return omikuji_list[random.randrange(10)]
@app.get("/index")
def index():
    html_content = """
   <!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>シンプルなウェブページ</title>
    
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
            <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-2">ウェブサイトへようこそ</h1>
            <p class="text-lg text-gray-600">これはシンプルでクリーンなウェブページのテンプレートです。</p>
        </header>

        <!-- メインコンテンツセクション -->
        <main>
            <!-- カード形式のレイアウト -->
            <div class="bg-white rounded-lg shadow-lg p-8 md:p-12 mb-8">
                <h2 class="text-2xl font-bold mb-4">このページについて</h2>
                <p class="mb-4">
                    このページは、最新のウェブ技術であるTailwind CSSを使用して作成されています。レスポンシブデザインに対応しているため、パソコン、タブレット、スマートフォンなど、どのデバイスから見てもきれいに表示されます。
                </p>
                <p>
                    この下の部分を編集して、自己紹介や、あなたの作品、趣味など、好きな内容を自由に追加してみてください。
                </p>
            </div>

            <!-- 2カラムレイアウトの例 -->
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white rounded-lg shadow-lg p-8">
                    <h3 class="text-xl font-bold mb-3">セクション1</h3>
                    <p>ここに内容を記述します。例えば、あなたの経歴やスキルなどを書くことができます。箇条書きを使っても見やすいでしょう。</p>
                    <ul class="list-disc list-inside mt-4">
                        <li>HTML & CSS</li>
                        <li>JavaScript</li>
                        <li>デザイン</li>
                    </ul>
                </div>
                <div class="bg-white rounded-lg shadow-lg p-8">
                    <h3 class="text-xl font-bold mb-3">セクション2</h3>
                    <p>こちらのセクションには、趣味や好きなことについて書くのはどうでしょうか。写真などを追加すると、より魅力的なページになります。</p>
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