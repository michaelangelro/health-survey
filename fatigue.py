import streamlit as st

# 질문 목록
questions = [
    "아침에 일어나도 피로가 남아 있는 편이다.",
    "오후에 졸음이나 무기력함을 자주 느낀다.",
    "스트레스가 많다고 느낀다.",
    "업무나 공부 중 집중력이 자주 떨어진다.",
    "운동을 자주 하지 못한다.",
    "식사가 불규칙하거나 결식이 잦다.",
    "수면 시간이 6시간 이하인 날이 많다.",
    "만성적인 두통, 근육통 등을 느낀다.",
    "에너지 음료나 커피를 자주 찾는다.",
    "평소보다 의욕이 떨어졌다고 느낀다."
]

# 제목
st.title("💊 피로/활력 설문")
st.write("아래 문항에 대해 현재 상태에 맞게 체크해주세요.")
st.markdown("👉 **1 = 아니다, 5 = 그렇다**")

scores = []
with st.form("survey_form"):
    for q in questions:
        score = st.slider(q, 1, 5, 3, format="%d")
        scores.append(score)
    submitted = st.form_submit_button("제출")

if submitted:
    total = sum(scores)
    st.subheader(f"📊 총점: {total}")

    # 고활력
    if total >= 40:
        st.success("✅ **고활력 필요**: 활력 보충이 필요합니다.")
        st.image("https://cdn.pixabay.com/photo/2017/06/06/22/24/ginseng-2372348_1280.jpg", width=200)
        st.markdown("[홍삼 캡슐 보기](https://example.com/ginseng-product)")
        st.image("https://cdn.pixabay.com/photo/2016/03/05/20/07/pills-1236728_1280.jpg", width=200)
        st.markdown("[타우린 드링크 보기](https://example.com/taurine-product)")

    # 일반 피로
    elif total >= 25:
        st.info("ℹ️ **일반 피로**: 기초 영양 보충이 좋습니다.")
        st.image("https://cdn.pixabay.com/photo/2018/04/14/18/43/magnesium-3310929_1280.jpg", width=200)
        st.markdown("[마그네슘+비타민B 복합제 보기](https://example.com/bcomplex)")

    # 양호
    else:
        st.warning("💡 **양호**: 현재 상태를 잘 유지하세요.")
        st.image("https://cdn.pixabay.com/photo/2021/02/21/21/28/probiotics-6035747_1280.jpg", width=200)
        st.markdown("[기초 종합비타민 보기](https://example.com/multivitamin)")

def run():
    # 설문 코드 전체를 이 함수 안에 넣으면 됩니다.
    # 예시:
    import streamlit as st

    st.header("⚡ 피로/활력 설문")
    # 질문, 슬라이더, 제출 버튼 등
