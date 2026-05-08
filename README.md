# AI Quant Trading Agent

## 安装

```bash
pip install -r requirements.txt
```

## 配置

复制 `.env.example` 为 `.env`

## 启动 API

```bash
uvicorn app.main:app --reload
```

## 启动 Agent

```bash
python app/scheduler.py
```
