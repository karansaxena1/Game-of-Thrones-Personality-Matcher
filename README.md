# ⚔️ Game of Thrones Personality Matcher  
## Working Link - https://gameofthronespersonalitymatcher.streamlit.app/
![Screenshot 2025-02-20 102345](https://github.com/user-attachments/assets/79314498-b8c6-4c96-b079-926afb580923)

## 🏰 About the Project  
This project is a **Game of Thrones Personality Matcher** that allows users to select a character from the show and find their closest personality match based on dialogue analysis.  

The application uses **Natural Language Processing (NLP)** to analyze dialogue, **t-SNE for dimensionality reduction**, and **Streamlit** for an interactive and visually appealing user interface.  

---

## 🚀 Features  
- 🔍 **Select any Game of Thrones character**  
- 🤖 **AI-powered personality matching**  
- 📊 **t-SNE visualization for character similarity**  
- 🎭 **Character descriptions & images fetched from Thrones API**  
- 🎨 **Enhanced UI with dark fantasy theme**  

---

## 🛠️ Tech Stack  
- **Python**  
- **Streamlit**  
- **Pandas, NumPy**  
- **Scikit-learn (t-SNE, NLP)**  
- **Plotly (Visualizations)**  
- **Requests (API calls)**  

---

## 🏗️ How It Works
- Extracts dialogues from Game of Thrones scripts and stores them in a DataFrame.
- Processes the text using CountVectorizer and converts it into embeddings.
- Uses t-SNE (t-distributed Stochastic Neighbor Embedding) for dimensionality reduction.
- Finds the closest personality match using Euclidean distance.
- Fetches character images & descriptions from the Thrones API.
- Displays the result in a beautiful Streamlit UI.

## 📦 Installation  

1️⃣ Clone the repository  
```sh
git clone https://github.com/your-username/GOT-Personality-Matcher.git
cd GOT-Personality-Matcher
```
2️⃣ Install dependencies

```sh
pip install -r requirements.txt
```
3️⃣ Run the Streamlit app

```sh
streamlit run app.py
```

🔥 Winter is Coming... But Your Match is Here! 🔥
