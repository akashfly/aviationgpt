import gradio as gr
import speech_recognition as sr

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# LOAD VECTOR DB
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)


# SPEECH TO TEXT
def speech_to_text(audio):
    if audio is None:
        return ""

    r = sr.Recognizer()

    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)

    try:
        text = r.recognize_google(audio_data)
        return text
    except:
        return ""


# QUESTION ANSWERING
def answer_question(question, pdf_file=None, image_file=None):

    docs = db.similarity_search(question, k=3)

    response = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return response


# CUSTOM CSS
css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');


body, .gradio-container {

    font-family: Inter, sans-serif !important;

    background:
    linear-gradient(
        rgba(8,8,10,0.48),
        rgba(12,12,14,0.55)
    ),
    url("https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=2000&auto=format&fit=crop");

    background-size: cover !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
}



/* WIDE WEB APP */
.gradio-container {
    max-width: 1700px !important;
    width: 97% !important;
    margin: auto !important;
    padding-top: 24px !important;
}



/* TITLE */
.main-title {
    text-align: center;
    font-size: 32px;
    font-weight: 400;
    color: #f3f5f7;
    letter-spacing: 1px;
    margin-bottom: 6px;
}



/* TAGLINE */
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #bfc9d8;
    margin-bottom: 24px;
    font-weight: 300;
}



/* GLASS PANEL */
.glass-panel {
    background: rgba(15,15,20,0.55) !important;
    backdrop-filter: blur(14px);
    border-radius: 22px;
    padding: 24px;
    border: 1px solid rgba(255,255,255,0.05);
}



/* INPUT BOX */
textarea {
    background: rgba(22,24,28,0.85) !important;
    color: white !important;
    border-radius: 14px !important;
    border: none !important;
}



/* BUTTONS — NAVY BLUE */
button {

    background: linear-gradient(
        135deg,
        #243b55,
        #141e30
    ) !important;

    color: #eef2f7 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    font-weight: 500 !important;
}



/* OUTPUT */
.output-box textarea {
    min-height: 320px !important;
}



/* REMOVE FOOTER */
footer {
    display: none !important;
}
"""


# UI
with gr.Blocks(css=css) as demo:

    gr.Markdown("""
    <div class='main-title'>✈ AviationGPT</div>
    <div class='sub-title'>AI Copilot for Aviators</div>
    """)

    with gr.Column(elem_classes="glass-panel"):

        question = gr.Textbox(
            label="Ask your question",
            placeholder="Ask anything about Air Navigation, Meteorology, Technical General...",
            lines=3
        )

        with gr.Row():

            audio_input = gr.Audio(
                type="filepath",
                label="🎙 Voice Recording",
                scale=1
            )

            pdf_input = gr.File(
                label="📄 Upload PDF",
                scale=1
            )

            image_input = gr.Image(
                type="filepath",
                label="🖼 Upload Image",
                scale=1
            )

        with gr.Row():

            speech_btn = gr.Button(
                "Convert Voice to Text"
            )

            ask_btn = gr.Button(
                "Ask AviationGPT"
            )

        output = gr.Textbox(
            label="Answer",
            lines=14,
            elem_classes="output-box"
        )


    speech_btn.click(
        fn=speech_to_text,
        inputs=audio_input,
        outputs=question
    )

    ask_btn.click(
        fn=answer_question,
        inputs=[
            question,
            pdf_input,
            image_input
        ],
        outputs=output
    )


demo.launch(share=True)