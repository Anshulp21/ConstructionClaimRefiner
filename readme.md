# 🛠️ Construction Claim Prompt Improver

A Streamlit-based application that transforms raw, unstructured construction claim prompts into professionally formatted, legally-sound prompts suitable for detailed LLM analysis. Built with Mistral AI integration and LangChain.

## 🚀 Features

- **Prompt Enhancement**: Converts basic construction queries into comprehensive, structured prompts
- **Legal Context**: Adds relevant legal terminology and construction law context
- **Professional Formatting**: Structures output for optimal LLM analysis
- **Real-time Processing**: Instant prompt transformation via Mistral API

## 📋 Prerequisites

- Python 3.8+
- Mistral API Key
- Git

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ConstructionClaimPromptImprover.git
cd ConstructionClaimPromptImprover
```

### 2. Create Virtual Environment
```bash
python -m venv myvenv
source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```env
MISTRAL_API_KEY=your_actual_mistral_api_key_here
```

## 🏃‍♂️ Running the Application

```bash
streamlit run prompt_refine.py
```

The application will be available at:
- Local URL: `http://localhost:8501`
- Network URL: `http://your-ip:8501`

## 📦 Dependencies

```txt
streamlit==1.28.0
langchain-core==0.1.52
langchain-community==0.0.38
mistralai==0.1.2
requests==2.31.0
python-dotenv==1.0.0
```

## 💡 Usage

1. **Launch the Application**: Run the Streamlit app
2. **Enter Raw Prompt**: Input your basic construction claim query
3. **Generate Enhanced Prompt**: Click the button to transform your prompt


### Sample Input
```
eot due to material delay. how to justify?
```

### Sample Output
```
As a construction claims consultant, please analyze the following Extension of Time (EOT) claim scenario:

**Claim Context**: Extension of Time due to material delivery delays

**Required Analysis**:
1. **Contractual Basis**: Examine the claim under relevant standard forms (JCT, FIDIC, NEC) focusing on:
   - Material procurement responsibilities
   - Critical path impact assessment
   - Notice requirements and time limits

2. **Documentation Requirements**:
   - Material delivery schedules and purchase orders
   - Correspondence with suppliers
   - Progress reports showing delay impact
   - Updated project schedules

3. **Legal Justification Framework**:
   - Assess causation between material delay and project delay
   - Evaluate concurrent delay issues
   - Review force majeure or frustration clauses
   - Consider mitigation measures taken

4. **Time Impact Analysis**:
   - Prepare detailed schedule analysis
   - Identify critical path disruption
   - Quantify actual delay period
   - Assess knock-on effects

Please provide a comprehensive analysis including legal precedents, contract interpretation, and recommendations for claim presentation.
```



### Core Components

1. **MistralLLM Class**: Custom LangChain LLM wrapper for Mistral API
2. **Prompt Template**: Structured template for construction claim enhancement
3. **Streamlit UI**: User-friendly interface for prompt input/output
4. **API Integration**: Secure connection to Mistral AI services



## PoC Summary
This proof-of-concept helps professionals refine unstructured prompts into structured, expert-level inputs suitable for LLM processing in the domain of construction claims. It uses the Mistral model provides a clean, focused UI using Streamlit.






