from app.services.rag_service import run_rag


if __name__ == "__main__":
    question = "You are approaching a pedestrian crossing. What should you do?"

    for model in ["gpt", "gemini", "phi3"]:
        print(f"\n=== {model.upper()} ===")
        result = run_rag(model, question)
        print("Answer:\n", result["answer"])