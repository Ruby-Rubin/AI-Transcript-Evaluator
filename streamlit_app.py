import streamlit as st
import tempfile
import matplotlib.pyplot as plt
import numpy as np

from backend import evaluate_video

DEBUG_MODE = False


def get_score_color(score):

    if score == 10:
        return "🥇"

    elif score >= 9:
        return "🟢"

    elif score >= 7:
        return "🟡"

    else:
        return "🔴"


def show_score_bar(title, score):

    st.write(
        f"**{get_score_color(score)} {title}: {score}/10**"
    )

    st.progress(score / 10)


def create_radar_chart(
    grammar,
    vocab,
    clarity,
    tech,
    prof
):

    labels = [
        "Grammar",
        "Vocab",
        "Clarity",
        "Tech",
        "Professionalism"
    ]

    values = [
        grammar,
        vocab,
        clarity,
        tech,
        prof
    ]

    values += values[:1]

    angles = np.linspace(
        0,
        2 * np.pi,
        len(labels),
        endpoint=False
    ).tolist()

    angles += angles[:1]

    fig, ax = plt.subplots(
        figsize=(3, 3),
        subplot_kw=dict(polar=True)
    )

    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#1A1D24")

    ax.plot(
        angles,
        values,
        linewidth=3
    )

    ax.fill(
        angles,
        values,
        alpha=0.25
    )

    ax.set_xticks(
        angles[:-1]
    )

    ax.set_xticklabels(
        labels,
        color="white",
        fontsize=6
    )

    ax.tick_params(
        colors="white"
    )

    ax.set_ylim(0, 10)

    plt.tight_layout()

    return fig


st.set_page_config(
    page_title="AI Transcript Evaluator",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Transcript Evaluator")

uploaded_file = st.file_uploader(
    "Upload Video",
    type=["mp4", "mov", "avi", "mkv"]
)

if uploaded_file is not None:

    with st.spinner(
        "Transcribing and evaluating..."
    ):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        ) as temp_file:

            temp_file.write(
                uploaded_file.read()
            )

            temp_path = temp_file.name

        if DEBUG_MODE:

            transcript = """
            Cloud Computing is the delivery of computing services over the internet.
            It provides scalable storage and computing resources.
            """

            report = {
                "grammar": {"score": 9},
                "vocabulary": {"score": 8.1},
                "clarity": {
                    "score": 8,
                    "reason": "Sample clarity feedback."
                },
                "technical_accuracy": {
                    "score": 9,
                    "reason": "Sample technical feedback."
                },
                "professionalism": {
                    "score": 7,
                    "reason": "Sample professionalism feedback."
                }
            }

        else:

            transcript, report = evaluate_video(
                temp_path
            )

    st.success(
        "Evaluation Complete!"
    )

    grammar = report["grammar"]["score"]
    vocab = report["vocabulary"]["score"]
    clarity = report["clarity"]["score"]
    tech = report["technical_accuracy"]["score"]
    prof = report["professionalism"]["score"]

    overall_score = round(
        (
            grammar
            + vocab
            + clarity
            + tech
            + prof
        ) / 5,
        2
    )

    if overall_score == 10:

        badge = "🥇 PERFECT"

    elif overall_score >= 9:

        badge = "🏆 EXCELLENT"

    elif overall_score >= 7:

        badge = "⭐ GOOD"

    else:

        badge = "📚 IMPROVE"

    st.header(
        f"{badge} • Overall Score: {overall_score}/10"
    )

    st.divider()

    st.subheader(
        "Evaluation Results"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            f"{get_score_color(grammar)} Grammar",
            grammar
        )

    with col2:
        st.metric(
            f"{get_score_color(vocab)} Vocabulary",
            vocab
        )

    with col3:
        st.metric(
            f"{get_score_color(clarity)} Clarity",
            clarity
        )

    col4, col5 = st.columns(2)

    with col4:
        st.metric(
            f"{get_score_color(tech)} Technical Accuracy",
            tech
        )

    with col5:
        st.metric(
            f"{get_score_color(prof)} Professionalism",
            prof
        )

    st.divider()

    st.subheader(
        "Score Breakdown"
    )

    show_score_bar(
        "Grammar",
        grammar
    )

    show_score_bar(
        "Vocabulary",
        vocab
    )

    show_score_bar(
        "Clarity",
        clarity
    )

    show_score_bar(
        "Technical Accuracy",
        tech
    )

    show_score_bar(
        "Professionalism",
        prof
    )

    st.divider()

    st.subheader(
        "Performance Radar"
    )

    radar_fig = create_radar_chart(
        grammar,
        vocab,
        clarity,
        tech,
        prof
    )

    st.pyplot(radar_fig)

    st.divider()

    st.subheader(
        "Feedback"
    )

    st.write(
        f"**Clarity:** {report['clarity']['reason']}"
    )

    st.write(
        f"**Technical Accuracy:** {report['technical_accuracy']['reason']}"
    )

    st.write(
        f"**Professionalism:** {report['professionalism']['reason']}"
    )

    st.divider()

    with st.expander(
        "View Transcript"
    ):

        st.write(
            transcript
        )