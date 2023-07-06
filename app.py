from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# create an interface for the model
textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
with gr.Interface(predict, inputs= textbox, outputs= "text", title="Summarize Text!!!") as interface:
    interface.launch()
