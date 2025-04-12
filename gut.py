import streamlit as st

# 장 건강 설문 문항
questions = [
    "배에 가스가 차는 느낌이 자주 있다.",
    "변비 또는 설사 증상이 반복된다.",
    "하루에 1회 이상 배변하지 않는다.",
    "변을 보고도 잔변감이 느껴진다.",
    "특정 음식(유제품, 밀가루 등) 섭취 후 속이 불편하다.",
    "과민성 대장 증후군 진단을 받은 적이 있다.",
    "아랫배가 자주 더부룩하거나 불편하다.",
    "식후 소화가 느리거나 더부룩함이 오래간다.",
    "유산균이나 장 건강 보조제를 먹으면 좋아지는 느낌이 든다.",
    "장 트러블로 피부 트러블이 생긴 적 있다."
]

# 제목
st.title("💩 장 건강 설문")
st.write("내 장 상태는 건강한가요? 지금 확인해보세요.")
st.markdown("👉 **1 = 아니다, 5 = 그렇다**")

scores = []
with st.form("gut_survey"):
    for q in questions:
        score = st.slider(q, 1, 5, 3, format="%d")
        scores.append(score)
    submitted = st.form_submit_button("제출")

if submitted:
    total = sum(scores)
    st.subheader(f"📊 총점: {total}")

    if total >= 40:
        st.error("🦠 **장 건강 불균형**: 유산균 고함량 제품 복용을 추천합니다.")
        st.image("https://cdn.pixabay.com/photo/2017/09/08/11/49/probiotic-2721469_1280.jpg", width=200)
        st.markdown("[고함량 유산균 제품 보기](https://example.com/high-probiotics)")

    elif total >= 25:
        st.info("🌿 **장 트러블 주의 단계**: 식이섬유 및 효소 보충이 좋습니다.")
        st.image("https://cdn.pixabay.com/photo/2020/07/13/10/56/bacteria-5398836_1280.jpg", width=200)
        st.markdown("[일반 장 건강 제품 보기](https://example.com/general-gut)")

    else:
        st.success("✅ **양호한 상태입니다**: 장 건강을 잘 유지 중입니다.")
        st.image("https://cdn.pixabay.com/photo/2016/11/19/21/25/capsules-1845857_1280.jpg", width=200)
        st.markdown("[기초 장 건강 제품 보기](https://example.com/basic-gut)")
def run():
    # 설문 코드 전체를 이 함수 안에 넣으면 됩니다.
    # 예시:
    import streamlit as st

    st.header("💩 장 건강 설문")
    # 질문, 슬라이더, 제출 버튼 등
