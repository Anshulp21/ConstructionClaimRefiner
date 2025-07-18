import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.language_models.llms import LLM
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
import os
import requests
from typing import Optional, List, Any
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()
mistralApiKey = os.getenv("MISTRAL_API_KEY") or "your-api-key-here"

if not mistralApiKey:
    st.error("MISTRAL_API_KEY is missing.")
    st.stop()

class MistralLLM(LLM):
    apiKey: str = Field(...)
    model: str = Field(default="mistral-tiny")
    temperature: float = Field(default=0.7)
    maxTokens: int = Field(default=2048)
    
    def __init__(self, apiKey: str, model: str = "mistral-tiny", temperature: float = 0.7, maxTokens: int = 2048):
        super().__init__(
            apiKey=apiKey,
            model=model,
            temperature=temperature,
            maxTokens=maxTokens
        )

    @property
    def _llm_type(self) -> str:
        return "mistral"

    def _call(self, prompt: str, stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None, **kwargs: Any) -> str:
        url = "https://api.mistral.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.apiKey}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.temperature,
            "max_tokens": self.maxTokens
        }

        if stop:
            payload["stop"] = stop

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                raise Exception(f"API Error: {response.status_code} - {response.text}")
        except Exception as e:
            raise Exception(f"Request failed: {str(e)}")

    @property
    def _identifying_params(self) -> dict:
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.maxTokens
        }

systemPromptTemplate = """
You are an expert construction claims consultant with deep knowledge of construction law, contract administration, and project management.

Your task is to transform the following raw, unstructured user prompt about construction claims into a structured, legally-sound, and professionally formatted prompt suitable for detailed LLM analysis.

Guidelines for transformation:
1. Add relevant legal context and terminology
2. Include specific claim categories and types
3. Reference standard construction contracts (JCT, FIDIC, NEC, etc.)
4. Mention required documentation and evidence
5. Include time impact analysis requirements
6. Add professional construction and legal terminology
7. Preserve the original user intent
8. Structure the output clearly and professionally
9. Format as a comprehensive prompt that would help an LLM provide detailed analysis

Raw User Prompt: {user_input}

Transform this into a comprehensive, structured prompt that would help an LLM provide detailed, legally-sound construction claim analysis. Make it professional, detailed, and actionable:
"""


def createPromptProcessor(llm):
    prompt = PromptTemplate(input_variables=["user_input"], template=systemPromptTemplate)

    def process(user_input: str) -> str:
        formatted = prompt.format(user_input=user_input)
        return llm.invoke(formatted)

    return process

st.title("Construction Claim Prompt Improver")

userPrompt = st.text_area("Enter raw construction prompt:", height=150)

if st.button("Generate Enhanced Prompt"):
    if not userPrompt.strip():
        st.warning("Please enter a valid prompt.")
    else:
        try:
            llm = MistralLLM(apiKey=mistralApiKey)
            processPrompt = createPromptProcessor(llm)
            refinedPrompt = processPrompt(userPrompt.strip())
            st.text_area("Enhanced Prompt:", value=refinedPrompt, height=400)
        except Exception as e:
            st.error(f"Error: {e}")




