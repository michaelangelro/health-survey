import streamlit as st

# 피부 건강 설문 문항
questions = [
    "세안 후 피부가 당기거나 건조함을 느낀다.",
    "잦은 트러블(여드름, 뾰루지 등)이 발생한다.",
    "피부가 칙칙하고 생기 없어 보일 때가 많다.",
    "화장이나 스킨케어 제품이 잘 스며들지 않는 느낌이 든다.",
    "각질이나 거친 피부결이 자주 느껴진다.",
    "햇볕에 노출되었을 때 피부가 쉽게 붉어지거나 자극을 받는다.",
    "피부에 탄력이 부족하고 처진 느낌이 든다.",
    "가려움이나 피부 당김이 자주 느껴진다.",
    "피부가 예민해서 새로운 제품 사용 시 자극이 있다.",
    "콜라겐, 히알루론산, 비오틴 등의 피부 영양제를 복용한 적 있다."
]

# 제목
st.title("🌸 피부 건강 설문")
st.write("피부 상태를 점검하고 적절한 보조제를 추천받아보세요.")
st.markdown("👉 **1 = 아니다, 5 = 그렇다**")

scores = []
with st.form("skin_survey"):
    for q in questions:
        score = st.slider(q, 1, 5, 3, format="%d")
        scores.append(score)
    submitted = st.form_submit_button("제출")

if submitted:
    total = sum(scores)
    st.subheader(f"📊 총점: {total}")

    if total >= 40:
        st.error("🔴 **복합 피부 문제**: 고함량 콜라겐+히알루론산 보조제를 추천합니다.")
        st.image("https://cdn.pixabay.com/photo/2020/08/25/10/34/collagen-5517885_1280.jpg", width=200)
        st.markdown("[집중 피부관리 제품 보기](https://example.com/skin-premium)")

    elif total >= 25:
        st.info("🟠 **불균형 피부**: 콜라겐+비타민C 보조제를 추천합니다.")
        st.image("https://cdn.pixabay.com/photo/2020/09/30/20/36/vitamin-5621364_1280.jpg", width=200)
        st.markdown("[기초 피부관리 제품 보기](https://example.com/skin-basic)")

    else:
        st.success("🟢 **피부 상태 양호**: 현재 상태 유지를 위한 기본 보조제를 추천합니다.")
        st.image("https://cdn.pixabay.com/photo/2020/10/10/13/58/vitamins-5641872_1280.jpg", width=200)
        st.markdown("[피부 유지 제품 보기](https://example.com/skin-maintain)")
def run():
    # 설문 코드 전체를 이 함수 안에 넣으면 됩니다.
    # 예시:
    import streamlit as st

    st.header("🌸 피부 건강 설문")
    # 질문, 슬라이더, 제출 버튼 등
