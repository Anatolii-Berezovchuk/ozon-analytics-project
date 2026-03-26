--Top‑Risk Professions Within Each Industry
WITH ranked AS (
    SELECT
        job_role,
        industry,
        automation_risk_percent,
        ROW_NUMBER() OVER (
            PARTITION BY industry
            ORDER BY automation_risk_percent DESC
        ) AS rn
    FROM ai_jobs
)
SELECT
    industry,
    job_role,
    automation_risk_percent
FROM ranked
WHERE rn <= 3
ORDER BY industry, automation_risk_percent DESC;

-- “Danger Zone” Professions: High Risk × Salary Decline × AI Replacement
WITH filtered AS (
    SELECT
        job_role,
        industry,
        automation_risk_percent,
        salary_change_percent,
        ai_replacement_score
    FROM ai_jobs
    WHERE automation_risk_percent > 70
      AND salary_change_percent < 0
      AND ai_replacement_score > 70
)
SELECT
    job_role,
    industry,
    automation_risk_percent,
    salary_change_percent,
    ai_replacement_score
FROM filtered
ORDER BY automation_risk_percent DESC, salary_change_percent ASC
LIMIT 25;
