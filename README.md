# 🔄 Discord Tag Changer

이 코드는는 사용자의 Discord 계정에 대해 일정 간격으로 여러 서버(guild)에 tag를 반복적으로 설정하는 **비공식 Discord API 사용 도구**입니다.


---

## 📜 기능 설명

- Discord API v9의 `/users/@me/clan` 엔드포인트에 PUT 요청을 반복적으로 전송합니다.
- 미리 정의된 서버(`guild_ids`)를 대상으로 `identity_guild_id`를 설정합니다.
- 2초 간격으로 순차 요청을 반복합니다.

---

## ⚙️ 사용법

### 1. 요구사항

- Python 3.x
- `requests` 라이브러리 (설치 필요 시 아래 명령어 사용)

```bash
pip install requests
```

---

### 2. 코드 설정

스크립트 상단에서 다음 항목을 설정해야 합니다:

```python
TOKEN = "당신의 디스코드 사용자 토큰"
PROPERTIES = "x-super-properties 값 (브라우저에서 추출 가능)"
```

> 🔐 토큰은 민감 정보이며 절대 외부에 공개하지 마세요.

---

### 3. 실행

```bash
python3 main.py
```

---

## 🔐 토큰 및 `x-super-properties` 값 추출 방법

> 브라우저 디버그 콘솔(F12 → Network 탭)에서 Discord 웹 클라이언트의 API 요청을 확인하여 Header 값 복사

- `authorization`: Discord 계정의 사용자 토큰
- `x-super-properties`: 브라우저 환경 정보 Base64 인코딩 값

---

## 🛑 주의사항

- 본 프로젝트는 학습 또는 테스트 목적 외 사용을 권장하지 않으며,  
  실제 계정으로 사용 시 계정 **제재**, **정지**, **IP 차단** 등의 위험이 있습니다.

---

## 📄 라이선스

MIT License  
이 프로젝트는 연구/학습 목적으로 자유롭게 사용 가능하지만, 책임은 사용자 본인에게 있습니다.
