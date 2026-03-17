# Make a prompt including the transcript data
PROMPT_TEMPLATE = """
### TASK
You are extracting quiz questions and their final correct answers from a transcript of the podcast Lateral.

Your goal is to return EVERY question and its correct final answer.

### DEFINITIONS
- A "question" is a puzzle or challenge posed to the panel.
- An "answer" is the final confirmed correct solution, typically stated after phrases like:
  "you are absolutely right", "you've got it", "the answer is", "it was", "spot on".

### RULES
- Extract ALL questions in the order they appear.
- Do NOT skip any questions.
- Do not stop early; process the entire transcript.
- Include questions asked by guests as well as the host.
- Include the teaser question at the start if it is answered later.
- Ignore discussion, guesses, jokes, hints, and partial ideas.
- Only include the FINAL confirmed correct answer.
- Do not include guesses or incomplete answers.
- If a question is repeated, use the clearest version.
- Do not merge multiple questions into one.
- Do not invent or assume answers.
- If the answer is not explicitly confirmed, do not include the question.

### PARTIAL TRANSCRIPT RULES
- This may be only part of an episode.
- Only include a question if its answer appears in this text.
- If a question appears without its answer, DO NOT include it.
- If an answer appears without a clear question, DO NOT include it.

### OUTPUT FORMAT
Return ONLY valid JSON.
Do not include explanations, comments, or extra text.

{
  "episode_number": {episode_number},
  "qa_pairs": [
    {
      "question": "<string>",
      "answer": "<string>"
    }
  ]
}

### VALIDATION
Before finishing:
- Ensure every question has a matching final answer.
- Ensure no question-answer pair is incomplete.
- Ensure no question has been skipped.

### TRANSCRIPT
---START---
{transcript_text}
---END---
"""
