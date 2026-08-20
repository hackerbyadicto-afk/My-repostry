import gradio as gr
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
code=gr.Interface(fn=check,inputs=[gr.Textbox(label="First number"),gr.Radio(["+","-","*",":","/","%"],label="Function"),gr.Textbox(label="Second number")],outputs=gr.Textbox(label="Result"),title="Calculator")
code.launch(server_name="0.0.0.0",server_port=10000)
