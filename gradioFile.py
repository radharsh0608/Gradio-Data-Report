import gradio as gr
import fileUpload as file
import pandas as pd

def echo(upload,model1, model2, prompt,temperature,topP,maxTokens):
    df = pd.read_excel(upload)
    df.to_excel("Data Bank.xlsx", index=False)
    file.write_to_excel("Data Bank.xlsx","Data Bank Report.xlsx",model1,model2,prompt,temperature,topP,maxTokens)
    return "Data written successfully"
demo = gr.Interface(fn=echo, inputs=[
    gr.File(file_types=[".xlsx"]),
gr.Dropdown(
        ["chatNBX - mixtral-8x7b-inst-v0-1-32k",
         "chatNBX - openhermes-2-5-m7b-4k",
         "chatNBX - Qwen1-5-7B-Chat",
         "chatNBX - gemma-7b-it",
         "chatNBX - nous-hermes-13b-4k",
         "chatNBX - Qwen1-5-14B-Chat",
         "OpenRouter - nousresearch/nous-capybara-7b:free",
         "OpenRouter - mistralai/mistral-7b-instruct:free",
         "OpenRouter - gryphe/mythomist-7b:free",
         "OpenRouter - undi95/toppy-m-7b:free",
         "OpenRouter - openrouter/cinematika-7b:free",
         "OpenRouter - google/gemma-7b-it:free",
         "OpenRouter - rwkv/rwkv-5-world-3b",
         "OpenRouter - recursal/rwkv-5-3b-ai-town",
         "OpenRouter - recursal/eagle-7b",
         "OpenRouter - huggingfaceh4/zephyr-7b-beta:free",
         "OpenRouter - openchat/openchat-7b:free"], label="Select the testing model"),
gr.Dropdown(
        ["chatNBX - mixtral-8x7b-inst-v0-1-32k",
         "chatNBX - openhermes-2-5-m7b-4k",
         "chatNBX - Qwen1-5-7B-Chat",
         "chatNBX - gemma-7b-it",
         "chatNBX - nous-hermes-13b-4k",
         "chatNBX - Qwen1-5-14B-Chat",
         "OpenRouter - nousresearch/nous-capybara-7b:free",
         "OpenRouter - mistralai/mistral-7b-instruct:free",
         "OpenRouter - gryphe/mythomist-7b:free",
         "OpenRouter - undi95/toppy-m-7b:free",
         "OpenRouter - openrouter/cinematika-7b:free",
         "OpenRouter - google/gemma-7b-it:free",
         "OpenRouter - rwkv/rwkv-5-world-3b",
         "OpenRouter - recursal/rwkv-5-3b-ai-town",
         "OpenRouter - recursal/eagle-7b",
         "OpenRouter - huggingfaceh4/zephyr-7b-beta:free",
         "OpenRouter - openchat/openchat-7b:free"], label="Select the verification model"),
    gr.Textbox(label="Enter your prompt:"),
    gr.Slider(0, 1, value=0.5, label="Temperature"),
    gr.Slider(0, 1, value=1, label="Top P"),
    gr.Slider(1, 1000, value=200, label="Max Tokens"),

], title="Elevmi Test Automation",outputs=["text"])




demo.launch()