from sklearn.decomposition import PCA

pca = PCA(n_components=2)
components = pca.fit_transform(X)

df["pc1"] = components[:, 0]
df["pc2"] = components[:, 1]

plt.figure(figsize=(10, 7))
sns.scatterplot(
    data=df,
    x="pc1",
    y="pc2",
    hue="cluster",
    palette="tab10",
    alpha=0.8
)
plt.title("Clusters of Professions (PCA)")
plt.show()
