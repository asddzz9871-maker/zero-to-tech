import json

from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel

app = FastAPI()

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
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
