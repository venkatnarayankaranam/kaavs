import torch
from transformers import pipeline

# Load GPT-2 for story generation
def load_gpt_model():
    return pipeline("text-generation", model="gpt2", device=0 if torch.cuda.is_available() else -1)

gpt_generator = load_gpt_model()

def generate_story_with_gpt2(prompt, max_new_tokens=300):
    """
    Generates a meaningful and structured story from the given prompt.
    """
    refined_prompt = (
        f"Once upon a time, {prompt}. The story unfolds as the hero embarks on a journey. "
        "Facing challenges, making allies, and discovering secrets, the adventure leads to a surprising conclusion."
    )

    story = gpt_generator(
    refined_prompt,
    max_new_tokens=100,  # ✅ Generate 100 new tokens instead of restricting length
    temperature=0.7,
    top_k=50,
    top_p=0.9,
    num_return_sequences=1,
    pad_token_id=50256
)

    return story[0]["generated_text"]
