import streamlit as st

# 관절 건강 설문 문항
questions = [
    "계단을 오르내릴 때 무릎이나 관절에서 통증을 느낀다.",
    "아침에 일어났을 때 관절이 뻣뻣하거나 굳은 느낌이 든다.",
    "오래 서 있거나 걷고 나면 관절에 피로감이나 통증이 있다.",
    "날씨가 흐리거나 추우면 관절이 더 불편해진다.",
    "관절에서 소리가 나거나 이물감이 느껴진다.",
    "특정 동작을 할 때 관절의 움직임이 제한되거나 불편하다.",
    "관절에 부종이나 붓기가 생기는 경우가 있다.",
    "가족 중 관절염이나 퇴행성 질환 병력이 있다.",
    "관절 영양제(글루코사민, MSM, 콘드로이친 등)를 복용한 적이 있다.",
    "평소 관절 건강을 위한 운동(스트레칭, 걷기 등)을 자주 하지 못한다."
]

# 제목
st.title("🦴 관절 건강 설문")
st.write("관절 상태를 확인하고 알맞은 제품을 추천받아보세요.")
st.markdown("👉 **1 = 아니다, 5 = 그렇다**")

scores = []
with st.form("joint_survey"):
    for q in questions:
        score = st.slider(q, 1, 5, 3, format="%d")
        scores.append(score)
    submitted = st.form_submit_button("제출")

if submitted:
    total = sum(scores)
    st.subheader(f"📊 총점: {total}")

    if total >= 40:
        st.error("🔴 **관절 퇴행 진행 가능성**: 고함량 MSM, 글루코사민 복합제를 추천합니다.")
        st.image("https://cdn.pixabay.com/photo/2017/08/01/08/29/pills-2563788_1280.jpg", width=200)
        st.markdown("[프리미엄 관절 제품 보기](https://example.com/joint-premium)")

    elif total >= 25:
        st.info("🟠 **관절 피로/초기 불균형**: MSM+비타민D 보조제를 추천합니다.")
        st.image("https://cdn.pixabay.com/photo/2021/06/18/13/07/pills-6345457_1280.jpg", width=200)
        st.markdown("[기초 관절 제품 보기](https://example.com/joint-basic)")

    else:
        st.success("🟢 **관절 상태 양호**: 기본적인 보조제를 통해 유지하면 좋습니다.")
        st.image("https://cdn.pixabay.com/photo/2016/02/19/10/00/pills-1200737_1280.jpg", width=200)
        st.markdown("[관절 유지 제품 보기](https://example.com/joint-maintain)")
def run():
    # 설문 코드 전체를 이 함수 안에 넣으면 됩니다.
    # 예시:
    import streamlit as st

    st.header("🦴 관절 건강 설문")
    # 질문, 슬라이더, 제출 버튼 등
