SELECT job_role, industry, automation_risk_percent
FROM ai_jobs
ORDER BY automation_risk_percent DESC
LIMIT 20;


SELECT industry, AVG(automation_risk_percent) AS avg_risk
FROM ai_jobs
GROUP BY industry
ORDER BY avg_risk DESC;


SELECT country, AVG(automation_risk_percent) AS avg_risk
FROM ai_jobs
GROUP BY country
ORDER BY avg_risk DESC;
