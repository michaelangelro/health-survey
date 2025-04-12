import streamlit as st

# 여성 건강 설문 문항
questions = [
    "생리 주기가 불규칙하거나 일정하지 않다.",
    "생리 전후로 심한 피로감이나 감정 기복이 있다.",
    "손발이 차거나 쉽게 냉증을 느낀다.",
    "질 건조감, 생식기 불편감이 있다.",
    "생리통이 심하거나 진통제를 자주 복용한다.",
    "갱년기 증상(안면홍조, 가슴 두근거림, 우울감 등)을 경험한 적 있다.",
    "피부 탄력, 모발 상태, 체중 변화 등 외형적 변화가 신경 쓰인다.",
    "평소 철분, 엽산, 칼슘, 마그네슘 등을 꾸준히 섭취하지 않는다.",
    "출산 후 회복이 오래 걸렸거나 호르몬 변화가 크게 느껴졌다.",
    "여성용 영양제(석류, 감마리놀렌산, 이소플라본 등)를 복용한 적 있다."
]

# 제목
st.title("🌸 여성 건강 설문")
st.write("여성 건강 상태를 점검하고 필요한 보조제를 추천받아보세요.")
st.markdown("👉 **1 = 아니다, 5 = 그렇다**")

scores = []
with st.form("women_survey"):
    for q in questions:
        score = st.slider(q, 1, 5, 3, format="%d")
        scores.append(score)
    submitted = st.form_submit_button("제출")

if submitted:
    total = sum(scores)
    st.subheader(f"📊 총점: {total}")

    if total >= 40:
        st.error("🔴 여성 건강 관리가 필요합니다. 전문가와 상담을 고려해보세요.")
    else:
        st.success("✅ 여성 건강 상태가 양호합니다. 현재 상태를 유지하세요.")
def run():
    # 설문 코드 전체를 이 함수 안에 넣으면 됩니다.
    # 예시:
    import streamlit as st

    st.header("🌸 여성 건강 설문")
    # 질문, 슬라이더, 제출 버튼 등
