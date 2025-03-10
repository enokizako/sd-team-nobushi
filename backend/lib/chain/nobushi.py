from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()


def nobushi_chain():
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.0)

    system_prompt = (
        "You are a helpful assistant. Your name is 野武士."
    )

    human_prompt = """あなたは彷徨える野武士です。野武士の口調で返答してください。
画像は、Inputに基づいて描画された散歩ルートの人工衛星画像です。あなたはこのルートを彷徨います。
この画像で示されるルートを彷徨ったらどんな風景が見えるか、ルートの雰囲気を簡潔に説明してください。
あくまでも衛星画像のみに基づいて、可能な限り正確に、歩いた時の雰囲気を語ってください。あなたの内部の知識を使ってはいけません。
Markdown記法は絶対に使わないでください。

Input:
{input}
"""

    image_template = {"image_url": {"url": "data:image/jpeg;base64,{image_data}"}}

    human_message_template = HumanMessagePromptTemplate.from_template([human_prompt, image_template])

    prompt = ChatPromptTemplate.from_messages([("system", system_prompt), human_message_template])

    return prompt | model
