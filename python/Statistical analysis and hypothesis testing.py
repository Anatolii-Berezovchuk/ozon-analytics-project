import numpy as np
import pandas as pd
from scipy import stats

# Функция для автоматической интерпретации p-value
def interpret_p(p):
    return "ЗНАЧИМО (p < 0.05)" if p < 0.05 else "НЕ значимо (p ≥ 0.05)"


# === 4.1. Тесты нормальности (Shapiro) ===
print("=== 4.1. Тесты нормальности (Shapiro) ===")

cols = ["automation_risk_percent", "salary_change_percent", "ai_replacement_score"]

for col in cols:
    series = df[col].dropna()
    sample = series.sample(10000, random_state=42) if len(series) > 5000 else series
    
    stat, p = stats.shapiro(sample)
    print(f"\n{col}: p-value = {p:.4e} → {interpret_p(p)}")


# === 4.2. Различия между индустриями (Kruskal–Wallis) ===
print("\n=== 4.2. Различия между индустриями (Kruskal–Wallis) ===")

groups_industry = [
    df.loc[df["industry"] == ind, "automation_risk_percent"].dropna()
    for ind in df["industry"].dropna().unique()
]

stat, p = stats.kruskal(*groups_industry)
print(f"automation_risk_percent по индустриям: p-value = {p:.4e} → {interpret_p(p)}")


# === 4.3. Различия между кластерами ===
print("\n=== 4.3. Различия между кластерами (Kruskal–Wallis) ===")

# salary_change_percent
groups_cluster_salary = [
    df.loc[df["cluster"] == c, "salary_change_percent"].dropna()
    for c in df["cluster"].dropna().unique()
]

stat, p = stats.kruskal(*groups_cluster_salary)
print(f"salary_change_percent по кластерам: p-value = {p:.4e} → {interpret_p(p)}")

# automation_risk_percent
groups_cluster_risk = [
    df.loc[df["cluster"] == c, "automation_risk_percent"].dropna()
    for c in df["cluster"].dropna().unique()
]

stat, p = stats.kruskal(*groups_cluster_risk)
print(f"automation_risk_percent по кластерам: p-value = {p:.4e} → {interpret_p(p)}")


# === 4.4. Корреляции (Spearman) ===
print("\n=== 4.4. Корреляционный анализ (Spearman) ===")

pairs = [
    ("automation_risk_percent", "ai_replacement_score"),
    ("automation_risk_percent", "salary_change_percent"),
    ("ai_replacement_score", "salary_change_percent"),
    ("automation_risk_percent", "skill_gap_index"),
]

for x, y in pairs:
    s1 = df[x].dropna()
    s2 = df[y].dropna()
    idx = s1.index.intersection(s2.index)
    
    rho, p = stats.spearmanr(s1.loc[idx], s2.loc[idx])
    print(f"\n{x} vs {y}: rho={rho:.3f}, p-value={p:.4e} → {interpret_p(p)}")
