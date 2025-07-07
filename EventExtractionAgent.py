from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st


# ---- PAGE CONFIGURATION ----
st.set_page_config(page_title="Story Event Extractor", page_icon="📖", layout="wide")

# ---- CUSTOM CSS STYLING ----
st.markdown("""
    <style>
        /* General Page Styling */
        body {
            background: linear-gradient(to right, #0F2027, #203A43, #2C5364);
            color: white;
        }
        /* Title Styling */
        .title {
            text-align: center;
            font-size: 60px !important; /* Force larger size */
            font-weight: bold;
            color: #FFFFE4;
            margin-bottom: 20px;
        }
        /* Subtitle */
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #B0C4DE; /* Light Steel Blue */
            margin-bottom: 25px;
        }     
    </style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.markdown('<p class="title">📖 Story Event Extractor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Analyze and extract key events from any story with AI-powered precision.</p>', unsafe_allow_html=True)

# ---- MODEL SETUP ----
template = """
You are an expert in literary analysis, designed to extract and summarize the most important events from long texts.

Context:
{context}


Task:
Identify the most important events ensuring that each includes:

Step 1:
Extract any information about the setting [location, atmosphere, time period]
example: "In a dark forest with long trees during midnight

Step 2:
Extract any information about the characters [physical description, emotions]

Determine if the character is a key participant in the event.

If yes, include them in the event description.
If no, do not include them.

Example: 
Pigsy -> Key participant
Sandy -> Key participant
Jeff -> Not a key participant
Characters: "Pigsy (a small pink pig with a twisted tail), Sandy (a tall and beautiful young lady with long black hair)"

Step 3:
Extract any information about the actions [what is happening in the scene]
It should be a clear and concise description of the event
Do not include vague or unnecessary descriptions.
Example: "Pigsy and Sandy are walking through the forest"
Negative example: "Pigsy and Sandy who was sick this morning are walking through the forest"

Step 4: 
Create a prompt from the extracted information
- prompt should be specific, clear, and concise
- prompt is used to generate an image of the event, so make it discriptive but brief
Example: "In a dark forest with long trees during midnight, a small pink pig with a twisted tail and a tall and beautiful young lady with long black hair are walking through the forest."
Negative example: "In a dark forest with long trees during midnight, a small pink animal with a twisted tail and a tall and beautiful young person with long black hair are walking through the forest, but they are also talking about their plans for the future."

Output Format:
For each event, structure your response as follows:

**Event X:**
- **Setting:** [Describe the environment vividly]  
- **Characters:** [List the key individuals and their emotional states]  
- **Actions:** [Explain what happens breifly but clearly]  
- **Prompt:** [Combine the setting, characters, and actions into a coherent narrative]

Ensure that each event is distinct and captures the essence of the story.

Guidelines:
- Your output must be precise and strictly adhere to the given context. Inaccuracies, fabrications, or assumptions are not tolerated. Ensure that all extracted events are factually correct and directly supported by the text.
- Continue extracting events until the full narrative is covered. 
- Avoid using proper nouns when referring to characters or locations; instead, use descriptive terms that capture their essence without naming them directly.
- If some information is missing, do not fabricate details or indicate that it is missing. Instead, focus on the information that is available and provide a clear, concise summary of the events based on the provided context.

"""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.1")
chain = prompt | model

# ---- USER INPUT ----
story = st.chat_input("✍️ Enter your story here and press Enter")

# ---- PROCESS & DISPLAY OUTPUT ----
if story:
    response = chain.invoke({"context": story})
    st.markdown(f'<div class="output-box">{response}</div>', unsafe_allow_html=True)

