Stock Trade Outlier Analysis using Graph Database:
Project Overview:
This project analyzes Forex (FX) trade data to detect unusual trading patterns using Z-score-based outlier detection. It builds a Streamlit web app to visualize normal and outlier trades.
1.Goals:
* Collect and process FX trade data
* Detect outliers using Z-score (volume & price deviations)
* Visualize normal vs. outlier trades using scatter plots
* Provide a user-friendly interface with Streamlit

2.How It Works?
🔹 Step 1: Data Collection & Storage
We use sample FX trade data with fields:

trade_id → Unique trade identifier
currency_pair → Example: EUR/USD
volume → Trade size (e.g., 100,000 units)
price → Trade price
timestamp → Date and time of the trade
All trade data is stored in a Pandas DataFrame.

🔹 Step 2: Outlier Detection (Using Z-score)
We apply Z-score analysis to detect abnormal trades in volume and price.

 What is Z-score?
Z-score measures how far a value deviates from the mean in terms of standard deviations.
𝑍=𝑋−𝜇𝜎
Z=σX−μ
​
Where:
𝑋
X = Value (Trade Volume or Price)
𝜇
μ = Mean (Average)
𝜎
σ = Standard Deviation
Outlier Criteria:
If Z-score > 2.5 or Z-score < -2.5, the trade is an outlier.
High volume outliers: Abnormally large or small trades.
High price outliers: Sudden price spikes or drops.
🔹 Step 3: Visualization
We use Matplotlib to create a scatter plot:
✔ Blue Dots → Normal trades
✔ Red Xs → Outliers

The plot helps us visually inspect abnormal trades.

3️ Running the App (Step-by-Step Guide)
🔹 Local Deployment
Install Dependencies
bash
Copy
Edit
pip install streamlit pandas numpy scipy matplotlib
Run the App
bash
Copy
Edit
streamlit run app.py
App Opens in Browser 🌐

4️ Real-World Applications
✔ Financial Market Analysis – Detect unusual trades in stock or forex markets.
✔ Fraud Detection – Identify suspicious trading activity.
✔ Anomaly Detection in Business – Track abnormal transaction patterns.
