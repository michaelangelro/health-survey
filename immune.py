import streamlit as st

# 면역 건강 설문 문항
questions = [
    "최근 들어 감기에 자주 걸린다.",
    "상처가 잘 낫지 않거나 자주 덧난다.",
    "아침에 일어나기 힘들고 무기력하다.",
    "계절이 바뀌면 쉽게 몸살이나 열이 난다.",
    "피로가 오래 지속되는 편이다.",
    "잇몸이 자주 붓거나 피가 난다.",
    "식사 시간이 불규칙하거나 편식하는 편이다.",
    "스트레스를 자주 받고 해소가 잘 되지 않는다.",
    "운동 부족이나 활동량이 적은 편이다.",
    "알레르기 증상이 자주 나타난다."
]

# 제목
st.title("🛡️ 면역 건강 설문")
st.write("최근 나의 면역 상태를 체크해보세요.")
st.markdown("👉 **1 = 아니다, 5 = 그렇다**")

scores = []
with st.form("immune_survey"):
    for q in questions:
        score = st.slider(q, 1, 5, 3, format="%d")
        scores.append(score)
    submitted = st.form_submit_button("제출")

if submitted:
    total = sum(scores)
    st.subheader(f"📊 총점: {total}")

    if total >= 40:
        st.error("🧬 **면역력 저하**: 강력한 면역 보충이 필요합니다.")
        st.image("https://cdn.pixabay.com/photo/2017/08/07/20/33/vitamin-2607262_1280.jpg", width=200)
        st.markdown("[비타민C + 아연 제품 보기](https://example.com/vitc-zinc)")
        st.image("https://cdn.pixabay.com/photo/2019/06/14/12/15/propolis-4277623_1280.jpg", width=200)
        st.markdown("[프로폴리스 제품 보기](https://example.com/propolis)")

    elif total >= 25:
        st.info("🔰 **일반 면역 케어**: 기초 면역 영양제 복용이 좋습니다.")
        st.image("https://cdn.pixabay.com/photo/2021/01/29/10/31/probiotic-5959570_1280.jpg", width=200)
        st.markdown("[유산균 보기](https://example.com/probiotic)")
        st.image("https://cdn.pixabay.com/photo/2022/01/10/11/07/ginseng-6927716_1280.jpg", width=200)
        st.markdown("[홍삼 제품 보기](https://example.com/ginseng)")

    else:
        st.success("✅ **양호한 상태입니다**: 현재 상태를 잘 유지하세요.")
        st.image("https://cdn.pixabay.com/photo/2021/04/08/09/12/vitamins-6161210_1280.jpg", width=200)
        st.markdown("[기초 종합비타민 보기](https://example.com/multivitamin)")
def run():
    # 설문 코드 전체를 이 함수 안에 넣으면 됩니다.
    # 예시:
    import streamlit as st

    st.header("🛡️ 면역 건강 설문")
    # 질문, 슬라이더, 제출 버튼 등
