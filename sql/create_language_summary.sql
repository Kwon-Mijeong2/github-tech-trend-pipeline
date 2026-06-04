CREATE TABLE language_summary AS

SELECT
    language,
    COUNT(*) AS repo_count,
    SUM(stars) AS total_stars,
    AVG(stars) AS avg_stars
FROM github_trending
GROUP BY language;