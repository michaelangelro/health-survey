import streamlit as st

# 눈 건강 설문 문항
questions = [
    "스마트폰이나 컴퓨터 화면을 하루 5시간 이상 본다.",
    "눈이 자주 피로하거나 뻑뻑한 느낌이 든다.",
    "눈이 쉽게 충혈되거나 건조해지는 편이다.",
    "작은 글씨를 볼 때 눈이 쉽게 피곤해진다.",
    "렌즈 착용 후 눈이 자주 건조하거나 아프다.",
    "밝은 빛에 눈부심을 자주 느낀다.",
    "시야가 흐려지거나 눈이 뿌옇게 보일 때가 있다.",
    "저녁이나 밤이 되면 시력이 더 나빠지는 느낌이 든다.",
    "루테인, 오메가3, 아스타잔틴 등의 눈 건강 보조제를 복용해본 적 있다.",
    "눈 피로로 인해 두통이나 집중력 저하를 경험한 적 있다."
]

# 제목
st.title("👁️ 눈 건강 설문")
st.write("최근 눈 건강 상태를 확인해보세요.")
st.markdown("👉 **1 = 아니다, 5 = 그렇다**")

scores = []
with st.form("eye_survey"):
    for q in questions:
        score = st.slider(q, 1, 5, 3, format="%d")
        scores.append(score)
    submitted = st.form_submit_button("제출")

if submitted:
    total = sum(scores)
    st.subheader(f"📊 총점: {total}")

    if total >= 40:
        st.error("👀 **눈 피로 및 건조 심함**: 루테인, 아스타잔틴 복용을 추천합니다.")
        st.image("https://cdn.pixabay.com/photo/2017/05/09/16/40/capsule-2291900_1280.jpg", width=200)
        st.markdown("[고함량 눈 건강 제품 보기](https://example.com/eye-premium)")

    elif total >= 25:
        st.info("🌿 **경미한 눈 피로**: 루틴 관리와 눈 보조제 복용 추천.")
        st.image("https://cdn.pixabay.com/photo/2020/06/22/05/39/eye-5327230_1280.jpg", width=200)
        st.markdown("[눈 건강 기본 제품 보기](https://example.com/eye-basic)")

    else:
        st.success("✅ **양호한 상태입니다**: 현재 상태 잘 유지하세요.")
        st.image("https://cdn.pixabay.com/photo/2018/03/02/10/01/capsule-3193125_1280.jpg", width=200)
        st.markdown("[눈 건강 유지 제품 보기](https://example.com/eye-support)")
def run():
    # 설문 코드 전체를 이 함수 안에 넣으면 됩니다.
    # 예시:
    import streamlit as st

    st.header("👁️ 눈 건강 설문")
    # 질문, 슬라이더, 제출 버튼 등
