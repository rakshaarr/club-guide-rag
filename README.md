clubGuide
Campus Club Information Assistant

clubGuide is a campus-specific AI assistant that helps students find information about student clubs at JSSATEB.

Currently, the knowledge base contains information about:

AWS Student Builders Group
GDG Campus

Students can ask questions in natural language and get answers based only on the information available in the campus knowledge base.

Features
Natural-language question answering
Campus-specific knowledge base
Semantic search using embeddings
FAISS vector similarity search
Gemini-powered answer generation
FastAPI backend
Web-based frontend
Suggested questions for quick access
Tech Stack
Python
FastAPI
Sentence Transformers
FAISS
NumPy
Google Gemini API
HTML
CSS
JavaScript
Project Structure
clubGuide/
│
├── main.py
├── club_info.txt
├── requirements.txt
├── README.md
├── .gitignore
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
How It Works

clubGuide uses a Retrieval-Augmented Generation (RAG) approach.

Campus Information
       ↓
   Text Chunks
       ↓
  Embeddings
       ↓
   FAISS Index
       ↓
 User Question
       ↓
Question Embedding
       ↓
Similarity Search
       ↓
Relevant Information
       ↓
     Gemini
       ↓
    Answer

The system retrieves relevant information from the campus knowledge base and provides it to Gemini as context before generating the answer.

Setup
1. Clone the repository
git clone https://github.com/rakshaarr/club-guide-rag.git
cd clubGuide
2. Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Add your Gemini API key

Create a config.py file in the project root:

API_KEY = "YOUR_GEMINI_API_KEY"

Replace YOUR_GEMINI_API_KEY with your own Gemini API key.

Do not commit your API key to GitHub.

Running the Project
Start the backend
python -m uvicorn main:app --reload

The FastAPI server will run at:

http://127.0.0.1:8000
Start the frontend

Open frontend/index.html using a local development server such as VS Code Live Server.

Make sure the FastAPI backend is running before using the frontend.

Example Questions
When does AWS recruitment happen?
Can first-year students apply for AWS?
What teams are available in GDG?
How much attendance is required for GDG?
Can I be a member of both AWS and GDG?
Knowledge Base

The campus information used by clubGuide is stored in club_info.txt.

The current knowledge base covers:

Club teams
Recruitment
Eligibility
Attendance
Events and workshops
Selection processes
Club leads
Membership information

The knowledge base can be updated by modifying club_info.txt.

Limitations
The assistant can only answer using information available in the knowledge base.
The current implementation retrieves the closest matching piece of information for a question.
The Gemini API requires an API key.
The project currently runs locally.
Future Improvements
Retrieve multiple relevant chunks
Add more campus clubs
Add event and workshop information
Add source references to answers
Add conversation history
Deploy the application
Add an interface for updating the knowledge base
Author

Built as a student project to explore RAG, semantic search, LLM integration, REST APIs, and frontend-backend integration.
