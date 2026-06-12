from transcript import generate_transcript
from grammar import grammar_score
from vocabulary import vocabulary_score
from evaluator import evaluate_transcript


VIDEO_PATH = "test.mp4"


def main():

    print("Generating transcript...")

    transcript = generate_transcript(VIDEO_PATH)

    print("\nTranscript Generated Successfully!\n")

    gemini_results = evaluate_transcript(transcript)

    final_report = {
        "grammar": grammar_score(transcript),
        "vocabulary": vocabulary_score(transcript),
        "clarity": gemini_results["clarity"],
        "technical_accuracy": gemini_results["technical_accuracy"],
        "professionalism": gemini_results["professionalism"]
    }

    print("\n===== FINAL REPORT =====\n")

    print(final_report)


if __name__ == "__main__":
    main()