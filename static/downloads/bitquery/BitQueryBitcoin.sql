SELECT
  f.repo_name,
  f.path,
  c.pkey
FROM
  [bigquery-public-data:github_repos.files] f
JOIN (
  SELECT
    id,
    REGEXP_EXTRACT(content, r'(?:^|[^a-zA-Z0-9])(5[HJK][123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ]{48,49})(?:$|[^a-zA-Z0-9])') AS pkey
  FROM
    [bigquery-public-data:github_repos.contents]
  WHERE
    REGEXP_MATCH(content, r'(?:^|[^a-zA-Z0-9])(5[HJK][123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ]{48,49})(?:$|[^a-zA-Z0-9])') ) c
ON
  f.id = c.id