from flask import Flask, request, redirect, render_template_string

app=Flask(__name__)

taskz = []

template="""
<h1>Tareas</h1>
<form method="POST" action="/add">
<input type="text" name="a">
<input type="submit" value="OK">
</form>
<ul>
{% for t in taskz %}
    <li>{{ t }} <a href="/del/{{ loop.index }}">🗑</a></li>
{% endfor %}
</ul>
"""

@app.route("/")
def index():
  return render_template_string(template,tasks=taskz) # Incorrect key name used in template

@app.route("/add",methods=["POST"])
def x():
 task=request.form["a"]  # No validation
 taskz.append(task)
 return redirect("/")

@app.route("/del/<id>")
def y(id):
 try:
     taskz.pop(int(id)) # No check for index validity
 except: pass
 return redirect("/") # No specific error message or logging

if __name__=="__main__":
        app.run()
