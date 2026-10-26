from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aditya Kumar | DevOps Engineer</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #38bdf8;
            --card-bg: rgba(30, 41, 59, 0.7);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #020617, #0f172a, #1e1b4b);
            color: var(--text-main);
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            max-width: 900px;
            width: 100%;
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            animation: fadeIn 1s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Header */
        .header {
            display: flex;
            align-items: center;
            gap: 30px;
            margin-bottom: 30px;
            border-bottom: 2px solid rgba(56, 189, 248, 0.2);
            padding-bottom: 30px;
        }

        .avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: linear-gradient(45deg, var(--accent), #818cf8);
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 3rem;
            font-weight: bold;
            color: #0f172a;
            box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
        }

        .header-text h1 {
            font-size: 2.5rem;
            color: var(--text-main);
        }
        
        .header-text h1 span {
            color: var(--accent);
        }

        .header-text h2 {
            font-size: 1.2rem;
            color: var(--text-muted);
            font-weight: 400;
            margin-top: 5px;
        }

        .badge {
            display: inline-block;
            background: rgba(56, 189, 248, 0.2);
            color: var(--accent);
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-top: 10px;
            border: 1px solid var(--accent);
        }

        /* Skills */
        .section-title {
            font-size: 1.5rem;
            margin: 30px 0 15px 0;
            color: var(--accent);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .skills-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .skill-tag {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            cursor: default;
        }

        .skill-tag:hover {
            background: var(--accent);
            color: #000;
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(56, 189, 248, 0.4);
        }

        /* Projects */
        .projects-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .project-card {
            background: rgba(0, 0, 0, 0.2);
            padding: 20px;
            border-radius: 12px;
            border-left: 4px solid var(--accent);
            transition: all 0.3s;
        }

        .project-card:hover {
            transform: scale(1.02);
            background: rgba(0, 0, 0, 0.4);
        }

        .project-card h3 {
            font-size: 1.1rem;
            margin-bottom: 10px;
            color: var(--text-main);
        }

        .project-card p {
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        /* Responsive */
        @media (max-width: 768px) {
            .header {
                flex-direction: column;
                text-align: center;
            }
            .projects-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Header Section -->
        <div class="header">
            <div class="avatar">A</div>
            <div class="header-text">
                <h1>Aditya <span>Kumar</span></h1>
                <h2>DevOps Engineer</h2>
                <div class="badge">● Live & Deployed on Kubernetes</div>
            </div>
        </div>

        <!-- Skills Section -->
        <h2 class="section-title">⚡ Tech Stack</h2>
        <div class="skills-grid">
            <span class="skill-tag">AWS (EC2, EKS, S3)</span>
            <span class="skill-tag">Docker</span>
            <span class="skill-tag">Kubernetes</span>
            <span class="skill-tag">Jenkins</span>
            <span class="skill-tag">Terraform</span>
            <span class="skill-tag">Linux</span>
            <span class="skill-tag">Git & GitHub</span>
            <span class="skill-tag">Python</span>
            <span class="skill-tag">Bash Scripting</span>
        </div>

        <!-- Projects Section -->
        <h2 class="section-title">🚀 Featured Projects</h2>
        <div class="projects-grid">
            <div class="project-card">
                <h3>End-to-End CI/CD Pipeline</h3>
                <p>Automated build, SonarQube scan, and Docker image push to Docker Hub using Jenkins and GitHub Webhooks.</p>
            </div>
            <div class="project-card">
                <h3>Kubernetes Microservices</h3>
                <p>Deployed a multi-tier application on EKS with Ingress routing, ConfigMaps, and Rolling Updates.</p>
            </div>
        </div>
    </div>

</body>
</html>
"""

@app.route('/')
def hello():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)