from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
tasks = []  # Lista global para almacenar tareas

# HTML con pequeños errores: sin etiquetas <html>/<body> cerradas, sin validación de entrada
template = """
<h1>Mis Tareas</h1>
<form method="POST" action="/add">
    <input type="text" name="task">
    <input type="submit" value="Agregar">
</form>
<ul>
{% for t in tasks %}
    <li>{{ t }} <a href="/delete/{{ loop.index }}">❌</a></li>  <!-- Error: loop.index en lugar de loop.index0 -->
{% endfor %}
</ul>
"""

@app.route("/")
def index():
    return render_template_string(template, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]  # No usa .get(), puede lanzar KeyError si falta 'task'
    tasks.append(task)  # No se valida si está vacío
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    try:
        tasks.pop(task_id)  # Usando índice incorrecto por el error en loop.index
    except IndexError:
        pass  # Error silencioso
    return redirect("/")

if __name__ == "__main__":
    app.run()
