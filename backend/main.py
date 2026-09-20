import json
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

profile = {
    "heroTitle": "关于我",
  "heroSubtitle": "项目，创意，灵感，心得，我的作品",
  "featuredWork": {
    "kicker": "作品",
    "title": "文字实验室",
    "copy": "拼音和情绪，挖掘中文里的细节",
    "linkLabel": "打开作品",
  },
  "identity": {
    "motto": "已识乾坤大，尤怜草木青",
    "learning": "零到全栈",
  },
}
class AnalyzeRequest(BaseModel):
    text: str


def utf8_json(data: dict) -> Response:
    """显式声明 UTF-8，兼容 Windows PowerShell 的响应解码。"""
    return Response(
        content=json.dumps(data, ensure_ascii=False),
        media_type="application/json; charset=utf-8",
    )


@app.get("/api/profile")
def get_profile() -> Response:
    return utf8_json(profile)


@app.post("/api/analyze")
def analyze(req: AnalyzeRequest) -> Response:
    return utf8_json({
        "text": req.text,
        "score": 0.5,
        "label": "偏平静",
        "pinyin": "（模块 6 再说）",
    })
