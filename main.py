from agents import Agent,Runner
from config import config
import chainlit as cl

translator_agent = Agent(
    name="TargetedTranslator",
    instructions="""
  You are a smart translator bot.

The user will always enter a sentence in this format:
"Convert in <target-language>: <sentence>"

Your job:

Read the command.
Detect the target language (e.g., Urdu, English, Roman Urdu) from the part after "Convert in".

Translate only the sentence part (after the colon :) into the target language.

Output only the translated sentence.
No headings, no extra text, no explanations—just the final translated line.
"""
)


@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Welcome to my translator agent! Type something like 'Convert in Urdu: How are you?'").send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content  # User ka message hasil krna

    # User k input ko agent k through process karo
    response = await Runner.run(
        translator_agent,
        input=user_input,
        run_config=config
    )
    
    # final output user ko return kro chainlit UI main 
    await cl.Message(
        content = response.final_output
    ).send()
