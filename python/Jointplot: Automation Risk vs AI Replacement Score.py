sns.jointplot(
    data=df,
    x="automation_risk_percent",
    y="ai_replacement_score",
    kind="hex",
    height=8,
    cmap="viridis"
)
