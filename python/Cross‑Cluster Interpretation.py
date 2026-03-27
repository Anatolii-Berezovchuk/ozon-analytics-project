from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

features = df[[
    "automation_risk_percent",
    "salary_change_percent",
    "ai_replacement_score"
]]

scaler = StandardScaler()
X = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=4, random_state=42)
df["cluster"] = kmeans.fit_predict(X)

df[["job_role", "industry", "cluster"]].head()
