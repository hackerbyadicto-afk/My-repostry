import gradio as gr
import math
def check(m,n,k):
    m=int(m)
    k=int(k)
    if n=="+":
        return m+k
    elif n=="-":
        return m-k
    elif n=="*":
        return m*k
    elif n==":" or n=="/":
        return m/k
    elif n=="%":
        return m*k/100
    else:
        return "It is not available"    
code=gr.Interface(
    fn=check,
    inputs=gr.Textbox(label="Enter your function:"),
    outputs=gr.Textbox(label="Result"),
    title="Calculator"
)
code.launch()
