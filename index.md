<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Cheatsheet</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #121212;
            color: #E0E0E0;
        }
        header {
            background: #1E1E1E;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }
        header h1 {
            margin: 0;
            font-size: 2rem;
        }
        #search {
            margin-top: 10px;
            padding: 10px;
            width: 50%;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
        }
        nav {
            background: #222;
            padding: 10px 0;
            text-align: center;
        }
        nav ul {
            list-style: none;
            padding: 0;
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        nav a {
            color: #E0E0E0;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s;
        }
        nav a:hover {
            color: #FF9800;
        }
        main {
            padding: 40px;
            max-width: 900px;
            margin: auto;
        }
        section {
            background: #1E1E1E;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }
        h2 {
            border-bottom: 2px solid #FF9800;
            padding-bottom: 5px;
        }
        pre {
            background: #333;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        footer {
            background: #181818;
            padding: 15px;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
            box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.3);
        }
        .theme-toggle {
            position: absolute;
            top: 15px;
            right: 20px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header>
        <h1>DevOps Cheatsheet</h1>
        <input type="text" id="search" placeholder="Search...">
        <i class="fas fa-moon theme-toggle" onclick="toggleTheme()"></i>
    </header>
    <nav>
        <ul>
            <li><a href="#docker">Docker</a></li>
            <li><a href="#kubernetes">Kubernetes</a></li>
            <li><a href="#ansible">Ansible</a></li>
        </ul>
    </nav>
    <main>
        <section id="docker">
            <h2>Docker</h2>
            <pre><code>docker run -it ubuntu</code></pre>
        </section>
        <section id="kubernetes">
            <h2>Kubernetes</h2>
            <pre><code>kubectl get pods</code></pre>
        </section>
        <section id="ansible">
            <h2>Ansible</h2>
            <pre><code>ansible-playbook site.yml</code></pre>
        </section>
    </main>
    <footer>
        <p>&copy; 2025 DevOps Cheatsheet</p>
    </footer>
    <script>
        document.getElementById('search').addEventListener('input', function() {
            let query = this.value.toLowerCase();
            document.querySelectorAll('section').forEach(section => {
                section.style.display = section.innerText.toLowerCase().includes(query) ? 'block' : 'none';
            });
        });

        function toggleTheme() {
            let body = document.body;
            body.classList.toggle('light-theme');
            if (body.classList.contains('light-theme')) {
                body.style.backgroundColor = '#F5F5F5';
                body.style.color = '#212121';
                document.querySelectorAll('section').forEach(section => section.style.background = '#E0E0E0');
            } else {
                body.style.backgroundColor = '#121212';
                body.style.color = '#E0E0E0';
                document.querySelectorAll('section').forEach(section => section.style.background = '#1E1E1E');
            }
        }
    </script>
</body>
</html>
