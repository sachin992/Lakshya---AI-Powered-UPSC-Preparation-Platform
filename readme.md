# 🎓 Lakshya - UPSC Preparation Platform

An intelligent, AI-powered platform designed to help aspirants master UPSC preparation with personalized learning tools, mock tests, answer evaluation, and real-time current affairs tracking.

## 📋 Project Description

Lakshya is an intelligent platform for UPSC aspirants featuring AI mock tests, automated answer evaluation, current affairs tracking, and gamified learning. Built with Streamlit and OpenAI, it provides personalized test generation, interactive quizzes, and performance analytics for comprehensive exam preparation.

---

## ✨ Key Features

### 1. **Authentication System** 🔐
- Secure user registration and login with SQLite database
- Password hashing using SHA256
- Email and phone validation
- Session state management
- User profile persistence

### 2. **UPSC GPT** 🤖
- AI-powered chatbot for UPSC-related queries
- PDF answer upload for evaluation and copy-checking
- RAG (Retrieval-Augmented Generation) with semantic search
- Real-time feedback on answers
- Multi-turn conversation support
- Web search integration for current information

### 3. **Test Generator** 📝
- AI-powered question generation for Prelims and Mains
- Customizable difficulty levels (Easy, Medium, Hard)
- Current affairs integration
- Support for mock questions and previous year questions
- Bilingual support (English & Hindi)
- Timer-based test interface with auto-submission
- 40+ question types and variations

### 4. **Mains Answer Evaluator** ✏️
- PDF upload for comprehensive answer evaluation
- AI examiner feedback based on UPSC standards
- Score calculation (1-100 scale)
- Detailed analysis of strengths and weaknesses
- Multi-criteria scoring system
- Structure and content evaluation
- Word limit tracking

### 5. **Current Affairs Module** 📰
- Daily updated current affairs articles
- Filterable by date and category
- Integration with UPSC prelims/mains topics
- Interactive calendar navigation
- Multi-language support
- Topic-wise categorization

### 6. **UPSC Puzzle (Question Sweeper)** 🧩
- Gamified learning with Minesweeper-like mechanics
- Real previous year questions
- Multiple difficulty levels (Beginner, Intermediate, Advanced)
- Score tracking and achievements
- Interactive grid-based question discovery
- Instant feedback on answers

### 7. **Dashboard** 📊
- User progress tracking
- Learning statistics
- Performance metrics
- Study hours logged
- Test history and analytics

---

## 🛠️ Technology Stack

### Frontend
- **Streamlit** - Interactive UI framework
- **HTML/CSS** - Custom styling
- **Streamlit Option Menu** - Navigation components

### Backend
- **Python 3.9+** - Core language
- **SQLite** - User database
- **LangGraph** - Agentic workflows
- **LangChain** - NLP orchestration

### AI/ML
- **OpenAI GPT-4o-mini** - Large Language Model
- **FAISS** - Vector database for semantic search
- **text-embedding-3-small** - Text embeddings
- **PyPDFLoader** - PDF parsing
- **RecursiveCharacterTextSplitter** - Text chunking
- **DuckDuckGo Search** - Web search integration

---

## 📦 Installation Guide

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- OpenAI API key
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/lakshya.git
cd lakshya
```

2. **Create and activate virtual environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create .env file**
```bash
cp .env.example .env
```

5. **Add your OpenAI API key to .env**
```
OPENAI_API_KEY=your_api_key_here
```

6. **Run the application**
```bash
streamlit run app.py
```

7. **Access the application**
```
Open your browser and go to: http://localhost:8501
```

---

## 📁 Project Structure

```
lakshya/
│
├── app.py                          # Main Streamlit application
├── login.py                        # Authentication & registration
├── db_utils.py                     # Database management utilities
├── final_backend.py                # LangGraph chatbot & PDF processing
│
├── pages/                          # Feature modules
│   ├── __init__.py
│   ├── home.py                    # Dashboard home
│   ├── upsc_gpt.py                # AI chatbot interface
│   ├── test_generator.py          # Mock test creation
│   ├── mains_evaluator.py         # Answer evaluation
│   ├── current_affairs.py         # Current affairs module
│   ├── upsc_puzzle.py             # Gamified learning
│   └── dashboard.py               # User statistics
│
├── databases/
│   ├── lakshya_users.db           # SQLite user database
│   └── chatbot.db                 # LangGraph checkpoints
│
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template
├── .gitignore                     # Git ignore rules
├── README.md                      # This file
└── LICENSE                        # MIT License

```

---

## 🚀 Usage Guide

### For Student Users

#### 1. **Registration & Login**
```
1. Go to home page
2. Click "Sign Up" tab
3. Fill in details (name, email, phone, password)
4. Select UPSC attempt number (71st, 72nd, etc.)
5. Check commitment checkbox
6. Click "Start My Journey"
```

#### 2. **Generate Mock Test**
```
1. Go to "Test Generator" from menu
2. Select exam type (Prelims/Mains)
3. Choose paper type (GS1, GS2, etc.)
4. Set number of questions
5. Select question source (Mock/PYQ/Mixed)
6. Toggle current affairs integration
7. Click "Generate Test"
8. Attempt the test with timer
9. Submit and view results with detailed analysis
```

#### 3. **Evaluate Answer**
```
1. Go to "Mains Evaluator"
2. Upload your answer PDF
3. Select paper and marks
4. Choose evaluator mode (Hard/Easy)
5. Click "Evaluate Answer"
6. Receive detailed AI feedback with score
```

#### 4. **Use UPSC GPT**
```
1. Go to "UPSC GPT"
2. Ask any UPSC-related question
3. Optionally upload PDF for analysis
4. Get instant AI-powered responses
5. Continue multi-turn conversation
```

#### 5. **Track Current Affairs**
```
1. Go to "Current Affairs"
2. Browse daily articles
3. Filter by date and category
4. View topic-wise organization
5. Track relevant affairs for UPSC
```

#### 6. **Play UPSC Puzzle**
```
1. Go to "UPSC Puzzle"
2. Choose GS or CSAT
3. Select category
4. Pick difficulty level
5. Click tiles to find questions
6. Answer correctly to score points
7. Earn achievements
```

---

## 🔧 Configuration

### Environment Variables (.env)
```
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small
DATABASE_PATH=lakshya_users.db
```

### Database Schema

**Users Table:**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    password_hash TEXT NOT NULL,
    bpsc_attempt TEXT,
    commitment_4hrs BOOLEAN,
    created_at TIMESTAMP,
    last_login TIMESTAMP
)
```

---

## 📊 Core Functionality Details

### Test Generation Engine
- **Prelims Questions:** MCQ format with 4 options
- **Mains Questions:** Descriptive format with word limits
- **Marks Distribution:** 2 marks (Prelims), 10-15 marks (Mains)
- **Question Sources:** AI-generated based on UPSC syllabus
- **Customization:** Difficulty, category, CA integration

### Answer Evaluation Criteria
- **Content Relevance** (40%) - Alignment with question, accuracy
- **Structure** (20%) - Introduction, body, conclusion
- **Examples** (20%) - Use of case studies, data
- **Language** (10%) - Clarity, coherence, grammar
- **Word Limit** (10%) - Adherence to specified limit

### RAG Pipeline (PDF Analysis)
1. PDF upload and parsing
2. Text chunking (1000 chars, 200 overlap)
3. Semantic embedding using OpenAI
4. FAISS vector storage
5. Similarity-based retrieval
6. Copy detection and plagiarism check

---

## 🔐 Security Features

- **Password Security:** SHA256 hashing
- **Session Management:** Streamlit session state
- **Input Validation:** Email, phone, password formats
- **SQL Injection Prevention:** Parameterized queries
- **PDF Processing:** Isolated temporary file handling
- **API Key Protection:** Environment variables only

---

## 🐛 Known Issues & Limitations

### Current Limitations
- Limited question database (sample data provided)
- Single-user per session
- Local PDF storage only
- No concurrent multi-user sessions

### Known Issues
- PDF parsing may fail with scanned/image-heavy documents
- Timer accuracy depends on system clock
- Large PDFs (>20MB) may slow down processing

---

## 🚀 Future Enhancements

- [ ] Multi-user concurrent sessions
- [ ] Cloud storage integration (AWS S3/Google Cloud)
- [ ] Advanced analytics dashboard with charts
- [ ] Mobile app version (React Native)
- [ ] Offline mode support
- [ ] Community features (peer review, forums)
- [ ] Interview preparation module
- [ ] Video learning integration
- [ ] Personalized study recommendations
- [ ] Optional subject support
- [ ] Live mock tests with leaderboards
- [ ] Email notifications for current affairs

---

## 📈 Performance Metrics

- **Test Generation:** ~15-30 seconds for 10 questions
- **Answer Evaluation:** ~30-60 seconds for one answer
- **PDF Processing:** ~5-10 seconds per document
- **Chat Response:** ~2-5 seconds per query

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Write unit tests for new features
- Update README for new features
- Test locally before submitting PR

---


---




---

## 🙏 Acknowledgments

- **OpenAI** for GPT models and embeddings API
- **LangChain** for LLM orchestration framework
- **Streamlit** for rapid web application development
- **UPSC aspirants** for feedback and suggestions
- **FAISS** team for vector similarity search

---

## 📊 Project Statistics

- **Total Features:** 7 major modules
- **Code Lines:** ~3000+
- **Database Tables:** 1
- **AI Models Used:** 2
- **Supported Languages:** 2 (English)
- **Current Users:** Growing community

---

## 🎯 Mission Statement

**Democratize UPSC preparation through AI-powered, personalized, and interactive learning to help aspirants achieve their dreams of becoming civil servants.**

---



---

**Version:** 1.0.0  
**Last Updated:** January 2026  
**Status:** Active Development  
**Maintained By:** Lakshya Development Team

---

## ⭐ Star Us!

If you find Lakshya helpful, please give us a star on GitHub! Your support motivates us to keep improving.

**Happy Learning! 🚀**