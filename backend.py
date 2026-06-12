from transcript import generate_transcript
from grammar import grammar_score
from vocabulary import vocabulary_score
from evaluator import evaluate_transcript


def evaluate_video(video_path):

    transcript = generate_transcript(video_path)

    gemini = evaluate_transcript(transcript)

    report = {
        "grammar": grammar_score(transcript),
        "vocabulary": vocabulary_score(transcript),
        "clarity": gemini["clarity"],
        "technical_accuracy": gemini["technical_accuracy"],
        "professionalism": gemini["professionalism"]
    }

    return transcript, report