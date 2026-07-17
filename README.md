# log-report

Terminal-Bench 2 (Harbor) task. The agent gets an Apache access log at /app/access.log
and has to write a JSON summary (total_requests, unique_ips, top_path) to /app/report.json.

To run it you need Docker and harbor (uv tool install harbor):

    harbor run -p . --agent oracle   # solution, reward 1.0
    harbor run -p . --agent nop      # no-op, reward 0.0

Layout: task.toml (config), instruction.md (agent prompt), environment/ (Dockerfile + input log),
solution/ (oracle), tests/ (pytest verifier, writes reward.txt + ctrf.json to /logs/verifier/).