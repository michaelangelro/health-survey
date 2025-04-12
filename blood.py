import streamlit as st

# 혈액순환 설문 문항
questions = [
    "손발이 자주 차고 저리거나 시리다.",
    "오래 앉아 있으면 다리가 붓거나 무거운 느낌이 든다.",
    "평소에 피로를 쉽게 느끼고 회복이 더디다.",
    "운동 후에도 체력이 쉽게 회복되지 않는다.",
    "피부가 창백하거나 혈색이 좋지 않다는 말을 들은 적 있다.",
    "갑자기 기온이 변할 때 혈압이 흔들리는 느낌이 든다.",
    "어깨나 목이 자주 뻐근하고 뭉치는 느낌이 든다.",
    "두통이나 어지럼증이 자주 나타난다.",
    "손끝, 발끝 감각이 둔하거나 시린 느낌이 자주 든다.",
    "혈액순환 보조제(오메가3, 은행잎, 나토 등)를 복용한 적 있다."
]

# 제목
st.title("🫀 혈액순환 설문")
st.write("혈액순환 상태를 점검해보세요.")
st.markdown("👉 **1 = 아니다, 5 = 그렇다**")

scores = []
with st.form("blood_survey"):
    for q in questions:
        score = st.slider(q, 1, 5, 3, format="%d")
        scores.append(score)
    submitted = st.form_submit_button("제출")

if submitted:
    total = sum(scores)
    st.subheader(f"📊 총점: {total}")

    if total >= 40:
        st.error("🔴 **혈액순환 저하**: 혈류 개선 보조제를 적극 권장합니다.")
        st.image("https://cdn.pixabay.com/photo/2017/08/06/02/32/pills-2581463_1280.jpg", width=200)
        st.markdown("[혈액순환 개선 제품 보기](https://example.com/blood-premium)")

    elif total >= 25:
        st.info("🟠 **가벼운 혈류 저하**: 은행잎 추출물, 비타민E 섭취 권장.")
        st.image("https://cdn.pixabay.com/photo/2016/11/29/05/08/pills-1862843_1280.jpg", width=200)
        st.markdown("[기초 혈액순환 제품 보기](https://example.com/blood-basic)")

    else:
        st.success("🟢 **양호한 상태입니다**: 현재 혈류 상태를 잘 유지하고 있습니다.")
        st.image("https://cdn.pixabay.com/photo/2016/10/27/22/52/medicine-1773737_1280.jpg", width=200)
        st.markdown("[혈류 유지 제품 보기](https://example.com/blood-maintain)")
def run():
    # 설문 코드 전체를 이 함수 안에 넣으면 됩니다.
    # 예시:
    import streamlit as st

    st.header("🫀 혈액순환 설문")
    # 질문, 슬라이더, 제출 버튼 등
