from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# .env  file se environment variables ko load karne ke liye
load_dotenv()

# gemini key .env se api get ki ja rahi hai 
gemini_api_key = os.getenv("GEMINI_API_KEY")

# agar api key set nhi ho gi to error  raise kre ga 
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# gemini key ko OpenAI-compatible banane k lie  external client banaya gaya hai  
# gemini  ko OpenAi compatible endpoint diya gaya hai 
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

# Gemini model ko define kiya gaya hai jise OpenAI ke formate main use kiya ja sakta hai 
model= OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", # Gemini ka speciifc model
    openai_client=external_client, # oper baya gaya client
)

# model run krne k lie configration set kiya hai 
config = RunConfig(
    model= model, # model jo oper define kiya hai
    model_provider=external_client,  # ye btata hai kon sa provider hai 
    tracing_disabled=True,  # tracing disable ki hai 
)